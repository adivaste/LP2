def greet():
    print("Chatbot: Hello! How can I assist you today?")

def chat():
    while True:
        user_input = input("User: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = generate_response(user_input)
            print("Chatbot:", response)

def generate_response(user_input):
    # Placeholder logic for generating a response based on user input
    if "order" in user_input.lower():
        return "Sure, I can help you with placing an order. Please provide me with the details."
    elif "payment" in user_input.lower():
        return "For payment-related queries, you can visit our website or contact our customer support."
    else:
        return "I'm sorry, I didn't understand. Can you please rephrase or ask a different question?"

# Main function
def main():
    greet()
    chat()

# Run the chatbot
if __name__ == '__main__':
    main()
