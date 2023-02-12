import time
import math 

def factors(n):
    count = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            count+=2
        if i**2 == n:
                count -= 1
        
    return count

t0=time.time()

m=0
f= 0
while f<=100:
    m+=1
    number = int((m*(m+1))/2)
    f= factors(number)
    print("Number: ", number, "  Factors: ", f)

t1=time.time()
print("\n runtime = ", t1-t0)


