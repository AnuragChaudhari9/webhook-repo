import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "webhookDB"
COLLECTION_NAME = "events"
