import math
def Calculate(weight, floor, elevator):
    if elevator == 1:
        if weight <= 50:
            sum = 300
        if weight <= 100:
            sum = 1000
        if weight <= 300:
            sum = 2000
    else:
        if weight <= 50:
            sum = 300 + 300*(floor-1)
        if weight <= 100:
            sum = 1000 + 300*(floor-1)
        if weight <= 300:
            sum = 2000 + 300 * (floor-1) * (math.ceil(weight/100))
    return(sum)

a = Calculate(250, 3, 0)
print(a)