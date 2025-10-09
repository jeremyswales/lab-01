def maximum( a, b,c):
    number=[a,b,c]
    highest= max(number)
    return highest

a=float(input("What is your first number:"))
b=float(input("What is your scond number:"))
c=float(input("What is your third number:"))

print(f"Your highest number is {maximum(a,b,c)}")

#'''''''''''''''''''''''''''''''''''''''''''''''''''''

def minimum( a,b,c):
    number=[a,b,c]
    lowest= min(number)
    return lowest

a=float(input("What is your first number:"))
b=float(input("What is your scond number:"))
c=float(input("What is your third number:"))

print(f"Your lowest number is {minimum(a,b,c)} ")

#''''''''''''''''''''''''''''''''''''''''''''''''''''''

def number_state(n):
    
    if n > 0:
        print("The number is positive")
    elif n < 0:
        print("The number is negative")
    else:
        print("The number is zero")
    

n = int(input("What is your number:"))
print(f"{number_state(n)}")

#''''''''''''''''''''''''''''''''''''''''''''''''''''''

def star_shape(rows):

    for i in range(1, rows + 1):
        print("*"*i)
    return
rows=int(input("what numnber:"))
print(f"{star_shape(rows)}")

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def multiple(n):
    i=0
    while i < n:
        i+= 1
        if i % 3 ==0:
            print(f"{i} is a multiple of three")

        else:
            print(i)
    return

count = int(input("What number do you want:"))
multiple(count)

#'''''''''''''''''''''''''''''''''''''''''''''

def even(a,b):
    list = []
    even_number =[]
    for i in range(a, b+1):
        list.append(i)
    
    for n in list:
        if n % 2 ==0:
            even_number.append(n)

    total=sum(even_number)
    return total

a=int(input("Your first number:"))
b=int(input("Your second number:"))
print(f"{even(a,b)}")