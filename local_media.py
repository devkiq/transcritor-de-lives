from pathlib import Path


def get_local_media_path(path_text: str) -> Path:
    media_path = Path(path_text.strip().strip('"'))

    if not media_path.exists():
        raise FileNotFoundError("O arquivo informado não existe.")

    if not media_path.is_file():
        raise ValueError("O caminho informado não é um arquivo.")

    return media_path