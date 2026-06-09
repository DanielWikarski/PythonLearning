
import random

range_a = int(input("Start range: "))
range_b = int(input("End range: "))
max_list_len = int(input("Max list length: "))



def ran_uniq_nums(range_a: int, range_b: int, max_list_len: int) -> list[int]:
    ran_uniq_nums_list = list()

    if max_list_len >= (range_b - range_a)+1:
        raise ValueError(f"Max list length [{max_list_len}] is out of range")
    while max_list_len > len(ran_uniq_nums_list):
        num = random.randint(range_a, range_b)
        if num not in ran_uniq_nums_list:
                ran_uniq_nums_list.append(num)

    return ran_uniq_nums_list


