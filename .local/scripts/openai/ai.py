
import openai
import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Your OpenAI API key
openai.api_key = os.getenv("API_KEY")

# Generate a unique log filename based on the current date and time if not already existing
timestamp = datetime.now().strftime("%d-%m-%Y_%H:%M")
log_filename = f'ai_log_{timestamp}.json'

# Ensure log directory exists
log_directory = os.path.expanduser("~/.local/scripts/openai/logs")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)
log_path = os.path.join(log_directory, log_filename)

def load_conversation_log():
    if os.path.exists(log_path):
        with open(log_path, 'r') as file:
            return json.load(file)
    else:
        return []

def save_conversation_log(conversations):
    with open(log_path, 'w') as file:
        json.dump(conversations, file, indent=4)

def append_conversation(question, answer):
    conversations = load_conversation_log()
    conversations.append({'question': question, 'answer': answer})
    save_conversation_log(conversations)

def get_chat_history():
    conversations = load_conversation_log()
    messages = []
    for convo in conversations:
        messages.append({"role": "user", "content": convo['question']})
        messages.append({"role": "assistant", "content": convo['answer']})
    return messages

def ask_question(question):
    chat_history_messages = get_chat_history()
    messages_for_prompt = [{"role": "system", "content": "You are a helpful assistant."}] + chat_history_messages
    messages_for_prompt.append({"role": "user", "content": question})

    response = openai.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {
                "role": "user",
                "content": question,
            },
    ],   
    )
    answer = response.choices[0].message.content
    return answer

def main():
    while True:
        question = input("\033[94mEnter new prompt: (Type 'q' to stop)\033[0m ")
        if question.lower() == 'q':
            break

        answer = ask_question(question)
        print()
        print(f"\033[92mAI:\033[0m {answer}")

        append_conversation(question, answer)

if __name__ == "__main__":
    main()

