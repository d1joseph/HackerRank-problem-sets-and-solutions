from itertools import permutations

string_int = input()

def permuta(string_int):
    arr = string_int.split(' ')
    arr_int = int(arr[-1])
    arr_result = permutations(arr, arr_int)
    return arr_result

for i in permuta(string_int):
    print(str(i))