# coding: utf-8
# Python Program to Reverse a Number using While loop
number = -123
orig_num=number
reverse = 0
if(number < 0):
   number = abs(number)
while(number !=0):
 reminder = number %10
 reverse = (reverse *10) + reminder
 number = number //10
if(orig_num < 0):
 print("\n Reverse of entered number is = %d" %(0-reverse))
else:
 print("\n Reverse of entered number is = %d" %reverse)

 #Note: if u can use strings, then convert the number as string and do [::-1] and convert back to int.