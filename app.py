from flask import Flask, render_template, request, redirect, url_for, session
import pyttsx3
import sqlite3
from fpdf import FPDF

app = Flask(__name__)
app.secret_key = 'chatbot_secret'

# Text-to-speech engine
engine = pyttsx3.init()

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS chats (user TEXT, message TEXT, response TEXT)''')
    conn.commit()
    conn.close()

init_db()

def get_bot_response(message):
    responses = {
        "hi": "Hello! How can I help you?",
        "what courses are available": "We offer BSCS, BSIT, and BSSE programs.",
        "admission deadline": "Admissions are open till July 30th.",
        "who is the hod": "Dr. Sarwat Nizamani is the HOD of Computer Science.",
        "bye": "Goodbye! Have a nice day."
    }
    return responses.get(message.lower(), "Sorry, I didn't understand that.")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = c.fetchone()
        if user:
            session["user"] = email
            return redirect(url_for("chat"))
        else:
            c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
            conn.commit()
            session["user"] = email
            return redirect(url_for("chat"))
    return render_template("login.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if "user" not in session:
        return redirect(url_for("login"))
    chat_history = []
    if request.method == "POST":
        message = request.form["message"]
        response = get_bot_response(message)
        engine.say(response)
        engine.runAndWait()
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO chats (user, message, response) VALUES (?, ?, ?)", (session["user"], message, response))
        conn.commit()
        conn.close()
        chat_history.append((message, response))
    return render_template("index.html", chat=chat_history)

@app.route("/history")
def history():
    if "user" not in session:
        return redirect(url_for("login"))
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT message, response FROM chats WHERE user=?", (session["user"],))
    rows = c.fetchall()
    return render_template("history.html", history=rows)

@app.route("/download")
def download():
    if "user" not in session:
        return redirect(url_for("login"))
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT message, response FROM chats WHERE user=?", (session["user"],))
    chats = c.fetchall()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for msg, res in chats:
        pdf.cell(200, 10, txt=f"You: {msg}", ln=True)
        pdf.cell(200, 10, txt=f"Bot: {res}", ln=True)
    pdf.output("chat_log.pdf")
    return "Chat saved as PDF!"

@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin123":
            session["admin"] = True
            return redirect(url_for("admin_dashboard"))
    return render_template("admin_login.html")

@app.route("/admin-dashboard")
def admin_dashboard():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT user FROM chats")
    users = c.fetchall()
    c.execute("SELECT user, message, response FROM chats")
    chats = c.fetchall()
    return render_template("admin.html", users=users, chats=chats)

if __name__ == "__main__":
    app.run(debug=True)