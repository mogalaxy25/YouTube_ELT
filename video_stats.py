import requests

API_KEY ="AIzaSyAMU6_zROQgGslPbR76oQx5Lo_qNZ7r6Q4"
CHANNEL_HANDLE = "MrBeast"
url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"
response = requests.get(url)
print(response)

