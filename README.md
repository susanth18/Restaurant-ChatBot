# Restaurant-ChatBot
# Overview
 The Restaurant Chatbot is a Python-based conversational interface built using Dialogflow, FastAPI, and MySQL. It allows users to interact with a restaurant's ordering system through natural language conversation. Users can place new orders, add items to existing orders, remove items from orders, and track the status of their orders.
# Features
 Natural Language Processing: Utilizes Dialogflow for understanding user input and generating appropriate responses. Created appropriate intents, entities and established contexts among them.
 Order Management: Allows users to place new orders, add items to existing orders, and remove items from orders.
 Order Tracking: Provides users with the ability to track the status of their orders.
 Persistent Storage: Stores order and food item details in a MySQL database for future reference and analysis.
 FastAPI Backend: Implements the backend using FastAPI, providing a robust and efficient API for communication between the chatbot and the database.
 # Technologies Used
 Python
 Dialogflow
 FastAPI
 MySQL
# Installation and Usage
 1. Clone the repository.
 2. Install dependencies using the command "pip install fastapi mysql-connector-python uvicorn easydict"
 3. Download and install ngrok to the project folder. Download link: https://ngrok.com/download
 4. Setup the MySQL database: Create a MySQL database and import the provided SQL schema (restaurant_schema.sql) to create necessary tables.
 5. Set up Dialogflow: Create a Dialogflow agent. Set up intents, entities, and fulfillment to interact with the FastAPI backend.
 6. Run the FastAPI server: uvicorn main:app --reload
 7. Connect FastAPI backend with Dialogflow using ngrok: Run ngrok to expose the FastAPI server to the internet. "ngrok http 8000". Update the fulfillment URL in Dialogflow with the ngrok URL.
# Acknowledgements
Special thanks to the developers of Dialogflow, FastAPI, and MySQL for providing excellent tools and documentation.

