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

# получает людей через подслушано
people_response = test.get_local_people()

# очишает его
people = parse.parse_response_people_id(people_response)

# парсит его
my_groups = parse.parse_group(my_group_response)

print(">>>>---<<<<<")
print(my_groups)
lal = []
for white in range(len(my_groups)):
    lal.extend(test.isMembers(my_groups[white],people))
    # compare.search_inst()
    #
    # test.isMembers()




# for group in range(len(my_groups)):
#     check_group = my_groups[group]
#     isMember.extend(test.isMember(check_group,people))
#
print(Counter(lal))
#
# from collections import Counter
#
# print()