#   notes: some characters from doc give weird formatting issues, resolve capitalization too (proper nouns make this hard)

import json

with open("statement_modifier/base-claims.json", "r") as file:
    bclaims = json.load(file)
with open("statement_modifier/modifiers.json", "r") as file:
    modifiers = json.load(file)

def modify_statements(base_claims, modifiers):
    modified_statements = []
    for statement in base_claims:
        modified_statements.append({
                "prompt": statement["statement"],
                "modifier_id": "",      # TODO: Determine what we do for unmodified data
                "true": statement["true"],
                "statement_id": statement["id"],
                "topic": statement["topic"],
                "indicator_category": ""
                })
        for modifier in modifiers:
            prompt = modifier["modifier"].replace("{statement}", statement["statement"])
            truth = 1 - statement["true"] if modifier["negation"] else statement["true"]
            modified_statements.append({
                "prompt": prompt,
                "modifier_id": modifier["id"],
                "true": truth,
                "statement_id": statement["id"],
                "topic": statement["topic"],
                "indicator_category": modifier["category"]
                })
    return modified_statements

with open("statement_modifier/modified-claims.json", "w") as file:
    json.dump(modify_statements(bclaims, modifiers), file, indent=4)