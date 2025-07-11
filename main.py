from flask import Flask, request
import requests

app = Flask(__name__)
BOT_TOKEN = "7619429510:AAFhVN18rurOAgPQgLYo05BUXCF0N7R58Cg"

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    data = request.json
    chat_id = data["message"]["chat"]["id"]
    message = data["message"].get("text", "Không có nội dung")

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": f"Bạn gửi: {message}"}
    )
    return "OK"

@app.route('/', methods=['GET'])
def home():
    return "Bot đang chạy OK"
