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

primes = prime_sieve(20)
numbers = np.linspace(1,20,20).astype(int)
factor_matrix = np.zeros((20,20))
for i in numbers:
    print(i)
    for p in primes:
        index = 0
        going = True
        n = i
        while going:
            if n%p ==0:
                index+=1
                n = n/p
            else:
                going = False
        factor_matrix[i-1,p-1] = index
print(factor_matrix)

solution = 1
for i in primes:
    solution = solution*i**max(factor_matrix[:,i-1])
print(solution)
