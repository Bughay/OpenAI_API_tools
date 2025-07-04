from llm_modules.chat_template import DeepseekChat

from dotenv import load_dotenv
import os
load_dotenv()  

api_key = os.getenv("DEEPSEEK_API_KEY")

chat = DeepseekChat(api_key,'answer as if you are a child').one_shot('what is your name?', temperature = 2, max_tokens=5)

print(chat)