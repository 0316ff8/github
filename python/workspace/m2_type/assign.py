x = 10
y = x
z = x + 10
print(x, y, z)
print(id(x), id(y), id(z))

a, b, c = 10, 20, 30
print(a, b, c)
print(id(a) ,id(b), id(c))

a = b = c =10
print(id(a), id(b), id(c))

import keyword
print(keyword.kwlist)
