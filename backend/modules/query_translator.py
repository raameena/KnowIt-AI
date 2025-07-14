import logging


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
