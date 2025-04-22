def chatbot():
    print("🤖 Hello! I'm your friendly chatbot.")
    print("You can ask me about products, support, pricing, or say 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if 'product' in user_input:
            print("🤖 We offer a range of products including phones, laptops, and accessories.")
        elif 'price' in user_input or 'cost' in user_input:
            print("🤖 Our products start from ₹999 and go up based on your needs.")
        elif 'support' in user_input or 'help' in user_input:
            print("🤖 You can contact our support team at support@example.com.")
        elif 'return' in user_input or 'refund' in user_input:
            print("🤖 We have a 7-day easy return policy. Visit our return portal.")
        elif 'bye' in user_input or 'exit' in user_input:
            print("🤖 Goodbye! Have a great day 😊")
            break
        else:
            print("🤖 Sorry, I didn't understand that. Could you please rephrase?")

# Run the chatbot
chatbot()
