# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    # 69 ms
    def first_solution(self, operations):
        x = 0
        for operation in operations:
            # if addition increment by 1
            if operation == "++X" or operation == "X++":
                x += 1
            # if subtraction decrement by 1
            elif operation == "--X" or operation == "X--":
                x -= 1
        
        print(x)

    # 55 ms
    def second_solution(self, operations):
        
        x = 0
        is_addition = "X++"
        still_addition = "++X"

        for operation in operations:
            # if add += 1
            if operation == is_addition or operation == still_addition:
                x += 1
            else:
                x -= 1

        print(x)


if __name__ == "__main__":
    # list of operations as string expressions
    ops_1 = ["--X", "X++", "++X"] # should return x=1
    ops_2 = ["X++", "X++", "X++", "X++"] # should return x=4
    ops_3 = [] # should return x
    ops_4 = [] # should return x
    ops_5 = [] # should return x
