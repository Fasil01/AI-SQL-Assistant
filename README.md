# 🧠 AI SQL Assistant

An interactive web app that allows you to ask questions in plain English, automatically generates the SQL query, executes it on a sample database, and returns the results with an option to download them as CSV.

✨ **Built with:** Python, Streamlit, SQLite, Pandas

---

## 🚀 Features

- 💬 **Natural language input** – Type questions like “List all users”  
- ⚡ **Automatic SQL generation** – Simple logic for demo (can be upgraded to AI-powered models)  
- 📊 **Instant query execution** – Runs SQL on a local SQLite database  
- 🎨 **Attractive dark UI** – Stylish background and bold fonts  
- 📥 **Download as CSV** – Save query results easily  
- 🗄 **Custom database support** – Swap in your own `.db` file

---

 ## 📂 Project Structure

   
    📦 AI-SQL-Assistant
     ┣ 📜 app.py              — 🎯 Main Streamlit application
     ┣ 📜 create_db.py        — 🛠 Script to create sample SQLite database
     ┣ 🗄 sample.db           — 💾 SQLite database file with demo data
     ┣ 🖼 background.jpg      — 🎨 Background image for the app UI
     ┣ 📄 requirements.txt    — 📦 Python dependencies
     ┗ 📄 README.md           — 📖 Project documentation
    

---

## 🛠 Installation & Setup

## 1. **Clone the repository**
```bash
git clone https://github.com/Fasil01/AI-SQL-Assistant
cd AI-SQL-Assistant/
```
## 2.Install dependencies
```bash
pip install -r requirements.txt
```
## 3.Create the sample database
```bash
python3 create_db.py
```
## 4.Run the app
```bash
streamlit run app.py
```
## 🎯 Usage
.Start the app and enter your question in plain English.

.The app generates a simple SQL query for demonstration.

.The query runs on sample.db and displays results.

.Click 📥 Download as CSV to save results.

## Example questions:
```bash
List all users
Show total users
```
## 🧩 Future Improvements
Integrate AI models (OpenAI GPT, LLaMA, etc.) for smarter SQL generation

Add authentication for private database access

Support multiple database types (MySQL, PostgreSQL, etc.)

Query history & saved queries

## 💡 Author
Developed by Fasil – Available for freelance projects on Upwork.
