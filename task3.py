import random
from random import randint


def get_unique_list_numbers() -> list[int]:
    len_ = 15
    maximum = 10
    minimum = -10
    list_unique = []
    while len(list_unique) != len_:
        var_ = randint(minimum, maximum)
        if var_ not in list_unique:
            list_unique.append(var_)
    return list_unique


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
