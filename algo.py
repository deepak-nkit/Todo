from typing import *


# def two_sum(values: List[int]):
#     for i in range(len(values)):
#         for j in range(i+1, len(values)):
#             print("Hello")
#             ...
#             # if values[i] + values[j] == target:
#             #     return [i, j]


def two_sum(values: List[int], target):
    
    value_dict = {} # [1, 3, 7]   => {1: 0, 3: 1, 7: 2}
    for i, value in enumerate(values):
        value_dict[value] = i

    for i in range(len(values)):
        curr_value = values[i]
        find_value = target - curr_value
        if find_value in value_dict:
            return [i, value_dict[find_value]]
            # if values[i] + values[j] == target:
            #     return [i, j]


# 999, 998
length = 1600000
print(two_sum(list(range(length)), length-1 + length -2))

# 9 + 8 + 7 + .. + 1 => 45 (math)

# 19 + 18 + .... 1 => 190 


# n
# (n-1) + (n-2) + ... + 1

# 1 + 2 + 3 + 4 + ... + n
# 