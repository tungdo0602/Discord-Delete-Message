import requests
import time
import colorama
from colorama import Fore

token = input("Token: ")
channelId = input("Channel Id: ")
userId = input("User Id: ")

headers = {"authorization": token}

sm = requests.get(f"https://discord.com/api/v9/channels/{channelId}/messages/search?author_id={userId}", headers=headers)

try:
    mlist = sm.json().get("messages")
    for item in mlist:
        messageId = item[0].get('id')
        mcontent = item[0].get('content')
        dm = requests.delete(f'https://discord.com/api/v9/channels/{channelId}/messages/{messageId}', headers=headers)
        if dm.status_code == 204:
            print(Fore.GREEN + f"Message Deleted: {mcontent}")
        else:
            print(Fore.RED + f"Error when delete message: {dm.status_code}")
        time.sleep(1)
    print(Fore.BLUE + "Done!")
except:
    print("Failed to get messages!")