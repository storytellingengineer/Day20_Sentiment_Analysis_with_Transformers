# Sentiment Analysis with Transformers 🤗

This project demonstrates how to perform **Sentiment Analysis** using HuggingFace Transformers.

### Model used:
- `distilbert-base-uncased-finetuned-sst-2-english` — a lightweight BERT model fine-tuned on the Stanford Sentiment Treebank (SST-2).

---

### What this project does:
- Classifies text as **positive** or **negative**
- Provides a confidence score
- Simple CLI script
- (Optional) Interactive Streamlit app

---

### Applications of Sentiment Analysis:
- **Customer Feedback Analysis**: understand what customers feel about your product.
- **Social Media Monitoring**: detect trends in user sentiment about brands.
- **Market Research**: analyze product reviews at scale.
- **Content Moderation**: flag negative/abusive content.
- **Public Sentiment Tracking**: understand sentiment around events, politics, movies.

---

### Issues / Learnings:

- Transformer-based models offer **far superior accuracy** vs traditional ML classifiers.
- The pipeline API in HuggingFace makes it extremely simple to get started — no need for manual tokenization or model loading.
- Streamlit + HuggingFace = rapid prototyping of **AI-powered apps**.

---

### How to run:

Install dependencies:

```
pip install transformers streamlit
```

Run CLI script:

```
python sentiment_analysis_transformer.py
```

Run Streamlit app:

```
streamlit run app.py
```

---

### Next Steps:

This marks the completion of the **NLP track** in my #90DaysOfAI series.  
Up next: I will be exploring **LLM Ops / ML Engineering** and **Computer Vision** topics to broaden my portfolio.

Follow me for more AI projects! [Linkedin](https://www.linkedin.com/in/storytellingengineer/)🚀 
