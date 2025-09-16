import math
# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y).
def polar_to_cartesian(r, theta): 
    x=r*math.cos(math.radians(theta))
    y=r*math.sin(math.radians(theta))
    return (round(x,5), round(y,5)) 

r=float(input("What is thwe radius of the cartesian plane:"))
theta=float(input("what is the angle in degrees for the polar plane:"))
print=(f"the coordiantes {r, theta} in the ploar plane represents the coordinates {polar_to_cartesian}")

# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ).
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x, y):  

    r= math.sqrt(x**2 + y**2) 
    theta=math.degrees(math.atan(y/x))
    return (round(r,5), round(theta,5))

print=(str"Question to number 2")
x=float("what is your x coordinate:")
y=float("what is your y coordinate:")
print(f"Your polar coordinates are {cartesian_to_polar}")

# Function 3 (40): Calculate the position of pendulum for (A, f, ϕ, t).
# This function should take (A, f, ϕ, t) as input and return the position value x.
def pendulum_position(A, f, phi, t):
    return 0 
w=2 
x=math.cos(w)
