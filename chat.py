# import the OpenAI Python library for calling the OpenAI API
from openai import OpenAI
import os
import json 

from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("OpenAI_API_key")

if api_key is None:
    raise ValueError("OpenAI_API_key is not set in the .env file")

client = OpenAI(api_key=api_key) 

MODEL = "gpt-3.5-turbo"
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Knock knock."},
        {"role": "assistant", "content": "Who's there?"},
        {"role": "user", "content": "Orange."},
    ],
    temperature=0,
)

print(json.dumps(json.loads(response.model_dump_json()), indent=4))