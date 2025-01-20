import random
from datasets import load_dataset
from openai import OpenAI

client = OpenAI()

def format_data(dataset, prmpt):
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    # messages=[
    #     {
    #         pass
    # ],)
    
    # TODO write fewshot examples, format into json, 