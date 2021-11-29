a = [(1,7),(3,4),(4,8),(1,4),(3,1)]
a.sort(key = lambda x:x[1])
a.sort(key = lambda x:x[0])
print(a)