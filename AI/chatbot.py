import re

# Predefined patterns and responses
patterns = {
    r"hi|hello|hey": "Hello! How can I help you today?",
    r"order.*status|where.*order": "Please provide your order ID to check the status.",
    r"product.*available|have.*(item|product)": "Which product are you looking for?",
    r"(return|refund).*order": "To process a return or refund, please share your order ID.",
    r"thank you|thanks": "You're welcome! Let me know if you need anything else.",
    r"bye|goodbye": "Goodbye! Have a great day."
}

def get_response(user_input):
    user_input = user_input.lower()
    for pattern, response in patterns.items():
        if re.search(pattern, user_input):
            return response
    return "I'm sorry, I didn't understand that. Can you please rephrase?"

def run_chatbot():
    print("🤖 Welcome to ShopBot! (Type 'exit' to end the chat)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Thank you for chatting with us. Bye!")
            break
        response = get_response(user_input)
        print(f"Bot: {response}")

# Run the chatbot
run_chatbot()
