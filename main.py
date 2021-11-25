from http.client import HTTPSConnection
from sys import stderr
from json import dumps
from time import sleep
import config

header_data = {
    "content-type": "application/json",
    "authorization": config.auth_token,
    "host": "discordapp.com",
    "referer": config.channel_URL
}


def get_connection():
    return HTTPSConnection("discordapp.com", 443)


def send_message(conn, channel_id, message_data):
    try:
        conn.request(
            "POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data)
    except:
        stderr.write("Failed to send_message\n")


def msg(variable):
    message_data = {
        "content": variable,
        "tts": "false",
    }
    send_message(get_connection(), config.channel_ID,
                 dumps(message_data))

if __name__ == '__main__':
    try:
        msg_list = []
        time_list = []
        count = 0
        num = int(input("Number Many Messages To Send : "))
        for i in range(0,num):
            message = input("Enter Message "+str(i+1)+" : ")
            time = int(input("Time (In Seconds) To Wait After Message "+str(i+1)+" : "))
            msg_list.append(message)
            time_list.append(time)
        loop = int(input("Number Of Times To Send Message (0 for infinite) : "))
        if (loop==0):
            while True:
                count = count+1
                print("Loop Number "+str(count))
                for j in range(0,num):
                    print("Sending Message "+str(j+1))
                    msg(msg_list[j])
                    sleep(time_list[j])
        elif(loop>0):
            k = 1
            while k<=loop:
                count = count+1
                print("Loop Number "+str(count))
                for j in range(0,num):
                    print("Sending Message "+str(j+1))
                    msg(msg_list[j])
                    sleep(time_list[j])
                k=k+1
    except ValueError:
        print("Enter a Valid Integer!!")
        
    