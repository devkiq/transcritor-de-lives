from config import create_project_directiories
from downloader import download_audio
from local_media import get_local_media_path
from transcriber import transcribe_audio
from transcript_writer import get_transcript_path, write_transcript


def main() -> None:
    create_project_directiories()

    print("=" * 50)
    print("TRANSCRITOR DE LIVES DE RPG")
    print("=" * 50)

    print("\nEscolha a origem:")
    print("1 - YouTube")
    print("2 - Arquivo local")

    option = input("\n> ").strip()

    if option == "1":
        url = input(
            "\nCole a URL da live do YouTube:\n> "
        ).strip()

        if not url:
            print("\nNenhuma URL foi informada.")
            return

        print("\nIniciando download do áudio...\n")

        try:
            media_path = download_audio(url)
        except Exception as error:
            print(f"\nErro ao baixar o áudio: {error}")
            return

        print("\nDownload concluído.")
        print(f"Arquivo salvo em: {media_path}")

    elif option == "2":
        path_text = input(
            "\nInforme o caminho do vídeo ou áudio:\n> "
        ).strip()

        try:
            media_path = get_local_media_path(path_text)
        except Exception as error:
            print(f"\nErro ao abrir o arquivo: {error}")
            return

        print("\nArquivo local carregado.")
        print(f"Arquivo selecionado: {media_path}")

    else:
        print("\nOpção inválida.")
        return

    print("\nIniciando transcrição...\n")

    try:
        segments, info = transcribe_audio(media_path)
    except Exception as error:
        print(f"\nErro ao iniciar a transcrição: {error}")
        return

    print(f"Idioma: {info.language}")
    print(f"Probabilidade: {info.language_probability:.2%}")

    transcript_path = get_transcript_path(media_path)

    print(f"\nSalvando transcrição em:")
    print(transcript_path)
    print()

    try:
        write_transcript(
            transcript_path,
            segments,
        )
    except Exception as error:
        print(f"\nErro durante a transcrição: {error}")
        return

    print("\nTranscrição concluída.")
    print(f"Arquivo salvo em: {transcript_path}")


if __name__ == "__main__":
    main()