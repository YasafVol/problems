"""
Implement an RPN calculator that takes an expression like 19 2.14 + 4.5 2 4.3 / - * which is usually expressed as (19 + 2.14) * (4.5 - 2 / 4.3) and responds with 85.2974. 
The program should read expressions from standard input and print the top of the stack to standard output when a newline is encountered. The program should retain the state of the operand stack between expressions.

https://programmingpraxis.com/2009/02/19/rpn-calculator/
"""
# 1 take in user input and put it into an array
try:
    my_list = []
      
    while True:
        my_list.append(input())

# 1.1 convert all int to float
# 1.2 reject "non number" before the 3rd position 
# 1.3 only numbers float and int and math operators are legal - regex ?
# 1.4 make a copy of the array
# 2 check if array is has on element 
# 2.1 TRUE print out the element and original array
# 2.2 FALSE loop through the array 
# 2.3 when the loop hits a "not number" in the A(n) position, it does A(n-2) A(n) A(n-1)
# 2.4 replace the three array elements in a single new elements (outcome) 
# 3.5 go back to 2
