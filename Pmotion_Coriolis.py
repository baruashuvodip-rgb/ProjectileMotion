import math

g = 9.8
v_angular = 7.2921159e-5  # angular velocity of the Earth in rad/s

#to calculate coriolis effect, we need to have three components of velocity.
#horizontal and vertical are given by v_x and v_y. v_z will start at 0 but will be updated with coriolis effect.
#v_x = horizontal velocity = v_0 * cos(theta) * cos(phi)
#v_y = vertical velocity = v_0 * sin(theta) * cos(phi)
# v_z = v_0 * sin(phi) where phi is the latitude of the launch site. or is it? 

#let's have a function just for adding in the coriolis mods
def coriolis(v_x, v_y, v_z, phi):
    #calculate coriolis acceleration components
    a_coriolis_x = -2 * v_angular_y * v_z
    a_coriolis_y = 2 * v_angular_x * v_z
    a_coriolis_z = -2 * (v_x * v_angular_y - v_y * v_angular_x)
    
    return a_coriolis_x, a_coriolis_y, a_coriolis_z

#define function for calculating instantaneous acceleration with drag
def acceleration(v_x, v_y, v_z, C, m):
    a_coriolis_x, a_coriolis_y, a_coriolis_z = coriolis(v_x, v_y, v_z, phi)
    a_x = -C * v_x * math.hypot(v_x, v_y) / m + a_coriolis_x
    a_y = -g - C * v_y * math.hypot(v_x, v_y) / m + a_coriolis_y
    a_z = a_coriolis_z

    return a_x, a_y, a_z

#quick function to update intial values for each increment
def update(x, y, z, v_x, v_y, v_z, a_x, a_y, a_z, dt):
    x = x + v_x * dt + 0.5 * a_x * dt * dt
    y = y + v_y * dt + 0.5 * a_y * dt * dt
    z = z + v_z * dt + 0.5 * a_z * dt * dt
    v_x = v_x + a_x * dt
    v_y = v_y + a_y * dt
    v_z = v_z + a_z * dt
    return x, y, z, v_x, v_y, v_z

#take initial input from user
v_0 = float(input("Enter initial velocity: "))
theta = float(input("Enter launch angle (in degrees): "))
phi = float(input("Enter latitude of launch site (in degrees): "))
print("What is the size of the time step?")
dt = float(input("Enter time step: "))
print("What is the mass?")
m = float(input("Enter mass: "))
print("What is the drag coefficient?")
C = float(input("Enter drag coefficient: "))

# angular velocity components depend on initial velocity and latitude
v_angular_x = v_angular * math.cos(math.radians(phi))  # horizontal component of angular velocity
v_angular_y = v_angular * math.sin(math.radians(phi))  # vertical component of angular velocity

#initial value for position, time and maximum height
x = 0.0
y = 0.0
z = 0.0
t = 0.0
y_max = y

#boolean activation condition
inflight = True

#break initial velocity into horizontal and vertical components
v_x = v_0 * math.cos(math.radians(theta)) * math.cos(math.radians(phi))
v_y = v_0 * math.sin(math.radians(theta)) * math.cos(math.radians(phi))
v_z = 0.0  # initial coriolis velocity component due to latitude

#open output file
output_file = open("Pmotion_Coriolis_output.txt", "w")
while inflight:
    a_x, a_y, a_z = acceleration(v_x, v_y, v_z, C, m)
    x, y, z, v_x, v_y, v_z = update(x, y, z, v_x, v_y, v_z, a_x, a_y, a_z, dt)
    t += dt
    if y >= 0:
        # Output x, y, z, v_x, v_y, v_z, a_x, a_y, a_z to file
        output_file.write(f"{t}, {x}, {y}, {z}, {v_x}, {v_y}, {v_z}, {a_x}, {a_y}, {a_z}\n")
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
print("The final z position was", z)