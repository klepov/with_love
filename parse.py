class parse():
    def parse_respone_people_id(response):
        people = []
        count = response['count']
        print(count)

        for i in range(count):
            print(i)
            people.append(response['items'][i]['id'])

        return people


    def parse_group(response):

        return response['groups']['items']

