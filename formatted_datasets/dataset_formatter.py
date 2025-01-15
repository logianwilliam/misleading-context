import random
from datasets import load_dataset
from openai import OpenAI

client = OpenAI()

def format_data(dataset, prmpt):
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "developer", 
            "content": f"{prmpt}"
        },
        {
            "role": "user", 
            "content": f"{dataset}"
        }
    ],
    
    # TODO write fewshot examples, format into json, 