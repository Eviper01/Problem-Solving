def n_sum(n):
    return (n+1)*n/2



def s_sum(n):
    total = 0
    for i in range(n+1):
        total +=i**2
    return total

print(s_sum(100)-n_sum(100)**2)
