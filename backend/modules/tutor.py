import json
import logging
from dotenv import load_dotenv
import google.generativeai as genai


def tutor_response(user_prompt, answer, PRO_MODEL):
    tutor_prompt = f"""
    You are a friendly and encouraging math tutor. If the user does not explicity asks for no steps, then your response will be
    a simple sentnece stating the final answer with no explanation. Otherwise, your task is to explain how a student can solve a problem.
    You will be given the original problem and the correct final answer.

    **Instructions:**
        1.  First, analyze the user's original problem to see if it includes phrases like "no steps," "no work," or "just the answer."
        2.  **IF** the user asked for no steps, your entire response MUST be ONLY a single, polite sentence confirming the final answer. For example: "Of course! The final answer is {answer}."
        3.  **ELSE** (if the user did not ask for no steps), you MUST provide a friendly, step-by-step explanation of how to get from the problem to the solution. Start your response with a sentence like "Of course! The final answer is {answer}. Here's how we get there step-by-step:"

    ---
    **User's Problem:** '{user_prompt}'
    **Correct Final Answer:** '{answer}'
    ---
    IMPORTANT: You must format your entire response using only plain text. Do not use any Markdown, HTML, or LaTeX formatting. For exponents, use the caret symbol (^), for example: x^2.
    Now, generate your response based on the instructions above.
    """
    tutor_response = PRO_MODEL.generate_content(tutor_prompt)
    tutor_response_text = tutor_response.text
    logging.info(f"Tutor response successfully created. {answer}")
    # returns the answer and the tutors step-by-step
    return {"final_answer": answer, "explanation": tutor_response_text}
