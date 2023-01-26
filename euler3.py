#--------------------------------------
# Problem 3 - Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#-------------------------------------

factors=[]
number = 600851475143
for i in range(1,number):
    if number%i==0:
        print("this is a prime factor ===>", i)
        factors.append(i)
        number=number/i
#this is needed to avoid it getting stuck in a range of 1
    if number <=1:
      break
print(factors)
