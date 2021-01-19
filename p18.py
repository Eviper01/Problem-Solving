file1 = open('p18.txt', 'r')
Lines = file1.readlines()

Data = []
for line in Lines:
    Data.append((line.rstrip()).split())


# print(Data)
Memory = {}

print(Data)
def PathMaximise(n,m):
    if n==len(Data)-1:
        return int(Data[n][m])
    try:
        return Memory["("+str(n)+","+str(m)+")"]
    except:
        pass
    Memory["("+str(n)+","+str(m)+")"] = int(Data[n][m]) + max([PathMaximise(n+1,m),PathMaximise(n+1,m+1)])
    return Memory["("+str(n)+","+str(m)+")"]

print(PathMaximise(0,0))
    #return the number if it is bottom row
    #else return self + highest total below
