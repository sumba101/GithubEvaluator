import os

import openai
import tiktoken
from dotenv import load_dotenv

from thresholds import OPENAI_TOKEN_LIMIT

load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')
def response_gen(message: str, system_prompt: str, count: int):
    print("Generating response")
    message = _token_limit(message)
    messages = []
    if count == 0:
        messages.append({
            "role": "system",
            "content": system_prompt
        })
    messages.append({
        "role": "user",
        "content": message
    })

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    ).choices[0].message

    messages.append(response)
    return response["content"]


def _token_limit(message):
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

    encode = encoding.encode(message)
    decode = encoding.decode(encode[:OPENAI_TOKEN_LIMIT])
    return decode
