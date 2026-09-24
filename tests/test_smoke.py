from jarvis import __version__
from jarvis.__main__ import main


def test_version_is_set():
    assert __version__ == "0.1.0"


def test_main_prints_greeting(capsys):
    main()
    assert "Jarvis" in capsys.readouterr().out
