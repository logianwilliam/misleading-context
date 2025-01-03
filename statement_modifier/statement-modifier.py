import json

def modify_statements(base_claims, modifiers):
    modified_statements = []
    for statement in base_claims:
        for modifier in modifiers:
            prompt = modifier["modifier"].replace("{statement}", statement["statement"])
            truth = 1 - statement[truth] if modifier["negation"] else statement["truth"]
            modified_statements.append({
                "prompt": prompt,
                "modifier_id": modifier["id"],
                "truth": truth,
                "statement_id": statement["id"]
            })