import math
# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y).
def polar_to_cartesian(r, theta): 
    x=r*math.cos(math.radians(theta))
    y=r*math.sin(math.radians(theta))
    return (round(x,5), round(y,5)) 

r=float(input("What is thwe radius of the cartesian plane:"))
theta=float(input("what is the angle in degrees for the polar plane:")) 
Coordinates = polar_to_cartesian(r,theta)
print(f"the coordiantes {Coordinates}")

# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ).
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x, y):  

    r= math.sqrt(x**2 + y**2) 
    theta=math.degrees(math.atan(y/x))
    return (round(r,5), round(theta,5))

x=float(input("what is your x coordinate:"))
y=float(input("what is your y coordinate:"))
Polar=cartesian_to_polar(x, y)
print(f"Your polar coordinates are {Polar}")

# Function 3 (40): Calculate the position of pendulum for (A, f, ϕ, t).
# This function should take (A, f, ϕ, t) as input and return the position value x.
def pendulum_position(A, T, phi, t):
    
    w = (2*math.pi)/T
    x = A * math.cos(w*t +phi)
    return (round(x, 5))

A = float(input("insert the amplitude of the pendulum:"))
T = float(input("What is the period of the pendulum:"))
phi = float(input("What is the phase of the constant in radians:"))
t = float(input("At what time:"))
Position = pendulum_position(A, T, phi, t)
print(f"The position of the pendulum at {t} is {Position}")