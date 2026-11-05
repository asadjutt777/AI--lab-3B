import re

samples = [
    "AI, search!",
    "I can't log in.",
    "help@example.com",
    "CS4944 version 2.1",
    "",
    "یہ ایک مثال ہے"
]

print("=== Task 1 Tokenization Comparison ===")
for text in samples:
    ws = text.split()
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    print(f"\nOriginal : {repr(text)}")
    print(f"Whitespace ({len(ws)}): {ws}")
    print(f"Word-like  ({len(words)}): {words}")

assert re.findall(r"\b\w+\b", "") == []

print("\n=== Model Subword Tokenizer Check ===")
try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
    for text in samples[:4]:
        subwords = model.tokenizer.tokenize(text)
        print(f"{repr(text)} -> Subwords ({len(subwords)}): {subwords}")
except Exception as e:
    print(f"SentenceTransformer not loaded: {e}")
