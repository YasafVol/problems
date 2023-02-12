# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

n = int(input("enter a number:"))

a = 0
b = 0

for i in range(n+1):
    a += i**2
    b += i
    print(i, ":", a, " | ", b)
    
c=b**2
d=c-a
print(c, " - ",a, " = ",d)
