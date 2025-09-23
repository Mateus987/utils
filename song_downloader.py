import yt_dlp

def download_audio_from_url(url, output_path='.', audio_format='mp3'):
    """
    Downloads only the audio from a given URL using yt-dlp.

    Args:
        url (str): The URL of the video to download audio from.
        output_path (str): The directory to save the audio file.
        audio_format (str): The desired audio format (e.g., 'mp3', 'm4a', 'wav').
    """
    ydl_opts = {
        'format': 'bestaudio/best',  # Prioritize best audio quality
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Output template
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': audio_format,
            'preferredquality': '192',  # Example: 192kbps for MP3
        }],
        'embed_thumbnail': True,  # Embed thumbnail as album art
        'embed_metadata': True,   # Embed metadata
        'verbose': True,          # Show detailed output
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download realizado com sucesso de:{url} para {output_path}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Example usage:
video_urls = [
    "https://www.youtube.com/watch?v=8wsgLaGUW7s"
    ]

download_directory = "./downloaded_audio"
desired_audio_format = "mp3"

for video_url in video_urls:
    download_audio_from_url(video_url, download_directory, desired_audio_format)
    print("!!")