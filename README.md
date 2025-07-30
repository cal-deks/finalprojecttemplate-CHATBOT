# Chatbot Template

Welcome to the Chatbot Template! This project provides a starter template for building a chatbot using **React** (frontend) and **Flask** (backend). It's designed for fellows to extend and customize to fit their needs, whether it's creating a customer support bot, a personal assistant, or something entirely unique!

## Overview
This template includes:
- A **React frontend** with a basic chat interface.
- A **Flask backend** that processes user messages.
- Example code to demonstrate how the frontend and backend communicate

Fellows can customize the:
1. **Frontend** to change the design and add features
2. **Backend** to enhance the bot’s logic or connect to APIs/AI models.


## Getting Started

### Prerequisites
Make sure you have the following installed:
1. **Python 3.7+**: [Download Python](https://www.python.org/downloads/)
2. **Node.js**: [Download Node.js](https://nodejs.org/)

---

### Setup Instructions

#### Backend (Flask)
cd backend
pip install -r requirements.txt
python app.py

Once running, the backend will be available at:
http://127.0.0.1:5000

---

#### Frontend (React)
cd frontend
npm install
npm start

Once running, the frontend will be available at:
http://localhost:3000

---

### Testing
1. Open the frontend at `http://localhost:3000`.
2. Type a message in the chatbox and click **Send**.
3. The message will be sent to the backend at `http://127.0.0.1:5000/api/get_response`, and you’ll see the bot’s response in the chatbox.

---

### Customization Tips
- **Frontend**: Modify the chat interface in `frontend/src/components/ChatBox.js`.
- **Backend**: Update the chatbot logic in `backend/app.py` to make the bot smarter or connect it to an API.

---

### What Can You Do with This Template?

1. **Customer Support Bot**  
   - Help users by answering FAQs, providing guidance, or troubleshooting common issues.

2. **Educational Assistant**  
   - Build a bot that helps users learn, provides study resources, or explains concepts.

3. **Data-Driven Application**  
   - Connect the bot to APIs like weather, news, or financial data to provide real-time information.

---

Feel free to customize and expand on these ideas to make the chatbot your own!
Chatbot project is running successfully!
