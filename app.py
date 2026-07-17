import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_NAME = "talhabutt72456/bert-review-rating"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    model.eval()
    return tokenizer, model

tokenizer, model = load_model()

st.title("⭐ BERT Review Rating Predictor")

text = st.text_area("Enter your review")

if st.button("Predict Rating"):

    if text.strip() == "":
        st.warning("Please enter a review.")

    else:

        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True
        )

        with torch.no_grad():
            outputs = model(**inputs)

        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)

        prediction = torch.argmax(probabilities, dim=1).item()

        confidence = probabilities[0][prediction].item()

        rating = prediction + 1

        st.success(f"Predicted Rating: {rating}/5")
        st.write("⭐" * rating)

        st.write(f"Confidence: {confidence:.2%}")
        st.progress(confidence)

        # ---------------- DEBUG ----------------

        st.subheader("Debug Information")

        st.write("Raw Logits:")
        st.write(logits)

        st.write("Class Probabilities:")
        st.write(probabilities)

        st.write(f"Predicted Class Index: {prediction}")

        st.write(f"Final Rating: {rating}")

        st.write("Probability per Rating")

        for i, prob in enumerate(probabilities[0]):
            st.write(f"{i+1} ⭐ : {prob.item():.4f}")

        st.balloons()
