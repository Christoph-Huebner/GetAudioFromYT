import ffmpeg
import logging
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix.exceptions import RegexMatchError, VideoUnavailable

class downloader:
    def __init__(self, url: str=None, convertAudio:bool=True, audioFormat:str='mp3'):
        self.__url = url
        self.__convertAudio = convertAudio
        self.__audioFormat = audioFormat

        self.__audioFile = None

        self.__providedAudioFormats = ['mp3', 'wma', 'flac', 'aac', 'opus', 'alac']
        self.__formatOptions = {
            'mp3':  {'acodec': 'libmp3lame',   'audio_bitrate': '320k'},
            'wma':  {'acodec': 'wmav2',        'audio_bitrate': '256k'},
            'flac': {'acodec': 'flac',         'compression_level': 6},
            'aac':  {'acodec': 'libfdk_aac',   'audio_bitrate': '256k'},
            'opus': {'acodec': 'libopus',      'audio_bitrate': '128k'},
            'alac': {'acodec': 'alac'}  ,
        }

    def run(self):
        '''
        Downloads the audio from a YouTube video and converts it to a specified format.
        '''
        if not self.__url:
            logging("❌ No URL provided.")
            return

        if self.__convertAudio and self.__audioFormat not in self.__providedAudioFormats:
            logging(f"❌ Invalid audio format '{self.__audioFormat}'. Supported formats are: {', '.join(self.__providedAudioFormats)}")
            return

        try:
            yt = YouTube(self.__url, on_progress_callback=on_progress)
        except RegexMatchError:
            logging("❌ Invalid YouTube URL.")
            return
        except VideoUnavailable:
            logging("❌ Video is unavailable or removed.")
            return

        audioStream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        self.__audioFile = audioStream.download()

        if self.__convertAudio:
            audioFile = self.__convert()

        logging(f"✅ Downloaded audio: {audioFile}")

    def __convert(self):
        ''' Converts an audio file to the specified format using ffmpeg.'''
        base = os.path.splitext(self.__audioFile)[0]

        opts = self.__formatOptions.get(self.__audioFormat, {})
        outputFile = f"{base}.{self.__audioFormat}"
        try:
            (
                ffmpeg
                .input(self.__audioFile)
                .output(outputFile, format=self.__audioFormat, **opts, vn=None)
                .run(overwrite_output=True, quiet=True)
            )
            return outputFile
        except ffmpeg.Error as e:
            logging("❌ Conversion failed:", e)
            return None
