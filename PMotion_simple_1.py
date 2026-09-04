import math

g = 9.81  # Acceleration due to gravity (m/s^2)

v0 = float(input("Enter initial velocity (m/s): "))
theta0 = float(input("Enter launch angle (degrees): "))

steps = int(input("Enter number of steps: "))

v_x0 = v0*math.cos(math.radians(theta0)) # Initial horizontal velocity
v_y0 = v0*math.sin(math.radians(theta0)) # Initial vertical velocity
flight_time = (2*v_y0)/g # Total flight time
time_step = flight_time/steps # Time increment for each step

output_file = open("Pmotion_output.txt", "w")

x = 0.0 # Initial horizontal position
y = 0.0 # Initial vertical position
v_y = v_y0 # Current vertical velocity
y_max = y

t = 0.0
for step in range(steps + 1):
    if(y<0):
            break

    x = x+v_x0*time_step
    y = y+v_y*time_step - 0.5*g*time_step**2
    v_y = v_y - g*time_step
    t = t + time_step

    output_file.write(f"{t:.2f} {x:.2f} {y:.2f} {v_x0:.2f} {v_y:.2f}\n")
    if(y>y_max):
        y_max = y
    
output_file.close()
print(f"Maximum height reached: {y_max:.2f}")
print(f"Horizontal distance traveled: {x:.2f}")