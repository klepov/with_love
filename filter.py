import time
import vk_api

from main import Model
from parse import parse
from compare import compare
from collections import Counter


list_group_overhear = [80178582]


test = Model(login='dima1da@yandex.ru', passw='rekord777888')





























parser = parse()
compare = compare()

my_group_response = test.get_subscribe(11853247)

people_response = test.get_local_people()

people = parse.parse_response_people_id(people_response)

my_groups = parse.parse_group(my_group_response)

print(">>>>---<<<<<")
print(my_groups)
lal = []
for white in range(len(list_group_overhear)):
    test.isMembers(list_group_overhear[white],people)
    # compare.search_inst()
    #
    # test.isMembers()

print(lal)

isMember = []

# for group in range(len(my_groups)):
#     check_group = my_groups[group]
#     isMember.extend(test.isMember(check_group,people))
#
# print(Counter(isMember))
#
# from collections import Counter
#
# print()