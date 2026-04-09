import pandas as pd

# Load dataset using absolute path
data = pd.read_csv(r'C:\Users\Anisha Reddy Chada\OneDrive\Documents\Desktop\ai-financial-chatbot\data\sample_queries.csv')

# Print dataset info
print("\n=== Sample Queries Dataset ===")
print(data.head())
print("\nTotal queries:", data.shape[0])
print("Unique users:", data['user_id'].nunique())