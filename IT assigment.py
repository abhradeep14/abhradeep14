# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 18:03:20 2021

@author: Lenovo
"""

menu1=input("Select a for Fibonaccis Sequence:\nSelect b for Armstrong number:\nSelect c for Reverse of a number:\nSelect d for checking Palidrome for a number:\nEnter the appropriate option: ")
if menu1==('a'):
    f=int(input("Numbers wanted for the Fibonaccis series:"))
    a=0
    b=1
    for i in range (f):
        c=a+b
        print(c)
        a,b=b,a+b
elif menu1==('b'):
    arm=int(input("Input the number for checking Armstrong Sequence:"))
    x=0
    y=arm
    while y>0:
        numb=y%10
        x += numb**3
        y //=10
    if  arm==x:
            print(arm,"Is a armstrong number")
    else:
            print(arm,"is not a Armstrong number")
elif menu1==('c'):
    rev=int(input("Enter the number which is to be reversed:"))
    n=0
    while(rev>0):
        r= rev%10
        n=(n*10) + r
        n=n//10
    print("Reverse of the number is"% n)
elif menu1==('d'):
    a=int(input("Enter the number to be checked for Palidrome:"))
    t=a
    b=0
    while(a>0):
       c=a%10
       b=b*10+c
       a=a//10
    if (t==b):
        print("The number entered is Palindrome")
    else:
        print("The number entered in not Palindrome\nTry Again")
else:
    print("The option entered is not from the option\nTry Again")