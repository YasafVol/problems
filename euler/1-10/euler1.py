#Problem 1 : Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000."""

threes=[]
fives=[]
for i in range(1000):
    if i%3==0:
        threes.append(i)
    if i%5==0:
        fives.append(i)
threes = set(threes)
fives = set(fives)
multiples=(threes|fives) #this  creates the list of unique members on BOTH list
print ("the sum of all the multiples of 3 or 5 below 1000 is", sum(multiples))
