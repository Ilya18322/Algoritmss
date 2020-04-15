import math

def Linefortable():
    print('{:<1} {:<10} {:<1} {:<10} {:<1}'.format("+","-"*10, "+", "-"*10, '+'))
        
def headertable():
    Linefortable()
    print('{:<1} {:<10} {:<1} {:<10} {:<1}'.format('|', 'x', "|",'y','|'))
    Linefortable()
    
def table(dx, R):
    x0 = -4.0
    x1 = 10.0
    headertable()
    while x0 < x1:
        z = round(x0, 10)
        y = round(example(x0, R), 8)
        print('{:<1} {:<10} {:<1} {:<10} {:<1}'.format('|', z, '|', y, '|'))
        Linefortable()
        x0 += dx


def example (x, R):

    if x >= -4 and x <= -2:
        return x + 3

    elif x >= -2 and x <= 4:
        return -(x/2)

    elif x >= 4 and x <= 6:
        return -2

    elif x >= 6 and x <= 10:
        return math.sqrt((R ** 2) - (x - 8) ** 2) - 2

dx = float(input("Введите шаг приращения, dx="))
R = float(input("Введите радиус, R="))

table(dx, R)

