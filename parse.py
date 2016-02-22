class parse():
    def drop_dubl(self,L):
        result = list()
        for item in L:
            if item not in result:
                result.append(item)
        return result

    def parse_response_people_id(response):
        # todo сделать передачу параметров
        peoples = []
        peoples_result = []

        for i in range(len(response)):
            peoples.extend(response[i])

        # peoples = self.drop_dubl(peoples)

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

