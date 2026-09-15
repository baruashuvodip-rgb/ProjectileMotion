import math

g = 9.8

#define function for calculating instantaneous acceleration with drag
def acceleration(v_x, v_y, C, m):
    a_x = -C * v_x * math.hypot(v_x, v_y) / m
    a_y = -g - C * v_y * math.hypot(v_x, v_y) / m
    return a_x, a_y

#quick function to update intial values for each increment
def update(x, y, v_x, v_y, a_x, a_y, dt):
    x = x + v_x * dt + 0.5 * a_x * dt * dt
    y = y + v_y * dt + 0.5 * a_y * dt * dt
    v_x = v_x + a_x * dt
    v_y = v_y + a_y * dt
    return x, y, v_x, v_y

#take initial input from user
v_0 = float(input("Enter initial velocity: "))
theta = float(input("Enter launch angle (in degrees): "))
print("What is the size of the time step?")
dt = float(input("Enter time step: "))
print("What is the mass?")
m = float(input("Enter mass: "))
print("What is the drag coefficient?")
C = float(input("Enter drag coefficient: "))

#initial value for position, time and maximum height
x = 0.0
y = 0.0
z = 0.0
t = 0.0
y_max = y

#boolean activation condition
inflight = True

#break initial velocity into horizontal and vertical components
v_x = v_0 * math.cos(math.radians(theta))
v_y = v_0 * math.sin(math.radians(theta))

#open output file
output_file = open("Pmotion_wAir_output.txt", "w")
while inflight:
    a_x, a_y = acceleration(v_x, v_y, C, m)
    x, y, v_x, v_y = update(x, y, v_x, v_y, a_x, a_y, dt)
    t += dt
    if y >= 0:
        # Output x, y, v_x, v_y, a_x, a_y to file
        output_file.write(f"{t}, {x}, {y}, {z}, {v_x}, {v_y}, {a_x}, {a_y}\n")
        if y > y_max:
            #update maximum height
            y_max = y
    else:
        inflight = False

#close output file
output_file.close()

#output summary
print("The maximum height was", y_max)
print("The horizontal range was", x)

