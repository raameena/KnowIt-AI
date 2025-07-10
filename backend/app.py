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
@app.route("/api/solve", methods=['POST'])
def test():
    # jsonify sends a json package to website
    # basically makes object with key (message) that says hi
    # return("hi") would print hi in html on website
    data = request.get_json()
    user_promt = data.get('prompt')
    subject = data.get('subject')
    return jsonify({'message': 'hi'})

# __name__ changes to __main__ when website activates 
if __name__ == "__main__":
    app.run(debug=True)
