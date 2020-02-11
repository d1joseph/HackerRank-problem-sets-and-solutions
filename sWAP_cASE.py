"""You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

Input Format

A single line containing a string.

Constraints:

0 < len(s) <_ 1000

Output Format

Print the modified string S.

Sample Input 0

HackerRank.com presents "Pythonist 2".

Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""
#save input to string variable
string = input()

#create function and pass string variable.
def swapCase(string):
    #use list comprehension to iterate and evaluate each letter using a seperator
    #and replace with an upper or lower. Join the string and save to new variable.
    newString = ''.join([i.lower() if i.isupper() else i.upper() for i in string])
    return newString

#string manipulation can be achieve using the ''.join(old_variable) method.

print(swapCase(string))
