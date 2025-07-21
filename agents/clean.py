# Simply copy non-blank lines from input to output
with open("data/training_data.jsonl", "r") as file, open("data/cleaned_data.json", "w") as output_file:
    lines = file.readlines()
    for line in lines:
        if line.strip() == "":
            continue  # Skip blank lines
        else:
            output_file.write(line)  # Write the line as-is