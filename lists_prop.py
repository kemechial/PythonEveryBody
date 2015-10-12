a=[1,4,6,2]
b=a*2
print b
print a
b=[7,3,9,1]
print a+b
a.append("house")
print a
new_stuff=list()
new_stuff.append(b)
new_stuff.append(5)
print new_stuff
print 9 in a
print 9 in b
new_stuff.sort()
print new_stuff
b.sort()
print b
print dir(a)
for i in range(len(a)):
    print i,a[i]
