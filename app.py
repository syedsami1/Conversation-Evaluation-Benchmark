
import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Conversation Turn Facet Scorer")

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

@st.cache_data
def load_facets():
    df = pd.read_csv("data/Facets Assignment.csv")
    return df["Facets"].tolist(), model.encode(df["Facets"].tolist())

model = load_model()
facet_list, facet_embs = load_facets()

st.title("🧠 Conversation Turn Facet Scorer")

turn = st.text_area("Paste a conversation turn:")

if st.button("Score"):
    turn_emb = model.encode(turn)
    sims = cosine_similarity([turn_emb], facet_embs)[0]
    top_idxs = sims.argsort()[-5:][::-1]
    st.subheader("Top 5 Matching Facets")
    for idx in top_idxs:
        st.write(f"**{facet_list[idx]}** → Score: {int(sims[idx]*4.5)} | Confidence: {sims[idx]:.2f}")
