test = 'STRING'
test1 = '12345'
test2 = 'This is a sentence string with spaces'
test3 = ' This is sentence string has leading and trailing whitespace '
print('Original string: '+ test)
print('coverting to lowercase: ' + test.lower())
print('converting to uppercase: ' + test.upper())
print('converting to capitalise: ' + test.capitalize())
print('slicing substring by index: ' + test[1:3] + ' (letters from index 1,3)')
print('slicing a substring from start until character index 4: ' + test[:4] + ' (letters from index 0 till 4 - not including index 4.)')
print('slicing a substring from character index 4 until start(index 0): ' + test[4:] + ' (letters from index 0 till 4 - not including index 4.)')
print('finding the index position of substring - passing (TR): ' + str(test.find('TR')))
print('find the index position of substring not part of the main string: ' + str(test.find('AS')))
print('finding a specific value in the string for index between a given range: ' + str(test1.find('3',0,5)))
print('substituting strings: ' + test.replace('STRING', 'NEWSTRING'))
print('seperating strings by passing seperators: ' + str(test2.rsplit(" ")))
print('Length of string (test3) with whitespace: ' + str(len(test3)))
print('Length of string after stripping leading and trailing whitespace: ' + str(len(test3.strip())))


"""
In this challenge, the user enters a string and a substring.

You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC

Sample Output

2

"""

string, substring = (input().strip(), input().strip())

def findsubstring(string, substring):
    return sum(([1 for i in range(len(string) - len(substring)+1) if string[i:i+len(substring)] == substring]))

print(findsubstring(string,substring))
