from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

AUDIO_DIR = BASE_DIR / "audios"
TRANSCRIPT_DIR = BASE_DIR / "transcricoes"

WHISPER_MODEL = "medium"  # Options: tiny, base, small, medium, large
LANGUAGE = "pt"  # Language code for transcription (e.g., 'en' for English, 'pt' for Portuguese)
DEVICE = "cpu"  # Options: 'cpu', 'cuda', 'mps' (for Apple Silicon), etc.
COMPUTER_TYPE = "int8"  # Options: 'int8', 'float16', 'float32', etc. depending on your hardware and model support


def create_project_directiories() -> None:
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)

