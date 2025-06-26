# 🎓 AI-Based Chatbot for University Student Inquiry and Academic Support

This is a Flask-based AI chatbot project designed for university students. It helps them get quick answers to academic queries like admission deadlines, course details, departmental info, and more — with support for voice input, PDF saving, and admin monitoring.

---

## 🔍 Features

✅ Text-based chatbot  
✅ Voice input + Bot speech reply  
✅ Save chat as PDF  
✅ Chat history per user  
✅ Login/Register system  
✅ Admin dashboard to view all users & chats  
✅ Dark-themed UI (CSS styled)  
✅ Deployed via Render.com for public access

---

## 🛠️ Technologies Used

- Python 3.8  
- Flask  
- SQLite  
- pyttsx3 (text-to-speech)  
- SpeechRecognition  
- fpdf (chat PDF logs)  
- HTML + CSS (custom dark UI)  
- Gunicorn (for deployment)  
- Render.com (free cloud hosting)

---

## 📂 Folder Structure

```
/project-root/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Procfile                # Render deployment config
├── render.yaml             # Render auto-deploy settings
│
├── templates/              # All HTML pages
│   ├── login.html
│   ├── index.html
│   ├── admin.html
│   ├── admin_login.html
│   └── history.html
│
├── static/
│   └── style.css           # CSS file
```

---

## 🔐 Admin Login

- **Username:** `admin`  
- **Password:** `admin123`  
- Admin can view all user chats and total activity.

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/yourusername/university-chatbot.git
cd university-chatbot
pip install -r requirements.txt
python app.py
```

Then visit `http://127.0.0.1:5000` in your browser.

---

## 🌍 Live Deployment (Render)

1. Upload this repo to GitHub  
2. Go to [https://render.com](https://render.com)  
3. Connect GitHub → Deploy Web Service  
4. Render will automatically use:
   - `requirements.txt`
   - `Procfile`
   - `render.yaml`

🎉 App is LIVE!

---

## 👤 Project By

**Abu Hassaan Khan Ghouri**  
**University of Mirpurkhas**  
**Supervisor:** Dr. Sarwat Nizamani  
**Department:** Computer Science (2k22/MKCS/02)
