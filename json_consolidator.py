import json

input_files = ['/Users/mac/Documents/misleading-context/synthetic_generation/assumptive_no_negations.json', '/Users/mac/Documents/misleading-context/synthetic_generation/emotional_no_negations.json', '/Users/mac/Documents/misleading-context/synthetic_generation/flattery_no_negations.json', '/Users/mac/Documents/misleading-context/synthetic_generation/polite_no_negations.json']
output_file = 'consolidated.json'

consolidated_data = []
current_id = 1

for file in input_files:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for entry in data:
            entry['id'] = current_id
            consolidated_data.append(entry)
            current_id += 1

# Write to the output file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(consolidated_data, f, indent=2, ensure_ascii=False)

print(f"Consolidated {len(consolidated_data)} entries into {output_file}")
