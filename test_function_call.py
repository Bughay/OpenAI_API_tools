from llm_modules.function_caller import DeepseekFunctionCaller
import os
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





api_key = os.getenv("DEEPSEEK_API_KEY") 

get_weather = 0
calculate_bmi = 0
send_email = 0
search_products = 0
wrong_tool = 0
total = 0
for key,values in test_prompts.items():
    for prompt in values:
        function_caller = DeepseekFunctionCaller(
                api_key=api_key,
                user_prompt=prompt,
                tools=tools
            )
        function_result = function_caller.get_json_output()
        total += 1
        if function_result['tool_name'] == key:
            print(f"Prompt: {prompt}")
            print(f"Expected: {key}, Got: {function_result['tool_name']}")

            if key == "get_weather":
                get_weather += 1
            elif key == "calculate_bmi":
                calculate_bmi += 1
            elif key == "send_email":
                send_email += 1
            elif key == "search_products":
                search_products += 1
            print("✅ Correct")
        else:
            wrong_tool += 1
            print("❌ Wrong")


final_result = get_weather + calculate_bmi + send_email + search_products
final_result = (total/wrong_tool) * 100
print(f'{final_result*100} percent success in function calling')