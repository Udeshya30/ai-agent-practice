from agent.controller import run_agent


def main():

    print("AI Agent Started")

    while True:

        user_input = input("You: ")

        if user_input == "exit":
            break

        answer = run_agent(user_input)

        print("\nAgent:", answer)


if __name__ == "__main__":
    main()