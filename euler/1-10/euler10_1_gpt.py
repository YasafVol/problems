import time

def primes_in_range(n):
    sieve = [True] * (n+1)
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [x for x in range(2, n+1) if sieve[x]]

t0 = time.time()
tst = 2000000
primes = primes_in_range(tst)
print(primes)
t1=time.time()
print("runtime = ", t1-t0)