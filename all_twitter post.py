#по требует доступ к акку телеги что не круто
#import asyncio
#05bb4b22b3f9099fb80a672d3402bba7
#6750236


import telethon
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest

api_id = '6750236'
api_hash = '05bb4b22b3f9099fb80a672d3402bba7'
chanel_id = '-1001349895158'
user_input_channel = 'https://t.me/neural_pushkin'


def client_connect():
    global client, api_id, api_hash
    client = TelegramClient("name", api_id, api_hash)
    assert client.connect()
    if not client.is_user_authorized():
        print('You not authorized')
        phone_number = str(input("Enter you number: "))
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input('Enter code: '))
        print(me)
    return client


def main():
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()
    messages = client.get_messages(chanel_id, limit=10)
    print(messages)
    print(type(messages))


if __name__ == '__main__':
    main()
