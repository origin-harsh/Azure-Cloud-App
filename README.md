# Flask Azure Demo

A small Flask application with five endpoints for Azure App Service deployment practice.

## Endpoints

- `GET /` — HTML page with CSS and JavaScript
- `GET /about` — About page
- `GET /health` — health-check JSON
- `GET /api/status` — app status JSON
- `GET /api/greeting` — greeting JSON

## Run locally

```bash
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install dependencies and run:

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:8000`.

## Azure App Service startup command

For a Linux App Service using a supported Python runtime, set the startup command to:

```bash
gunicorn --bind=0.0.0.0 --timeout 600 app:app
```

Deploy `app.py` and `requirements.txt` (or the complete project folder). Do not use Flask's debug server for production.
