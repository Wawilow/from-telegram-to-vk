import vk_api
from datetime import datetime
from time_convert import data_time_convert


def all_postponed_post(VK, groupId):
    params = {"owner_id": f'-{groupId}', "count": f'100', "filter": f'postponed'}
    time_post = VK.wall.get(**params)
    # ic(time_post)
    return time_post['items']


def text_posts(VK, groupId, how_many=10):
    params = {"owner_id": f'-{groupId}', "count": f'{how_many}'}
    posts = VK.wall.get(**params)
    return posts


def last_post(VK, groupId):
    params = {"owner_id": f'-{groupId}', "count": f'100'}
    time_post = int(f"{VK.wall.get(**params)['items'][-1]['date']}")
    time_post = datetime.utcfromtimestamp(time_post).strftime('%Y-%m-%d %H:%M:%S')
    time_post = [*time_post.split(' ')[0].split('-'), *time_post.split(' ')[1].split(':')]
    time_post = data_time_convert(time_post, delta_hours=3)
    return time_post


def last_postponed_post(VK, groupId):
    params = {"owner_id": f'-{groupId}', "count": f'100', "filter": f'postponed'}
    try:
        time_post = int(f"{VK.wall.get(**params)['items'][-1]['date']}")
        time_post = datetime.utcfromtimestamp(time_post).strftime('%Y-%m-%d %H:%M:%S')
        time_post = [*time_post.split(' ')[0].split('-'), *time_post.split(' ')[1].split(':')]
        time_post = data_time_convert(time_post, delta_hours=3)
    except:
        return [False, 'no postponed post']
    return time_post


def next_post_time(VK, groupId):
    return [*str(last_postponed_post(VK, groupId)).split(' ')[0].split('-'),
     *str(last_postponed_post(VK, groupId)).split(' ')[1].split(':')]


if __name__ == '__main__':
    main_token = 'ad135a8d6e65aa945e86f32aa44e9fd8f5ce4977a18a8b85a12ac9b3079c991c46699611ff17e7679bff6'  # личный токен моего аккаунта,
    # можешь сделать свой, для этого перейди по ссылке
    # https://oauth.vk.com/authorize?client_id=7594388&scope=wall,offline&redirect_uri=http://api.vk.com/blank.html&response_type=token
    vk_api = vk_api.VkApi(token=main_token)
    VK = vk_api.get_api()
    groupId = '204952505'  # id тестового паблика
    # groupId = '204952505'  #id основного паблика

    # print(last_post(VK, groupId))
    print(text_posts(VK, groupId))