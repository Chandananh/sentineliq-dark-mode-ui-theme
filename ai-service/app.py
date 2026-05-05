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
    level=logging.DEBUG,   # 👈 change INFO → DEBUG
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
    force=True             # 👈 VERY IMPORTANT (fixes issue)
)
logging.info("App started")
app = Flask(__name__)
client = GroqClient()


# ✅ Health check route
@app.route("/", methods=["GET"])
def home():
    return {"message": "AI Service is running"}


# ✅ Main AI endpoint (safe + logging)
@app.route("/generate", methods=["GET", "POST"])
def generate():
    logging.info("Request received")

    # Safe JSON handling (prevents crash)
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
        return jsonify({"error": "Internal server error"}), 500


# ✅ Security headers
@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Content-Security-Policy"] = "default-src 'self'"

    # Remove server info
    response.headers.pop("Server", None)

    return response


# ✅ Global error handler
@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Unhandled Exception: {e}")
    return jsonify({"error": "Something went wrong"}), 500
# ✅ Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)