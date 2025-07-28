import os
import psycopg2
from flask import Flask, jsonify
from dotenv import load_dotenv

#load
load_dotenv() 

app = Flask(__name__)
db_url = os.getenv("DATABASE_URL")

# This is the root endpoint to check if the API is running
@app.route("/")
def index():
    return "EduSentry API is alive!"

# This is our critical endpoint for testing the database connection
@app.route("/db_check")
def db_check():
    conn = None
    try:
        # Try to connect to the database
        conn = psycopg2.connect(db_url)
        conn.close() # Immediately close the connection
        # If successful, return a success message
        return jsonify({"status": "success", "message": "Database connection successful."})
    except Exception as e:
        # If it fails, return an error message
        return jsonify({"status": "error", "message": f"Database connection failed: {e}"}), 500