if __name__ == '__main__':
    print("1. Enter new configurations.\n2. Load configurations.")
    option = int(input("Enter Option : "))
    if(option == 1):
        auth = input("Enter auth-token  : ")
        url = input("Enter channel url : ")
        id = input("Enter channel ID  : ")
        f = open("config.py", "w")
        f.write("auth_token = \""+auth+"\"\n")
        f.write("channel_URL = \""+url+"\"\n")
        f.write("channel_ID = \""+id+"\"\n")
        f.close()
    elif(option == 2):
        b = 1
    from lib.program import program
    program()
