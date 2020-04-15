  
import math

def z1(a):

	return 1 - 1/4 * (math.sin(2 * a) * math.sin(2 * a)) + math.cos(2 * a)

def z2(a):

	return (math.cos(a) * math.cos(a)) + (math.cos(a) * math.cos(a) * math.cos(a) * math.cos(a))

a = float(input("Ввидите значение a = "))

print (z1(a),z2(a))