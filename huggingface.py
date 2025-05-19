from datasets import Dataset
from huggingface_hub import HfApi

repo_id = "logianwilliam/misleading_context"

# Paths to your JSON files
STATEMENTS_FILE = "/Users/mac/Documents/misleading-context/statements.json"
MODIFIERS_FILE = "/Users/mac/Documents/misleading-context/modifiers.json"
PROMPTS_FILE = "/Users/mac/Documents/misleading-context/prompts.json"

# Load the files into Hugging Face Dataset objects
statements = Dataset.from_json(STATEMENTS_FILE)
modifiers = Dataset.from_json(MODIFIERS_FILE)
prompts = Dataset.from_json(PROMPTS_FILE)

# Push each dataset as a different split
statements.push_to_hub("logianwilliam/misleading_context_statements")
modifiers.push_to_hub("logianwilliam/misleading_context_modifiers")
prompts.push_to_hub("logianwilliam/misleading_context_prompts")
