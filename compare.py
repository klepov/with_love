class compare():

    def compare_groups(group_him,my_group):
        pass

    def search_inst(response):

        members = []
        for positive in range(len(response)):
            if response[positive]['member'] == 1:
                    members.append(response[positive]['user_id'])
            else:
                pass

        return members