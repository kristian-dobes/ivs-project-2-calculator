import sys
from mathlibrary import *

x = [int(x) for x in input().split()]
#sumy ctvercu a prumer
total = 0
suma = 0
n = len(x)
for ele in range(0, len(x)):
    square = pow(x[ele], 2)
    total = sum(total, square)

    suma = sum(suma, x[ele])

power = pow(suma, 2) 
divi = div(power, n)

substr = sub(total, divi)           #rozdil v zavorce

temp = sub(n, 1)
temp2 = div(1, temp)
temp3 = mult(temp2, substr)
res = nroot(temp3, 2)
print(res)