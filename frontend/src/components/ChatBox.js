import React, { useState } from "react";
import "./ChatBox.css"; // Import CSS file for styling

const ChatBox = () => {
    const [messages, setMessages] = useState([]); // Stores chat messages
    const [input, setInput] = useState(""); // Tracks user input

    const sendMessage = async () => {
        if (!input.trim()) return; // Prevent sending empty messages
    
        const userMessage = { sender: "user", text: input, timestamp: new Date().toLocaleTimeString() };
        
        // Set user message first
        setMessages(prevMessages => [...prevMessages, userMessage]);
    
        try {
            const response = await fetch("http://127.0.0.1:5000/api/get_response", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: input }),
            });
            const data = await response.json();
    
            const botMessage = { sender: "bot", text: data.response, timestamp: new Date().toLocaleTimeString() };
    
            // Add bot response after user message
            setMessages(prevMessages => [...prevMessages, botMessage]);
        } catch (error) {
            console.error("Error:", error);
        }
    
        setInput(""); // Clear input field after sending
    };
    

    return (
        <div className="chat-container">
            <h1>Chatbot</h1>
            <div className="chat-box">
                {messages.map((msg, index) => (
                    <div key={index} className={`message ${msg.sender}`}>
                        <p>{msg.text}</p>
                        <span className="timestamp">{msg.timestamp}</span>
                    </div>
                ))}
            </div>
            <div className="input-box">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Type your message..."
                />
                <button onClick={sendMessage}>Send</button>
            </div>
        </div>
    );
};

export default ChatBox;
