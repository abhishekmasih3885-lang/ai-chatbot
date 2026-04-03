chat_history = []

@app.route("/get", methods=["POST"])
def chat():
    user_msg = request.form["msg"]

    chat_history.append({"role": "user", "content": user_msg})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history
    )

    reply = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": reply})

    return jsonify({"response": reply})
