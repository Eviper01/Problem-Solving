file1 = open('p13.txt', 'r')
Lines = file1.readlines()
Data = []
digits = []
carry = 0
for line in Lines:
    Data.append(line.rstrip())




sum = 0
for i in Data:
    sum += int(i)
print(sum)
print("done")


#edit I am an actual retard
