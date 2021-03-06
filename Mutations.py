"""
Task
Read a given string, change the character at a given index and then print the modified string.

Input Format
The first line contains a string,S.

The next line contains an integer i, denoting the index location and a character, c, separated by a space.

Output Format
Using any of the methods explained above, replace the character at index
with character.

Sample Input

abracadabra
5 k

Sample Output

abrackdabra

"""

def mutate_string(string, position, character):
    mutableString = list(string)
    mutableString[position] = character
    string = ''.join(mutableString)
    return string
