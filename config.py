from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

AUDIO_DIR = BASE_DIR / "audios"
TRANSCRIPT_DIR = BASE_DIR / "transcricoes"

WHISPER_MODEL = "medium"  # Options: tiny, base, small, medium, large
LANGUAGE = "pt"  # Language code for transcription (e.g., 'en' for English, 'pt' for Portuguese)


def create_project_directiories() -> None:
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)

