from flask import Flask, request, jsonify, render_template, redirect, url_for
import cohere
import pandas as pd
import random

app = Flask(__name__)
app.secret_key = "secretkey123"

# Cohere API initialization
co = cohere.Client("N244KmHCu2Ua93qwLcGIsxPpS6aGCfqqSazh3WtQ")

# Load responses from CSV
data = pd.read_csv("doubtslayer_prompts_500.csv")
prompts = data.to_dict(orient="records")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat')
def chat():
    return render_template("chat.html", username="Warrior")

@app.route('/chat', methods=['POST'])
def chat_api():
    user_input = request.json.get("message", "")
    trigger_keywords = [
        "fail", "not good", "can't", "scared", "doubt",
        "worthless", "burnout", "overthinking", "quit", "tired"
    ]

    if any(word in user_input.lower() for word in trigger_keywords):
        bot_reply = random.choice(prompts)['bot_response']
    else:
        prompt = (
            "You're Self-DoubtSlayer — a confident, no-nonsense motivational coach. "
            "You challenge people firmly but with purpose. You're honest and direct, but not cruel. "
            "You don't tolerate self-pity or excuses, but you believe in building people up. "
            "Speak with authority and clarity. Push them to act, but show that you believe in their ability to grow.\n"
            f"User: {user_input}\nDoubtSlayer:"
        )

        response = co.generate(
            model="command-xlarge",
            prompt=prompt,
            max_tokens=300,
            temperature=0.9
        )
        bot_reply = response.generations[0].text.strip()

    return jsonify({"reply": bot_reply})

@app.route('/logout')
def logout():
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
