#Task 1

# def sum_num(x):
#     if x == 1 or x == 0:
#         return x
#     else:
#         return x + sum_num(x -1)
    
# print(sum_num(4))    

#Task 2   

# def num_count(x):
#     if x < 10:
#         return 1
#     else:
#         return num_count(x / 10) + 1
    
# print(num_count(1000000))    

#Task 3

# def stepen(n, y):
#     print(n, y)
#     if y == 0:
#         return 1
#     else:
#         return stepen(n, y-1) * n

# print(stepen(7, 7))#

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def print_to(n: int) -> None:
#     if n > 20:
#         return 0
#     print_to(n * 2)
#     print(n)

# print_to(1)    
  



# if n % 2 == 0:
#     for i in range(0,n +1):
#         s = i * (i + 2)
# else:
#     for i in range(1,n +1):
#         s = i * (i + 2)  
# print(s)

# n = int(input())
# def double_fact(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * double_fact(n - 2)

# print(double_fact(n))       

# n = int(input())
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2) 
    
# print(fib(n))    

# n = int(input())
# def three(n):
#     if n <= 2:
#         return n
#     else:
#         return three(n - 1) + three(n - 2) + three(n - 3)
# print(three(n))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Task 1

# def sumi(n):
#     if n == 0:
#         return 0
#     else:
#         return sumi(n - 1) + n

# print(sumi(4))

# Task 2

# def sum_numbers(n):
#     if n == 0:
#         return 0
#     else:
#         return sum_numbers(n // 10) + 1

# print(sum_numbers(10))
 
# Task 3

# def num_step(n, y):
#     if y == 0:
#         return 1
#     else:
#         return num_step(n, y -1) * n
    
# print(num_step(7,7))    

#Task 4

# lst = [99, 121, 55, 68, 95, 1408,8, 95, 95, 666]

# def min_el(n):
#     if len(n) == 1:
#         return n[0]
#     else:
#         return min(n[0], min_el(n[1:]))

# print(min_el(lst))

# Task 5

# lst = [99, 121, 55, 68, 95, 1408, 8, 95, 95, 666]

# def sum_list(n):
#     if len == 0:
#         return 0
#     else:
#         return 

#Task 6
