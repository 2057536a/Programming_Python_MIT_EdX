#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:47:43 2018

@author: yannis
"""

#Now write a program that calculates the minimum fixed monthly payment needed in order pay off 
#a credit card balance within 12 months. By a fixed monthly payment, we mean a single number 
#which does not change each month, but instead is a constant amount that will be paid each month.

#Assume that the interest is compounded monthly according to the balance at the end of the 
#month (after the payment for that month is made). The monthly payment must be a multiple 
#of $10 and is the same for all months. Notice that it is possible for the balance to become 
#negative using this payment scheme, which is okay. A summary of the required math is found below:

#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)




## TESTING VALUES##
##UN- COMMENT TO CHECK##
balance = 61              
annualInterestRate = 0.18


#The interest rate each month
monthlyInterestRate = annualInterestRate / 12.0

#Start off with an initial lowest payment
lowest_payment = 0;

#A reference to the initial balance so that can be reset if the lowest payment needs recalculation
reused_balance = balance

#Keep looping for as long as the balance is positive
# i.e. for as long as there is money to be paid still.
while balance > 0:
    
    #Increase the minimum payment, as the previous one was not enough to get the balance down to 0 after 12 months
    lowest_payment += 10
    #Reset the balance to the initial one
    balance = reused_balance
    
    #Loop over the months and calculate...
    for i in range(12):
    
        #The minimum payment each month
        minimumMonthlyPayment = lowest_payment
    
        #What portion of the current balance will be unpaid after the minimum payment
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
    
        #The new balance after the interest has been applied to it
        updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
        #The balance for next month will be the new updated balance after interest
        balance = updatedBalance
   
#Result   
print("Lowest Payment: " + str(lowest_payment))












