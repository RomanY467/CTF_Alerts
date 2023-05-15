import requests
import time
import video_player

# CTFd API endpoint
ctfd_url = "http://ctf5.saltacybersecurity.club/api/v1"

# Challenge ID to check for completion
challenge_id = 1

# Interval to check for new solves (in seconds)
interval = 5

# URL to video file to play on solve
video_url = "chad.mp4"

# API key for accessing the CTFd API
api_key = "81c4c7b7cb5a54be438206a63fd5831e7d7ee7eeef467f93956503aa3cbc75f5"

# Keep track of the number of solves
solves = 0

while True:
    try:
        # Send a request to the CTFd API to get the list of solves for the challenge
        headers = {"Authorization": f"Token {api_key}"}
        r = requests.get(f"{ctfd_url}/challenges/{challenge_id}/solves", headers=headers)

        # If the request was successful, check if the number of solves has increased
        if r.status_code == 200:
            new_solves = len(r.json()["data"])
            if new_solves > solves:
                # If a new solve has been added, play the video in fullscreen
                video_player.play_video(video_url)
                solves = new_solves

        # Wait for the specified interval before checking again
        time.sleep(interval)

    except requests.exceptions.ConnectionError:
        # If there is a connection error, wait for a short time and then try again
        time.sleep(2)

