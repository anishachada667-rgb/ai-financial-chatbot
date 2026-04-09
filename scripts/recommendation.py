import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
data = pd.read_csv(r'C:\Users\Anisha Reddy Chada\OneDrive\Documents\Desktop\ai-financial-chatbot\data\sample_queries.csv')

# Initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['query'])

# User query
user_query = "How to save on taxes?"

# Transform user query and compute similarity
query_vec = vectorizer.transform([user_query])
similarities = cosine_similarity(query_vec, X).flatten()

# Get top 2 similar queries
top_indices = similarities.argsort()[-2:][::-1]

print("=== Recommended Queries ===")
for idx in top_indices:
    print(f"- {data['query'][idx]}")