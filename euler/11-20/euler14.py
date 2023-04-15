'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
'''

import time
import sys

sys.setrecursionlimit(100000)

memo_object={}
limit = 1000000  

def collatz(n):
    global memo_object
    if n not in memo_object:
        if n==1:
            memo_object[n] =1
        elif n%2==0:
            memo_object[n] = collatz(n/2)[0] +1
        else:
            memo_object[n] = collatz(n*3+1)[0] +1
    return memo_object[n], n

t0= time.time()
for i in range(3,limit,2):
    collatz(i)

max_value = max(memo_object, key=memo_object.get)    
print("\n", "Number=> " ,max_value)
t1=time.time()
print("\n runtime = ", t1-t0)
