# Task 4: Basic Chatbot

# Function to generate chatbot responses
def chatbot(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."


# Main program
print("Welcome to Basic Chatbot!")

while True:
    user_input = input("You: ")

    response = chatbot(user_input)

    print("Bot:", response)

    if user_input.lower() == "bye":
        break
