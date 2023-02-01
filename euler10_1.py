import time

def func(n):
    sieve = [True] *(n+1)
    for i in range(2, int(n**0.5) +1):
        if sieve[i]:
            for j in range(i*i,n+1,i):
                sieve[j]=False
    return [x for x in range(2, n+1) if sieve[x]]

t0=time.time()
number = 2000000
primes = func(number)
t1=time.time()
print (primes)
print ("run time ==> ", (t1-t0))