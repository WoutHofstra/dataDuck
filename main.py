import os
import pandas as pd
from google import genai
from google.genai import types
from dotenv import load_dotenv
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
	raise ValueError("No GEMINI_API_KEY in your .env file")
client = genai.Client(api_key=api_key)

with open("prompt.txt", "r", encoding="utf-8") as f:
	system_prompt = f.read()

if len(sys.argv) < 2:
	print("Please provide a valid prompt")
	sys.exit(1)

prompt = sys.argv[1]
if len(sys.argv) > 2:
	print("Too many arguments provided. Usage: uv run main.py <csv file>")
	sys.exit(1)

messages = [
	types.Content(role = "user", parts = [types.Part(text=prompt)]),
]

def main():
	try:
		response = client.models.generate_content(
			model='gemini-2.0-flash-001',
			contents=messages,
			config=types.GenerateContentConfig(
				system_instruction=types.Content(
					role="system",
					parts=[types.Part(text=system_prompt)]
				),
			),
		)

		for candidate in response.candidates:
			text = ""
			if candidate.content and candidate.content.parts:
				for part in candidate.content.parts:
					if hasattr(part, "text"):
						text += part.text
			messages.append(types.Content(role="model", parts=[types.Part(text=text)]))
			print(text)

	except Exception as e:
		print(f"[ERROR] {e}")
		sys.exit(1)

if __name__ == "__main__":
    main()
