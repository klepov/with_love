import requests
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

    def get_local_people(self, city, age_from, age_to, sex, relation):
        offset_result = 0
        response_offset = []
        """
        отдает людей по критерию
        :param city: айди города
        :param age_from: возраст начало
        :param age_to: возраст конец
        :param sex: пол 1 - Ж/ 2 - М
        :param relation: 1 — не женат/не замужем; 2 — есть друг/есть подруга; 3 — помолвлен/помолвлена; 4 — женат/замужем: 5 — всё сложно; 6 — в активном поиске; 7 — влюблён/влюблена; 0 — не указано.
        :return: все найденые страницы
        """

        response = self.tools.get_all('users.search',10000,
                                      {'city':city,
                                       'age_from':age_from,
                                       'age_to': age_to,
                                       'sex': sex,
                                       'status' : relation})

        print("ss")
        # response = self.vk.users.search(city = city,
        #                                 age_from= age_from,
        #                                 age_to= age_to,
        #                                 sex= sex,
        #                                 status = relation,
        #                                 count = 1000)


        # count = response['count']
        # if response['count'] > 1000:
        #     q = count // 1000
        #     response = self.vk.users.search(city = city,
        #                                 age_from= age_from,
        #                                 age_to= age_to,
        #                                 sex= sex,
        #                                 status = relation,
        #                                 count = 1000,
        #                                 offset = q)

        return response

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
