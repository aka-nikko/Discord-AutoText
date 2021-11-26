from http.client import HTTPSConnection

def get_connection():
    return HTTPSConnection("discordapp.com", 443)
