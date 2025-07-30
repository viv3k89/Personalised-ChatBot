import json
import ollama

# Load JSON data
with open("data.json", "r") as file:
    data = json.load(file)

# Function to get an answer from JSON (ignoring case and extra spaces)
def get_answer_from_json(question):
    normalized_question = question.strip().lower()  # Normalize input
    for key in data.keys():
        if key.strip().lower() == normalized_question:
            return data[key]  # Return the matched answer
    return None  # Return None if no match is found

# Chat loop 
while True:
    user_question = input("\n🟢 You: ")  # Ask for user input

    if user_question.lower() in ["exit", "quit", "bye"]:
        print("\n👋 Chatbot: Goodbye!")
        break

    # Retrieve answer from JSON
    answer = get_answer_from_json(user_question)

    if answer:
        print("\n🤖 Chatbot:", answer)
        continue  # Skip Mistral-7B and go to next input

    # If not found, generate an answer using Mistral-7B
    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "system", "content": "You are an AI assistant. If the user asks a question not in the database, generate a response."},
            {"role": "user", "content": user_question}
        ]
    )

    print("\n🤖 Chatbot:", response['message']['content'])

    # Save the question and answer to the JSON file
    data[user_question] = response['message']['content']
    with open("data.json", "w") as file:
        json.dump(data, file)