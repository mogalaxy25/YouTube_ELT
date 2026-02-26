import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_HANDLE = os.getenv("YOUTUBE_CHANNEL_ID")


def get_playlist_id(api_key, channel_handle):
    """
    Fetch the uploads playlist ID for a YouTube channel.
    """

    try:
        # Validate inputs
        if not api_key:
            raise ValueError("YOUTUBE_API_KEY is not set.")

        if not channel_handle:
            raise ValueError("YOUTUBE_CHANNEL_ID is not set.")

        # Build URL
        url = (
            "https://www.googleapis.com/youtube/v3/channels"
            f"?part=contentDetails&forHandle={channel_handle}&key={api_key}"
        )

        # Make API request
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        # print(json.dumps(data, indent=4))

        # Extract uploads playlist ID
        channel_items = data["items"][0]
        channel_playlistId = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

        return channel_playlistId

    except requests.exceptions.RequestException as e:
        print("API request failed.")
        print(f"Error: {e}")
        raise

    except (KeyError, IndexError) as e:
        print("Unexpected response structure.")
        print(f"Error: {e}")
        raise

    except Exception as e:
        print("Something unexpected happened.")
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    playlist_id = get_playlist_id(API_KEY, CHANNEL_HANDLE)

    print(playlist_id)
