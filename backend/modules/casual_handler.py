import logging
from flask import jsonify


def handle_casual_query(user_prompt, FLASH_MODEL):
    casual_prompt = f"""
    You are a friendly and helpful AI Homework Helper. The user has just said something casual to you.
    Respond with a short, friendly, and encouraging message that gently guides them back to asking an intellectual question. Keep your response to one or two sentences.
    Try to generate unique responses.
    You can incorporate emojis in your responses.
    
    User's message: "{user_prompt}"
    Your friendly response:
    """
    logging.info("Processing casual query with Gemini Flash")
    response = FLASH_MODEL.generate_content(casual_prompt)

    return jsonify({"final_answer": "📚✏️", "explanation": response.text})
