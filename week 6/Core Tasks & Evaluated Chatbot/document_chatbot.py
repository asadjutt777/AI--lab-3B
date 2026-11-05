import json
from task2_chunks import make_chunks
from lab6_search import Retriever

if __name__ == "__main__":
    with open("corpus.json", encoding="utf-8") as f:
        docs = json.load(f)

    chunks = make_chunks(docs, "sentence")
    backend = "tfidf"
    try:
        import sentence_transformers
        backend = "embedding"
    except ImportError:
        backend = "tfidf"

    print(f"Initializing Document Assistant using backend: '{backend}' and sentence-aware chunking...")
    engine = Retriever(chunks, backend=backend)
    print("Evidence Assistant online. Type 'exit' to stop.")

    while True:
        try:
            query = input("\nQuestion: ")
        except (EOFError, KeyboardInterrupt):
            break
        if query.strip().lower() == "exit":
            break

        hits = engine.search(query, k=3)
        if not hits or (backend == "tfidf" and hits[0][1] == 0.0):
            print("No candidate evidence found. Please rephrase or contact the academic help desk.")
            continue

        print("\nCandidate evidence retrieved (Confirmation Required):")
        for number, (r, score) in enumerate(hits, 1):
            print(f"[{number}] Chunk: {r['id']} | Similarity: {score:.3f} | Span: chars {r['start']} to {r['end']}")

        chosen = input("Choose 1-3 to inspect evidence (Press Enter if none apply): ")
        if not chosen.isdigit() or not (1 <= int(chosen) <= len(hits)):
            print("No evidence selected. Please rephrase or contact human support.")
            continue

        r, score = hits[int(chosen) - 1]
        print("\n--- Verified Retrieved Passage ---")
        print(f"Document : {r['doc']}")
        print(f"Location : Characters {r['start']} - {r['end']}")
        print(f"Content  : {r['text']}")
