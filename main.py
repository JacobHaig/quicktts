import argparse

import pytchat
from yapper import Yapper, PiperSpeaker, PiperQuality, PiperVoiceGB

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--id", required=True, help="Your Video ID")
parser.add_argument("-v", "--volume", required=False, type=float, default=0.25, help="Your Video Volume")

yt_video_id = str(parser.parse_args().id)
volume = float(parser.parse_args().volume)


def get_speaker(custom_volume=0.25):
    speaker = PiperSpeaker(
        voice=PiperVoiceGB.NORTHERN_ENGLISH_MALE,
        quality=PiperQuality.MEDIUM,
        volume=custom_volume,
    )

    return Yapper(speaker=speaker)


yapper = get_speaker(custom_volume=volume)


def say(user: str, saying: str) -> None:
    yapper.yap(f"{user} said: {saying}")


def main():
    chat = pytchat.create(video_id=yt_video_id)

    if chat.is_alive():
        print(" === Youtube Stream is connected! ===")
    else:
        print(" === Youtube Stream is not connected! ===")
        return

    while chat.is_alive():
        for c in chat.get().sync_items():
            print(f"{c.datetime} [{c.author.name}]- {c.message}")
            say(c.author.name, c.message)


if __name__ == '__main__':
    main()
