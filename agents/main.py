# Use relative imports for files in the same directory
from agent import agent 
from agent_secondary import agent_secondary
from agent_tertiary import agent_tertiary
from agent_fourth import agent_fourth
import json
import threading

system_prompt = """
You are generating **high-quality, SOA syllabus-aligned training data** for fine-tuning a language model to perform as an actuarial expert at the level of SOA IFM, STAM, and ALTAM exams.  

## Objective:
Given an excerpt from exam commentary or solutions, extract and rephrase the key actuarial concepts, techniques, or challenges into **realistic, long-answer actuarial exam-style question-answer pairs** that test understanding, application, and reasoning.

## Rules:
✅ **Focus on long-answer questions only. Do NOT generate multiple choice or short factual recall questions.**  
✅ Use only the substantive actuarial concepts & explanations from the text.  
✅ Ignore commentary about exam candidates or exam mechanics (e.g., “most candidates did well…”).  
✅ Each question must:
- Resemble a long-answer actuarial exam question: applied, scenario-based, or calculation-based.
- Require explanation of reasoning, interpretation of results, or clear steps.
- Be aligned to SOA syllabus topics: insurance, pensions, risk theory, financial markets, reserves, survival models, credibility, etc.

✅ Each answer must:
- Be clear, complete, and use correct actuarial terminology.
- Include key reasoning steps, formulas if applicable, and proper justification.
- Be proportional in depth to an SOA long-answer solution.

✅ For each substantive concept identified in the text, create 1–2 question-answer pairs demonstrating:
- Understanding (what it means and why it matters).
- Application (how to compute, model, or interpret in practice).

✅ Output **only valid JSON objects, one per line**, in this exact format:
```json
{"Question": "text here", "Answer": "text here"}
```
DO NOT OUTPUT "Here is the extracted and rephrased actuarial concept, technique, or challenge in a realistic long-answer actuarial exam-style question-answer pair", just output the JSON object.
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
