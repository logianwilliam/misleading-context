import random
from datasets import load_dataset
from openai import OpenAI

client = OpenAI()

def format_data(examples):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": ""},
            {"role": "user", "content": ""}
        ]
    )
    
    # TODO write fewshot examples, format into json, 