from flask import Flask, render_template, request, jsonify
import model

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Load the correct file

@app.route("/chatbot", methods=["POST"])
def chatbot_response():
    user_message = request.json.get("message")
    bot_reply = model.chatbot_response(user_message)  # Call the function in `model.py`
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
