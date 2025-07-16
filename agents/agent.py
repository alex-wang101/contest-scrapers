import requests
import json


ollama_url = "http://localhost:11434/api/generate"
model_name = "llama3.2:3b"

def agent(input_data, system_prompt, divide):
    with open("data/training_data_primary.jsonl", "w") as file:
        ranges = divide * 2
        for idx in range(ranges, (ranges + divide)):  
            j = input_data[idx]
            for key, value in j.items():
                data = value

                full_prompt = system_prompt + data
                payload: dict = {
                    "model": model_name,
                    "prompt": full_prompt,
                    "stream": False,
                }
                response = requests.post(ollama_url, json=payload)
                response.raise_for_status()
            
                print("Raw response content:")
                print(response.text[:500])  # Print first 500 chars to avoid flooding console
                
                response_text = response.text
                
                try:
                    lines = response_text.strip().split('\n')
                    for line in lines:
                        if line.strip():
                            try:
                                json_obj = json.loads(line)
                                if 'response' in json_obj:
                                    # Found a response field, write it
                                    file.write(json_obj['response'] + '\n')
                            except json.JSONDecodeError:
                                # If not valid JSON, write the line as is
                                file.write(line + '\n')
                except Exception as e:
                    print(f"Error processing response: {e}")
                    # Fallback: just write the raw text
                    file.write(response_text)
