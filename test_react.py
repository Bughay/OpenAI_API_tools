from llm_modules.function_caller import DeepseekFunctionCaller
import os
from openai import OpenAI
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

test_prompts = {
    "get_weather": [
        "What's the temperature in New York right now?",
        "Check weather for London, UK",
        "How's the weather in Tokyo today?",
        "Get me weather info for Paris in fahrenheit",
        "What's the forecast for Sydney, Australia?",
        "Check temperature in Berlin in celsius",
        "How's weather looking in Mumbai?",
        "Get weather for Chicago with fahrenheit units"
    ],
    
    "calculate_bmi": [
        "Calculate my BMI - I'm 1.8m tall and weigh 75kg",
        "What's my BMI if I'm 165cm and 60kg?",
        "BMI calculation: height 1.65 meters, weight 58 kilograms",
        "Compute body mass index for 70kg and 1.75m",
        "My weight is 65kg and height 1.7m, what's my BMI?",
        "Calculate BMI: 80kg weight, 1.85m height",
        "What's the BMI for someone 1.6m tall weighing 55kg?"
    ],
    
    "send_email": [
        "Send email to sarah@company.com with subject 'Project Update' and body 'Hi Sarah, here's the latest status'",
        "Email john@test.com and mary@test.com about 'Meeting Reminder' with message 'Don't forget our 2pm meeting'",
        "Send high priority email to support@help.com subject 'URGENT: System Down' body 'Our system is experiencing issues'",
        "Email team@company.com with subject 'Weekly Report' and body 'Attached is this week's performance report'",
        "Send message to clients@business.com subject 'New Features' body 'Check out our latest updates' with low priority",
        "Email recruitment@hr.com about 'Job Application' with 'I am interested in the developer position'",
        "Send high priority email to admin@site.com subject 'Security Alert' body 'Unusual login detected'",
        "Email friends@group.com with subject 'Party Planning' and body 'Let's organize the weekend get-together'"
    ],
    
    "search_products": [
        "Search for gaming laptops under $1200",
        "Find wireless headphones in electronics category",
        "Look for running shoes under $100, show me 5 results",
        "Search smartphones in mobile category with max price $800",
        "Find coffee makers, limit to 8 results",
        "Search for office chairs under $300 in furniture category",
        "Look for winter jackets, max price $150, show 12 items"
    ]
}
def get_weather(location: str, unit: str = "celsius"):
    """Get current weather information for a location"""
    print(f"🔍 Calling get_weather function now - this is a test")
    print(f"   📍 Location: {location}")
    print(f"   🌡️  Unit: {unit}")
    print(f"   ✅ Weather data retrieved for {location} in {unit}\n")
    return f"Weather data for {location} in {unit}: 22°C, Sunny"

def calculate_bmi(weight: float, height: float):
    """Calculate Body Mass Index based on height and weight"""
    print(f"🔍 Calling calculate_bmi function now - this is a test")
    print(f"   ⚖️  Weight: {weight} kg")
    print(f"   📏 Height: {height} m")
    bmi = weight / (height ** 2)
    print(f"   📊 BMI calculated: {bmi:.2f}\n")
    return f"BMI: {bmi:.2f} (Weight: {weight}kg, Height: {height}m)"

def send_email(to: list, subject: str, body: str, priority: str = "normal"):
    """Send an email to specified recipients"""
    print(f"🔍 Calling send_email function now - this is a test")
    print(f"   📧 To: {', '.join(to)}")
    print(f"   📝 Subject: {subject}")
    print(f"   📄 Body: {body[:50]}..." if len(body) > 50 else f"   📄 Body: {body}")
    print(f"   🚨 Priority: {priority}")
    print(f"   ✅ Email sent successfully!\n")
    return f"Email sent to {len(to)} recipient(s) with subject '{subject}'"

def search_products(query: str, category: str = None, max_price: float = None, limit: int = 10):
    """Search for products in the database"""
    print(f"🔍 Calling search_products function now - this is a test")
    print(f"   🔎 Query: {query}")
    print(f"   📂 Category: {category if category else 'Any'}")
    print(f"   💰 Max Price: ${max_price if max_price else 'No limit'}")
    print(f"   📊 Limit: {limit} results")
    print(f"   ✅ Found {limit} products matching '{query}'\n")
    return f"Found {limit} products for '{query}'" + (f" in {category}" if category else "")

function_map = {
    "get_weather": get_weather,
    "calculate_bmi": calculate_bmi,
    "send_email": send_email,
    "search_products": search_products
}


api_key = os.getenv("DEEPSEEK_API_KEY")


# def react_agent(user_prompt,tools,function_map):

#     tools['task_complete'] = {
#         "description": "Call this when the task is finished and no more actions are needed",
#         "parameters": {
#             "completion_message": {
#                 "type": "string", 
#                 "description": "Confirmation that the task is complete",
#                 "required": False
#             }}
#     }
#     function_map['task_complete'] = lambda: "Task completed"

#     memory = []
#     while True:
#         current_prompt = f'Here is the memory {memory}, \n Here is the user prompt = {user_prompt}'
#         function_caller = DeepseekFunctionCaller(
#             api_key=api_key,
#             user_prompt=current_prompt,
#             tools=tools
#         )
#         action = function_caller.get_json_output()
#         memory.append(f'Reasoning: {action["reasoning"]}')
        
#         if action["tool_name"] == "task_complete" or action["tool_name"].strip() == "":
#             memory.append("No more tools required - ending loop")
#             print('ENDING THIS WORKED')
#             break
            
#         memory.append(f'Action: function_name {action["tool_name"]}, parameters: {action["parameters"]}')
        
#         tool_name = action["tool_name"] 
#         if tool_name in function_map :
#             function_result = function_map[tool_name](**action["parameters"])
#             memory.append(f'Observation: {function_result}')
            
#             current_prompt = f"Previous result: {function_result}. What should we do next?"
#         else:
#             memory.append(f'Observation: Function {tool_name} not found in function map')
#             break
    
#     return memory
    
p = "Search for gaming laptops under $1200 and then i need to calculate th my BMI if I'm 165cm and 60kg? then Send email to sarah@company.com with subject 'Project Update' and body should mention that i bought a laptop and my bmi"

from llm_modules.react_agent import ReActAgent
react_agent = ReActAgent(api_key,tools,function_map)
result = react_agent.run(p)


for string in result:
    print(string)
