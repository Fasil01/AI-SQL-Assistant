import sqlite3
import pandas as pd
import streamlit as st
import base64

st.set_page_config(page_title="AI SQL Assistant", layout="centered")

# Background image
def get_base64_bg(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_image = get_base64_bg("background.jpg")

# CSS Styling
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
        font-weight: bold;
    }}
    .main > div {{
        background-color: rgba(0, 0, 0, 0.7);
        padding: 2rem;
        border-radius: 12px;
    }}
    .chat-input-wrapper {{
        display: flex;
        align-items: center;
        margin-top: 20px;
    }}
    .chat-input-wrapper input {{
        flex-grow: 1;
        background-color: #1e1e1e;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        font-weight: bold;
    }}
    .chat-input-wrapper input:focus {{
        outline: none;
        border: 1px solid #666;
    }}
    .stDownloadButton > button {{
        background-color: #ff704d;
        color: white;
        font-weight: bold;
        border-radius: 6px;
        padding: 10px 16px;
    }}
    code {{
        color: #00ffcc;
        background-color: #111;
        padding: 10px;
        border-radius: 5px;
        font-size: 15px;
        font-weight: bold;
    }}
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align:center; font-weight:bold;'>🧠 AI SQL Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-weight:bold;'>Ask your question in plain English. The app will generate and run the SQL query for you.</p>", unsafe_allow_html=True)

# Chat-like input with real-time listener
question = st.text_input("Your SQL question", placeholder="e.g. List all users", label_visibility="collapsed")

if question:
    sql_query = "SELECT * FROM users;" if "list" in question.lower() else "SELECT COUNT(*) FROM users;"
    sql_query = sql_query.replace("CURRENT_DATE", "date('now')")

    st.markdown("### 🧠 Generated SQL Query:")
    st.code(sql_query, language="sql")

    try:
        conn = sqlite3.connect("sample.db")
        cur = conn.cursor()
        cur.execute(sql_query)
        rows = cur.fetchall()
        col_names = [desc[0] for desc in cur.description]
        conn.close()

        df = pd.DataFrame(rows, columns=col_names)

        st.markdown("### 📊 Query Result:")
        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download results as CSV",
            data=csv,
            file_name="query_results.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"❌ Error running SQL: {e}")

