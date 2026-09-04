import math

g=9.8

def acceleration(v_x, v_y, C, m):
    a_x = -C * v_x * math.hypot(v_x, v_y) / m
    a_y = -g - C * v_y * math.hypot(v_x, v_y) / m
    return a_x, a_y

def update(x, y, v_x, v_y, a_x, a_y, dt):
    x = x + v_x * dt + 0.5 * a_x * dt * dt
    y = y + v_y * dt + 0.5 * a_y * dt * dt
    v_x = v_x + a_x * dt
    v_y = v_y + a_y * dt
    return x, y, v_x, v_y

v_0 = float(input("Enter initial velocity: "))
theta = float(input("Enter launch angle (in degrees): "))
print("What is the size of the time step?")
dt = float(input("Enter time step: "))
print("What is the mass?")
m = float(input("Enter mass: "))
print("What is the drag coefficient?")
C = float(input("Enter drag coefficient: "))
print("What is the initial position?")
x, y = map(float, input("Enter initial x and y positions: ").split())

v_x = v_0 * math.cos(math.radians(theta))
v_y = v_0 * math.sin(math.radians(theta))

update(x, y, v_x, v_y, a_x, a_y, dt)

if y >= 0:
    # Output x, y, v_x, v_y, a_x, a_y to file
    pass
if y > y_max:
    y_max = y
else:
    projectile no longer in flight
print("The maximum height was", y_max)
print("The horizontal range was", final_value_of_x)