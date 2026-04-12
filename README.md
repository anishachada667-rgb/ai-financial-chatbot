# AI Financial Chatbot – 5-Day Project

---

## 📌 Overview
AI Financial Chatbot is an end-to-end AI/ML project that provides financial guidance, investment insights, and personalized query recommendations. The system allows users to input natural language queries related to finance (taxes, investments, accounts) and receive intelligent responses using a GPT-2 based chatbot along with a recommendation engine.

This project demonstrates a complete pipeline including data analysis, NLP-based chatbot development, recommendation system, and final integration — all executed locally using Python scripts.

---

## 📈 Key Features
- Data analysis of financial queries dataset using Pandas  
- GPT-2 based chatbot for generating responses  
- Query recommendation system using TF-IDF and cosine similarity  
- Integration of chatbot responses with recommendation system  
- Modular Python scripts for each stage of the pipeline  
- Runs locally with simple setup and minimal dependencies  

---

## 🛠️ Tech Stack
- Programming Language: Python  
- Machine Learning / NLP: PyTorch, Hugging Face Transformers (GPT-2)  
- Recommendation System: Scikit-learn (TF-IDF, Cosine Similarity)  
- Data Processing: Pandas, NumPy  
- Dataset: CSV (sample_queries.csv)  
- Environment: Local Machine (VS Code, Git Bash)

---

## 🔄 Architecture Overview
User Query  
   └──> GPT-2 Chatbot (Generates Response)  
        └──> Recommendation System (TF-IDF Similarity)  
             └──> Final Output (Response + Suggested Queries)  

---

## 🛐 Current Status
The project is completed as a functional MVP with dataset analysis, GPT-2 chatbot, TF-IDF recommendation system, and end-to-end integration. All components run locally using Python scripts and demonstrate a complete NLP pipeline.

---

## 📊 Highlights
- End-to-end NLP pipeline combining chatbot and recommendation system  
- GPT-2 based response generation with similarity-based suggestions  
- Modular script-based architecture (Day-wise implementation)  
- Lightweight and easy to execute on a local environment  
- Demonstrates practical application of NLP and machine learning concepts  

---

## 🌐 Future Enhancements
- Add Streamlit UI for interactive chatbot interface  
- Improve chatbot accuracy through fine-tuning  
- Integrate real-time financial data APIs  
- Deploy using Docker or cloud platforms  
- Add user personalization and session management  

---

## 👨‍💼 Author
Anisha Reddy Chada  
Email: anishachada667@gmail.com  

---

## 🛠️ Setup Instructions

```bash
# Clone the repository
git clone <YOUR_REPO_URL>
cd ai-financial-chatbot

# Install dependencies
pip install pandas numpy scikit-learn torch transformers

# Verify dataset
# Ensure file exists: data/sample_queries.csv

# Run scripts
python scripts/data_analysis.py
python scripts/llm_chatbot.py
python scripts/recommendation.py
python scripts/chatbot_integration.py

