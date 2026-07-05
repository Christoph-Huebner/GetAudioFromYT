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
        self.__audio_file = audio_stream.download(output_path='files')

        if self.__convert_audio:
            self.__convert()

        logging.info(f"✅ Downloaded audio: {self.__audio_file}")

    def __convert(self):
        ''' Converts an audio file to the specified format using ffmpeg.'''
        base, _ = os.path.splitext(self.__audio_file)
        output_file = f"{base}.{self.__audio_format}"

        opts = self.FORMAT_OPTIONS.get(self.__audio_format)

        if opts is None:
            logging.error("❌ Unknown audio format: %s", self.__audio_format)
            return

        try:
            # This is because .m4a is essentially an MPEG-4 audio container, and FFmpeg often uses the mp4 muxer internally.
            output_format = "mp4" if self.__audio_format == "m4a" else self.__audio_format

            # FFmpeg cannot write to the same file it is reading from.
            # If input and output paths are identical, use a temporary output file.
            final_output_file = output_file
            if os.path.abspath(self.__audio_file) == os.path.abspath(output_file):
                output_file = f"{base}.converted.{self.__audio_format}"

            (
                ffmpeg
                .input(self.__audio_file)
                .output(output_file, format=output_format, **opts, vn=None)
                .run(
                    overwrite_output=True,
                    capture_stdout=True,
                    capture_stderr=True
                )
            )

            # Cleanup the not neeed files
            os.remove(self.__audio_file)

            if output_file != final_output_file:
                os.rename(output_file, final_output_file)

            self.__audio_file = final_output_file

            logging.info("✅ Converted audio: %s", self.__audio_file)

        except ffmpeg.Error as e:
            stderr = e.stderr.decode("utf-8", errors="replace") if e.stderr else ""
            logging.error("❌ Conversion failed for %s", self.__audio_file)
            logging.error("FFmpeg stderr:\n%s", stderr)

        except Exception:
            logging.exception("❌ Unexpected conversion error")
