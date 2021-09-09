# find the pythagorean triplet for 1000. There exists only one set for this integer.
# a tripet can be defined as a^2 + b^2 = c^2

def find_triplet(num):
    # a loop
    for a in range(1, num):
        # b loop
        for b in range(1, num - a):
            # c remainder ab
            c = num - a - b
            
            # check triplet validity
            if a**2 + b**2 == c**2:
                return a*b*c
            else:
                pass # continue looking

print(find_triplet(1000))
