import numpy as np
def prime_sieve(n):
    numbers  = np.linspace(0,n,n+1).astype(int)
    primes = []
    # done = False
    # while done==False:
    for i in numbers:
        if i>1 and i not in primes:
            primes.append(i)
            for j in numbers:
                if j%i==0:
                    numbers[j]=0
    return primes
