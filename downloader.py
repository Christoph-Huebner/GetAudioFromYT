import ffmpeg
import logging
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix.exceptions import RegexMatchError, VideoUnavailable
import toml

class Downloader:
    _cfg = toml.load("config.toml")
    FORMAT_OPTIONS = _cfg["format_options"]

    def __init__(self, url: str=None, convert_audio:bool=True, audioFormat:str='mp3'):
        self.__url = url
        self.__convert_audio = convert_audio
        self.__audio_format = audioFormat

        self.__audio_file = None

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

    def run(self):
        '''
        Downloads the audio from a YouTube video and converts it to a specified format.
        '''
        try:
            yt = YouTube(self.__url, on_progress_callback=on_progress)
        except RegexMatchError:
            logging.error("❌ Invalid YouTube URL.")
            return
        except VideoUnavailable:
            logging.error("❌ Video is unavailable or removed.")
            return

        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        self.__audio_file = audio_stream.download(output_path='Files')

        if self.__convert_audio:
            self.__convert()

        logging.info(f"✅ Downloaded audio: {self.__audio_file}")

    def __convert(self):
        ''' Converts an audio file to the specified format using ffmpeg.'''
        base = os.path.splitext(self.__audio_file)[0]

        opts = self.FORMAT_OPTIONS.get(self.__audio_format, {})
        output_file = f"{base}.{self.__audio_format}"
        try:
            (
                ffmpeg
                .input(self.__audio_file)
                .output(output_file, format=self.__audio_format, **opts, vn=None)
                .run(overwrite_output=True, quiet=True)
            )
            os.remove(self.__audio_file)
            self.__audio_file = output_file
        except ffmpeg.Error as e:
            logging.error("❌ Conversion failed:", e)
            return None
