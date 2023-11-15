import sys

sys.setrecursionlimit(1000000)
lookup = {}

def countTerms(n):
   if n not in lookup:
      if n == 1:
         lookup[n] = 1
      elif not n % 2:
         lookup[n] = countTerms(n / 2)[0] + 1
      else:
         lookup[n] = countTerms(n*3 + 1)[0] + 1

   return lookup[n], n

print (max(countTerms(i) for i in range(3, 100, 2)))
print(lookup)
