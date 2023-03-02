num1 = input("Enter the First Number: ")
num2 = input("Enter the Second Number: ")


''' Approach 1
print("Value of num1 after swapping: ", num1.replace(num1, num2))
print("value of num2 after swapping: ", num2.replace(num2, num1))
'''

# Approach 2
num1, num2 = num2, num1
# Displaying results
print("Value of num1:", num1)
print("Value of num2:", num2)