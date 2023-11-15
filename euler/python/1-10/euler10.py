#   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#   Find the sum of all the primes below two million.


# >> this code is very slow O(n^2) - runtime =  2684.8913905620575 (~45 min)
import time
tst = 200

def primes_in_range(n):
    lst = [x for x in range(2,n+1)] # make a list of all numbers up to n
    primes = []
    while len(lst)>0 :
        a=lst[0] # by removing the multiples - the first number is always a prime 
        print(a)
        primes.append(lst[0]) 
        p = [x for x in lst if x%a!=0] # make a list of all numbers left that are NOT a prime multiplication
        lst = p
    print (">>",primes)
    print ("sum >>> ",sum(primes))

t0 = time.time()

primes_in_range(tst)

t1=time.time()
print("runtime = ", t1-t0)