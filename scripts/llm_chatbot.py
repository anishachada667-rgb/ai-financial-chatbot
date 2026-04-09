# llm_chatbot.py
from transformers import pipeline

# Initialize GPT-2 text-generation pipeline
chatbot = pipeline("text-generation", model="gpt2")

# Sample queries
queries = [
    "How to file taxes?",
    "Best investment plans?",
    "Check my account balance"
]

print("=== LLM Chatbot Responses ===")
for query in queries:
    response = chatbot(query, max_length=50, do_sample=True)
    print(f"Query: {query}")
    print(f"Response: {response[0]['generated_text']}\n")