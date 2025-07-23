import json
import re

def clean_line(line: str) -> str:
    # Load JSON
    obj = json.loads(line)
    # Fix Answer: replace \* with *
    obj["Answer"] = re.sub(r'\\\*', '*', obj["Answer"])
    # (optional) fix other invalid escapes here
    return json.dumps(obj, ensure_ascii=False)

with open("data/cleaned_data.jsonl", "r", encoding="utf-8") as infile, open("data/training_data_fixed.jsonl", "w", encoding="utf-8") as outfile:
    for i, line in enumerate(infile, 1):
        if line.strip() == "":
            continue
        try:
            fixed_line = clean_line(line)
            outfile.write(fixed_line + "\n")
        except Exception as e:
            print(f"Error at line {i}: {e}")
