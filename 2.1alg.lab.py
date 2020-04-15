import math

def example (x, R):

    if x >= -4 and x <= -2:
        return x + 3

    elif x >= -2 and x <= 4:
        return -(x/2)

    elif x >= 4 and x <= 6:
        return -2

    elif x >= 6 and x <= 10:
        return math.sqrt((R ** 2) - (x - 8) ** 2) - 2

    else:
        return("Значение не в диапозоне.")
        
x = float(input("Введите значение x= "))
R = float(input("Введите значение R= "))

print("Значение функции:", example(x,R))
