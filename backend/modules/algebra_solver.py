import json
import logging
from sympy import sympify, Symbol, Eq, solveset, simplify
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask, jsonify, request
from modules import tutor
from modules import query_translator


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def solve_algebra_problem(user_prompt, FLASH_MODEL, PRO_MODEL):
    algebra_dict = query_translator.x_solver_translator(user_prompt, FLASH_MODEL)
    logging.info("algebra dict in algebra solver successful")
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
        sympy_answer = sympy_answer[1:-1]

        logging.info(f"Solved answer with Sympy: {sympy_answer}")

        try:
            return tutor.tutor_response(user_prompt, sympy_answer, PRO_MODEL)
        except Exception as e:
            logging.error("Tutor was unable to create response.")
            return {"error": "Tutor was unable to create response."}

    except Exception as e:
        logging.error(f"Sympy failed to solve the equation. Error: {e}")
        return {"error": "I was unable to solve that specific algebra problem."}


def simplify_algebra_problem(user_prompt, FLASH_MODEL, PRO_MODEL):
    simplify_eq = query_translator.simplify_translator(user_prompt, FLASH_MODEL)
    logging.info("simplify translator successful")

    try:
        # sympy simplifier
        simplified_answer = simplify(simplify_eq)
        simplified_answer = str(simplified_answer)

        logging.info(f"Simplified answer: {simplified_answer}")
        try:
            return tutor.tutor_response(user_prompt, simplified_answer, PRO_MODEL)
        except Exception as e:
            logging.error("Tutor was unable to create response.")
            return {"error": "Tutor was unable to create response."}
    except Exception as e:
        logging.error(f"Sympy failed to solve the equation. Error: {e}")
        return {"error": "I was unable to solve that specific algebra problem."}
