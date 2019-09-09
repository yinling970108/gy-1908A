j = [1,2,3,4,5,6,7,8,9,10,11]
j.append(22)
print(j)
j.insert(4,33)
print(j)
k = [44,45,46,47,48,49,50]
j.extend(k)
print(j)
print(k)


print(j.pop())
print(j)
print(j.pop(12))
print(j)
print(j.pop(-5))
print(j)


print(j.remove(44))
print(j)
print(j.remove(48))
print(j)