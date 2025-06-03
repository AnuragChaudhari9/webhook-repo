from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
import config

app = Flask(__name__)

# MongoDB connection
client = MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]
collection = db[config.COLLECTION_NAME]

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.is_json:
        data = request.get_json()
        print("📩 Webhook received:")
        print(data)

        event_type = request.headers.get("X-GitHub-Event")

        if event_type == "push":
            entry = {
                "event_type": "push",
                "author": data["pusher"]["name"],
                "to_branch": data["ref"].split("/")[-1],
                "timestamp": datetime.utcnow()
            }
            collection.insert_one(entry)

        elif event_type == "pull_request":
            pr = data["pull_request"]
            entry = {
                "event_type": "pull_request",
                "author": pr["user"]["login"],
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "timestamp": datetime.utcnow()
            }

            if pr.get("merged"):
                entry["event_type"] = "merge"

            collection.insert_one(entry)

        return jsonify({"msg": "Webhook received"}), 201

    else:
        return jsonify({"error": "Expected JSON"}), 400

@app.route('/')
def home():
    events = list(collection.find().sort("timestamp", -1))  # newest first
    for e in events:
        e["_id"] = str(e["_id"])  # avoid ObjectId issues in HTML
    return render_template("index.html", events=events)

if __name__ == '__main__':
    app.run(debug=True, port=5000)