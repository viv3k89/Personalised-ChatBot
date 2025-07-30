# Personalised-ChatBot
# 🧠 Personalized Chatbot using Ollama + Mistral 7B + Gradio

This project is a personalized chatbot built using the [Mistral 7B](https://mistral.ai/news/introducing-mistral-7b/) model via [Ollama](https://ollama.com), with a frontend interface created and deployed using [Gradio](https://www.gradio.app/).

## 📁 Project Structure

.
├── .gradio/ # Gradio-related config (e.g., state, sessions)
├── frontend/ # HTML/CSS frontend files (optional customization)
├── chatbot.py # Main chatbot logic
├── chatbotdeployment.py # Gradio deployment script
├── data.json # Sample or training data
├── style.css # Custom styling for Gradio app
├── txt # Additional static resources or logs

markdown
Copy
Edit

## 🚀 Features

- Uses **Mistral 7B** model for intelligent responses
- Runs locally via **Ollama**
- Clean and simple UI with **Gradio**
- Easy to customize and extend
- Can be deployed for local or web-based usage

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/personalized-chatbot.git
cd personalized-chatbot
2. Install Dependencies
Ensure Python 3.8+ is installed. Then:

bash
Copy
Edit
pip install -r requirements.txt
You may need to create a requirements.txt file with:

txt
Copy
Edit
gradio
requests
3. Install and Run Ollama with Mistral
Make sure you have Ollama installed and running. Then pull the Mistral model:

bash
Copy
Edit
ollama pull mistral
4. Run the Chatbot
bash
Copy
Edit
python chatbotdeployment.py
This will launch the Gradio interface in your browser.

🧠 Model Details
Model: Mistral 7B

Provider: Ollama

Inference: Local LLM execution via Ollama's API

💻 Example
Once the app is running, you can start chatting:

makefile
Copy
Edit
User: Hello!
Bot: Hi there! How can I assist you today?
📌 Notes
Make sure Ollama is running in the background before launching the bot.

Customize style.css for UI styling.

Use data.json to load or save past conversations or context.

---

