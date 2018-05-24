#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 13:46:36 2018

@author: yannis
"""

#Same as problem 2 but with bisection serach to reduce the 
# execution time. Still using:

#balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

#and 

#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly payment lower bound = Balance / 12
#Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) / 12.0


#Write a program that uses these bounds and bisection search to find the  smallest monthly 
#payment to the cent (no more multiples of $10) such that we can pay off the debt within a year





## TESTING VALUES##
##UN- COMMENT TO CHECK##
balance = 999999              
annualInterestRate = 0.18

#The interest rate each month
monthlyInterestRate = annualInterestRate / 12.0

#Bounds and midpoint calculation
lower_pay_bound = balance /12
upper_pay_bound = (balance * ((1 + monthlyInterestRate)**12)) / 12.0
midpoint = (lower_pay_bound + upper_pay_bound)/2

#A reference to the initial balance so that can be reset if the lowest payment needs recalculation
reused_balance = balance


#Check that the balance is within an accepted limit
while (abs(balance) > 0.1):

    # If balance is not satisfactory then keep calculating the midpoint with new limit values
    midpoint = (lower_pay_bound + upper_pay_bound)/2
    
    #Reset the balance to the initial one
    balance = reused_balance
    
    #Loop over the months and calculate...
    for i in range(12):
    
        #The minimum payment each month
        minimumMonthlyPayment = midpoint
    
        #What portion of the current balance will be unpaid after the minimum payment
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
    
        #The new balance after the interest has been applied to it
        updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
        #The balance for next month will be the new updated balance after interest
        balance = updatedBalance
        
    #If the balance is -ve then the monthly payment is way too high
    # reset the upper limit to be the midpoint in this case,
    # If it is +ve then the monthly payment is way to low. Adjust the
    #lower limit in this case       
    if balance < 0 :
        upper_pay_bound = midpoint
    else:
        lower_pay_bound = midpoint
        
print(round(minimumMonthlyPayment,2))
           
   

