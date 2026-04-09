# AI Financial Chatbot – 5-Day Project

## Description
**AI Financial Chatbot** is an end-to-end AI/ML project providing financial guidance, investment insights, and personalized query recommendations. Users can interact with the chatbot using natural language queries about taxes, investments, accounts, and receive intelligent responses powered by **LLMs** and a **recommendation system**. This project demonstrates a complete workflow from data analysis to model deployment and integration.

---

## Features
- Data analysis of financial queries (Day 2)
- AI-powered chatbot using GPT-2 (Day 3)
- Query recommendation system using TF-IDF & cosine similarity (Day 4)
- End-to-end chatbot integration combining LLM responses + recommendations (Day 5)
- Easy-to-use Python scripts with modular structure
- Dataset-based testing and demonstration
- Extensible for larger LLMs and datasets

---

## Tech Stack

- **Programming Language:** Python  
- **Machine Learning / AI:** PyTorch, Hugging Face Transformers, Scikit-learn  
- **Natural Language Processing:** GPT-2, TF-IDF, Cosine Similarity  
- **Big Data / Data Processing:** Pandas, NumPy, PySpark  
- **Data Storage:** CSV datasets (sample_queries.csv), optional models/ folder for saved models  
- **Deployment / MLOps:** Docker (optional), AWS SageMaker (optional), MLflow (optional)  
- **Workflow / Scripts:** Modular Python scripts for analysis, chatbot, recommendation, and integration

---

## Highlights

- End-to-end AI chatbot for financial guidance  
- LLM-powered responses combined with recommendation system  
- Modular Python scripts for each project phase (Day 2 → Day 5)  
- Dataset-based testing and demonstration  
- Easy to extend for larger datasets or more advanced LLMs  
- Simple to run locally with Python scripts and minimal setup 

---

## Future Enhancements

- Add a Streamlit web interface for live user interaction  
- Integrate real-time financial data feeds for dynamic insights  
- Improve LLM recommendation accuracy with fine-tuning  
- Add user authentication and personalized dashboards  
- Expand dataset to include more financial queries and scenarios  
- Integrate advanced analytics for portfolio performance tracking  

---

## Project Structure

```text
ai-financial-chatbot/
│
├─ scripts/
│   ├─ data_analysis.py             # Day 2: Load and analyze queries dataset
│   ├─ llm_chatbot.py               # Day 3: LLM chatbot
│   ├─ recommendation.py            # Day 4: Query recommendation system
│   └─ chatbot_integration.py       # Day 5: End-to-end integration
│
├─ data/
│   └─ sample_queries.csv           # Sample queries dataset
│
├─ models/                          # Optional: store fine-tuned models
├─ .gitignore
└─ README.md






