from all_telegram_post import all_post_telegram
from icecream import ic
import vk_api
from last_vk_post import text_posts
from difflib import SequenceMatcher


ic.configureOutput(includeContext=True)



def same_text_or_not(text_one, text_two, similarity_kaf=0.8):
    similarity = SequenceMatcher(None, text_one, text_two).ratio()
    if similarity >= similarity_kaf:
        return True
    else:
        return False


def have_this_post_in_vk(VK, groupId, telegram_text, how_many=100):
    global vk_texts
    if vk_texts == []:
        # pass
        vk_texts = text_posts(VK, groupId, how_many=how_many)
    text = [[i['id'], i['text']] for i in vk_texts['items']]
    for i in text:
        try:
            same_text = same_text_or_not(''.join((i[1])), ''.join(telegram_text))
        except:
            print('i', i, type(i))
            print('teleg', telegram_text, type(telegram_text))
            same_text = False
        if same_text:
            return True
    return False


if __name__ == '__main__':
    token = 'cb0400ae1b14d0875b4803640297401794c9d0984e0585a5521672c3f9aa60e88c856f5ce2248b640ef60'
    main_token = 'ad135a8d6e65aa945e86f32aa44e9fd8f5ce4977a18a8b85a12ac9b3079c991c46699611ff17e7679bff6'
    vk_api = vk_api.VkApi(token=main_token)
    VK = vk_api.get_api()
    groupId = '204952505'
    vk_texts = []
    for tg in all_post_telegram(limit=100):
        tg_text = tg['message']
        if have_this_post_in_vk(VK, groupId, tg_text):
            print(True)