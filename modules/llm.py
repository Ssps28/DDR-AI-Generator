import json
import logging
import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY missing in .env")

client = genai.Client(api_key=API_KEY)


def load_prompt(filename):
    with open(
        f"prompts/{filename}",
        "r",
        encoding="utf-8"
    ) as f:
        return f.read()


EXTRACTION_PROMPT = load_prompt("extraction_prompt.txt")
MERGE_PROMPT = load_prompt("merge_prompt.txt")


def clean_json(text):
    """
    Remove markdown wrappers if Gemini returns them.
    """

    text = text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "")

    if text.startswith("```"):
        text = text.replace("```", "")

    if text.endswith("```"):
        text = text[:-3]

    return text.strip()


def ask_gemini(prompt):

    retries = 3

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            cleaned = clean_json(response.text)

            return json.loads(cleaned)

        except Exception as e:

            logging.warning(f"Attempt {attempt+1} failed: {e}")

            if attempt == retries - 1:
                raise

            time.sleep(2)


def extract_document(document_text, document_type):

    logging.info(f"Extracting {document_type}")

    prompt = f"""
{EXTRACTION_PROMPT}

DOCUMENT TYPE:
{document_type}

DOCUMENT:

{document_text}
"""

    return ask_gemini(prompt)


def merge_documents(inspection_json, thermal_json):

    logging.info("Generating Final DDR")

    prompt = f"""
{MERGE_PROMPT}

Inspection JSON

{json.dumps(inspection_json, indent=2)}

Thermal JSON

{json.dumps(thermal_json, indent=2)}
"""

    return ask_gemini(prompt)