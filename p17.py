file1 = open('p17.txt', 'r')
Lines = file1.readlines()
sum = 0
for Line in Lines:
    sum += len(Line)-1

sum += 891*3 #add on missing ands
print(sum)
