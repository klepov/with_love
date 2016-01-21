import vk_api

from main import Model
from parse import parse

test = Model(login='dima1da@yandex.ru',passw='rekord777888')
parser = parse()

my_group_response = test.get_subscribe(11853247)


response = test.get_local_people(483,17,19,1,6)

people = parse.parse_respone_people_id(response)
my_group = parse.parse_group(my_group_response)

print(my_group)