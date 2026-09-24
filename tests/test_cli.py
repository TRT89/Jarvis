from jarvis import __version__
from jarvis.cli import main


def test_version():
    assert __version__ == "0.1.0"


def test_main_prints_banner(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == f"Jarvis {__version__} - chat loop coming in the next step."
