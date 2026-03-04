from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('GOOGLE_API_KEY')

def collect_llm_excerpts(prompt):
    client = genai.Client(api_key = key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    excerpt = response.text

    with open('excerpts/llm_excerpts.md', 'w') as f:
        f.write(excerpt)

    return excerpt

