import json
import logging
from sympy import sympify, Symbol, Eq, solveset
from dotenv import load_dotenv
import google.generativeai as genai

from flask import Flask, jsonify, request

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def solve_algebra_problem(user_prompt, FLASH_MODEL, PRO_MODEL):

    # prompt for llm
    prompt = f"""
    Your task is to parse a user's algebra problem into its left-hand side (LHS), right-hand side (RHS), and the symbol to solve for.
    Use standard Python/SymPy syntax for the equation parts. Respond with ONLY a valid JSON object.

    Example:
    User prompt: "solve for x in 2*x + 10 = 20"
    Your JSON response:
    {{
        "lhs": "2*x + 10",
        "rhs": "20",
        "symbol": "x"
    }}

    Now, parse the following user prompt.
    User prompt: "{user_prompt}"
    IMPORTANT: Your entire response must be ONLY the raw JSON object, without any surrounding text or 
    markdown formatting like ```json.
    Your JSON response:
    """
    # llm runs prompt
    response = FLASH_MODEL.generate_content(prompt)

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
    except json.JSONDecodeError as e:
        logging.error(f"Failed to decode JSON from AI: '{clean_json_string}'. Error: {e}")
        # Raise an exception to signal the failure to the calling function
        raise ValueError("The AI returned an invalid format.") from e
    # responses are placed in specific vars
    lhs = algebra_dict.get("lhs")
    rhs = algebra_dict.get("rhs")
    symbol = algebra_dict.get("symbol")

    # should print in console if successful
    logging.info(f"Successfuly did lhs as {lhs}, rhs as {rhs}, and symbol as {symbol}")

    try:
        # sympy basic math solver
        lhs_eq = sympify(lhs)
        rhs_eq = sympify(rhs)
        variable = Symbol(symbol)
        equation = Eq(lhs_eq, rhs_eq)
        solution = solveset(equation, variable)
        sympy_answer = str(solution)

        logging.info(f"Solved answer with Sympy: {sympy_answer}")

        # llm making steps from the answer
        tutor_prompt = f"""
        You are a friendly and encouraging math tutor.
        The user's problem was: '{user_prompt}'
        The correct final answer is: '{sympy_answer}'

        Please provide a friendly, step-by-step explanation of how to get from the problem 
        to the solution. Start your response with a sentence like 'Of course! The answer is...'
        """
        tutor_response = PRO_MODEL.generate_content(tutor_prompt)
        tutor_response_text = tutor_response.text

        # returns the answer and the tutors step-by-step
        return {"final_answer": sympy_answer, "explanation": tutor_response_text}
    except Exception as e:
        logging.error(f"Sympy failed to solve the equation. Error: {e}")
        return "I was unable to solve that specific algebra problem."
