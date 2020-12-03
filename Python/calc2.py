def doMath(a,b):
	print("Sum:", a+b)
	print("Difference:", a-b)
	print("Product", a*b)
	print("Quotient", round(a/b, 2))
	print("Modulo", a%b)


number_1 = float(input("Enter the first number:"))
number_2 = float(input("Enter the second number"))


(doMath(number_1,number_2))
