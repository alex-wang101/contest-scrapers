import requests
import json


ollama_url = "http://localhost:11434/api/generate"
model_name = "llama3.2:3b"


def agent_secondary(input_data, system_prompt):
    with open("training_data_secondary.jsonl", "w") as file:
        input_end = 3 * (len(input_data)  // 4)
        for idx in range(len(input_data)-1, input_end-1, -1):
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
                
                # Print the raw response content for debugging
                print("Raw response content:")
                print(response.text[:500])  # Print first 500 chars to avoid flooding console
                
                # Process the response text directly
                response_text = response.text
                
                # Try to extract JSON objects from the response
                try:
                    # Check if the response contains valid JSON
                    lines = response_text.strip().split('\n')
                    for line in lines:
                        if line.strip():
                            try:
                                # Try to parse each line as JSON
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
