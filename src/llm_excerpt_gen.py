from google import genai
import os
from dotenv import load_dotenv
from pathlib import Path

EXCERPTS_DIR = Path(__file__).parent.parent / "excerpts"

load_dotenv()
key = os.getenv('GOOGLE_API_KEY')
if not key:
    raise EnvironmentError("GOOGLE_API_KEY not set in environment or .env file")

def collect_llm_excerpts(prompt):
    client = genai.Client(api_key=key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    excerpt = response.text

    with open(EXCERPTS_DIR / "llm_excerpts.md", 'w') as f:
        f.write(excerpt)

    return excerpt

