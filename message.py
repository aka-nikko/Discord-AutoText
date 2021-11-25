from json import dumps
import send_msg
import connection
import config

def msg(variable):
    message_data = {
        "content": variable,
        "tts": "false",
    }
    send_msg.send_message(connection.get_connection(), config.channel_ID,
                 dumps(message_data))
