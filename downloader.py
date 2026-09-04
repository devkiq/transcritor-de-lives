from pathlib import Path
from yt_dlp import YoutubeDL
from config import AUDIO_DIR

def download_audio(url: str) -> Path:
    options = {
        "format": "m4a/bestaudio/best",
        "outtmpl": str(AUDIO_DIR / "%(title)s [%(id)s].%(ext)s"),
        "noplaylist": True,
    }
    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        downloads = info.get("requested_downloads")

        if not downloads:
            raise RuntimeError("Não foi possível identificar o arquivo de áudio baixado.")

        filepath = downloads[0].get("filepath")

        if not filepath:
            raise RuntimeError("O yt-dlp não informou o caminho do áudio")

        return Path(filepath)