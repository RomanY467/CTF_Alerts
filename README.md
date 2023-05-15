Project Name: CTFd_Alerts(SCC edition)

This is a Python script that interacts with the CTFd API using the requests 
library from Python. The script checks for specific changes on the CTF 
status, such as leaderboard updates or new challenge solves. Additionally, 
it can play videos on the host computer when requested.

Installation

Clone the repository: git clone 
https://github.com/RomanY467/CTF_Alerts.git
Install the required dependencies: pip install requests moviepy
Usage

Change the video file path on play_video.py.
Run the script: python3 challenge.py <url> <admin_token> <challenge_id>
The script will play the video in fullscreen mode on the host computer. Note 
that the full screen feature does not stretch the video, so if your video 
has a different aspect ratio than your screen, there may be black bars on 
the sides.

Contributing

If you would like to contribute to this project, feel free to submit a pull 
request or open an issue. Any feedback or suggestions are also welcome.

License

This project is licensed under the MIT License - see the LICENSE file for 
details.

Acknowledgments

Thanks to the creators of the CTFd API for providing a useful tool for 
monitoring CTF status.
Thanks to the creators of the moviepy library for providing an easy-to-use 
solution for playing videos in Python.
