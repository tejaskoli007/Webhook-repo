# Webhook-repo

This repository contains a Flask-based webhook server that listens for GitHub webhook events, stores them in a MongoDB database, and displays recent events in a dynamic web UI.

## Features
- Receives GitHub webhook events via `/webhook` POST endpoint.
- Supports storing event data including repository name, event type, sender, and timestamp in MongoDB.
- Serves a frontend UI at `/` displaying recent events in a table.
- Frontend dynamically fetches and refreshes events using AJAX every 10 seconds.
- Proper handling of JSON payloads and timestamps (stored in UTC).
- Distinct display for "merge" events to highlight them (optional feature implemented).
- Code includes error handling and validation for incoming requests.

## Prerequisites
- Python 3.8 or newer
- MongoDB (locally installed or cloud instance such as MongoDB Atlas)
- `pip` for Python package management

## Installation

1. Clone the repository:

    ```bash
    git clone <your-webhook-repo-url>
    cd webhook-repo
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Linux/macOS
    venv\Scripts\activate      # On Windows
    ```

3. Install required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure MongoDB is running and accessible. The default connection URI is:

    ```
    mongodb://localhost:27017
    ```

    Modify the URI in `app.py` if using a remote or cloud database.

## Running the Server

```bash
python app.py

## The server will start on http://localhost:5000.

Testing
You can manually POST test webhook events using tools like curl or Invoke-RestMethod in PowerShell:

bash
Copy
curl.exe -X POST http://localhost:5000/webhook -H "Content-Type: application/json" -d "{\"repository\": {\"full_name\": \"test/repo\"}, \"action\": \"test_event\", \"sender\": {\"login\": \"tester\"}}"
Access the UI in your browser at http://localhost:5000/ to see received events.

For live webhook testing, configure your GitHub repository to send events to your public URL (using ngrok or hosted deployment).

Notes
Timestamp of events is stored and displayed in UTC.

The frontend currently displays all events without filtering for freshness; you can enable filtering in index.html.

To highlight merge events distinctly, the UI styles and display logic have been updated accordingly.

For local development behind NAT/firewalls, tools like ngrok are recommended to expose your local server publicly.

Author
Tejas Koli
