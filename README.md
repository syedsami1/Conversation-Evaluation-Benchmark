# 🧠 Conversation Evaluation - Streamlit UI

This is an interactive Streamlit web app to evaluate and score **conversation turns** across 300+ facets related to **emotional tone, safety, pragmatics, and linguistic quality**. It’s designed as a scalable benchmark framework for conversation understanding.

---

## 🚀 Features

- Upload and score any **user or bot message**
- Supports **300+ facets** from CSV (can scale to 5000+ facets)
- Uses **sentence embeddings** for scoring
- Shows **top 5 matching facets** per turn
- Outputs both **facet scores** and **confidence**
- Upload a full conversation `.json` and get **CSV results**
- 🔓 100% Open weights (free to use)
- ✅ Compatible with local or **Streamlit Cloud** deployment

---

## 📦 Project Structure

```

convo-eval-streamlit/
├── app.py                         # Streamlit app UI
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── data/
├── Facets Assignment.csv     # List of facet labels (e.g., empathy, safety, etc.)
└── sample\_conversations.json # Sample conversations for batch testing

````

---

## 🔧 Tech Stack

- [Streamlit](https://streamlit.io/) – UI Framework
- [SentenceTransformers](https://www.sbert.net/) – `all-MiniLM-L6-v2` open embedding model
- `scikit-learn` – Cosine similarity
- `pandas` – Data handling
- No external APIs or closed-weight models used

---

## 📁 Facets Format (`Facets Assignment.csv`)

You can provide your own CSV with any number of facets:
```csv
Facets
Empathy
Non-judgment
Helpfulness
Sensitivity
Linguistic fluency
...
````

✅ Can scale to 5000+ facets without architecture changes.

---

## 💬 JSON Conversation Format

Upload files in this format:

```json
[
  {
    "conv_id": "001",
    "turns": [
      {"turn_id": 1, "speaker": "user", "text": "I'm feeling overwhelmed."},
      {"turn_id": 2, "speaker": "bot", "text": "That sounds really tough. I'm here for you."}
    ]
  }
]
```

---

## 💻 Run Locally

Make sure Python 3.8+ is installed.

```bash
git clone https://github.com/syedsami1/Conversation-Evaluation-Benchmark.git
cd convo-eval-streamlit
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌍 Deploy on Streamlit Cloud (Free)

1. Push this project to your GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **"New App"**
4. Choose your repo
5. Set the main file to `app.py`
6. Click **Deploy** 🎉

---

## 📊 Sample Output

| turn\_id | speaker | text                       | facet      | score | confidence |
| -------- | ------- | -------------------------- | ---------- | ----- | ---------- |
| 1        | user    | I’m feeling anxious today. | Empathy    | 4     | 0.88       |
| 1        | user    | I’m feeling anxious today. | Validation | 3     | 0.75       |
| ...      | ...     | ...                        | ...        | ...   | ...        |

Use the **CSV download** button in the app for your full results.

---

## 🧠 Evaluation Method

* Uses the `all-MiniLM-L6-v2` open model from SentenceTransformers
* Computes **cosine similarity** between conversation turn and each facet
* Picks top 5 facets per turn
* Scores are scaled from cosine \[0,1] → discrete \[0–4]


