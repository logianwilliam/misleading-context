import random
from datasets import load_dataset

# Load a specific split of the dataset
ds1 = load_dataset("armanc/ScienceQA", split="train")

# Shuffle the dataset
ds1 = ds1.shuffle(seed=42)

# Print the first two rows
print(ds1[1])