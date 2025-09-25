import yt_dlp

def download_video_from_url(url, output_path='.'):
    """
    Downloads the full video (with audio) from a given URL using yt-dlp.

    Args:
        url (str): The URL of the video to download.
        output_path (str): The directory to save the video file.
    """
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Melhor vídeo + melhor áudio
        'merge_output_format': 'mp4',          # Força saída em MP4
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Nome do arquivo
        'embed_thumbnail': True,   # Tenta embutir thumbnail
        'embed_metadata': True,    # Mantém metadados
        'verbose': True,           # Log detalhado
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Vídeo baixado com sucesso de: {url} para {output_path}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
video_urls = [
    "https://www.youtube.com/watch?v=8wsgLaGUW7s"
]

download_directory = "./downloaded_videos"

for video_url in video_urls:
    download_video_from_url(video_url, download_directory)
    print("!!")
