#!/usr/bin/env python
# coding: utf-8

# In[5]:


#-----------------------------------------------

#Write a function that takes a string as a parameter and returns True if and only if the string is a palindrome

#---------------------------------------------------


def pali_ndrome(string):      
    
    '''Takes a string and returns true if it is 
        palindrome'''
    
    if string == string[::-1]:
        return True       
    else:
        return False
       
pali_ndrome('arora')            


#--------------------------------------------------


# In[42]:


#---------------------------------------------
#Write a function that takes a string as a parameter, converts the string to upper-case
#and returns the most frequent letter/digit.

#------------------------------------------------

def string(s):
    
    '''Takes a string and returns the most frequent
        letter/digit'''
    
    upper_case = s.upper() #converting to upper case
    print(upper_case)
    
    convrt_list = list(upper_case)   #counverting to list
    digits =[]
    letters = []
    for i in convrt_list:       
        if i.isdigit():               #creating a list of the digits
            digits.append(i)       
        elif i.isalpha():             #creating a list of the letters
            letters.append(i)
        else:                         #ignore anything else other than letters and digitd
            continue
            
    if digits == []:                  
        print('No digits found')
    else:
        mst_cmndigit = max(digits, key = digits.count)
        print('most frequent digit is: ',mst_cmndigit)
        
        
    if letters == []:
        print('All are numbers,No letters found')
    else:
        mst_comnlettr = max(letters, key = letters.count)
        print('most frequent letter is: ',mst_comnlettr)
    return 
    
string('we**r44 hdfhgr 35 gt6y h ')


#----------------------------------------------------------------


# In[40]:


#----------------------------------------------------------------
#Write a function that takes a string as a parameter, counts the number of letters,
#digits, and spaces in the string and returns a tuple containing the three counts.

#------------------------------------------------------------------

def string(s):
    
    '''Takes a string and and returns the no
        of digits/letter/space'''
    
    upper_case = s.upper()    #converting to upper case
    print(upper_case,'\n')
    
    
    convrt_list = list(s)     #counverting to list
    digits =[]
    letters = []
    for i in convrt_list:        #creating a list of the digits
        if i.isdigit():
            digits.append(i)       
        elif i.isalpha():        #creating a list of the letters
            letters.append(i)
        else:
            continue 
            
    no_of_lettr = len(letters)   #counting the letters
    no_of_digits = len(digits)   #counting the digits
    no_of_space = s.count(' ')   #counting the space
    
    
    
    tuple_format= (('Letter :',no_of_lettr),      #creating a tuple  format       
                   ('Digit :',no_of_digits),
                   ('Space: ',no_of_space))    
    print(tuple_format)   
    return
    
string('ffvfv web456fger r erfur;rf')

#----------------------------------------------------------

