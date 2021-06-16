import vk_api
from time_convert import for_vk_post_convert

textPost = 'тест'

textPost = input()

#token = '54041327cd1967dc10fcce01620b625c4e6949672e5b754f10f7e7920510aabb58f3babe8febf1df4c34f'#токен основного аккаунта https://vk.com/neural_pushkin
token = 'cb0400ae1b14d0875b4803640297401794c9d0984e0585a5521672c3f9aa60e88c856f5ce2248b640ef60' #тестовое сообщество https://vk.com/algoritms_bot
main_token = 'ad135a8d6e65aa945e86f32aa44e9fd8f5ce4977a18a8b85a12ac9b3079c991c46699611ff17e7679bff6' #личный токен моего аккаунта,
#можешь сделать свой, для этого перейди по ссылке https://oauth.vk.com/authorize?client_id=7594388&scope=wall,offline&redirect_uri=http://api.vk.com/blank.html&response_type=token
vk_api = vk_api.VkApi(token=main_token)
VK = vk_api.get_api()
groupId = '204098688'  #id тестового паблика
#groupId = '204952505'  #id основного паблика

def new_texts_post(data=for_vk_post_convert()):
    attachments = []
    params = {"owner_id": f'-{groupId}', "message": textPost, "attachments": attachments, 'publish_date': data}
    VK.wall.post(**params)


def new_image_post(img, text=''):
    attachments = []
    params = {"owner_id": f'-{groupId}', "message": textPost, "publish_date": for_vk_post_convert()
        , "attachments": attachments}
    VK.wall.post(**params)


new_texts_post()