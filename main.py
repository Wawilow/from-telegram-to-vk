from all_telegram_post import all_post_telegram
from icecream import ic
from vk_api import VkApi
from last_vk_post import text_posts, last_postponed_post
from difflib import SequenceMatcher
from new_post import new_texts_post, time_to_post
from time_convert import unixtime_convert


ic.configureOutput(includeContext=True)



def same_text_or_not(text_one, text_two, similarity_kaf=0.8):
    similarity = SequenceMatcher(None, text_one, text_two).ratio()
    if similarity >= similarity_kaf:
        return True
    else:
        return False


def have_this_post_in_vk(VK, groupId, telegram_text, vk_texts, how_many=100):
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


def cross_posting_to_vk(main_token, groupId):
    vk_api = VkApi(token=main_token)
    VK = vk_api.get_api()
    vk_texts = []
    for tg in all_post_telegram(limit=10)[::-1]:
        tg_text = tg['message']
        if not have_this_post_in_vk(VK, groupId, tg_text, vk_texts):
            ic(new_texts_post(VK, groupId, tg_text,
                              data=unixtime_convert(time_to_post(VK, groupId,
                                                                 last_time=(last_postponed_post(VK, groupId))))))


if __name__ == '__main__':
    # отличный сайт для получения токена, вроде даже норм https://vkhost.github.io/
    main_token = '7590a1ae275d8b38b843371b2d9c4b64b196df60e43284e50e246f984c22b0f2c3cfe21a159f450d286a2'
    groupId = '204952505'
    cross_posting_to_vk(main_token=main_token,
                        groupId=groupId)
