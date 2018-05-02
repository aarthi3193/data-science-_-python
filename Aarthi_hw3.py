#AARTHI SHUNMUGAM-10411286
#Program to get the amount from user
while True:
    input_price = raw_input("Enter the price amount in cents:") #Get the input from the user
    
    if input_price == 'done': #if user enters 'done' exit or stop the progarm
            print "\n Goodbye!!"
            break
    try:
       input_price=int(input_price) #check whether the input is an integer
       
    except ValueError:
        
        print("\nPlease enter an integer value!") # only integer input is accepted (eg:string or float not accepted)
        continue
        
    if int(input_price)%5 == 0:
        print "\n The amount you entered is:",input_price,"cents"   #print this statement if the entered amount is multiple of 5
        continue
        
    elif int(input_price)%5 != 0:
        print "\n Please try entering a different amount!!" #print this statement if entered amount is not multiple of 5
        continue
           
    elif input_price <=0:
        print"\n The price amount cannot be neagtive" #negative amount is not accepted
        break
    