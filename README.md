# ⭐ BERT Review Rating Prediction

A deep learning project that predicts product review ratings (1–5 stars) using a fine-tuned BERT model from Hugging Face.

## 📌 Project Overview

This project uses the `bert-base-uncased` transformer model and fine-tunes it for multi-class review rating prediction.

Given a review, the model predicts the most likely rating between **1 and 5 stars**.

Example:

Input:

```
"This product exceeded my expectations!"
```

Prediction:

```
⭐⭐⭐⭐⭐ (5/5)
```

---

## 🚀 Features

- Fine-tuned BERT (`bert-base-uncased`)
- Multi-class (5-class) classification
- Hugging Face Transformers
- PyTorch training loop
- Streamlit web application
- Hosted model on Hugging Face Hub
- Real-time prediction

---

## 🛠 Tech Stack

- Python
- PyTorch
- Hugging Face Transformers
- Streamlit
- Scikit-learn
- Pandas
- NumPy

---

## 📊 Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | 72.60% |
| Precision | 70.77% |
| Recall | 72.60% |
| F1 Score | 71.29% |

---

## 📂 Project Structure

```
bert-review-rating-prediction/
│
├── app.py
├── notebook.ipynb
├── requirements.txt
├── README.md
└── images/
```

---

## 🤗 Hugging Face Model

You can access the trained model here:

**https://huggingface.co/talhabutt72456/bert-review-rating**

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/bert-review-rating-prediction.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Demo

(Add screenshots here)

---

## 📚 What I Learned

- Fine-tuning transformer models
- Hugging Face ecosystem
- AutoTokenizer
- AutoModelForSequenceClassification
- PyTorch training loops
- Streamlit deployment
- Hugging Face Hub

---

## 🔮 Future Improvements

- Improve model accuracy
- Hyperparameter tuning
- Better UI/UX
- Docker deployment
- AWS deployment

---

## 👨‍💻 Author

**Talha Butt**

If you found this project useful, consider giving it a ⭐.
