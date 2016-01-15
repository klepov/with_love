import requests
import vk_api



def main():
    """ Пример получения последнего сообщения со стены """

    login, password = 'dima1da@yandex.ru', 'rekord777888'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.authorization()
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()
    tools = vk_api.VkTools(vk_session)


    # for i in range(31):
    response = tools.get_all('groups.getMembers',1,{'group_id':'glitchheart','fields':'city,sex'})

    print(response)

main()

