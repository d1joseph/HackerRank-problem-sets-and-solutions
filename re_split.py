import re

# re.split() using a regex pattern for commas and fullstops as the separator.
# hackerank problem - https://www.hackerrank.com/challenges/re-split/problem
# output each of the separated values on a new line.
# 100,000,000.000
# > 100
# > 000
# > 000
# > 000

string_var = '100,000,000.000'
regex_pattern = r"[,.]"
split_string = "\n".join(re.split(regex_pattern, string_var))

print(split_string)

