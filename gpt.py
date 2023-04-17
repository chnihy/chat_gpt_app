import atexit
import os
import openai
import requests
import random as r

from utils import get_files_recursively, show_dict


class ChatGPT:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
        # Register the save_history method with atexit
        #atexit.register(self.save_history)
        self.name = "ChatGPT"
        self.model = "text-davinci-003"
        #self.conversation_history = ""
        #self.load_history()

    def chat(self, prompt:str=None):
        """ open a single chat exchange
            returns response text and exits chat
        """
        if not prompt:
            prompt = input("you: ")
        
        #self.conversation_history += f"User: {prompt}\n{self.name}:"

        res = openai.Completion.create(
                model=self.model,
                #prompt=#self.conversation_history,
                prompt=prompt,
                max_tokens=1000,
                temperature=0,
                debug=True)

        reply = res.choices[0].text.strip()
        
        #self.conversation_history += reply + "\n"
        show_dict(res)
    
    @property
    def talk(self):
        """ open a conversation in a While loop
            exit with <quit> command
        """
        while True:
            prompt = input("you: ")
            if prompt.lower() == "quit":
                print("Goodbye!")
                break
            
            res = self.chat(prompt)
            print(f"gpt:\n{res}")

    #def save_history(self):
    #    from datetime import datetime
#
#    #    # Get current date and time
#    #    now = datetime.now()
#
#    #    # Format date and time as string
#    #    timestamp = now.strftime("%Y%m%d%H%M%S")
#
#    #    with open("history.txt", 'w') as f:
#    #        f.write(f"timestamp: {timestamp}")
    #        f.write(#self.conversation_history + "\n")
    #        f.close()
    #        
    #    print("history saved")

    """def load_history(self):
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
            print("history cleared!")"""

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
