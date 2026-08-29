def chatbot():
    print(" Chatbot: Hello! I am your basic chatbot.")
    name = input("You: What's your name? ")
    print(f"Chatbot: Wow, beautiful name !! Nice to meet you, {name}!")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or  user_input == "hi":
            print(f"Chatbot: Hi {name}!")
        elif user_input == "how are you":
            print("Chatbot: I'm doing great, thanks for asking!")
        elif user_input == "time":
            from datetime import datetime
            current_time = datetime.now().strftime('%H:%M')
            print(f"Chatbot: The current time is {current_time}.")
        elif user_input == "date":
            from datetime import datetime
            current_date = datetime.now().strftime('%Y-%m-%d')
            print(f"Chatbot: Today's date is {current_date}.")
        elif user_input == "help":
            print("Chatbot: You can ask me about the time, date, or even ask for a joke!")
        elif user_input == "joke":
            print("Chatbot: What do programmers eat ? Answer: Cookies, because they are always accepting them!")
        elif user_input == "thank you" or user_input == "thanks":
            print(f"Chatbot: You are welcome dear {name}!")
        elif user_input == "bye":
            print(f"Chatbot: Goodbye {name}! Have a wonderful day ahead!")
            break
        else:
            print("Chatbot: Sorry, I did not understand that. Can you try something else?")

chatbot()