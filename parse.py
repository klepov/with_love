class parse():
    def parse_response_people_id(response):
        # todo сделать передачу параметров
        peoples = []
        peoples_result = []

        for i in range(len(response)):
            peoples.extend(response[i])

        for people in range(len(peoples)):

            try:
                if peoples[people]['city']['title'] == 'Красногорск'\
                    and peoples[people]['sex']== 1\
                        and peoples[people]['relation']== 6:

                    peoples_result.append(peoples[people]['id'])

            except KeyError:
                pass

        return peoples_result


    def parse_group(response):

        return response['groups']['items']

