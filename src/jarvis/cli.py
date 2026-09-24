from jarvis import __version__
from jarvis.chat import run


def main() -> None:
    print(f"Jarvis {__version__}")
    run()


if __name__ == "__main__":
    main()
