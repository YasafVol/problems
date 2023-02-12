#Problem 1 : Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000."""

#this is an iteration on EulerP1 - abstracted and generalizes for any 2 multiples and any range 

upper = int(input("enter a number to get it's multiples:\n"))
a = int(input("enter 1st multiple:\n"))
b = int(input("enter 2nd multiple:\n"))


listA=[]
listB=[]
for i in range(upper):
    if i%a==0:
        listA.append(i)
    if i%b==0:
        listB.append(i)
listA = set(listA)
listB = set(listB)
multiples=(listA|listB) #this  creates the list of unique members on BOTH list
print (f"the sum of all the multiples of {a} or {b} below {upper} is", sum(multiples))

# an even more generalized and more efficient take
# make the multiples into a list - and allow as many as wanted
# iterate the counter over list members, if it fits any one append and move on
# this saves duplicated stages 