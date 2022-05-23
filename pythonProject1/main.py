l = [1, 2, 9, 4, 7, 6, 3, 8, 5]
x = list('spam')

l.reverse()
print(l)
l.sort()
print(l)
l[2] = l[2] + 6
print(l)
l.sort()
print(l)
# x=len(l)-1
# l[x] = l[x]+6

print(l[:-3])

print(x)

x.pop(2)
print(x)
x.insert(2,'k')
print(x)

x.insert(2,'k')
print(x)


x.remove('k')
print(x)

x.extend('a')
print(x)