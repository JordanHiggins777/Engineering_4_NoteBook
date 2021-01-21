import cmath
print("Quadratic Solver:Enter the coefficients for ax^2 + bx + c = 0")
a = float(input("Input a:"))
b = float(input("Input b:"))
c = float(input("Input C:"))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

if(a == 0):
	print("you're gay")

if(d < 0):
	print("No real roots")
	print("The solutions are {0} and {1}".format(sol1,sol2))
else:
	print("These roots are real")
	print("The solutions are {0} and {1}".format(sol1,sol2))
