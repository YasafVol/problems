"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

#brute force - ugly code - with duplicates
import math
import time

start = time.time()

lst=[]
for i in range(1,1000,1):
    for j in range (1,1000,1):
        k=math.sqrt(i**2 + j**2)
        if k- int(k)==0:
            l=[]
            l.append(i)
            l.append(j)
            l.append(int(k))
            if l not in lst:
                lst.append(l)
            print (i,j,k)
print(lst)

trip = [itm for itm in lst if sum(itm) == 1000]
print(trip)
print(math.prod(trip[0]))

end = time.time()
print("total run time",end - start)