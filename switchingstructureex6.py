from openai import OpenAI

client = OpenAI(api_key="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")

def generate_response(prompt, chat_history):
    messages = chat_history + [
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        max_tokens=200
    )

    return response.choices[0].message.content

chat_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Bot: Bye!")
        break

    answer = generate_response(user_input, chat_history)
    print(f"Bot: {answer}\n")

    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": answer})
