
import math,time,sys


#Function to add two numbers of any type

#First solution to add from list given
def add_nums_1(nums):
    sum = 0
    for i in nums:
        sum += i
    print('Sum is ',sum)

#Second solution to add from list given Recursively
def add_nums_2(nums):
    for i in range(0,len(nums)):
        if i+1 in range(0,len(nums)):
            return nums[i] + add_nums_2(nums[i+1:])
        else :
            return nums[i]

#Maximum of list of numbers
def max_list(nums):
    max, min = nums[0],nums[0]
    for i in nums:
        if max < i:
            max = i
        if min > i:
            min = i
    return min, max

#Factorial function RECURSIVE
def factorial_1(num):
    if num !=1:
        return num * factorial_1(num-1)
    else:
        return 1

#Factorial using Ternery Operator
def factorial_2(num):
    return 1 if (num==1 or num==0) else num * factorial_2(num-1)

#Compound Interest
def comp_interest_1(p,t,r):
    return (p * (1+r/100)**t) - p


# find order or lenght of a number
def ord_num(num):
    order = 0
    while(num!=0):
        order += 1
        num = num//10
    return order

#Check if number is Armstrong number or not
def check_armstrong_1(num):
    sum = 0
    temp_num = num
    len_num = ord_num(num)
    for i in range(1,len_num+1):
        sum += (temp_num % 10) ** len_num
        temp_num = temp_num//10
    if sum == num:
        return True
    else:
        return False

#Area Of Circle with Radius given
def rad_circle_1(r):
    return math.pi * pow(r,2)

#Print Prime numbers in an interval
def get_primenums(start,end):
    prime_nums = []
    for i in range(start,end+1):
        for divisors in range(2,i):
            if i !=divisors and i%divisors==0:
                break
        else:
            prime_nums.append(i)
    return prime_nums

#Check given number is Prime or not
def check_prime(num):
    if num==2 or num==3:
        return True
    elif num%2==0 or num%3==0:
        return False
    else:
        for i in range(5,math.ceil(math.sqrt(num))):
            if num % i == 0:
                return False
    return True

#Return list of Fibonacci Numbers below a given number
def ret_fibnums_1(num):
    fib_list = [0,1]
    if num <= len(fib_list):
        return fib_list[:num]
    for i in range(2,num):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list

#Get Nth Fibonacci Number
def get_n_fibnum(num):
    start = 0
    end = 1
    for i in range(2,num):
        end = start + end
        start = end - start
    return end

#Check if a number is a perfect square or not
def isperfectsqr(num):
    sqrt = int(math.sqrt(num))
    sqr = sqrt ** 2
    print(num, sqrt,sqr)
    if num == sqrt ** 2:
        return True
    return False

##Check if given number is a Fibonacci or not
def check_fibnum(num):
    check1 = 5*pow(num,2) + 4
    check2 = 5*pow(num,2) - 4
    if isperfectsqr(check1) or isperfectsqr(check2):
        return True

#Return Nth multiple of a number in Fibonacci series
def ret_nnul_fib(n,k):
    muls_of_n = []
    start = 0
    end = 1
    index = 0
    while(len(muls_of_n) != n):
        if end%k ==0:
            muls_of_n.append(end)
        end = start + end
        start = end - start
        index += 1
    return index

#Return sum of squares of first N numbers
def sum_sqrs(num):
    sum = 0
    for i in range(1,num+1):
        sum += i**2
    return sum

#Return sum of cubes of first N numbers
def sum_cubes(num):
    sum = 0
    for i in range(1,num+1):
        sum += i**3
    return sum



L1 = [1,3,5,7,9,0.05,4.5,-1,-5,-10]
start_time = time.time()
add_nums_1(L1)
print('Time taken for above run in seconds - {0:.7f}'.format(time.time()-start_time))
start_time = time.time()
#add_nums_1(list(map(int,input().split())))
print('sum is',math.floor(add_nums_2(L1)))
print('Time taken for above run in seconds - {0:.7f}'.format(time.time()-start_time))
start_time = time.time()
print('Min and Max in the list are ',max_list(L1))
print('Time taken for above run in seconds - {0:.7f}'.format(time.time()-start_time))
start_time = time.time()
print(factorial_1(5))
print('Time taken for above run in seconds - {0:.7f}'.format(time.time()-start_time))
start_time = time.time()
print(factorial_1(5))
print('Time taken for above run in seconds - {0:.7f}'.format(time.time()-start_time))
start_time = time.time()
print(comp_interest_1(10000,5,10.25))
print('Time taken for above run in seconds - {0:.7f}'.format(time.time()-start_time))

start_time = time.time()
print('Number is Armstrong ' if check_armstrong_1(1634) else 'Number is not Armstrong')
print('Time taken for above run in seconds - {0:.7f}'.format(time.time()-start_time))


start_time = time.time()
print('Radius of the circle is {0:.5f}'.format(rad_circle_1(5)))
print('Time taken for above run in seconds - {0:.7f}'.format(time.time()-start_time))

start_time = time.time()
print('List of Prime numbers in range given are - ',get_primenums(1,20))
print('Time taken for above run in seconds - {0:.7f}'.format(time.time()-start_time))


start_time = time.time()
print('Num give is prime ' if check_prime(12997) else 'Num is not Prime')
print('Time taken for above run in seconds - {0:.7f}'.format(time.time()-start_time))

start_time = time.time()
print('List of Fibonacci numbers in range given are - ',ret_fibnums_1(13))
print('Time taken for above run in seconds - {0:.7f}'.format(time.time()-start_time))

start_time = time.time()
print('List of Fibonacci numbers in range given are - ',get_n_fibnum(13))
print('Time taken for above run in seconds - {0:.7f}'.format(time.time()-start_time))

start_time = time.time()
print('Num give is a Fibonacci Number ' if check_fibnum(4) else 'Num is not a Fibonacci Number')
print('Time taken for above run in seconds - {0:.7f}'.format(time.time()-start_time))

start_time = time.time()
print('List of Fibonacci numbers in range given are - ',ret_fibnums_1(50))
print('Nth index is at is  ',ret_nnul_fib(2,5) )
print('Time taken for above run in seconds - {0:.7f}'.format(time.time()-start_time))

print(ord('c'))

start_time = time.time()
print('Sum is  ',sum_sqrs(3) )
print('Time taken for above run in seconds - {0:.7f}'.format(time.time()-start_time))

start_time = time.time()
print('Sum is  ',sum_cubes(5) )
print('Time taken for above run in seconds - {0:.7f}'.format(time.time()-start_time))



