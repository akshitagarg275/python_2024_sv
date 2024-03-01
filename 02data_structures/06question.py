# Check if given no is prime or not
# 11 , 13, 5

num = 11

if num > 1:
    # for i in range(2 , int(num/2) +1):
    for i in range(2 , num//2 +1):
    
        print(i)
        if num%i == 0:
            print(num, " It is not a prime no")
            break
    else:
        print(num, " It is a prime no")

else:
    print(num, " It is not a prime no")
