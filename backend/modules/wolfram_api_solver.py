import os
import logging
import requests
from flask import Flask, jsonify, request

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

def wolframalpha(user_prompt):
    WA_API_KEY = os.getenv("WOLFRAM_APP_ID")
    BASE_URL = "https://api.wolframalpha.com/v1/result"
    params = {"appid": WA_API_KEY, "i": user_prompt}

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()  # raises exception if response generation was unsucessful
        logging.info("WA API calculated final answer successfully!")
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Wolfram Alpha API unsuccessful: {e}")
        raise ValueError("Failed to get an answer from the calculation engine.") from e
