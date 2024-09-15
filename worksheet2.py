L = [11, 12, 13, 14]

# (i) 
L += [50, 60]

# (ii) 
L.remove(11)
L.remove(13)

# (iii) 
L.sort()

# (iv) 
L.sort(reverse=True)

# (v)
print("13 is in the list" if 13 in L else "13 is not in the list")

# (vi) 
print("Number of elements:", len(L))

# (vii)
print("Sum of all elements:", sum(L))

# (viii) 
print("Sum of odd numbers:", sum(x for x in L if x % 2 != 0))

# (ix) 
print("Sum of even numbers:", sum(x for x in L if x % 2 == 0))

# (x) 
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

print("Sum of prime numbers:", sum(x for x in L if is_prime(x)))

# (xi) 
L.clear()

# (xii) 
del L

# Functions for sum and multiplication
def sum_list(lst):
    return sum(lst)

def multiply_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

# Q 2 & 3
my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))  
print(multiply_list(my_list))

D = {1: 5.6, 2: 7.8, 3: 6.6, 4: 8.7, 5: 7.7}

# (i) 
D[8] = 8.8

# (ii) 
del D[2]

# (iii) 
print("Key 6 is present." if 6 in D else "Key 6 is not present.")

# (iv)
print("Number of elements:", len(D))

# (v)
print("Sum of values:", sum(D.values()))

# (vi)
D[3] = 7.1

# (vii) 
D.clear()

S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

# (i)
S1 |= {55, 66}

# (ii) 
S1 -= {10, 30}

# (iii) 
print("40 is present in S1." if 40 in S1 else "40 is not present in S1.")

# (iv) 
union_set = S1 | S2

# (v) 
intersection_set = S1 & S2

# (vi) 
difference_set = S1 - S2

import random, string

# (i) 
for _ in range(100):
    print(''.join(random.choices(string.ascii_letters, k=random.randint(6, 8))))

# (ii)
for num in range(600, 801):
    if is_prime(num):
        print(num)

# (iii)
for num in range(100, 1001):
    if num % 7 == 0 and num % 9 == 0:
        print(num)

exam_st_date = (11, 12, 2014)
print("Exam start date:", *exam_st_date, sep="/")

numbers = [1, 5, 10, 15, 20, 23, 25]
print([num for num in numbers if num % 5 == 0])

def is_even(num):
    return num % 2 == 0

num = 10
print(f"{num} is even." if is_even(num) else f"{num} is odd.")

def count_emma(s):
    return s.count("Emma")

text = "Emma is girl. Emma likes to play football."
print("'Emma' appears", count_emma(text), "times")

def create_new_list(list1, list2):
    return [x for x in list1 if x % 2 != 0] + [x for x in list2 if x % 2 == 0]

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print("New list:", create_new_list(list1, list2))