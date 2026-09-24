from jarvis.chat import run


def test_echoes_input_until_exit():
    inputs = iter(["hello", "exit"])
    outputs = []

    run(input_fn=lambda prompt: next(inputs), output_fn=outputs.append)

    assert "Jarvis: You said: hello" in outputs
    assert outputs[-1] == "Goodbye!"


def test_blank_input_is_skipped():
    inputs = iter(["", "  ", "quit"])
    outputs = []

    run(input_fn=lambda prompt: next(inputs), output_fn=outputs.append)

    assert outputs == ["Jarvis is ready. Type 'exit' or 'quit' to leave.", "Goodbye!"]


def test_eof_exits_gracefully():
    def raise_eof(prompt):
        raise EOFError

    outputs = []
    run(input_fn=raise_eof, output_fn=outputs.append)

    assert outputs[-1] == "Goodbye!"


def test_keyboard_interrupt_exits_gracefully():
    def raise_interrupt(prompt):
        raise KeyboardInterrupt

    outputs = []
    run(input_fn=raise_interrupt, output_fn=outputs.append)

    assert outputs[-1] == "Goodbye!"
