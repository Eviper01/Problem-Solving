




Memory = {"(1,0)":1}
def pathnumber(x,y):
    try:
        return Memory["("+str(x)+","+str(y)+")"]
    except:
        pass
    try:
        return Memory["("+str(y)+","+str(x)+")"]
    except:
        pass
    if x<0 or y<0: #the zero checks should happen first tehcinally
        return 0
    Memory["("+str(x)+","+str(y)+")"] = pathnumber(x-1,y) + pathnumber(x,y-1)
    return Memory["("+str(x)+","+str(y)+")"]

print(pathnumber(20,20))
print(Memory)
