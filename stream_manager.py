# stream_manager.py

import subprocess
import requests
import time
from config import TWITCH_URL, RTMP_DESTINATIONS, FALLBACK_VIDEO

def is_twitch_live():
    try:
        response = requests.get(f"{TWITCH_URL}/embed", timeout=5)
        return "isLiveBroadcast" in response.text
    except:
        return False

def start_stream(source):
    for url in RTMP_DESTINATIONS:
        cmd = [
            "ffmpeg",
            "-re",
            "-i", source,
            "-c:v", "copy",
            "-c:a", "aac",
            "-f", "flv",
            url
        ]
        subprocess.Popen(cmd)

def monitor_and_stream():
    while True:
        if is_twitch_live():
            print("🔴 Twitch is live. Streaming...")
            start_stream(TWITCH_URL)
        else:
            print("⚠️ Twitch offline. Streaming fallback...")
            start_stream(FALLBACK_VIDEO)
        time.sleep(60)  # Check every minute
