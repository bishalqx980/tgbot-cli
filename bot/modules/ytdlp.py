import os
from yt_dlp import YoutubeDL

def youtube_download(url, tg_upload=False):
    """
    Note: only `mp3` audio file download
    """
    try:
        options = {
            "format": "bestaudio[ext=mp3]/bestaudio/best"
        }

        if tg_upload:
            try:
                os.remove("downloads/audio.mp3")
            except Exception as e:
                print(e)
            options.update({"outtmpl": "downloads/audio.mp3"})
        else:
            options.update({"outtmpl": "downloads/%(title)s.mp3"})

        ytdl = YoutubeDL(options)
        ytdl.download([url])

        if tg_upload:
            file_info = ytdl.extract_info(url)
            data = {
                "file_name": file_info["title"],
                "file_path": "downloads/audio.mp3"
            }

            return data
    except Exception as e:
        print(e)
