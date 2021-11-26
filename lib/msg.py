from json import dumps
from connection import get_connection
from send_msg import send_message
from config import channel_ID

def msg(variable):
    message_data = {
        "content": variable,
        "tts": "false",
    }
    send_message(get_connection(), channel_ID,
                 dumps(message_data))