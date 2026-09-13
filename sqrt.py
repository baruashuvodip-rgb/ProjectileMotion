import math 

v_x = 38.84588249374119
v_y = 50.7882580860628
v_z = 4.883144759365985e-09

a = math.hypot(v_x, v_y, v_z)
b = math.sqrt(v_x*v_x + v_y*v_y + v_z*v_z)

print(a,b)