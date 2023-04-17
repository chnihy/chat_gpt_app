import atexit
import os
import openai
import requests
import random as r

from utils import get_files_recursively


class ChatGPT:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
        # Register the save_history method with atexit
        #atexit.register(self.save_history)
        
        self.model = "text-davinci-003"
        self.conversation_history = ""
        self.load_history()


    def chat(self, prompt:str=None):
        if not prompt:
            prompt = input("you: ")
        
        self.conversation_history += f"User: {prompt}\nAI:"

        res = openai.Completion.create(
                model=self.model,
                #prompt=self.conversation_history,
                prompt=prompt,
                max_tokens=1000,
                temperature=0)

        reply = res.choices[0].text.strip()
        
        self.conversation_history += reply + "\n"
        print(f"{self.name}: {reply}")
        return reply
    
    @property
    def talk(self):
        while True:
            prompt = input("you: ")
            if prompt.lower() == "quit":
                print("Goodbye!")
                break
            
            res = self.chat(prompt)
            print(f"gpt:\n{res}")

    def save_history(self):
        from datetime import datetime

        # Get current date and time
        now = datetime.now()

        # Format date and time as string
        timestamp = now.strftime("%Y%m%d%H%M%S")

        with open("history.txt", 'w') as f:
            f.write(f"timestamp: {timestamp}")
            f.write(self.conversation_history + "\n")
            f.close()
            
        print("history saved")

    def load_history(self):
        with open("history.txt", 'r') as f:
            data = f.read()
            self.conversation_history += data
            f.close()
    
    def clear_history(self):
        yorn = input("ARE YOU SURE??? y or n: ")
        if yorn.lower() == "y":
            random_num = str(r.randint(1000, 9999))
            confirm = input(f"Enter {random_num} to clear history: ")
            if confirm == random_num:
                with open("history.txt", 'w') as f:
                    data = f.write("")
                    f.close()
            print("history cleared!")

    def read_file(self, path:str=None):
        if not path:
            path = input("Enter path: ")
        self.chat(files._get_file(path))


#class FileStorage:
#    def __init__(self):
#        pass
#    def _get_file(self, path:str=None, name:str=None):
#        if not path:
#            path = input("Enter path: ")    
#        if not name:
#            name = os.path.basename(path)
#            dot = name.index(".")
#            name = name[:dot]
#            print(f"Name: {name}")
#
#        with open(path, 'r') as f:
#            data = f.read()
#
#        self.__setattr__(name, data)
#        print(f"{name} successfully uploaded")
#        return data
#

openai.api_key = "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"
gpt = ChatGPT()
gpt.name = "Gpt # 1"
gpt2 = ChatGPT()
gpt2.name = "Gpt #2"
class Convo:
    def __init__(self):
        self.res = gpt.chat("start a conversation")
    
    def go(self):
        print(gpt2.chat(self.res))
        print(gpt.chat(gpt2.chat(self.res)))

convo = Convo()
convo.go()