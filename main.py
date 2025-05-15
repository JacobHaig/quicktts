import argparse
import time

from yapper import Yapper, PiperSpeaker, PiperQuality, PiperVoiceGB
from profanityfilter import ProfanityFilter

import livestream


parser = argparse.ArgumentParser()
parser.add_argument(
    "-v",
    "--volume",
    required=False,
    type=float,
    default=0.25,
    help="The Volume level of the TTS",
)
volume = float(parser.parse_args().volume)

##################### STREAM VARIABLES #####################

STREAMING_ON_TWITCH = True
STREAMING_ON_YOUTUBE = True


##################### TWITCH VARIABLES #####################
# Replace this with your Twitch username. Must be all lowercase.
TWITCH_CHANNEL = "aaren202"


##################### YOUTUBE VARIABLES #####################
# If you're streaming on Youtube, replace this with your Youtube's Channel ID
# Find this by clicking your Youtube profile pic -> Settings -> Advanced Settings
YOUTUBE_CHANNEL_ID = "UC6nQpwfyfXZnh1gRpIsAFLQ"  # "a-aron101"

# If you're using an Unlisted stream to test on Youtube, replace "None" below with your stream's URL in quotes.
# Otherwise you can leave this as "None"
YOUTUBE_STREAM_URL = None


streams = []

if STREAMING_ON_TWITCH:
    t = livestream.Twitch()
    t.stream_connect(TWITCH_CHANNEL)
    streams.append(t)
if STREAMING_ON_YOUTUBE:
    t = livestream.YouTube()
    t.stream_connect(YOUTUBE_CHANNEL_ID, YOUTUBE_STREAM_URL)
    streams.append(t)


pf = ProfanityFilter()


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


def handle_message(message: dict) -> None:
    """
    Handle the incoming message from the stream.
    This function can be extended to include more complex logic.
    """
    # Example: You can add more processing here if needed
    # For now, we just print the message
    print(f"username: {message['username']} message: {message['message']}")
    say(message["username"], message["message"])


def main():
    if not STREAMING_ON_TWITCH and not STREAMING_ON_YOUTUBE:
        print(" === No streams are connected! ===")
        return

    # Collect messages from all streams
    message_queue = []
    while True:
        # Receive messages from each stream
        for stream in streams:
            message_queue.extend(stream.receive_messages())

        # Print and say all the messages
        for message in message_queue:
            handle_message(message)

        time.sleep(0.5)
        message_queue.clear()


if __name__ == "__main__":
    main()
