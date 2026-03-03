# ============================================
# Task 8: Simple Chatbot (CLI)
# Built by: Gunn Fulwani
# ============================================

def get_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ['hi', 'hello', 'hey', 'howdy', 'hola']:
        return "Hello! How can I help you today?"

    elif user_input in ['how are you', 'how are you?', 'how r u']:
        return "I'm doing great, thank you for asking! How about you?"

    elif user_input in ['good', 'fine', 'great', 'i am good', "i'm good"]:
        return "That's wonderful to hear!"

    # Name
    elif 'your name' in user_input or 'who are you' in user_input:
        return "I'm HexaBot, your personal assistant built by Gunn Fulwani!"

    # Creator
    elif 'who made you' in user_input or 'who created you' in user_input or 'who built you' in user_input:
        return "I was built by Gunn Fulwani as part of a Python internship project."

    # Age
    elif 'how old are you' in user_input or 'your age' in user_input:
        return "I'm brand new! Just created today."

    # Help
    elif 'help' in user_input or 'what can you do' in user_input:
        return ("I can chat with you! Try asking me:\n"
                "  - My name\n"
                "  - A joke\n"
                "  - The time\n"
                "  - About Python\n"
                "  - General greetings")

    # Jokes
    elif 'joke' in user_input or 'tell me a joke' in user_input or 'funny' in user_input:
        import random
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the programmer quit his job? Because he didn't get arrays!",
            "How do you comfort a JavaScript bug? You console it!",
            "Why do Java developers wear glasses? Because they don't C#!",
            "A SQL query walks into a bar, walks up to two tables and asks... Can I join you?"
        ]
        return random.choice(jokes)

    # Time
    elif 'time' in user_input or 'what time' in user_input:
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}."

    # Date
    elif 'date' in user_input or 'today' in user_input or "what's today" in user_input:
        from datetime import datetime
        today = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today}."

    # Python
    elif 'python' in user_input:
        return ("Python is an amazing programming language! "
                "It's great for data analysis, web development, automation and AI.")

    # Weather (redirect)
    elif 'weather' in user_input:
        return "I can't check live weather, but try asking a weather app for that!"

    # Thanks
    elif user_input in ['thanks', 'thank you', 'thankyou', 'ty']:
        return "You're welcome! Happy to help."

    # Bye
    elif user_input in ['bye', 'goodbye', 'exit', 'quit', 'see you']:
        return "Goodbye! Have a great day!"

    # Default
    else:
        return "I'm not sure I understand that. Try asking something else or type 'help'."


def chatbot():
    print("=" * 45)
    print("             HexaBOT")
    print("      Your Personal CLI Assistant")
    print("=" * 45)
    print("Type 'bye' to exit.")
    print()

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        response = get_response(user_input)
        print(f"HexaBot: {response}")
        print()

        if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit', 'see you']:
            break


chatbot()

