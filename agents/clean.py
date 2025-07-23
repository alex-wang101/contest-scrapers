import re
with open("data/training_data.jsonl", "r") as file, open("data/cleaned_data.json", "w") as output_file:
    lines = file.readlines()
    for line in lines:
        line_fixed = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', line)
        if line_fixed.strip() == "":
            continue 
        else:
            output_file.write(line_fixed)
    