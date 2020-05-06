#Task

'''
Read in two integers, a and b, and print three lines.
The first line is the integer division a // b.
The second line is the result of the modulo operator: a%b.
The third line prints the divmod of a and b. 

'''

#The first line contains the first integer, a, and the second line containts the second integer, b.

#Output format
#print the result described above

#Example;

'''
Input = 177,10

Sample output:

17
7
(17,7)

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b= int(input())

def mod_divmod(a,b):
    division = a // b
    modu = a%b
    dmod = divmod(a,b)
    answer_list = [division,modu,dmod]
    for i in range(len(answer_list)):
        print(answer_list[i])

mod_divmod(a,b)
