import os
import psycopg2
from flask import Flask, jsonify
from dotenv import load_dotenv

#load
load_dotenv() 

app = Flask(__name__)
db_url = os.getenv("DATABASE_URL")

#checker endpoint to verify the API is running
@app.route("/")
def index():
    return "EduSentry API is alive!"

#checker endpoint to verify the database connection
@app.route("/db_check")
def db_check():
    conn = None
    try:
        # connec to database
        conn = psycopg2.connect(db_url)
        conn.close()
        # success!1!1
        return jsonify({"status": "success", "message": "Database connection successful."})
    except Exception as e:
        # err err err
        return jsonify({"status": "error", "message": f"Database connection failed: {e}"}), 500