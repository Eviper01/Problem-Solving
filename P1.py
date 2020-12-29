end = 1000
total = 0
for i in range(end):
    if i%3==0:
        total +=i
    elif i%5==0:
        total +=i
print(total)
