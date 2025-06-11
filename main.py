import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="GetAudioFromYT",
        description="Download audio from YouTube and convert it."
    )

    parser.add_argument("url",
        help="YouTube-Video-URL"
    )
    parser.add_argument("-c", "--convert",
        action="store_true",
        dest="convert_audio",
        help="Convert to the selected format after download"
    )
    parser.add_argument("-f", "--format",
        choices=['mp3','wma','flac','aac','opus','alac'],
        default="mp3",
        help="Audio format (default: mp3)"
    )

    args = parser.parse_args()
    downloader = downloader(
        url=args.url,
        convertAudio=args.convert_audio,
        audioFormat=args.format
    )
    downloader.run()

if __name__ == '__main__':
    main()
