import random
from datetime import datetime
import requests

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    
    responses = {
        "hello|hi|hey": ["Hello!", "Hi there!", "Hey! How can I assist you today?"],
        "how are you": ["I'm just a bot, but I'm doing great! How about you?"],
        "i am fine|i'm fine|i am good|i'm good|fine|good": ["That's great to hear!", "Glad to know you're doing well!", "Awesome! Stay positive!"],
        "what is your name|your name": ["I'm ChatBot, your virtual assistant."],
        "tell me a joke": [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call fake spaghetti? An impasta!",
            "Why don’t skeletons fight each other? They don’t have the guts!"
        ],
        "tell me a fact": [
            "Did you know? Honey never spoils! Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible.",
            "Bananas are berries, but strawberries are not!",
            "Octopuses have three hearts and their blood is blue!"
        ],
        "what can you do": [
            "I can chat with you, tell jokes, fetch weather updates, and more!"
        ]
    }
    
    for pattern, response_list in responses.items():
        if user_input in pattern.split('|'):
            return random.choice(response_list)
    
    if "time" in user_input:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"
    
    if "date" in user_input:
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}"
    
    if "weather in" in user_input:
        city = user_input.split("weather in ")[-1]
        return get_weather(city)
    
    return "I'm not sure how to respond to that. Can you ask something else?"

def get_weather(city):
    api_key = "8025cd789f3a486392172935250203"  # Replace with a valid API key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    try:
        response = requests.get(url).json()
        return f"The temperature in {city} is {response['current']['temp_c']}°C with {response['current']['condition']['text']}."
    except:
        return "Sorry, I couldn't fetch the weather right now."

def start_chat():
    print("ChatBot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ["bye", "exit", "quit"]:
            print("ChatBot: Goodbye! Have a wonderful day!")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")
        
if __name__ == "__main__":
    start_chat()
