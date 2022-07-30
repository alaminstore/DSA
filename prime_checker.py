# The number is not divisible except 0 or 1 is called prime number.
num = 55
def prime_checker(num):
    global flag 
    flag = 0
    if num > 1:
        for item in range(2,num):
            if num%item == 0:
                flag = 1
                break
        
prime_checker(num)
if(flag==1):
    print(num,'is Not a prime number')
else:
    print(num,'is a prime number')
