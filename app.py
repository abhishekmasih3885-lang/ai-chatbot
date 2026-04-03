from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

# 🔑 Put your OpenAI API key here
client = OpenAI(api_key="sk-")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_msg = request.form["msg"]

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # fast & cheap
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_msg}
            ]
        )

        reply = response.choices[0].message.content
        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"response": "Error: " + str(e)})

if __name__ == "__main__":
    app.run(debug=True)
