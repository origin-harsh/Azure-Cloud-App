from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} | Flask Azure Demo</title>
    <style>
        :root { --bg: #0b1220; --panel: #121d31; --accent: #38bdf8; --text: #e5eefb; --muted: #9fb0c8; }
        * { box-sizing: border-box; }
        body { margin: 0; font-family: system-ui, Arial, sans-serif; background: radial-gradient(circle at top, #17345a, var(--bg) 60%); color: var(--text); min-height: 100vh; }
        header { padding: 28px 20px; text-align: center; }
        header p { color: var(--muted); }
        main { width: min(1000px, 92%); margin: 0 auto 40px; }
        .hero, .card { background: rgba(18,29,49,.92); border: 1px solid #263b59; border-radius: 18px; padding: 24px; box-shadow: 0 12px 32px #0003; }
        .hero { text-align: center; }
        h1 { margin: 0 0 10px; font-size: clamp(2rem, 5vw, 3.2rem); }
        .accent { color: var(--accent); }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-top: 18px; }
        .card h2 { margin-top: 0; font-size: 1.15rem; }
        a, button { color: #06111f; background: var(--accent); border: 0; border-radius: 10px; padding: 10px 14px; font-weight: 700; text-decoration: none; cursor: pointer; display: inline-block; }
        .muted { color: var(--muted); }
        pre { white-space: pre-wrap; overflow-wrap: anywhere; background: #07101d; border-radius: 10px; padding: 12px; color: #a7f3d0; }
        footer { text-align: center; padding: 20px; color: var(--muted); }
        #clock { font-size: 1.8rem; font-weight: 700; }
    </style>
</head>
<body>
    <header>
        <h1><span class="accent">Flask</span> + Azure App Service</h1>
        <p>A small demo application for practicing cloud deployment.</p>
    </header>
    <main>
        <section class="hero">
            <h2>{{ title }}</h2>
            <p>{{ message }}</p>
            <p class="muted">This page is being served by a Flask endpoint.</p>
            <a href="/about">About this app</a>
            <a href="/api/status">View API status</a>
        </section>
        <section class="grid">
            <article class="card">
                <h2>Endpoint 1: Home</h2>
                <p class="muted">GET /</p>
                <p>Returns this HTML page with CSS and JavaScript.</p>
            </article>
            <article class="card">
                <h2>Endpoint 2: About</h2>
                <p class="muted">GET /about</p>
                <p>Returns a second HTML page.</p>
            </article>
            <article class="card">
                <h2>Endpoint 3: Health</h2>
                <p class="muted">GET /health</p>
                <p>Useful for checking whether the app responds.</p>
            </article>
            <article class="card">
                <h2>Endpoint 4: API status</h2>
                <p class="muted">GET /api/status</p>
                <p>Returns JSON that you can inspect in a browser.</p>
            </article>
        </section>
        <section class="card" style="margin-top:16px">
            <h2>JavaScript demo clock</h2>
            <div id="clock">Loading...</div>
            <p class="muted">This clock runs in your browser.</p>
            <button onclick="showMessage()">Test JavaScript</button>
            <p id="js-message"></p>
        </section>
    </main>
    <footer>Flask Azure Demo · Built for deployment practice</footer>
    <script>
        function updateClock() {
            document.getElementById("clock").textContent =
                new Date().toLocaleTimeString();
        }
        function showMessage() {
            document.getElementById("js-message").textContent =
                "JavaScript is working. Your page loaded successfully!";
        }
        updateClock();
        setInterval(updateClock, 1000);
    </script>
</body>
</html>
"""

ABOUT_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>About | Flask Azure Demo</title>
<style>
body{font-family:Arial,sans-serif;background:#f3f7fb;color:#172033;margin:0;padding:40px}
main{max-width:720px;margin:auto;background:white;padding:28px;border-radius:16px;box-shadow:0 8px 28px #10204018}
h1{color:#0369a1}li{margin:10px 0}a{color:#0369a1}
</style>
</head>
<body><main>
<h1>About this Flask application</h1>
<p>This is a lightweight Flask app created to practice deploying a Python web application to Azure App Service.</p>
<ul><li>Python + Flask backend</li><li>HTML, CSS and JavaScript frontend</li><li>JSON API endpoint</li><li>Health-check endpoint</li></ul>
<p><a href="/">← Back to home</a></p>
</main></body></html>
"""


@app.get("/")
def home():
    return render_template_string(
        PAGE,
        title="Your app is running!",
        message="Welcome — this Flask application is ready for deployment practice."
    )


@app.get("/about")
def about():
    return render_template_string(ABOUT_PAGE)


@app.get("/health")
def health():
    return jsonify(status="healthy", app="flask-azure-demo"), 200


@app.get("/api/status")
def api_status():
    return jsonify(
        application="Flask Azure Demo",
        status="running",
        endpoints=["/", "/about", "/health", "/api/status", "/api/greeting"]
    ), 200


@app.get("/api/greeting")
def greeting():
    return jsonify(message="Hello from Flask!", purpose="Azure deployment practice"), 200


if __name__ == "__main__":
    # Local development only. Azure App Service uses its production startup command.
    app.run(host="0.0.0.0", port=8000, debug=True)
