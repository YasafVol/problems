#--------------------------------------
#Problem 4 - Largest palindrome product
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
#--------------------------------------

list=[]
for i in range(999,500,-1):         
    for j in range(999,500,-1):
        a = str(i*j)
        print ((i),(j),(a))
        b = a[::-1]
        if a==b:
            list.append(i*j)
            list.append(i)
            list.append(j)
            break

print(max(list))    

print(list)