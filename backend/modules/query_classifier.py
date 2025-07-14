import json
import logging


def classify_query(user_prompt, FLASH_MODEL):
    """
    Classify user query into categories: Algebra, Math-Other, History, or General
    """
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

    try:
        classification = FLASH_MODEL.generate_content(router_prompt)
        json_string = classification.text
        classification_dict = json.loads(json_string)
        category = classification_dict.get("category")

        logging.info(f"Successfully classified query as '{category}'")
        return category

    except json.JSONDecodeError as e:
        logging.error(f"JSON did not parse correctly. Json: {json_string}")
        raise ValueError("The AI returned an invalid format.") from e
