from guided_chatbot import build_bot

engine = build_bot(backend="tfidf")
query = "assignment upload"
print("Suggested questions for lexical query:")
for record, score in engine.search(query, k=3):
    if score > 0:
        print(f"{record['question']} ({score:.3f})")
