import logging
from flask import jsonify


def handle_history_query(user_prompt, PRO_MODEL):
    """
    Handle history-related queries using Gemini Pro
    """
    history_prompt = f"""
    You are an expert at history and have a vast knowledge of the past.
    Provide a concise and accurate answer for the following inquiry.
    Inquiry: {user_prompt}
    """

    logging.info("Processing history query")
    response = PRO_MODEL.generate_content(history_prompt)

    return jsonify({"final_answer": "History Answer", "explanation": response.text})
