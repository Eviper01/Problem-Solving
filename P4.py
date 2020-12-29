import numpy as np
def pali_check(n):
    n = str(n)
    if n[0]==n[5] and n[1]==n[4] and n[2]==n[3]:
        return True
    else:
        return False
pali = []
for i in range(500,999):
    if i%100==0:
        print(i)
    for j in range(500,999):
        if pali_check(i*j)==True:
            pali.append(i*j)
print(max(pali))
