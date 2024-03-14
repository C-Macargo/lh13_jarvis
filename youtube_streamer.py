import yt_dlp

class YouTubeStreamer:
    @staticmethod
    def get_audio_url(video_url):
        with yt_dlp.YoutubeDL({'format': 'worstaudio', 'noplaylist': True}) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            audio_url = info_dict.get('url', None)
            return audio_url
