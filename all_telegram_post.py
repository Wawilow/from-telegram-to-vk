#по требует доступ к акку телеги что не круто
#import asyncio
#05bb4b22b3f9099fb80a672d3402bba7
#6750236


from telethon import TelegramClient, events, sync

from icecream import ic


api_id = '6750236'
api_hash = '05bb4b22b3f9099fb80a672d3402bba7'
chanel_id = '-1001349895158'
user_channel = 'https://t.me/neural_pushkin'


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


def all_post_telegram(limit=1):
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()
    messages = client.get_messages(user_channel, limit=limit)
    message = []
    for i in messages:
        app_end = {'id': i.id, 'datatime': i.date, 'message': i.message}
        message.append(app_end)
    return message

def main():
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()
    messages = client.get_messages(user_channel, limit=100)
    for message in messages:
        print(message)
        print()
        print(message.message)
        print()


if __name__ == '__main__':
    main()
    # print(all_post_telegram(limit=10))
