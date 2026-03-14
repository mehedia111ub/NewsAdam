import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")


def post_to_discord(message: str) -> bool:
    """
    Sends a message to Discord using a webhook.

    Returns True if successful, otherwise False.
    """

    if not DISCORD_WEBHOOK_URL:
        raise ValueError("DISCORD_WEBHOOK_URL not found in .env file")

    payload = {
        "content": message[:1900]  # Discord message limit protection
    }

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=10)

        if response.status_code in (200, 204):
            return True
        else:
            print("Discord error:", response.text)
            return False

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return False
