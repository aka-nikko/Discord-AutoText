from sys import stderr
import config

header_data = {
    "content-type": "application/json",
    "authorization": config.auth_token,
    "host": "discordapp.com",
    "referer": config.channel_URL
}

def send_message(conn, channel_id, message_data):
    try:
        conn.request(
            "POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data)
    except:
        stderr.write("Failed to send_message\n")
