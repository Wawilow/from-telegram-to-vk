from all_telegram_post import all_post_telegram
from icecream import ic
import vk_api
from  new_post import time_to_post2
from last_vk_post import text_posts
from difflib import SequenceMatcher


ic.configureOutput(includeContext=True)



def same_text_or_not(text_one, text_two):
    similarity = SequenceMatcher(None, ''.join(i[1]), ''.join(tg_text)).ratio()
    if similarity >= 0.8:
        return True
    else:
        return False


if __name__ == '__main__':
    token = 'cb0400ae1b14d0875b4803640297401794c9d0984e0585a5521672c3f9aa60e88c856f5ce2248b640ef60'
    main_token = 'ad135a8d6e65aa945e86f32aa44e9fd8f5ce4977a18a8b85a12ac9b3079c991c46699611ff17e7679bff6'
    vk_api = vk_api.VkApi(token=main_token)
    VK = vk_api.get_api()
    groupId = '204952505'

    tg = all_post_telegram(limit=100)[0]
    tg_text = tg['message']
    text = text_posts(VK, groupId, how_many=100)
    # ic(text['items'])
    # ic((text['items']))
    texts = [[i['id'], i['text']] for i in text['items']]
    for i in texts:
        diff = SequenceMatcher(None, ''.join(i[1]), ''.join(tg_text))
        print(same_text_or_not(''.join((i[1])), ''.join(tg_text)))
