# Make sure you are not modifying the method signatures
# Function 1: Write a simple Hello World program
# This function should print "Hello, World!" to the screen.
def hello_world():
    # TODO: Implement this function
    print("Hello world")
    pass  # Replace with your code

# Function 2: Get input and output with different variable types
# This function should prompt the user for their name (string), age (int), and height (float),
# and then print them back in a formatted message.
def input_output():
    # TODO: Implement this function 

    name = str(input("Please enter your name:"))
    age = int(input("Please enter your age:")) 
    height = float(input("Please enter your height (in metres):"))
    print(f"Hi, {name}")
    print(f"You are {age} years old")
    print(f"you are {height} metres tall")

pass  # Replace with your code 
hello_world()
input_output()