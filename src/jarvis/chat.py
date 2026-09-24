EXIT_COMMANDS = {"exit", "quit"}


def respond(message: str) -> str:
    return f"You said: {message}"


def run(input_fn=input, output_fn=print) -> None:
    output_fn("Jarvis is ready. Type 'exit' or 'quit' to leave.")
    while True:
        try:
            user_input = input_fn("You: ")
        except (EOFError, KeyboardInterrupt):
            output_fn("Goodbye!")
            return

        stripped = user_input.strip()
        if not stripped:
            continue
        if stripped.lower() in EXIT_COMMANDS:
            output_fn("Goodbye!")
            return

        output_fn(f"Jarvis: {respond(stripped)}")
