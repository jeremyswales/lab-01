def hollow_sqaure(n): 
    for i in range(1, n + 1): 
        if i == 1: 
            print("*"*n)
        elif 1 < i < n:
            a = "*"
            b = " "*(n - 2)
            print(a+b+a)
        else:
            print("*"*n)
    return

a= int(input("What number do you want to be in a square: "))
hollow_sqaure(a)

def number_pattern(n):
    i = 1
    while i <= n: 
        a = 1
        while a <= i: 
            print(a, end="")
            a += 1
        print() 
        i += 1

    return 

y = int(input("What is the height of the triangle?: "))
number_pattern(y)

def sum_of_natural_numbers(n):
    count = []
    i = 1
    while i <= n:
        count.append(i)
        i += 1

    total = sum(count)
    print(total)
    return 

number = int(input("What number do you want to count all natural numbers to?: "))
sum_of_natural_numbers(number)

def centered_star_pyramid(n): 
    for i in range(1, n + 1): 
        spaces = " "*(n - i)
        stars = "*"*(2*i - 1)
        print(spaces+ stars)
    return 

triangle = int(input("What size do you want your triangle to be: "))
centered_star_pyramid(triangle)