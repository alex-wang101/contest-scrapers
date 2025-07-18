import json

# Debug version to see exactly what's happening
json_list = []
buffer = ""
count = 0

with open("data/training_data.jsonl", "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, 1):
        
        buffer += line.strip()
        
        try:
            obj = json.loads(buffer)
            json_list.append(obj)
            print(f"✓ Successfully parsed line {line_num}")
            buffer = ""  # Reset buffer after successful parse
        except json.JSONDecodeError as e:
            print(f"✗ JSON Error on line {line_num}: {e}")
            print(f"Error position: {e.pos if hasattr(e, 'pos') else 'unknown'}")
            continue
        count += 1

print(f"Final count: {count}")

