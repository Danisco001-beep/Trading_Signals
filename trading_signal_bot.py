from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "PASTE_YOUR_NEW_TOKEN_HERE"
CHAT_ID   = "6902684806"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, json=payload)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    alert = data.get("alert", "")

    if "BUY" in alert.upper():
        message = (
            "🟢 <b>BUY SIGNAL DETECTED</b>\n\n"
            "📈 EMA 5 &amp; 15 crossed ABOVE SMA 27\n"
            "✅ MACD moving UP from below\n"
            "✅ Stochastic coming UP from oversold\n\n"
            "⏱ <b>Expiry: 3 Minutes</b>\n"
            "⚠️ Check resistance before entering!"
        )
    elif "SELL" in alert.upper():
        message = (
            "🔴 <b>SELL SIGNAL DETECTED</b>\n\n"
            "📉 EMA 5 &amp; 15 crossed BELOW SMA 27\n"
            "✅ MACD moving DOWN from above\n"
            "✅ Stochastic coming DOWN from overbought\n\n"
            "⏱ <b>Expiry: 3 Minutes</b>\n"
            "⚠️ Check resistance before entering!"
        )
    else:
        message = f"📊 Signal: {alert}"

    send_telegram(message)
    return {"status": "ok"}, 200

@app.route("/signal", methods=["GET"])
def signal():
    text = request.args.get("text", "")

    if "BUY" in text.upper():
        message = (
            "🟢 <b>BUY SIGNAL DETECTED</b>\n\n"
            "📈 EMA 5 &amp; 15 crossed ABOVE SMA 27\n"
            "✅ MACD moving UP from below\n"
            "✅ Stochastic coming UP from oversold\n\n"
            "⏱ <b>Expiry: 3 Minutes</b>\n"
            "⚠️ Check resistance before entering!"
        )
    elif "SELL" in text.upper():
        message = (
            "🔴 <b>SELL SIGNAL DETECTED</b>\n\n"
            "📉 EMA 5 &amp; 15 crossed BELOW SMA 27\n"
            "✅ MACD moving DOWN from above\n"
            "✅ Stochastic coming DOWN from overbought\n\n"
            "⏱ <b>Expiry: 3 Minutes</b>\n"
            "⚠️ Check resistance before entering!"
        )
    else:
        message = f"📊 Signal received: {text}"

    send_telegram(message)
    return {"status": "ok"}, 200

@app.route("/")
def home():
    return "Trading Signal Bot is running! ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
