def digit_sum(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum

print(digit_sum(2**1000))
