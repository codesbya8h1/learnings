import random
import json

def shuffle_string(input_str):
    input_str_list  = list(input_str)

    for i in range(len(input_str_list)):
        random_index = int(random.random() * len(input_str_list) -1)
        input_str_list[i], input_str_list[random_index] = input_str_list[random_index], input_str_list[i]
    
    return ''.join(input_str_list) if len(input_str_list) == len(input_str) else 'shuffle failed!'


# print(shuffle_string("abcd"))


def analyze_shuffle():
    result = {}
    input_str = 'blah'

    for i in range(10000):
        shuffled_st = shuffle_string(input_str)
        for j, char in enumerate(shuffled_st):
            if char not in result:
                result[char] = {}

            if j not in result[char]:
                result[char][j] = 0
            
            result[char][j] += 1
    
    print(json.dumps(result, indent=4))

analyze_shuffle()