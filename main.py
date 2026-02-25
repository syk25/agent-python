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

# parser 설정: CLI에서 사용자 프롬프트 받기, --verbose 플래그 추가 
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
content = args.user_prompt
response = client.models.generate_content(model=model, contents=messages)
print(f"User prompt: {content}")
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
print(f"Response:\n{response.text}")
