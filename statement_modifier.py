import json

# Input file paths
statements_file = '/Users/mac/Documents/misleading-context/statements.json'
modifiers_file = '/Users/mac/Documents/misleading-context/modifiers.json'
output_file = 'prompts.json'

# Load the statements and modifiers
with open(statements_file, 'r', encoding='utf-8') as f:
    statements = json.load(f)

with open(modifiers_file, 'r', encoding='utf-8') as f:
    modifiers = json.load(f)

# Generate prompts
combined = []
for statement in statements:
    for modifier in modifiers:
        prompt_text = modifier['phrase'].replace("{statement}", statement['statement'])
        combined.append({
            'statement_id': statement['id'],
            'modifier_id': modifier['id'],
            'prompt': prompt_text,
            'statement_category': statement.get('category', ''), 
            'modifier_category': modifier.get('indicator_category', '')
        })

# Write the output
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(combined, f, indent=2, ensure_ascii=False)

print(f"Generated {len(combined)} prompts in {output_file}")
