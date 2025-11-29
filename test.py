# from llm_modules.chat_template import DeepseekChat

# from dotenv import load_dotenv
# import os
# load_dotenv()  

# api_key = os.getenv("DEEPSEEK_API_KEY")

# chat = DeepseekChat(api_key,'answer as if you are a child').one_shot('what is your name?', temperature = 2, max_tokens=5)

# print(chat)

tools = {
    "get_weather": {
        "description": "Get current weather information for a location",
        "parameters": {
            "location": {
                "type": "string",
                "description": "City name or geographic coordinates",
                "required": True
            },
            "unit": {
                "type": "string", 
                "description": "Temperature unit: celsius or fahrenheit",
                "required": False,
                "default": "celsius"
            }
        }
    },
    
    "calculate_bmi": {
        "description": "Calculate Body Mass Index based on height and weight",
        "parameters": {
            "weight": {
                "type": "number",
                "description": "Weight in kilograms",
                "required": True
            },
            "height": {
                "type": "number", 
                "description": "Height in meters",
                "required": True
            }
        }
    },
    
    "send_email": {
        "description": "Send an email to specified recipients",
        "parameters": {
            "to": {
                "type": "array",
                "description": "List of email addresses",
                "required": True
            },
            "subject": {
                "type": "string",
                "description": "Email subject line",
                "required": True
            },
            "body": {
                "type": "string",
                "description": "Email content",
                "required": True
            },
            "priority": {
                "type": "string",
                "description": "high, normal, or low",
                "required": False,
                "default": "normal"
            }
        }
    },
    
    "search_products": {
        "description": "Search for products in the database",
        "parameters": {
            "query": {
                "type": "string",
                "description": "Search keywords",
                "required": True
            },
            "category": {
                "type": "string",
                "description": "Product category filter",
                "required": False
            },
            "max_price": {
                "type": "number",
                "description": "Maximum price limit",
                "required": False
            },
            "limit": {
                "type": "integer",
                "description": "Maximum number of results",
                "required": False,
                "default": 10
            }
        }
    }
}



def tools_to_string(tools):
    string = ''

    for function_name,_description in tools.items():
        
        string += f'FUNCTION NAME: {function_name}\n'
        string += f'FUNCTION DESCRIPTION: {_description['description']}\n'
        string += f'{function_name} PARAMETERS: \n'

        for parameter_name, parameter_details in _description['parameters'].items():
            if 'default' in parameter_details:
                string += f'  - {parameter_name} :{parameter_details['description']}, DATA_TYPE:{parameter_details['type']}, REQUIRED: {parameter_details['required']}, DEFAULT: {parameter_details['default']}\n'
            else:
                string += f'  - {parameter_name} :{parameter_details['description']}, DATA_TYPE:{parameter_details['type']}, REQUIRED: {parameter_details['required']}\n'
    return string


result = tools_to_string(tools)
print('TOOLS: ')
print(tools)
print('RESULT: ')
print(result)





