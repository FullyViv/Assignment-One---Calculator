import random
from datetime import datetime
quote_me = [" 'They say it all started out with a big bang. But, what I wonder is, was it a big bang or did it just seem big because there wasn't anything else drown it out at the time?' - Karl Pilkington",
" 'People who live in a glass house have to answer the door.' - Karl Pilkingtod", " 'Stay green, stay in the woods, and stay safe.' - Brett Pilkington", " 'Parrots have gone a bit quiet since pirates have gone.' - Little Baldy Manc Twat", " 'If you can't look a knob in the face there's something wrong.' - Mr. K Dilkington"]
print (random.choice(quote_me))
currrent_date = datetime.now()
day_day = currrent_date.strftime("%b %d, %Y")
time_time = currrent_date.strftime("%I:%M %p")
print ("Welcome to the Handy Calculator!")
print ("It is currently " + time_time + " on " + day_day)
print ("Type in a number, then an operator, then another number and see what answer you get")
number_one = None
while number_one == None:
    try:
        number_one = float(input("Gimme the first number: ") )
        
    except:
        print ("OOPS TRY AGAIN")

smooth_operator = None
while smooth_operator == None:        
    enter_smooth_operator = input("Now a smooth operator: ")
    if enter_smooth_operator in ["+","-","*","/","^"]:
        smooth_operator = enter_smooth_operator
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

    



