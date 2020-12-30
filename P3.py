import numpy as np
def prime_sieve(n):
    primes = []
    numbers  = np.linspace(0,n,n+1).astype(int)
    for i in numbers:
        if i>1 and i not in primes:
            primes.append(i)
            for j in numbers:
                if j%i==0:
                    numbers[j]=0
    return primes
n = 600851475143
factors = []
for i in prime_sieve(3000):
    if n%i==0:
        factors.append(i)
print(factors)

for i in factors:
    n = int(n/i)
print(n)

#notes:
#this method kinda hopes that all of the factors except the largest one are smaller than what you can reasonably sieve up to
#there should be a much better way to do this
