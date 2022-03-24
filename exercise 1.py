#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#------------------------------------------------------------------------------------

#importing datetime

from datetime import datetime

my_dob = input('Enter date of birth in the format mm/dd/yyyy : ') #input date
print('\n')

check = True
try:
    Req_format = '%m/%d/%Y'
    Format_date = datetime.strptime(my_dob,Req_format)   
    Today_Date = datetime.today()
    Age_ = Today_Date.year - Format_date.year - ((Today_Date.month, Today_Date.day) < (Format_date.month, Format_date.day))
    
    #dob_Eu = (Format_date.day,'/',Format_date.month,'/',Format_date.year)
    dob_Eu = datetime.strptime(my_dob,Req_format).strftime('%d/%m/%Y')  #changing the date format
    
    print('The DOB in EU format ; ',dob_Eu)
    print('The age of the person as on Today is: ',Age_)
    
except ValueError:
    check = False
    print('Enter the DOB in the req format')
    
#----------------------------------------------------------------------------------------

