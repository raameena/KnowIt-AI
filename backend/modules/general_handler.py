import logging
from flask import jsonify


def handle_general_query(user_prompt, FLASH_MODEL):
    """
    Handle general queries using Gemini Flash
    """
    logging.info("Processing general query with Gemini Flash")
    response = FLASH_MODEL.generate_content(user_prompt)

    return jsonify({"final_answer": "Answer", "explanation": response.text})
