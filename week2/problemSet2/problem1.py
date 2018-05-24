#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:15:41 2018

@author: yannis
"""

#Write a program to calculate the credit card balance after one year if a person only pays 
#the minimum monthly payment required by the credit card company each month.

#The following variables contain values as described below:

#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#monthlyPaymentRate - minimum monthly payment rate as a decimal

#For each month, calculate statements on the monthly payment and remaining balance. At the end 
#of 12 months, print out the remaining balance. Be sure to print out no more than two decimal 
#digits of accuracy 

#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)




#The interest rate each month
monthlyInterestRate = annualInterestRate / 12.0

#Loop over the months and calculate...
for i in range(12):
    
    #The minimum payment each month
    minimumMonthlyPayment = monthlyPaymentRate * balance
    
    #What portion of the current balance will be unpaid after the minimum payment
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    
    #The new balance after the interest has been applied to it
    updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
    #The balance for next month will be the new updated balance after interest
    balance = updatedBalance
  
#Print results
print( "Remaining balance: " + str(round(updatedBalance,2)))

    
    
    