"""Module providing a function printing python version."""
import math

#The user should be allowed to choose which calculation they want to do.
#The first output that the user sees when the program runs should look like this :
#investment - to calculate the amount of interest you'll earn on your investment
#bond - to calculate the amount you'll have to pay on a home loan
#Enter either 'investment' or 'bond' from the menu above to proceed:

#Print entry line and menu/definitions
print("Welcome to the Finance Calculator!")
print("\nInvestment - To calculate the amount of interest you'll earn on your investment.")
print("Bond - To calculate the amount you'll have to pay on a home loan.")

#Blank line betweet menu and input
print("")

#Ask user for input and transform it to lower case using .casefold
#this way the entry is going to be reconized without case distinction
service_needed = str.casefold(input("Enter either 'investment' or 'bond' from the menu above to proceed: "))

#Blank line betweet menu and input
print("")

#Investment inputs
if service_needed == "investment":
    amount = float(input("Enter the amount of money you are depositing: "))
    rate = float(input("Enter the interest rate (as a percentage): ")) /100
        #percentage so divided by 100
    years = int(input("Enter the number of years you plan on investing: "))
    interest = str.casefold(input("Do you want 'simple' or 'compound' interest? "))

    #Investment calculation
    calculate_simple_interest = amount * (1 + rate * years)
    calculate_compound_interest = amount * math.pow((1 + rate), years)

    #Output
    if interest == "simple":
        total_amount = calculate_simple_interest
    elif interest == "compound":
        total_amount = calculate_compound_interest
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'. ")

    print("___________________________________________________________________")
    print(f"\nThe total amount after {years} years will be: {total_amount}")
    print("___________________________________________________________________")


#Bond inputs
elif service_needed == "bond":
    present_value = int(input("Enter the present value of the house: "))
    annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): ")) /100
        #percentage so divided by 100
    months = int(input("Enter the number of months you plan to take to repay the bond: "))

    #Bond calculation
    monthly_interest_rate = annual_interest_rate / 12
    repayment = (monthly_interest_rate * present_value) / (1 - ((1 + monthly_interest_rate)**(-months)) )

    #Output
    print("___________________________________________________________________")
    print(f"\nYou will have to repay approximately: {repayment} per month")
    print("___________________________________________________________________")


else:
    print("Invalid choice. Please enter 'investment' or 'bond'.")

print("")

# End-of-file (EOF)
