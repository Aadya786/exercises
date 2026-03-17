def get_weather(city):
    return f"The weather in {city} is sunny (fake news)."

def calculate_math(numbers):
    return f"The sum is {sum(numbers)}."

def main():
    while True:
        user_input = input("\nAsk something (or type 'quit'): ").lower()

        if user_input == "quit":
            break

        if "weather" in user_input:
            words = user_input.split()
            city = words[-1].capitalize()
            result = get_weather(city)

        elif "add" in user_input or "plus" in user_input:
            numbers = [int(w) for w in user_input.split() if w.isdigit()]
            result = calculate_math(numbers)

        else:
            result = "I don't know how to help with that yet."

        print(result)

if __name__ == "__main__":
    main()
