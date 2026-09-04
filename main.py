from config import create_project_directiories
from downloader import download_audio
from transcriber import transcribe_audio
from transcript_writer import get_transcript_path, write_transcript




def main() -> None:
    create_project_directiories()

    print("=" * 50)
    print("TRANSCRITOR DE LIVES DE RPG")
    print("=" * 50)

    url = input("\nCole a URL da live do YouTube:\n> ").strip()

    if not url:
        print("\nNenhuma URL foi informada.")
        return

    print("\nIniciando download do áudio...\n")

    try:
        audio_path = download_audio(url)
    except Exception as error:
        print(f"\nErro ao baixar o áudio: {error}")
        return

    print("\nDownload concluído.")
    print(f"Arquivo salvo em: {audio_path}")
    print("\nIniciando transcrição do áudio...\n")

    try:
        segments, info = transcribe_audio(audio_path)
    except Exception as error:
        print(f"\nErro ao transcrever o áudio: {error}")
        return

    print(f"\nIdioma: {info.language}")
    print(f"Probabilidade: {info.language_probability:.2%}\n")

    transcript_path = get_transcript_path(audio_path)

    print(f"Salvando transcrição em: {transcript_path}\n")

    try:
        write_transcript(transcript_path, segments)
    except Exception as error:
        print(f"\nErro ao salvar a transcrição: {error}")
        return

    print("\nTranscrição concluída.")
    print(f"Arquivo salvo em: {transcript_path}")



if __name__ == "__main__":
    main()