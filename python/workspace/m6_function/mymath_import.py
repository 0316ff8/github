# import模組
# P101-P102
import m6_function.mymath
print(m6_function.mymath.mypow(4, 2))
print(m6_function.mymath.mysum(5, 6))
print(m6_function.mymath.myabs(-4))

import m6_function.mymath as math
print(math.mypow(4, 2))
print(math.mysum(5, 6))
print(math.myabs(-4))

from m6_function.mymath import mypow
print(mypow(4, 2))

from m6_function.mymath import mypow, mysum
print(mypow(4, 2))
print(mysum(5, 6))

from m6_function.mymath import myabs as abs
print(abs(-4))