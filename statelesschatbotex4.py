chat_history = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("\n--- end chat ---\n")
        break

    chat_history.append(user_input)

    print("\n--- Chat History ---")
    for msg in chat_history:
        print(msg)
    print("--------------------\n")