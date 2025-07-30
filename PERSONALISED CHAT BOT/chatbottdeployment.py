import json
import ollama
import gradio as gr
import os

# Ensure data.json exists
if not os.path.exists("data.json"):
    with open("data.json", "w") as file:
        json.dump({}, file)

# Load JSON data
with open("data.json", "r") as file:
    try:
        data = json.load(file)
    except json.JSONDecodeError:
        data = {}

# Function to get an answer from JSON (ignoring case and extra spaces)
def get_answer_from_json(question):
    normalized_question = question.strip().lower()
    for key in data.keys():
        if key.strip().lower() == normalized_question:
            return data[key]
    return None

# Function to handle chatbot response
def chatbot(user_question, history):
    # Retrieve answer from JSON
    answer = get_answer_from_json(user_question)

    if answer:
        return answer

    # If not found, generate an answer using Mistral-7B
    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "system", "content": "You are an AI assistant. If the user asks a question not in the database, generate a response."},
            {"role": "user", "content": user_question}
        ]
    )

    answer = response['message']['content']

    # Save the new question and answer to JSON file
    data[user_question] = answer
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    return answer

# Gradio interface
demo = gr.ChatInterface(fn=chatbot)

if __name__ == "__main__":
    demo.launch(share=True)
