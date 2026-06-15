from datetime import datetime
import random

# ==============================
#        SMART CHATBOT
# ==============================

print("=" * 50)
print("        WELCOME TO SMART CHATBOT")
print("=" * 50)
print("Type 'help' to see commands")
print("Type 'exit' to close chatbot\n")

# Random responses
greetings = [
    "Hello! Nice to meet you.",
    "Hi there!",
    "Hey! How can I help you today?"
]

how_are_you = [
    "I'm doing great!",
    "All systems are running perfectly.",
    "I am fine. Thanks for asking!"
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did Python go to school? To improve its class.",
    "Why was the computer cold? Because it left its Windows open!"
]

while True:

    user_input = input("You: ").lower().strip()

    # EXIT
    if user_input == "exit":
        print("Bot: Goodbye! Have a great day.")
        break

    # HELP MENU
    elif user_input == "help":
        print("\n===== AVAILABLE COMMANDS =====")
        print("hello")
        print("how are you")
        print("time")
        print("date")
        print("joke")
        print("calculator")
        print("about python")
        print("motivate me")
        print("exit")
        print("=" * 35)

    # GREETING
    elif user_input in ["hello", "hi", "hey"]:
        print("Bot:", random.choice(greetings))

    # HOW ARE YOU
    elif user_input == "how are you":
        print("Bot:", random.choice(how_are_you))

    # TIME
    elif user_input == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current Time is", current_time)

    # DATE
    elif user_input == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's Date is", current_date)

    # JOKE
    elif user_input == "joke":
        print("Bot:", random.choice(jokes))

    # ABOUT PYTHON
    elif user_input == "about python":
        print("Bot: Python is a powerful and beginner-friendly programming language.")

    # MOTIVATION
    elif user_input == "motivate me":
        print("Bot: Keep learning consistently. Small progress daily becomes huge success.")

    # CALCULATOR
    elif user_input == "calculator":

        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                print("Bot: Result =", num1 + num2)

            elif operator == "-":
                print("Bot: Result =", num1 - num2)

            elif operator == "*":
                print("Bot: Result =", num1 * num2)

            elif operator == "/":
                if num2 == 0:
                    print("Bot: Cannot divide by zero.")
                else:
                    print("Bot: Result =", num1 / num2)

            else:
                print("Bot: Invalid operator.")

        except ValueError:
            print("Bot: Please enter valid numbers.")

    # UNKNOWN COMMAND
    else:
        print("Bot: Sorry, I don't understand that command.")