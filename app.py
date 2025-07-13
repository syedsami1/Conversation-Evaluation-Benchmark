import streamlit as st
import pandas as pd
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Conversation Facet Evaluator", layout="centered")

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

@st.cache_data
def load_facets():
    df = pd.read_csv("data/Facets Assignment.csv")
    return df["Facets"].tolist(), model.encode(df["Facets"].tolist())

model = load_model()
facet_list, facet_embs = load_facets()

st.title("🧠 Conversation Turn Facet Evaluator")
st.markdown("Score conversation turns against emotion, empathy, linguistic and safety facets.")

tab1, tab2 = st.tabs(["🔎 Score Single Turn", "📁 Upload JSON & Score All"])

with tab1:
    turn = st.text_area("Paste a conversation turn (user or bot):")

    if st.button("Score This Turn"):
        turn_emb = model.encode(turn)
        sims = cosine_similarity([turn_emb], facet_embs)[0]
        top_idxs = sims.argsort()[-5:][::-1]

        st.subheader("Top 5 Matching Facets")
        for idx in top_idxs:
            st.write(f"**{facet_list[idx]}** → Score: {int(sims[idx]*4.5)} | Confidence: {sims[idx]:.2f}")

with tab2:
    uploaded_file = st.file_uploader("Upload a conversation JSON file", type="json")
    if uploaded_file:
        conversations = json.load(uploaded_file)
        all_scores = []

        for convo in conversations:
            conv_id = convo["conv_id"]
            for turn in convo["turns"]:
                turn_emb = model.encode(turn["text"])
                sims = cosine_similarity([turn_emb], facet_embs)[0]
                top_idxs = sims.argsort()[-5:][::-1]

                for idx in top_idxs:
                    all_scores.append({
                        "conv_id": conv_id,
                        "turn_id": turn["turn_id"],
                        "speaker": turn["speaker"],
                        "text": turn["text"],
                        "facet": facet_list[idx],
                        "score": int(sims[idx]*4.5),
                        "confidence": float(sims[idx])
                    })

        df = pd.DataFrame(all_scores)
        st.success("✅ Scoring completed.")
        st.dataframe(df.head(20))

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Full Scores as CSV", csv, "scored_conversations.csv", "text/csv")
