'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
# this gets all the factors of n 
def getFactors(n):
    factors=[]
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 1
    if n > 1:
        factors.append(n)
    return (factors)


i= int(input("enter an integer: " ))
allF=[]

# a list of lists of all factors
while i>1: 
    allF.append(getFactors(i))
    i-=1

print(allF)

factors = []
for i in range(len(allF)):
    l=allF[i]
    for j in range(len(l)):
        # adds unique factors to the empty list 
        if l[j] not in factors:
            factors.append(l[j])
        else:
            # if the unique factor is already in the list - add it ad many times as needed (eg - 8 >> 2,2,2)
            count=(l.count(l[j])-factors.count(l[j]))
            factors.extend([l[j]]*count)

commonINT=1

# this can be accomplished with import math, compound (i think) - i arbitrarily chose to make my own
for i in range(len(factors)):
    commonINT*=factors[i]
    print(commonINT)

print(">>>  ", commonINT, "  <<<")