from unittest.mock import patch

from jarvis import __version__
from jarvis.cli import main


def test_version():
    assert __version__ == "0.1.0"


def test_main_prints_banner_and_starts_chat(capsys):
    with patch("jarvis.cli.run") as mock_run:
        main()

    captured = capsys.readouterr()
    assert captured.out.strip() == f"Jarvis {__version__}"
    mock_run.assert_called_once()
