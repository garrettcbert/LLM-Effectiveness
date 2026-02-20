from google import genai

def collect_llm_excerpts(prompt):
    client = genai.Client(api_key = 'AIzaSyBeL08dq579faCI_dRvJ0h-9Gks9GRwA7Q')

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    excerpt = response.text

    with open('llm_excerpts.md', 'w') as f:
        f.write(excerpt)

    return excerpt

