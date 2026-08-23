def simple_chatbot():
    print("Chatbot: Hello! I am your assistant. Type 'bye' to exit.")
    
    # 5 basic questions and answers
    qa_pairs = {
        "what is your name": "I am a simple Python chatbot.",
        "how are you": "I'm doing great, thank you!",
        "what can you do": "I can answer 5 basic questions for you.",
        "who created you": "I was created using Python.",
        "what time is it": "Time is an illusion, but I'm running right now!"
    }

    while True:
        try:
            user_input = input("\nYou: ").strip().lower()
            
            if not user_input:
                raise ValueError("Input cannot be empty. Please try again.")
            
            if user_input == "bye":
                print("Chatbot: Goodbye! Have a nice day.")
                break
            elif user_input in ["hi", "hello", "hey"]:
                print("Chatbot: Hi there! How can I help you today?")
            elif user_input in qa_pairs:
                print(f"Chatbot: {qa_pairs[user_input]}")
            else:
                print("Chatbot: I'm sorry, I don't understand that question. Try asking something else!")
                
        except ValueError as ve:
            print(f"Chatbot Error: {ve}")
        except Exception as e:
            print(f"Chatbot: An unexpected error occurred: {e}")

if __name__ == "__main__":
    simple_chatbot()