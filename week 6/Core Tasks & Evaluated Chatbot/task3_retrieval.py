import csv
import json
import time
from pathlib import Path
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from task2_chunks import make_chunks

def evaluate(scores, chunks, items):
    hits, reciprocal = [], []
    for row, q in zip(scores, items):
        if q["doc"] is None:
            continue
        top = np.argsort(-row, kind="stable")[:3]
        good = [
            rank for rank, i in enumerate(top, 1)
            if chunks[i]["doc"] == q["doc"] and q["evidence"] in chunks[i]["text"]
        ]
        hits.append(bool(good))
        reciprocal.append(1 / good[0] if good else 0)
    return (float(np.mean(hits)), float(np.mean(reciprocal))) if hits else (None, None)

def main():
    with open("corpus.json", encoding="utf-8") as f:
        docs = json.load(f)
    with open("queries.json", encoding="utf-8") as f:
        items = json.load(f)

    for q in items:
        assert q["split"] in {"dev", "test"}
        if q["doc"] is not None:
            assert q["evidence"] and q["evidence"] in docs[q["doc"]]

    t0 = time.perf_counter()
    has_model = False
    try:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
        has_model = True
        print(f"Model load time: {time.perf_counter() - t0:.4f}s")
    except Exception as e:
        print(f"SentenceTransformer not loaded: {e}")

    query_texts = [q["query"] for q in items]
    logs = []

    print("\n--- Benchmark Retrieval Evaluation ---")
    for strategy in ["0", "10", "sentence"]:
        chunks = make_chunks(docs, strategy)
        texts = [c["text"] for c in chunks]

        backends = ["tfidf", "embedding"] if has_model else ["tfidf"]
        for method in backends:
            t = time.perf_counter()
            if method == "tfidf":
                vectorizer = TfidfVectorizer()
                C = vectorizer.fit_transform(texts)
                Q = vectorizer.transform(query_texts)
                encode_sec = time.perf_counter() - t
                t_s = time.perf_counter()
                scores = (Q @ C.T).toarray()
                search_sec = time.perf_counter() - t_s
            else:
                lengths = [len(model.tokenizer(t, truncation=False)["input_ids"]) for t in texts + query_texts]
                if max(lengths) > model.max_seq_length:
                    raise ValueError("Input exceeds encoder token limit")
                C = model.encode(texts, normalize_embeddings=True)
                Q = model.encode(query_texts, normalize_embeddings=True)
                encode_sec = time.perf_counter() - t
                t_s = time.perf_counter()
                scores = Q @ C.T
                search_sec = time.perf_counter() - t_s

            for split in ["dev", "test"]:
                indices = [i for i, q in enumerate(items) if q["split"] == split and q["doc"] is not None]
                if indices:
                    hit, mrr = evaluate(scores[indices], chunks, [items[i] for i in indices])
                    print(f"Strat: {strategy:>8} | Method: {method:>9} | Split: {split:>4} | "
                          f"Hit@3: {hit:.3f} | MRR@3: {mrr:.3f} | Chunks: {len(chunks)}")

            for row, q in zip(scores, items):
                for rank, i in enumerate(np.argsort(-row, kind="stable")[:3], 1):
                    c = chunks[i]
                    logs.append({
                        "strategy": strategy,
                        "method": method,
                        "query": q["query"],
                        "split": q["split"],
                        "rank": rank,
                        "score": round(float(row[i]), 4),
                        "chunk_id": c["id"],
                        "doc": c["doc"],
                        "start": c["start"],
                        "end": c["end"],
                        "text": c["text"],
                        "answerable": q["doc"] is not None
                    })

    with open("retrieval_log.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(logs[0].keys()))
        writer.writeheader()
        writer.writerows(logs)
    print("retrieval_log.csv created successfully.")

if __name__ == "__main__":
    main()
