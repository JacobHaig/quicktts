import argparse
import time

from yapper import Yapper, PiperSpeaker, PiperQuality, PiperVoiceGB
from profanityfilter import ProfanityFilter

import LiveStream_Connecter


##################### STREAM VARIABLES #####################

STREAMING_ON_TWITCH = True
STREAMING_ON_YOUTUBE = True


##################### TWITCH VARIABLES #####################
# Replace this with your Twitch username. Must be all lowercase.
TWITCH_CHANNEL = 'aaren202'


##################### YOUTUBE VARIABLES #####################
# If you're streaming on Youtube, replace this with your Youtube's Channel ID
# Find this by clicking your Youtube profile pic -> Settings -> Advanced Settings
YOUTUBE_CHANNEL_ID = "UC6nQpwfyfXZnh1gRpIsAFLQ"  # "a-aron101"

# If you're using an Unlisted stream to test on Youtube, replace "None" below with your stream's URL in quotes.
# Otherwise you can leave this as "None"
YOUTUBE_STREAM_URL = None


streams = []

if STREAMING_ON_TWITCH:
    t = LiveStream_Connecter.Twitch()
    t.stream_connect(TWITCH_CHANNEL)
    streams.append(t)
if STREAMING_ON_YOUTUBE:
    t = LiveStream_Connecter.YouTube()
    t.stream_connect(YOUTUBE_CHANNEL_ID, YOUTUBE_STREAM_URL)
    streams.append(t)


pf = ProfanityFilter()


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--volume", required=False, type=float, default=0.25, help="The Volume level of the TTS")
volume = float(parser.parse_args().volume)


def get_speaker(custom_volume=0.25):
    speaker = PiperSpeaker(
        voice=PiperVoiceGB.NORTHERN_ENGLISH_MALE,
        quality=PiperQuality.MEDIUM,
        volume=custom_volume,
    )

    return Yapper(speaker=speaker)


yapper = get_speaker(custom_volume=volume)


def say(username: str, saying: str) -> None:
    full_saying = f"{username} said: {saying}"
    if username.lower() == "jacob haig":
        full_saying = f"Wisward said: {saying}"

    yapper.yap(pf.censor(full_saying))


def main():
    if not STREAMING_ON_TWITCH and not STREAMING_ON_YOUTUBE:
        print(" === No streams are connected! ===")
        return

    # Collect messages from all streams
    message_queue = []
    while True:
        for stream in streams:
            if isinstance(stream, LiveStream_Connecter.Twitch):
                message_queue.extend(stream.receive_messages())
            elif isinstance(stream, LiveStream_Connecter.YouTube):
                message_queue.extend(stream.receive_messages())

        # Print and say all the messages
        for message in message_queue:
            print(f"username: {message["username"]} message: {message["message"]}")
            say(message["username"], message["message"])
        
        time.sleep(2)
        message_queue.clear()


if __name__ == '__main__':
    main()
