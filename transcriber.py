from pathlib import Path
from faster_whisper import WhisperModel
from config import (COMPUTER_TYPE, DEVICE, LANGUAGE, WHISPER_MODEL)


def transcribe_audio(audio_path: Path):
    model = WhisperModel(
        WHISPER_MODEL,
        device=DEVICE,
        compute_type=COMPUTER_TYPE
        )

    segments, info = model.transcribe(
        str(audio_path),
        language=LANGUAGE,
        beam_size=5,
        vad_filter=True,
    )

    return segments, info