import argparse
from downloader import Downloader

def main():
    '''
    Main function to parse command line arguments and initiate the downloader.
    '''
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
        choices=Downloader.FORMAT_OPTIONS.keys(),
        default="mp3",
        help="Audio format (default: mp3)"
    )
    args = parser.parse_args()

    downloader = Downloader(
        url = args.url,
        convert_audio=args.convert_audio,
        audioFormat=args.format)
    downloader.run()

if __name__ == '__main__':
    main()

# Test
