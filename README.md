# QuickTTS

QuickTTS is a streamlined text-to-speech application that converts chat messages from Twitch and YouTube livestreams into spoken audio. With minimal setup and configuration, you can have your stream chat being read aloud in minutes.

## Features

- **Multi-platform Support**: Works with both Twitch and YouTube livestreams simultaneously
- **Customizable TTS**: Control volume and use high-quality voice synthesis via Piper
- **Profanity Filter**: Automatically censors inappropriate language
- **British English Voice**: Uses a Northern English Male voice by default
- **Fully Local Processing**: All TTS processing happens on your machine with no internet dependency for voice generation

## Installation

### Step 1: Install Python
Download and install Python 3.13+ from the [official Python website](https://www.python.org/downloads/).
Make sure to check "Add Python to PATH" during installation.

### Step 2: Install UV Package Manager
UV is a fast Python package installer that QuickTTS uses.

```bash
pip install uv --upgrade
```

### Step 3: Clone or Download the Repository
Download the QuickTTS files to a directory on your computer.

### Step 4: Install Dependencies
Open a terminal/command prompt in the QuickTTS directory and run:

```bash
uv sync
```

## Configuration

Before running QuickTTS, you need to configure it for your streaming accounts.

### Open `main.py` in a text editor and modify:

1. **Streaming Platforms**:
   - Set `STREAMING_ON_TWITCH = True` to enable Twitch integration
   - Set `STREAMING_ON_YOUTUBE = True` to enable YouTube integration

2. **Twitch Configuration**:
   - Replace `TWITCH_CHANNEL = "aaren202"` with your Twitch username

3. **YouTube Configuration**:
   - Replace `YOUTUBE_CHANNEL_ID = "UC6nQpwfyfXZnh1gRpIsAFLQ"` with your YouTube Channel ID
   - You can find your Channel ID by going to YouTube → Settings → Advanced Settings
   - For testing with unlisted streams, you can set `YOUTUBE_STREAM_URL` to your stream URL

4. **Optional**: Voice customization
   - The application uses a Northern English Male voice by default
   - Voice settings can be modified in the `get_speaker` function

## Running QuickTTS

After configuration, run QuickTTS using:

```bash
uv run main.py
```

### Volume Control

Adjust the TTS volume with the `-v` or `--volume` parameter (default is 0.25):

```bash
uv run main.py -v 0.75
```

The volume parameter accepts values between 0.0 (silent) and 1.0 (maximum volume).

## Usage Tips

- **Start QuickTTS after going live**: Launch the application after starting your stream to ensure it's properly connected
- **Test with an unlisted stream**: For YouTube, use an unlisted stream URL for testing
- **Monitor CPU usage**: If performance issues occur, try closing unnecessary applications
- **Keep the terminal window open**: Closing the terminal window will stop QuickTTS

## Credits

QuickTTS is built on:
- [Yapper TTS](https://github.com/mush42/yapper) for text-to-speech functionality
- [DougDoug's TwitchPlays](https://github.com/DougDougGithub/TwitchPlays) framework
- Original Twitch Plays template by Wituz, expanded by DougDoug and DDarknut
- YouTube integration with help from Ottomated
