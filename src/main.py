# #Allow the user to enter a calculation with two numbers and an operator, perform the calculation, and print the result. (10 marks) The allowed operators should be +, -, *, /, ^ (add, subtract, multiply, divide, power). Use separate variables to store the entered numbers and operator. 
# #number_one = 1 number_three = 3 print (number_one + number_three)
print ("Welcome to the Handy Calculator!")
print ("Type in a number, then an operator, then another number and see what answer you get")
number_one = None
while number_one == None:
    try:
        number_one = float(input("Gimme the first number: ") )
        print ("YAY!")
    except:
        print ("OOPS TRY AGAIN")

smooth_operator = None
while smooth_operator == None:        
    enter_smooth_operator = input("Now a smooth operator: ")
    if enter_smooth_operator == "+":
        smooth_operator = "+"
    elif enter_smooth_operator == "-":
        smooth_operator = "-"
    elif enter_smooth_operator == "*":
         smooth_operator = "*"   
    elif enter_smooth_operator == "/":
          smooth_operator = "/"  
    elif enter_smooth_operator == "^":
        smooth_operator = "^"  
    else:
        print ("NOT SMOOTH ENOUGH")

number_two = None
while number_two == None:
    try:
        number_two = float(input("Now gimme the second number: ") )
        print ("drumroll...")
        if smooth_operator == "+":
            print (number_one+number_two)
        elif smooth_operator == "-":
            print (number_one-number_two)
        elif smooth_operator == "*":
            print (number_one*number_two)
        elif smooth_operator == "/":
            print (number_one/number_two)
        elif smooth_operator == "^":
            print (number_one**number_two)
    except:
        print ("OOPS TRY AGAIN")

    
# number_uno = None 
# while number_uno == None:
#     try:
#         number_uno = float (input("number_uno: "))
#         print ("YAY")
#     except:
#         print ("TRY AGAIN")


