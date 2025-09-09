# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# 
def calculate_height(h0, t):
    g=9.8
    result=h0-1/2*g*t**2 
    return result
h0=float(input("Enter initial height in meters:"))
t=float(input("After how many seconds:"))
print(f"the height of the ball is", {calculate_height(h0, t)}, "meters")
  
# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
        # TODO: Implement this function
        pass  # Replace with your code 
speed=20
time= float(input("what is the time for the car(seconds): ")) 
distance = speed * time 
print("The distance of the object is", distance)