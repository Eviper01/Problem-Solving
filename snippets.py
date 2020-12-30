import numpy as np
def prime_sieve(n):
    numbers  = np.linspace(0,n,n+1).astype(int)
    primes = []
    for i in numbers:
        if i>1 and i not in primes:
            primes.append(i)
            for j in numbers:
                if j%i==0:
                    numbers[j]=0
    return primes


def atkin_sieve(n):
    results_list = [2,3,5]
    sieve_list = list(range(1,n))
    primality = np.zeros(n)
    for n in sieve_list:
        if n%60 in [1,13,17,29,37,41,49,53]:
            if quadratic_curve_solutions(4,1,n)%2==1:
                primality[n-1] = 1
        if n%60 in [7,19,31,43]:
            if quadratic_curve_solutions(3,1,n)%2==1:
                primality[n-1] = 1
        if n%60 in [11,23,47,59]:
            if hyperbolic_curve_solutions(3,-1,n)%2==1:
                primality[n-1] = 1
    for n in sieve_list:
        if primality[n-1]==1:
            results_list.append(n)
            counter = n**2
            while counter<len(primality):
                primality[counter-1]=0
                counter+=n**2
    return results_list

def quadratic_curve_solutions(a,b,c):
    #ax^2+by^2=c
    solutions = []
    for i in range(1,int(np.ceil(np.sqrt(c)))):
        for j in range(1,int(np.ceil(np.sqrt(c)))):
            solutions.append(a*i**2+b*j**2)
    return solutions.count(c)

def hyperbolic_curve_solutions(a,b,c):
    #ax^2+by^2=c
    solutions = []
    for i in range(1,c):
        for j in range(1,c):
            if i>j:
                solutions.append(a*i**2+b*j**2)
    return solutions.count(c)

#this is insane
import math
def atkin(nmax):
    """
    Returns a list of prime numbers below the number "nmax"
    """
    is_prime = dict([(i, False) for i in range(5, nmax+1)])
    for x in range(1, int(math.sqrt(nmax))+1):
        for y in range(1, int(math.sqrt(nmax))+1):
            n = 4*x**2 + y**2
            if (n <= nmax) and ((n % 12 == 1) or (n % 12 == 5)):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 + y**2
            if (n <= nmax) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 - y**2
            if (x > y) and (n <= nmax) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]
    for n in range(5, int(math.sqrt(nmax))+1):
        if is_prime[n]:
            ik = 1
            while (ik * n**2 <= nmax):
                is_prime[ik * n**2] = False
                ik += 1
    primes = []
    for i in range(nmax + 1):
        if i in [0, 1, 4]: pass
        elif i in [2,3] or is_prime[i]: primes.append(i)
        else: pass
    return primes
atkin(2000000)
print("done")
