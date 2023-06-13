import math
# this code is a investment and home loan calculator.

print("Please select one of the following calculators :\n ")

print("Investment calculator - Use this to calculate the interest you will earn on your investment. \n")

print("Bond calculator - Use this to calculate the monthly payments you will have on a home loan. \n")

# user selects the appropriate calculator.
choice = input("please enter either 'Investment' or 'Bond' to continue: \n") 

# this turns the users input into lower case to stop input errors.
user_choice = choice.lower()         

# this is the investment calculator.
if user_choice == "investment" : 
    deposit = int(input("Please enter your deposit amount.\n "))
    interest_rate = int(input("Please enter interest rate. \n"))
    i_rate = interest_rate / 100 
    years = int(input("How many years would do you plan to invest? \n"))
    interest = input("Would you like either 'simple' or 'compound' interest? \n")
    # this turns the users input into lower case to stop input errors.
    user_interest = interest.lower()                                                   

    # this uses the data collected above to calculate the simple interest gains.
    if user_interest == "simple" :
        print("Your investment will earn you!")
        print(int(deposit*(1+(i_rate)*years)))

      # this uses the data collected above to calculate the compound interest.  
    if user_interest == "compound" :
        print("Your investment will earn you!")
        print(int(deposit*math.pow((1+i_rate),years)))
    
# this is the bond calculator.
elif user_choice == "bond" :
    value = int(input("Please enter the value of the house. \n"))
    Interest_rate = int(input("Please enter interest rate. \n"))
    # this calculates the annual interest rate.
    I_rate = ((Interest_rate/100)/12)                                                     
    time = int(input("Please enter how many months you would like to repay the loan. \n"))
    calculation = (int(I_rate*value)/(1 - (1 + I_rate)**(-time)))
    # this rounds up the calculation to two decimal places.
    Payments = round(calculation,2)                                                        
    print("Your monthly payments will be: ")
    print(Payments)
   

# this runs if either 'Investment' or 'Bond' is not entered.
else:
    print("Invalid selection")