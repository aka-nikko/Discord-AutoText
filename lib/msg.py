from json import dumps
from lib.connection import get_connection
from lib.send_msg import send_message
from lib.config import channel_ID

def msg(variable):
    message_data = {
        "content": variable,
        "tts": "false",
    }
    send_message(get_connection(), channel_ID,
                 dumps(message_data))