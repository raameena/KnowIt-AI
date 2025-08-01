import logging
from flask import jsonify


def handle_file_query(user_prompt, document_text, PRO_MODEL):
    file_prompt = f"""
    Based ONLY on the following document text, provide a clear and concise answer to the user's question.
    If the answer cannot be found in the text, say "I could not find the answer to that in the document."

    --- DOCUMENT CONTEXT ---
    {document_text}
    --- END OF CONTEXT ---

    User's Question: "{user_prompt}"
    Answer:
    """
    logging.info("Processing file query with Gemini Pro")
    response = PRO_MODEL.generate_content(file_prompt)

    json_string = response.text
    # clean it
    clean_json_string = json_string.strip()
    if clean_json_string.startswith("```json"):
        clean_json_string = clean_json_string.removeprefix("```json").strip()
    if clean_json_string.endswith("```"):
        clean_json_string = clean_json_string.removesuffix("```").strip()

    return jsonify({"final_answer": "Let's take a look 🤔", "explanation": clean_json_string})
