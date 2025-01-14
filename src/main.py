#Allow the user to enter a calculation with two numbers and an operator, perform the calculation, and print the result. (10 marks) The allowed operators should be +, -, *, /, ^ (add, subtract, multiply, divide, power). Use separate variables to store the entered numbers and operator. 
#number_one = 1 number_three = 3 print (number_one + number_three)
print ("Welcome to the Handy Calculator!")
print ("Type in a number, then an operator, then another number and see what answer you get")
number_one = float(input("Gimme the first number: ") )
smooth_operator = input("Now a smooth operator: ")
number_two = float(input("Now gimme the second number: ") )
if smooth_operator == "+":
    print (number_one+number_two)
if smooth_operator == "-":
    print (number_one-number_two)
if smooth_operator == "*":
    print (number_one*number_two)
if smooth_operator == "/":
    print (number_one/number_two)
if smooth_operator == "^":
    print (number_one**number_two)    