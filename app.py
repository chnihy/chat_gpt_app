import openai
import os
import requests

class ChatGPT:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model = "text-davinci-003"
        self.conversation_history = ""

    def chat(self, prompt:str=None):
        if not prompt:
            prompt = input("you: ")
        
        self.conversation_history += f"User: {prompt}\nAI:"

        res = openai.Completion.create(
                model=self.model,
                prompt=self.conversation_history,
                max_tokens=1500,
                temperature=0)

        reply = res.choices[0].text.strip()
        
        self.conversation_history += reply + "\n"
        
        return reply
    
    @property
    def talk(self):
        while True:
            prompt = input("you: ")
            if prompt.lower() == "quit":
                print("Goodbye!")
                break
            
            res = self.chat(prompt)
            print(f"<<< gpt >>>:\n{res}")
