import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function


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

for _ in range(20):
    response = client.models.generate_content(
                                            model=model,
                                            contents=messages,
                                            config=types.GenerateContentConfig(
                                                tools=[available_functions],
                                                system_instruction=system_prompt
                                                )
                                            )

    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    if not response.function_calls:
        print(f"Response:\n{response.text}")
        exit(0)
        

    for function_call in response.function_calls:
        function_call_result = call_function(function_call)
        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response['result']}")
        else:
            print(f" - Calling function: {function_call.name}")
        messages.append(function_call_result)

print(f"Iteration limit exceeded")
exit(1)