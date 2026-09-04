from pathlib import Path

from config import TRANSCRIPT_DIR


def get_transcript_path(audio_path: Path) -> Path:
    return TRANSCRIPT_DIR / f"{audio_path.stem}.txt"


def format_timestamp(seconds: float) -> str:
    total_seconds = int(seconds)

    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{hours:02}:{minutes:02}:{seconds:02}"


def write_transcript(transcript_path: Path, segments) -> None:
    with transcript_path.open("w", encoding="utf-8") as file:
        for segment in segments:
            start = format_timestamp(segment.start)
            end = format_timestamp(segment.end)
            text = segment.text.strip()

            file.write(f"[{start} - {end}] {text}\n")
            file.flush()