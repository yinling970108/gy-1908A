s = 0
for i in range (1,101):
    s += i
print(s)



s = 1
for i in range (1,101):
    s *= i
print(s)




for i in range (2,100):
    f = False
    for j in range (2,i):
        if (i % j == 0):
            f = True
        break
    if (not f):
         print(i)




for i in range (1,10):
    for j in range (1,i+1):
        print('%s * %s = %s'%(i,j,i+j),end = ('  ') )
    print('')


alist = [3,5,6,9,8,7,4,1,2,13,78,42,12,25,36,45,58,59]
for i in range (len(alist)-1):
    for j in range (len(alist)-i-1):
        if alist[j] > alist[j+1]:
            temp = alist[j]
            alist[j] = alist[j+1]
            alist[j+1] = temp
print(alist)
