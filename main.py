import requests
import time
import vk_api


# def main():
#     """ Пример получения последнего сообщения со стены """
#
#     # поиск людей
#     response = tools.get_all('users.search', 1, {'city': '483',
#                                                  'age_from': '17',
#                                                  'age_to': '19',
#                                                  'sex': '1',
#                                                  'status': '6'})
#
#     # парсинг на айди
#     id = response['items'][0]['id']
#
#     # запрос на паблики


class Model():
    vk_session = None
    vk = None
    tools = None

    def __init__(self, login, passw):

        vk_session = vk_api.VkApi(login, passw)

        try:
            vk_session.authorization()
        except vk_api.AuthorizationError as error_msg:
            print(error_msg)

        self.vk = vk_session.get_api()
        self.tools = vk_api.VkTools(vk_session)

    def get_local_people(self):

        """
        отдает людей
        :return: все найденые страницы
        """

        finder_people = []
        offset = 0
        while True:
            response = self.vk.groups.getMembers(group_id = "62784408",
                                        fields = ('sex,bdate,city,relation'),
                                        offset= offset
                                        )


            count = response['count']

            if count < offset:
                break

            else:
                finder_people.append(response['items'])

                offset += 1000

            # time.sleep(1)


        return finder_people

    def get_subscribe(self, id):
        subscribe = self.vk.users.getSubscriptions(user_id=id, extended=0)
        return subscribe

    def isMembers(self,group_id,user_id):
        response = []
        users_500 = 0
        user_len = len(user_id)
        retry = (user_len//500)+1
        count = 0

        while count != retry:
            users_500 = user_id[count*500:(count+1)*500]
            print("------500-------")
            print(users_500)
            response.extend(self.vk.groups.isMember(group_id=group_id, user_ids=str(users_500)))


            count +=1

        print(len(response))
        return response


# main()
