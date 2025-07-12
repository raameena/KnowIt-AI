# https://g.co/gemini/share/c240e8e5d3ef // gemini helped me with this entire thing

# import libraries

# os ( operating systems ) python-dotenv import one thing , import gemini ai
import logging
import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

from flask import Flask, jsonify, request

# CORS gives server permission to access/be changed from another server
# backend and frontend servers can exist together
from flask_cors import CORS
from modules import algebra_solver

# set up my logging in console
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

# loads my .env file with my google api key ( top secret )
load_dotenv()
# loads the variable from env to a usable var for app.py
api_key = os.getenv("GOOGLE_API_KEY")
# configures my ai with variable
genai.configure(api_key=api_key)

# gemini 1.5 pro model
FLASH_MODEL = genai.GenerativeModel("gemini-1.5-flash")
PRO_MODEL = genai.GenerativeModel("gemini-1.5-pro")

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
        subject = data.get("subject")  # NULL for now ( will use later ;)
        # classifying user's prompt
        router_prompt = f"""
            Your task is to classify the user's query into one of the following specific categories:
            "Algebra - Solve for Variable", "Math - Other", "History", or "General".
            You must respond with a single, valid JSON object with one key: "category".

            - If the user is asking to find the value of a specific variable in an equation (e.g., "solve for x", "what is y?"), classify it as "Algebra - Solve for Variable".
            - If it's any other type of math or science question (like finding a slope, a derivative, a chemical property, etc.), classify it as "Math - Other".
            - Use "History" for history questions and "General" for all other queries.

            Examples:
            - Query: "who was the first president of the united states?"
            - Response: {{"category": "History"}}

            - Query: "what is the integral of 2x dx?"
            - Response: {{"category": "Math - Other"}}

            - Query: "solve for y in 3y - 12 = 0"
            - Response: {{"category": "Algebra - Solve for Variable"}}

            - Query: "what is the capital of nepal?"
            - Response: {{"category": "General"}}

            Now, classify the following query.

            Query: "{user_prompt}"
            IMPORTANT: Your entire response must be ONLY the raw JSON object, without any surrounding text or markdown.
            Response:
        """

        # make put the router_prompt into llm
        classification = FLASH_MODEL.generate_content(router_prompt)
        # make llms response a python useable dictionary
        json_string = classification.text
        try:
            classification_dict = json.loads(json_string)
        except json.JSONDecodeError as e:
            logging.error(
                "JSON did not parse into python right. Json: %s", {json_string}
            )
            return jsonify({"error": "The AI returned an invalid format."}), 500

        # put categories in their own vars
        category = classification_dict.get("category")

        logging.info(f"Successfuly parsed: category as '{category}'")

        final_prompt = ""
        if category == "Algebra - Solve for Variable":
            algebra_solution_data = algebra_solver.solve_algebra_problem(
                user_prompt, FLASH_MODEL, PRO_MODEL
            )
            logging.info("algebra solver worked.")
            return jsonify(algebra_solution_data)
        elif category == "History":
            final_prompt = f"""
            You are a expert at history and have a vast knowledge of the past.
            Provide a concise and accurate answer for the following inquiry.
            Inquiry: {user_prompt}
            """
            logging.info("history prompt worked")
            response = PRO_MODEL.generate_content(final_prompt)
            return jsonify(
                {"final_answer": "History Answer", "explanation": response.text}
            )
        else:
            final_prompt = user_prompt
            response = FLASH_MODEL.generate_content(final_prompt)
            return jsonify({"final_answer": "Answer", "explanation": response.text})
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500


# __name__ changes to __main__ when website activates
if __name__ == "__main__":
    app.run(debug=True)
