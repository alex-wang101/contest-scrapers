# Use relative imports for files in the same directory
from agent import agent 
from agent_secondary import agent_secondary
import json
import threading

system_prompt = """
Rules:
1. For each variable or concept mentioned, create ONE question-answer pair
2. Questions should ask "What does [variable] represent?" or similar
3. Answers should be concise descriptions
4. Output ONLY valid JSON objects, one per line
5. Use this exact format: {"Question": "text here", "Answer": "text here"}

Example input: "IncidentNumber: unique identifier for each incident (e.g., 000008-01012018)"
Example output: {"Question": "What does IncidentNumber represent?", "Answer": "A unique identifier for each incident, example: 000008-01012018"}
IF THE TEXT IS A TABLE, CREATE A SEPARATE QUESTION-ANSWER PAIR FOR EACH VARIABLE DESCRIBED.
IF THE TEXT DOES NOT ACTUALLY INCLUDE A QUESTION REGARDING ACTURARY EXAM MATERIALS, DO NOT CREATE A QUESTION-ANSWER PAIR, SIMPLY OUTPUT "".

Text to process:
"""

def main():
    # Load the input data
    with open("data/output.json", "r") as file:
        input_data = json.load(file)
    
    divide = len(input_data) // 5
    # Create threads for each agent
    thread1 = threading.Thread(target=agent, args=(input_data, system_prompt, divide))
    thread2 = threading.Thread(target=agent_secondary, args=(input_data, system_prompt, divide))
    thread3 = threading.Thread(target=agent_tertiary, args=(input_data, system_prompt, divide))
    thread4 = threading.Thread(target=agent_fourth, args=(input_data, system_prompt, divide))
    
    # Start both threads
    print("Starting agent 1...")
    thread1.start()
    print("Starting agent 2...")
    thread2.start()
    print("Starting agent 3...")
    thread3.start()
    print("Starting agent 4...")
    thread4.start()
    
    # Wait for both threads to complete
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    
    print("Both agents have completed processing.")

# Call the main function when the script is run
if __name__ == "__main__":
    main()
