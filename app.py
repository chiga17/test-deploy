from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "<p>Привет, друг! 👋</p><button hx-get='/' hx-target='body'>Назад</button>"

@app.route("/form", methods=["POST"])
def form():
    username = request.form.get("username", "Аноним")
    return f"<p>Рад знакомству, {username}! 🎉</p><button hx-get='/' hx-target='body'>Назад</button>"

# New route for htmx: returns current time
@app.route("/time")
def time():
    now = datetime.now().strftime('%H:%M:%S')
    return f"<p>Текущее время: <b>{now}</b></p>"
