Chatbot Project

📦 Project Overview

This project is a simple chatbot designed to handle basic interactions and provide automated responses. It is structured to be easily extensible for more advanced features.

🚀 Features

Basic chatbot logic

Modular code structure

Easy to extend and customize

🛠️ Installation & Setup

Clone the repository:

git clone <https://github.com/prescottcassy/1stChatbot>
cd chatbot_project

Install the required dependencies:

npm install

Create a .env file for configuration:

cp .env.example .env

Start the server:

node server.js

🗂️ Project Structure

/chatbot-project/  
│── /archive/               # Training data, if applicable
│   ├── dialogs.txt         # Dataset 1
│   ├── label_texts.txt     # Dataset 2 
│   ├── input_texts.txt     # Dataset 3
│── /chatbot.env/           # Environment variables 
│── /__pycache__/           # Documentation files 
│── /static/                # Static assets (images, icons) 
│── /templates/  
│   ├── index.html          # Main application strucuture file 
│── app.py                  # Main application entry point
│── intents.json            # Predefined responses and intents 
│── model.py                # Main chatbot logic
│── my_model.keras          # Last saved model
│── preprocessing.py        # Preprocessing script 
│── README.md               # Project overview and setup instructions 

📄 License

This project is licensed under the MIT License. See the LICENSE file for more details.


