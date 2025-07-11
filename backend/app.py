# https://g.co/gemini/share/c240e8e5d3ef // gemini helped me with this entire thing
# import libraries

# os ( operating systems ) python-dotenv import one thing , import gemini ai
import os
from dotenv import load_dotenv
import google.generativeai as genai

from flask import Flask, jsonify, request

# CORS gives server permission to access/be changed from another server
# backend and frontend servers can exist together
from flask_cors import CORS

# loads my .env file with my google api key ( top secret )
load_dotenv()
# loads the variable from env to a usable var for app.py
api_key = os.getenv("GOOGLE_API_KEY")
# configures my ai with variable
genai.configure(api_key=api_key)

# creates app ( __name__ is starting point )
app = Flask(__name__)
# allows the app to be accessed from multiple servers
CORS(app)


# app.route is url page, this is solve endpoint
@app.route("/api/solve", methods=["POST"])
def test():
    # error handeling
    try:
        data = request.get_json()

        # get user's prompt info from front end ( json package )
        user_prompt = data.get("prompt")
        subject = data.get("subject")

        # gemini 1.5 pro model
        model = genai.GenerativeModel("gemini-1.5-pro")

        response = model.generate_content(user_prompt)
        ai_answer = response.text
        try: 
            return jsonify({"answer": ai_answer})
        except Exception as f:
            return jsonify({"error": "ai_answer did not work"})
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500


# __name__ changes to __main__ when website activates
if __name__ == "__main__":
    app.run(debug=True)
