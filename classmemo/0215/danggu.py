import math

start = (0,0)
end = (3,4)

a = abs(end[0]-start[0])
b = abs(end[1]-start[1])

r = math.sqrt(a**2+b**2)

radian = math.atan(b/a)
print(r,math.degrees(radian))