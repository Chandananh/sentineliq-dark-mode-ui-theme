Day 18 - AI Developer 2 Demo Notes

Flask + Groq 60-Second Explanation

Our AI service is built using Flask and the Groq API.

Flask is used as the backend framework to create API endpoints like /generate and /health. These endpoints allow the frontend or test scripts to send prompts and receive AI-generated responses.

Groq provides fast AI inference using the Llama language model. When a user sends a prompt, Flask receives the request, sends it to the Groq API, and returns the generated response in JSON format.

This setup helps create a lightweight and fast AI service for recommendation and report generation.