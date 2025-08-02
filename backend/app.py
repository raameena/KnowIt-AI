# https://g.co/gemini/share/c240e8e5d3ef // gemini helped me with this entire thing

# import libraries

# os ( operating systems ) python-dotenv import one thing , import gemini ai
import logging
import json
import os
import requests
import PyPDF2
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask, jsonify, request
from database import (
    init_db, 
    update_database, 
    get_text_from_session,
    delete_session
)

# CORS gives server permission to access/be changed from another server
# backend and frontend servers can exist together
from flask_cors import CORS
from sympy.core import parameters
from modules import (
    algebra_solver,
    wolfram_api_solver,
    tutor,
    query_classifier,
    query_translator,
    casual_handler,
    history_handler,
    general_handler,
    file_handler,
)

# set up my logging in console
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

# loads my .env file with my google api key ( top secret )
load_dotenv()
# loads the variable from env to a usable var for app.py

# gemini api
gemini_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=gemini_api_key)
FLASH_MODEL = genai.GenerativeModel("gemini-1.5-flash")
PRO_MODEL = genai.GenerativeModel("gemini-1.5-pro")

# creates app ( __name__ is starting point )
app = Flask(__name__)
# allows the app to be accessed from multiple servers
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 
init_db()


# app.route is url page, this is solve endpoint
@app.route("/api/solve", methods=["POST"])
def solve_query():
    """Main endpoint to handle and route user queries"""
    try:
        data = request.get_json()
        user_prompt = data.get("prompt")
        session_id = data.get("sessionId")
        document_text = get_text_from_session(session_id)
        subject = data.get("subject")  # NULL for now (will use later)
        logging.info("Checking for document.")

        if document_text:
            plan = file_handler.file_planner(user_prompt, document_text, FLASH_MODEL)
            source = plan.get("source")
            topic = plan.get("topic")

            if source == "Document":
                return file_handler.handle_file_query(user_prompt, document_text, PRO_MODEL)
            else:
                if topic == "Algebra - Solve for Variable":
                    return algebra_solver.solve_algebra_problem(
                user_prompt, FLASH_MODEL, PRO_MODEL)

                elif topic == "Algebra - Simplify":
                    return algebra_solver.simplify_algebra_problem(
                        user_prompt, FLASH_MODEL, PRO_MODEL
                    )

                elif topic == "Math - Other":
                    translated_query = query_translator.translate_for_wolfram(
                        user_prompt, FLASH_MODEL
                    )
                    wolfram_answer = wolfram_api_solver.wolframalpha(translated_query)
                    return tutor.tutor_response(translated_query, wolfram_answer, PRO_MODEL)

                elif topic == "History":
                    return history_handler.handle_history_query(user_prompt, PRO_MODEL)

                elif topic == "General":
                    return general_handler.handle_general_query(user_prompt, FLASH_MODEL)

                elif topic == "Casual":
                    return casual_handler.handle_casual_query(user_prompt, FLASH_MODEL)

        # Classify the query
        category = query_classifier.classify_query(user_prompt, FLASH_MODEL)
        logging.info(f"Query classified as: {category}")

        # Route to appropriate handler
        if category == "Algebra - Solve for Variable":
            return algebra_solver.solve_algebra_problem(
                user_prompt, FLASH_MODEL, PRO_MODEL
            )

        elif category == "Algebra - Simplify":
            return algebra_solver.simplify_algebra_problem(
                user_prompt, FLASH_MODEL, PRO_MODEL
            )

        elif category == "Math - Other":
            translated_query = query_translator.translate_for_wolfram(
                user_prompt, FLASH_MODEL
            )
            wolfram_answer = wolfram_api_solver.wolframalpha(translated_query)
            return tutor.tutor_response(translated_query, wolfram_answer, PRO_MODEL)

        elif category == "History":
            return history_handler.handle_history_query(user_prompt, PRO_MODEL)

        elif category == "General":
            return general_handler.handle_general_query(user_prompt, FLASH_MODEL)

        elif category == "Casual":
            return casual_handler.handle_casual_query(user_prompt, FLASH_MODEL)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/upload", methods=["POST"])
def upload_doc():
    try:
        if "file" not in request.files:
            return jsonify({"error": "PDF was not sent to request."})

        file = request.files["file"]
        session_ID = request.form.get("sessionId")
        if file.filename == " ":
            return jsonify({"error": "No PDF has been selected."})

        if file and file.filename.endswith(".pdf"):
            reader = PyPDF2.PdfReader(file.stream)
            full_text = " "
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    full_text += page_text + "\n"
            logging.info("Successfully extracted text from PDF")

            update_database(session_ID, full_text)

            return jsonify({"message": "File uploaded successfully!"})
        else:
            return jsonify(
                {"error": "Invalid file type selected, please select a PDF."}
            )
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/api/clear_session", methods=["POST"])
def delete_user_session():
    try:
        data = request.get_json()
        session_ID = data.get("sessionId")
        
        if session_ID:
            delete_session(session_ID)
            return jsonify({"message": "Session cleared successfully."})
        else:
            return jsonify({"error": "Session ID missing."})
    except Exception as e:
        logging.error(f"Error in clear_session endpoint: {e}")
        return jsonify({"error": str(e)}), 500

# __name__ changes to __main__ when website activates
if __name__ == "__main__":
    app.run(debug=True, port=5001)
