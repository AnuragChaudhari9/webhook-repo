# webhook-repo

Flask webhook receiver for GitHub events — logs `push`, `pull_request`, and `merge` events into MongoDB and displays them in a simple UI.

## Features

- Receives GitHub webhook events
- Stores them in MongoDB
- Displays events on a Flask dashboard

---

## Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/AnuragChaudhari9/webhook-repo.git
cd webhook-repo
```
### 2. Create and activate virtual environment (Windows)
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Start MongoDB (must be running on localhost:27017)
Make sure MongoDB service is running locally. You can verify via MongoDB Compass or CLI.

### 5. Run the Flask app
```bash
python app.py
```
App will be available at:
http://127.0.0.1:5000

## Webhook Integration (for testing)
Use ngrok to expose your local server:

```bash
ngrok http 5000
```
In your GitHub repo settings (e.g. action-repo):

- Go to Settings > Webhooks

- Payload URL: https://your-ngrok-url/webhook

- Content type: application/json

- Select events: push, pull_request

## View Events
Open the dashboard in your browser:

```cpp
http://127.0.0.1:5000
```
You'll see a table showing all received events in reverse chronological order.
