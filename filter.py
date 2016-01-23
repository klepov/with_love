import vk_api

from main import Model
from parse import parse
from compare import compare

test = Model(login='*', passw='*')
parser = parse()
compare = compare()

my_group_response = test.get_subscribe(11853247)

peolpe_response = test.get_local_people(483, 17, 19, 1, 6)

people = parse.parse_respone_people_id(peolpe_response)
my_group = parse.parse_group(my_group_response)

for i in range(len(people)):
    temp_people = people[i]
    group_him = parse.parse_group(test.get_subscribe(temp_people))
    compare.compare_groups(group_him, my_group)
