#!/usr/bin/env python
# coding: utf-8

# In[70]:


#---------------------------------------------------

#Write a function that returns a list of all non-prime numbers between two positive integers
#supplied as arguments. 

#............................................................


FirstNumber = input('enter the first whole no: ')
SecondNumber = input('enter the second whole no: ')

FirstNumber_check= FirstNumber.strip().isdigit()      #checking the numbers are integer or not
SecondNumber_check= SecondNumber.strip().isdigit()    

if FirstNumber_check == False or SecondNumber_check == False:
    print('\n','Enter Two Positive Integers ')
else:    
    num_1= int(FirstNumber)
    num_2 = int(SecondNumber)

    if (num_1 or num_2) <= 0:                         #checking the nos are positive orr not
        print('\n','Enter Two Positive Integers')
 
#----------------------------------------------------------

    elif num_1 > num_2:                               
        Largest_No = num_1                            #finding the largest no
        Smallest_No = num_2
    else:
       Largest_No = num_2
       Smallest_No  = num_1
        
#-------------------------------------------------------------

    def NotPrime(num_1, num_2):   
        
            '''Takes two positive integers and print all
                               non prime nos b/w them'''
            
            list = []
            Second_list=[]
            for i in range(Smallest_No, Largest_No + 1):
                for j in range(2, i):
                    if (i % j == 0):
                       list.append(i)
                       break            
            for n in range(0,len(list),10):
                Second_list.append(list[n:n+10])
                
            print('\n'.join(map(str, Second_list)))  
            return 
        
    NotPrime(num_1,num_2)
    
    
#-----------------------------------------------------------------
       
        

