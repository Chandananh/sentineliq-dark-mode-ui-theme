import logging
import os
from flask import Flask, request, jsonify
from services.groq_client import GroqClient

# ✅ Create logs folder
if not os.path.exists("logs"):
    os.makedirs("logs")

# ✅ Configure logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
    force=True
)

logging.info("App started")

# ✅ Initialize app
app = Flask(__name__)
client = GroqClient()

# ✅ Home route
@app.route("/", methods=["GET"])
def home():
    return {"message": "AI Service is running"}

# ✅ Health check route (IMPORTANT)
@app.route("/health", methods=["GET"])
def health():
    return {"status": "AI service is running"}

# ✅ Main AI endpoint
@app.route("/generate", methods=["GET", "POST"])
def generate():
    logging.info("Request received")

    # Safe JSON handling
    data = request.get_json(silent=True)

    # If opened in browser (GET)
    if not data:
        logging.warning("No JSON data received")
        return jsonify({"message": "API is working"}), 200

    prompt = data.get("prompt")

    if not prompt:
        logging.warning("Prompt missing")
        return jsonify({"error": "Prompt is required"}), 400

    try:
        result = client.generate_response(prompt)
        logging.info("Response generated successfully")
        return jsonify({"response": result})

    except Exception as e:
        logging.error(f"Error: {e}")
        print("REAL ERROR:", e)   # 👈 shows error in terminal
        return jsonify({"error": "Internal server error"}), 500

# ✅ Security headers
@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers.pop("Server", None)
    return response

# ✅ Global error handler (shows real error)
@app.errorhandler(Exception)
def handle_error(e):
    print("REAL ERROR:", e)
    return {"error": str(e)}, 500

# ✅ Run server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)