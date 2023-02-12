#Problem 1 : Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#this is an iteration on EulerP1 - abstracted and generalizes for any number of multiples and any range
# iterate the counter over list members, if it fits any one append and move on
  

upper = int(input("enter a number to get it's multiples:\n"))

multipliers = []
while True:
    a = input("enter multipliers, enter DONE to finish:\n")
    if a=="done": 
        break
    multipliers.append(int(a))

numbers = []

for i in range(upper):
    for j in range(len(multipliers)):
        if (i%multipliers[(j-1)] == 0) and not (i in numbers):
            numbers.append(i)

print (f"the sum of all the multiples of {multipliers} below {upper} is", sum(numbers))