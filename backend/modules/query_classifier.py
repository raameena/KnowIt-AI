import json
import logging


def classify_query(user_prompt, FLASH_MODEL):
    """
    Classify user query into categories: Algebra, Math-Other, History, or General
    """
    router_prompt = f"""
        Classify the following query into ONE of these categories:
        ["Math - Other" ( doesn't solve for letter variable or need simplification for polynomials ), "Algebra - Solve for Variable", 
        "Algebra - Simplify", "History", "General" ( for legitimate inquiry questions ), "Casual" ( small talk or other conversation )]

        Respond with a single JSON object: {{"category": "CLASSIFICATION"}}

        Query: "{user_prompt}"
        Response:
        """

    try:
        classification = FLASH_MODEL.generate_content(router_prompt)
        
        json_string = classification.text
        # clean it
        clean_json_string = json_string.strip()
        if clean_json_string.startswith("```json"):
            clean_json_string = clean_json_string.removeprefix("```json").strip()
        if clean_json_string.endswith("```"):
            clean_json_string = clean_json_string.removesuffix("```").strip()

        classification_dict = json.loads(clean_json_string)
        category = classification_dict.get("category")
        
        logging.info(f"Successfully classified query as '{category}'")
        return category

    except json.JSONDecodeError as e:
        logging.error(f"JSON did not parse correctly. Json: {json_string}")
        raise ValueError("The AI returned an invalid format.") from e
