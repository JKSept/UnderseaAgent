import os
import argparse
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("api key not found...")


client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

response = client.models.generate_content(model="gemini-2.5-flash", contents=args.user_prompt)


token_usage_info = response.usage_metadata
if token_usage_info is None:
    raise RuntimeError("usage metadata return none?")
prompt_tokens = token_usage_info.prompt_token_count
candidate_tokens = token_usage_info.candidates_token_count

print(f"Prompt tokens: {prompt_tokens}")
print(f"Response tokens: {candidate_tokens}")



print(response.text)




