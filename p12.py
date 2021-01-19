import math
def triangle(n):
    return int(n*(n+1)/2)


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


def prime_characteristic(number):
    primes = atkin(number)
    combos = []
    for p in primes:
        n = number
        char = 0
        while n%p==0:
            char +=1
            n = int(n/p)
        if char !=0:
            combos.append(char)
    return combos

def m_list_product(list):
    p = 1
    for elm in list:
        p = p*(int(elm)+1)
    return p



def triangle_reduced(n):
    number = triangle(n)
    p = n
    combos = []
    char = 0
    while number%p==0:
        char +=1
        number = int(number/p)
    if char !=0:
        factors = prime_characteristic(p)
        for i in factors:
            combos.append(i*char)
    p = n+1
    char = 0
    while number%p==0:
        char +=1
        number = int(number/p)
    if char !=0:
        factors = prime_characteristic(p)
        for i in factors:
            combos.append(i*char)
    return [number,combos]



f=5
while True:
    t_n = triangle_reduced(f)
    factors = m_list_product(prime_characteristic(t_n[0]) + t_n[1])
    print(triangle(f),factors)
    if factors>500:
        print(t_n,"done")
        exit()
    f+=1
