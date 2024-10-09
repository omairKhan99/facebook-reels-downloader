
A Python-based tool to download Facebook Reels in various video and audio formats. This project is designed to scrape Facebook Reels URLs using Selenium and download them using `yt-dlp`. It supports popular video formats such as **MP4, MOV, WebM, MKV**, and audio formats such as **MP3, AAC, WAV**.

## Features

- **Download Facebook Reels**: Extract and download multiple Facebook Reels from a channel URL.
- **Video Formats**: Supports MP4, MOV, WebM, MKV.
- **Audio Formats**: Supports MP3, AAC, WAV.
- **Cross-platform**: Works on Windows, macOS, and Linux.


### Python Libraries Required:
- **Selenium**: Used for interacting with the Facebook web interface.
- **yt-dlp**: Used for downloading the Reels and converting them to the desired format.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/omairKhan99/facebook-reels-downloader.git
   cd facebook-reels-downloader
    ```

2. **Install the required Python libraries:**

   Make sure you are using a Python 3.x environment and install the dependencies:

   ```bash
   selenium
   yt-dlp

3. **Verify selenium and yt-dlp Installation:**
   ```bash
   pip install selenium
   pip install yt-dlp
   ```

## Usage

Once the setup is complete, you can download Facebook Reels by running the Python script.
 ```bash 
python reels_downloader.py <channel_name> <channel_reel_url> <format>
```
- channel_name: Name of the Facebook channel (used for saving downloaded files)
- channel_reel_url: The URL of the channel's Reels page
- format: The desired format for the download. Supported formats include mp4, mov, webm, mkv for videos and mp3, aac, wav for audio


## Example
To download all Reels from a channel in MP4 format:
 ```bash 
python reels_downloader.py my_channel https://www.facebook.com/reels/1234567890 mp4
```

To download only the audio in MP3 format:
```bash 
python reels_downloader.py my_channel https://www.facebook.com/reels/1234567890 mp3
```


## Output

- The script will download all the Facebook Reels from the provided URL.
- Downloaded files will be saved in the output/<channel_name> directory.
- The filenames will be in the format: <reel_id>.<ext>, where <ext> depends on the format chosen (e.g., mp4, mp3).


