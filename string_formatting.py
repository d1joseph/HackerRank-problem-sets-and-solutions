"""
Given an integer, n, print the following values for each integer i from 1 to n:

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

The four values must be printed on a single line in the order specified above for each i from 1 to n. Each value should be space-padded to
match the width of the binary value of n.

"""

#make a conversion table which converts int to either decimal, octal, hexadecimal (capitalized), binary
#take in a parameter N as the range of ints to convert
#create an output function that prints on a single line, the conversion of for each type and then to a new line the next value in the int range

#conversion function to binary, octal, hex
#1 explore this...can we make this more succinct? Think D.R.Y.
def convert_all(n):
    for x in range(1,n):
        print(int(x))
        print (oct(x).replace("0o", ""))
        print (hex(x).upper().replace("0X", ""))
        print (bin(x).replace("0b", ""))

#2 space padding the output
test_num = str(1)
test_num_space = test_num.rjust(4)
print('This is non-padded: ' + str(test_num))
print('This is padded by width = binary: ' + str(test_num_space))


#3 output each result of range n exclusively to that line.
