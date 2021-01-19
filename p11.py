import numpy as np


def list_product(list):
    p = 1
    for elm in list:
        p = p*int(elm)
    return p


file1 = open('p11.txt', 'r')
Lines = file1.readlines()
data = []
for line in Lines:
    line = line.split()
    data.append(line)


data = np.array(data)
max = 0
coord = [0,0]
type = "none"
for i in range(len(data)):
    for j in range(len(data[i])):
        #horizontal product
        try:
            if list_product(data[i,j:j+4])>max:
                max = list_product(data[i,j:j+4])
                coord = [i,j]
                type = "horizontal"
                thing = data[i,j:j+4]
        except Exception as e:
            print(e)
        #vertical product
        try:
            if list_product(data[i:i+4,j])>max:
                max>list_product(data[i:i+4,j])
                coord = [i,j]
                type = "vertical"
        except Exception as e:
            print(e)
        #diagonal product
        diag_list = []
        for k in range(4):
            try:
                diag_list.append(data[i+k,j+k])
            except:
                pass
        if list_product(diag_list)>max:
            max = list_product(diag_list)
            coord = [i,j]
            type = "diag"
            thing = diag_list
        #other diagonal product
        diag_list = []
        for k in range(4):
            try:
                diag_list.append(data[i-k,j+k])
            except:
                pass
        if list_product(diag_list)>max:
            max = list_product(diag_list)
            coord = [i,j]
            type = "diag2"
            thing = diag_list
print(max,coord,type)
print(thing)
