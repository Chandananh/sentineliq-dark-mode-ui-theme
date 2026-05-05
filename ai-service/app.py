from flask import Flask, request, jsonify
from services.groq_client import GroqClient

app = Flask(__name__)

client = GroqClient()


# ✅ Health check route
@app.route("/", methods=["GET"])
def home():
    return {"message": "AI Service is running"}


# ✅ Main AI endpoint
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    result = client.generate_response(prompt)

    return jsonify({"response": result})

@app.after_request
@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Content-Security-Policy"] = "default-src 'self'"

    # ✅ REMOVE server header
    response.headers.pop("Server", None)

    return response
# ✅ Run server
if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000)