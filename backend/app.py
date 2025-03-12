from flask import Flask, request, jsonify  # type: ignore
from flask_cors import CORS  # type: ignore

app = Flask(__name__)
CORS(app)  # Allow frontend and backend to communicate across ports

# Simple in-memory conversation history (for current session only)
chat_history = []

# Predefined chatbot responses
def chatbot_logic(user_message):
    user_message = user_message.lower()

    responses = {
        "hello": "Hi there! How can I assist you today?",
        "hi": "Hello! How's your day going?",
        "how are you": "I'm just a bot, but I'm here to help! How about you?",
        "what's your name": "I'm ChatBot 1.0, your virtual assistant!",
        "who created you": "I was created by Calvin, a software engineer passionate about AI!",
        "bye": "Goodbye! Have a great day!",
        "thanks": "You're welcome! Let me know if you need anything else! 😊",
        "help": "Sure! You can ask me anything about programming, tech, or just chat casually.",
    }

    # Default response if input isn't found in predefined responses
    return responses.get(user_message, "I'm not sure how to respond to that 🤖, but I'm learning!")

# Route for the root URL
@app.route("/")
def home():
    return "Welcome to the Chatbot Backend!"

# API endpoint for chatbot responses
@app.route("/api/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"response": "I didn't catch that. Can you repeat?"})

    bot_response = chatbot_logic(user_message)

    # Store the conversation history (can be replaced with a database later)
    chat_history.append({"user": user_message, "bot": bot_response})

    return jsonify({"response": bot_response})

# Route to get chat history (optional, can be used in frontend later)
@app.route("/api/get_history", methods=["GET"])
def get_history():
    return jsonify({"chat_history": chat_history})

if __name__ == "__main__":
    app.run(debug=True)
