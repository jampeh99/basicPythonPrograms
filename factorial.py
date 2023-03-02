num = int(input("Enter a number: "))
# Counter variable to count factors of the enter number
factorial=1

# Case for negative numbers
if num<0:
    print("The factorial for a negative number cannot be calculated")

# Test case for 0
elif num==0:
    print("The factorial of 0 is 1")

else:
    for i in range(1,num+1):
        factorial *=i
    print("Factorial of %i is %i" % (num, factorial))