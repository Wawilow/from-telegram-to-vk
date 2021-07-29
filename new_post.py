import vk_api
from time_convert import one_day_plus_time, time_now, for_vk_post_convert
from last_vk_post import last_postponed_post, last_post


def new_texts_post(VK, groupId, textPost, data=for_vk_post_convert()):
    attachments = []
    params = {"owner_id": f'-{groupId}', "message": textPost, "attachments": attachments, 'publish_date': data}
    VK.wall.post(**params)


def new_image_post(img, text=''):
    attachments = []
    params = {"owner_id": f'-{groupId}', "message": textPost, "publish_date": for_vk_post_convert()
        , "attachments": attachments}
    VK.wall.post(**params)


def time_to_post(VK, groupId, last_time=False, small=False, fall=False):
    if type(last_time) == type([]):
        if not last_time[0]:
            if last_time[1] == 'no postponed post':
                last_time = last_post(VK, groupId)
                # print(f'time last post = {last_time}\ntime now = {time_now()}')
                if str(last_time).split(' ')[0] == str(('-').join(time_now()[0:3])):
                    return one_day_plus_time(time_now())
                else:
                    return one_day_plus_time(last_time, delta=1)
            else:
                last_time = time_now()
    return one_day_plus_time(last_time)


if __name__ == '__main__':
    textPost = 'тест'
    token = 'cb0400ae1b14d0875b4803640297401794c9d0984e0585a5521672c3f9aa60e88c856f5ce2248b640ef60'
    # тестовое сообщество https://vk.com/algoritms_bot
    main_token = 'ad135a8d6e65aa945e86f32aa44e9fd8f5ce4977a18a8b85a12ac9b3079c991c46699611ff17e7679bff6'
    # личный токен моего аккаунта,
    # можешь сделать свой, для этого перейди по ссылке
    # https://oauth.vk.com/authorize?client_id=7594388&scope=wall,offline&redirect_uri=http://api.vk.com/blank.html&response_type=token
    vk_api = vk_api.VkApi(token=main_token)
    VK = vk_api.get_api()
    groupId = '204952505'  # id тестового паблика
    # groupId = '204952505'  #id основного паблика
    print(time_to_post(VK, groupId, last_time=(last_postponed_post(VK, groupId))))