from task2_chunks import make_chunks
from lab6_search import Retriever, show_hits

texts = {
    "it": "A forgotten password can be reset using the recovery link.",
    "assessment": "Assignments are uploaded through the learning portal."
}

records = make_chunks(texts, "sentence")

paraphrases = [
    "How can I regain access to my account?",
    "Where do I turn in my lab deliverables?",
    "Can someone unlock my campus login?"
]

for q in paraphrases:
    print(f"\n==========================================")
    print(f"Query: {q}")
    for backend in ["tfidf", "embedding"]:
        print(f"--- Backend: {backend} ---")
        try:
            engine = Retriever(records, backend=backend)
            show_hits(engine.search(q, k=2))
        except Exception as e:
            print(f"Error ({backend}): {e}")
