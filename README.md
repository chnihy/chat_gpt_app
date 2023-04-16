# chat_gpt_app
cmd line interface with gpt apt

chat() is a one time call with optional msg arg
talk() opens a continuing conversation, you can quit by entering "quit"

```bash
$ python3
>>> from app import ChatGPT
>>> gpt = ChatGPT()
>>> gpt.chat()
... or
>>> gpt.talk()
```
