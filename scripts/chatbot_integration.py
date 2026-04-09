import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline

# Load dataset
data = pd.read_csv(r'C:\Users\Anisha Reddy Chada\OneDrive\Documents\Desktop\ai-financial-chatbot\data\sample_queries.csv')

# Initialize TF-IDF vectorizer for recommendation
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['query'])

# Initialize GPT-2 chatbot
chatbot = pipeline("text-generation", model="gpt2")

# Function to get recommendations
def get_recommendations(user_query, top_n=2):
    query_vec = vectorizer.transform([user_query])
    similarities = cosine_similarity(query_vec, X).flatten()
    top_indices = similarities.argsort()[-top_n:][::-1]
    return [data['query'][idx] for idx in top_indices]

# User query (example)
user_query = "How to save on taxes?"

# Get LLM response
response = chatbot(user_query, max_length=50, do_sample=True)[0]['generated_text']

# Get recommended queries
recommended = get_recommendations(user_query)

# Print results
print("=== User Query ===")
print(user_query)
print("\n=== LLM Response ===")
print(response)
print("\n=== Recommended Queries ===")
for rec in recommended:
    print(f"- {rec}")