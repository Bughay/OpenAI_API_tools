from chat_template import DeepseekChat


class DeepseekClassification:
    def __init__(self,api_key,user_message,categories,examples):
        self.api_key = api_key
        self.categories = categories
        self.examples = examples
        self.user_message = user_message
        self.prompt = f"""Act as a text classification expert. Follow these rules strictly:
                                                                                                           
                    1. Task: Classify the user's text into exactly one of these categories:  
                    {categories}

                    2. Guidelines:  
                    - Respond ONLY with the category name. No explanations.  
                    - If uncertain, choose the closest match.  
                    - Ignore typos/grammar errors.  

                    3. Examples (for context):  
                        {examples}"""
                        

    def classify(self):
        chat = DeepseekChat(self.api_key,self.prompt).one_shot(self.user_message)
        return(chat)






