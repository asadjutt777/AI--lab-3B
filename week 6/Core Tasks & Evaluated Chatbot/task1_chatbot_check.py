from guided_chatbot import build_bot, reply

engine = build_bot(backend="tfidf")

res_exact = reply(engine, "How do I reset my password?")
assert "it_help.txt" in res_exact, "Exact query failed"

res_empty = reply(engine, "")
assert res_empty == "Please enter a question.", "Empty query validation failed"

res_unsupported = reply(engine, "volcano geology")
assert "No matching FAQ" in res_unsupported, "Unsupported lexical query failed"

res_paraphrase = reply(engine, "password recovery")
assert "Possible matches" in res_paraphrase, "Suggestion workflow failed"

print("All Task 1 FAQ verification checks passed successfully.")
