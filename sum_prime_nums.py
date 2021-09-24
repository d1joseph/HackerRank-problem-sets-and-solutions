# find the sum of all prime numbers <= 2m.
# prime numbers are numbers evenly divisible by itself and 1.


# O(n log log n) provided the array update operation is O(1) 
def make_primes_sieve(n):
    # list of n bools set to true
    primes = [True for i in range(n + 1)]
    p = 2
    sum_of_primes_n = []

    while (p * p <= n):

        if (primes[p] == True):

            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1

    primes[0] = False
    primes[1] = False

    for p in range(n + 1):
        if primes[p]:
            sum_of_primes_n.append(p)

    print(sum(sum_of_primes_n))


# make_primes_sieve(2000000)
