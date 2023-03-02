# Approach 1
'''
num = int(input("Enter a number: "))
# Counter variable to count factors of the enter number
count=0

if num>1:
    # The reason why we are iterating to num-1 is because we can safely assume 1 will always be a prime number
    # We can speed up efficiency by skipping the final operation of dividing by the number itself
    for i in range(1,num):
        if (num % i) == 0:
            count+=1
        else:
            continue
    
    if (count==1):
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

else:
    print(num, "is not a prime number")
'''       

# Approach 2
num = int(input("Enter a number: "))
mainPrime = (2,3,5,7)
if(num/1==num and num/num==1 and num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0):
    print(num,"is prime")

elif (num in mainPrime):
    print(num,"is prime")

else:
    print(num, "is not prime")