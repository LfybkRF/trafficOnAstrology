import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


vk_session = vk_api.VkApi(token = 'vk1.a.0pUWik5ExTWO-NomNTpBl7zRh1VjPPGex9R7BbbeFN5BWWrTeIXImbp1ehUHu6y0tJDn0F6a-tvnRVak2eoFb1dMrlsAKbV_4i4s4GsBCrP_5qvUlTklVFLVyfmslLpJqRiaZqV9Th4Dy85aimCGTt7u0ptAmOqslmoVbAioBCGZsu468tjL_TMjEiiDqWoO7yPN498kjJL226pBSdXB3Q')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def message_send(user,msg):
    vk.messages.send(
                        user_id = user,
                        message = msg,
                        random_id = 0,
                    )


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        try:
            if event.to_me:
                spam_message = 'Чтобы заключить брак со своей второй половинкой, жми на ссылку ниже💍😍\n\n👉https://vk.com/app51581689❤'
                message_send(event.user_id, spam_message)
                print(event.user_id, event.text)
        except:
            message_send(event.user_id, 'Ой! Кажется, вы сделали что-то непонятное для меня.\n Попробуйте сделать запрос по другому')
                
