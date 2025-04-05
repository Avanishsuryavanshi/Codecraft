from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend requests

# 🔑 Replace with your Gemini API key
genai.configure(api_key="AIzaSyBSSM15UJI2976462OCvh2EoCY2QSiZNSk")

# Gemini model setup
model = genai.GenerativeModel("models/gemini-1.5-flash")

@app.route("/explain", methods=["POST"])
def explain_code():
    data = request.get_json()
    code = data.get("code", "")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    prompt = f"Explain the following code in simple terms:\n\n{code}"
    
    try:
        response = model.generate_content(prompt)
        explanation = response.text
        return jsonify({"explanation": explanation})
    except Exception as e:
        print("Gemini Error:", e)
        return jsonify({"error": "Failed to generate explanation"}), 500

if __name__ == "__main__":
    app.run(debug=True)
