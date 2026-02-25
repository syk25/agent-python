import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("ERROR: api key does not exist")

client = genai.Client(api_key=api_key)
model = "gemini-2.5-flash"

# CLI에서 프롬프트로 주어진 인자 가져오기
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

# 
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
content = args.user_prompt
response = client.models.generate_content(model=model, contents=messages)
print(f"User prompt: {content}")
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
print(f"Response:\n{response.text}")
