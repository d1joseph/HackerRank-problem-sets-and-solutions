# Enter your code here. Read input from STDIN. Print output to STDOUT
num_cases = input()

for x in range(int(num_cases)):
    a, b = input().split(' ')

    def except_this(a, b):
        try:
            # perform division
            print(int(a)//int(b))
            # if it's a zero division error print the zde exception
        except ZeroDivisionError as e:
            print('Error Code: ' + str(e))
        except ValueError as ve:
            print('Error Code: ' + str(ve))

    except_this(a, b)