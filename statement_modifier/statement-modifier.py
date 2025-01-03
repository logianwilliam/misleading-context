import json

with open("statement_modifier/base-claims.json", "r") as file:
    bclaims = json.load(file)
with open("statement_modifier/modifiers.json", "r") as file:
    modifiers = json.load(file)

def modify_statements(base_claims, modifiers):
    modified_statements = []
    for statement in base_claims:
        for modifier in modifiers:
            prompt = modifier["modifier"].replace("{statement}", statement["statement"])
            truth = 1 # - statement[truth] if modifier["negation"] else statement["true"]
            modified_statements.append({
                "prompt": prompt,
                "modifier_id": modifier["id"],
                "true": truth,
                "statement_id": statement["id"],
                "topic": statement["topic"],
                "indicator_category": modifier["category"]
                })
    return modified_statements

print(modify_statements(bclaims, modifiers))