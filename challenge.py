import requests
import sys
import time
import json
import test

def main():
    try:
        url = sys.argv[1]
        token = sys.argv[2]
        challenge_id = sys.argv[3]
    except IndexError:
        print("Usage: python3 watch_challenge.py <url> <admin_token> <challenge_id>")
        sys.exit(1)

    # Create API Session
    url = url.strip("/")
    s = requests.Session()
    s.headers.update({"Authorization": f"Token {token}"})

    # Watch Challenge
    while True:
        r = s.get(
            f"{url}/api/v1/challenges/{challenge_id}/solves",
            headers={"Content-Type": "application/json"},
        )
        response = json.loads(r.content)
        if response['data'] != []:
            test.play_video_in_fullscreen()
            sys.exit()
        time.sleep(3)

if __name__ == "__main__":
    main()
