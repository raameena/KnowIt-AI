import logging
import json
from flask import jsonify

def file_planner(user_prompt, document_text, FLASH_MODEL):
    planner_prompt = f"""
    You are a planner for an AI assistant. Analyze the user's query and the provided document context.
    Your task is to determine the 'source' for the answer and the 'topic' of the query.

    Respond with ONLY a valid JSON object with two keys: "source" and "topic".

    - The 'source' can be either "Document" or "General".
    - Use "Document" if the user is asking a question that can likely be answered from the provided text.
    - Use "General" if the question is unrelated to the document.

    - The 'topic' can be one of: "Algebra - Solve", "Algebra - Simplify", "Math - Other", "History", "Casual", or "General".

    ---
    DOCUMENT CONTEXT:
    {document_text}
    ---
    USER PROMPT:
    {user_prompt}
    ---

    JSON RESPONSE:
    """
    try:
        classification = FLASH_MODEL.generate_content(planner_prompt)
        
        json_string = classification.text
        # clean it
        clean_json_string = json_string.strip()
        if clean_json_string.startswith("```json"):
            clean_json_string = clean_json_string.removeprefix("```json").strip()
        if clean_json_string.endswith("```"):
            clean_json_string = clean_json_string.removesuffix("```").strip()

        classification_dict = json.loads(clean_json_string)
        
        logging.info(f"Successfully created file dict as '{classification_dict}'")
        return classification_dict

    except json.JSONDecodeError as e:
        logging.error(f"JSON did not parse correctly. Json: {json_string}")
        raise ValueError("The AI returned an invalid format.") from e


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
