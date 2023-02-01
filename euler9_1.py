"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import time
import math

def pyth_trips(n):
    for a in range(1, n//3):
        for b in range(2, n//2):
            c=n-a-b
            print ("a>",a, "b>", b, "c>", c)
            if (a<b) and (b<c) and (c**2 == a**2 + b**2):
                triplet  = [a,b,c]
                print (">>> ", triplet)
                return print(math.prod(triplet))

start = time.time()

number=1000
pyth_trips(number)

end = time.time()
print("total run time",end - start)
