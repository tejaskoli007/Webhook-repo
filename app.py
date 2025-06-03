from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
import datetime

app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017")  # Adjust URI if needed
mongo_db = client["webhook_db"]
collection = mongo_db["events"]

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        if not request.is_json:
            return "Invalid content-type, expecting JSON", 400
        
        data = request.get_json()
        timestamp = datetime.datetime.utcnow()  # Store as datetime object

        # Check if this is a pull request merge event
        if data.get("action") == "closed" and data.get("pull_request", {}).get("merged") is True:
            event_type = "pull_request_merged"
            repository = data.get("repository", {}).get("full_name", "unknown")
            author = data.get("sender", {}).get("login", "unknown")
        else:
            event_type = data.get("action", "unknown")
            repository = data.get("repository", {}).get("full_name", "unknown")
            author = data.get("sender", {}).get("login", "unknown")

        event_doc = {
            "author": author,
            "event_type": event_type,
            "repository": repository,
            "timestamp": timestamp
        }
        
        try:
            collection.insert_one(event_doc)
            print(f"Stored event in MongoDB: {event_doc}")
        except Exception as e:
            print(f"Error storing event: {e}")
            return "Failed to store event", 500
        
        return "Event received", 200

@app.route("/api/events")
def api_events():
    events = list(collection.find().sort("timestamp", -1))
    for e in events:
        e["_id"] = str(e["_id"])
        # Convert Mongo datetime to ISO string for JSON serialization
        if "timestamp" in e and isinstance(e["timestamp"], datetime.datetime):
            e["timestamp"] = e["timestamp"].isoformat()
    return jsonify(events)

if __name__ == "__main__":
    app.run(debug=True)
