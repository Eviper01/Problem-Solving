def next_term(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

def seq_n(n):
    length = 2
    term = n
    while next_term(term)!=1:
            length +=1
            term = next_term(term)
    return length

top = 0
start = 1
for i in range(1,1000000):
    if i%1000==0:
        print(i)
    l = seq_n(i)
    if l>top:
        top = l
        start = i
print(top,start)
