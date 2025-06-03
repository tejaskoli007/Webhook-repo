# Webhook-repo
This repository contains a Flask-based webhook server that listens for GitHub webhook events, stores them in a MongoDB database, and displays recent events in a web UI.
## Features
- Receives GitHub webhook events via `/webhook` endpoint.
- Stores event data (repository, event type, sender, timestamp) in MongoDB.
- Serves a simple front-end UI at `/` showing latest events in a table.
- Uses AJAX to fetch and update events dynamically.
- Proper handling of JSON payloads and date formatting.

## Prerequisites
- Python 3.8+
- MongoDB (local or cloud, e.g., MongoDB Atlas)
- `pip` for installing Python packages

## Installation
1. Clone the repository:

   ```bash
   git clone <your-webhook-repo-url>
   cd webhook-repo

2. Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate       # Linux/Mac
   venv\Scripts\activate          # Windows

3. Install required packages:
   pip install -r requirements.txt

4. Make sure MongoDB is running and accessible at the URI defined in app.py. (Default: mongodb://localhost:27017)

## Running the Server
    python app.py
## Testing
Use curl or GitHub Actions to POST events to http://localhost:5000/webhook.

View logged events in the browser at /.

## Notes
Make sure to configure your GitHub repository webhook to point to your server URL.

For local development behind a firewall or NAT, use tools like ngrok to expose your localhost.

## Author
## Tejas Koli
