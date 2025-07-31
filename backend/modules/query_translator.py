import logging
import json


def translate_for_wolfram(user_prompt, FLASH_MODEL):
    """
    Translate natural language math query into Wolfram Alpha compatible format
    """
    translator_prompt = f"""
        Your job is to translate a user's natural language math query into a direct, computable query suitable for an API like Wolfram|Alpha.
        Extract the core mathematical instruction and the expression.

        Examples:
        - User query: "Can you please find the derivative of f(x) = x^2 + 2x?"
        - Your response: "derivative of x^2 + 2x"

        - User query: "what is the integral of 5x dx, thanks"
        - Your response: "integral of 5x"

        - User query: "I need to know the slope for the line y = 4x - 8"
        - Your response: "slope of y = 4x - 8"

        Now, translate the following query.

        User query: "{user_prompt}"
        Your response:
    """

    translator_response = FLASH_MODEL.generate_content(translator_prompt)
    final_translator_response = translator_response.text
    logging.info(f"Translated query for Wolfram Alpha: {final_translator_response}")

    return final_translator_response


def x_solver_translator(user_prompt, FLASH_MODEL):
    # change this part so it goes to query translator
    # prompt for llm
    logging.info("x_solver_translator running")
    prompt = f"""
    Parse the user's algebra problem into a valid JSON object with three keys: "lhs", "rhs", and "symbol".
    
    CRITICAL RULES:
    - The 'lhs' and 'rhs' values must be strings formatted for Python/SymPy.
    - You MUST explicitly include multiplication operators (*). For example, "2x" must be written as "2*x".
    - Respond with ONLY the raw JSON object and no other text.

    User Prompt: "{user_prompt}"
    JSON Response:
    """
    # llm runs prompt
    response = FLASH_MODEL.generate_content(prompt)
    logging.info("flash model generated content")
    # response is turned into a python dict
    json_string = response.text
    # clean it
    clean_json_string = json_string.strip()
    if clean_json_string.startswith("```json"):
        clean_json_string = clean_json_string.removeprefix("```json").strip()
    if clean_json_string.endswith("```"):
        clean_json_string = clean_json_string.removesuffix("```").strip()

    # try to load json -> python dict
    try:
        algebra_dict = json.loads(clean_json_string)
        logging.info("algebra_dict made successfully")
        return algebra_dict
    except json.JSONDecodeError as e:
        logging.error(
            f"Failed to decode JSON from AI: '{clean_json_string}'. Error: {e}"
        )
        # Raise an exception to signal the failure to the calling function
        raise ValueError("The AI returned an invalid format.") from e


def simplify_translator(user_prompt, FLASH_MODEL):
    # change this part so it goes to query translator
    # prompt for llm
    logging.info("simplify_translator")
    simplify_translator_prompt = f"""
    Your single task is to extract the mathematical expression from the user's query.
    Respond with ONLY the raw mathematical expression, formatted for Python/SymPy.

    CRITICAL RULE: You MUST explicitly include multiplication operators (*). For example, "2x" must be written as "2*x".

    User Query: "{user_prompt}"
    Expression:
    """
    # llm runs prompt
    response = FLASH_MODEL.generate_content(simplify_translator_prompt)
    logging.info("flash model generated content")
    # response is turned into a python dict
    json_string = response.text
    # clean it
    clean_json_string = json_string.strip()
    if clean_json_string.startswith("```json"):
        clean_json_string = clean_json_string.removeprefix("```json").strip()
    if clean_json_string.endswith("```"):
        clean_json_string = clean_json_string.removesuffix("```").strip()

    # try to load json -> python dict
    try:
        logging.info(f"simplify_translator: {clean_json_string}")
        return clean_json_string
    except json.JSONDecodeError as e:
        logging.error(
            f"Failed to decode JSON from AI: '{clean_json_string}'. Error: {e}"
        )
        # Raise an exception to signal the failure to the calling function
        raise ValueError("The AI returned an invalid format.") from e
    # ^^^^^
