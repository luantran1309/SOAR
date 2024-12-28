#!/usr/bin/python3

import requests
import json
import sys  

telegram_bot_token = "API Token of bot Telegram"
telegram_chat_id = "Chat ID Telegram"

# Send message to Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    params = {
        "chat_id": telegram_chat_id,
        "text": message
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print("Message sent successfully to Telegram!")
        else:
            print(f"Failed to send message: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 " + sys.argv[0] + " <message>")
        sys.exit(1)
    
    # Take message
    message = sys.argv[1]
    send_telegram_message(message)