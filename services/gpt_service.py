import os
from typing import Optional
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

_ = load_dotenv(find_dotenv())
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


class GPTService:
    def __init__(self, gpt_client: OpenAI = None):
        if gpt_client is None:
            gpt_client = OpenAI(api_key=OPENAI_API_KEY)
        self.gpt_client = gpt_client

    def query_chatgpt(
        self,
        messages=None,
        model="gpt-4o",
        temperature=0.6,
        response_format=None,  # noqa
    ) -> Optional[str]:
        stream = self.gpt_client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            response_format=response_format,
        )

        response = stream.choices[0].message.content
        return response