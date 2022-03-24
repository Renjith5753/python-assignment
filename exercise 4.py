#!/usr/bin/env python
# coding: utf-8

# In[88]:


#importing all libraries

#--------------------------------------------------
import csv
from pathlib import Path
import sys
from tabulate import tabulate
#---------------------------------------------------

#input datafile fron the user

DataFile = str(input('Enter the file path'))
print('\n')

paths = Path(DataFile)
if paths.is_file():
    print('file found')
    print('\n')
    
else:
    print('Please Enter a Vailid File path') #exit program if the file not found
    sys.exit()
    
#------------------------------------------------------    

#Reading the file and display as list of tuples
    
with open(DataFile) as f1:
    ListOfTuples=[tuple(line) for line in csv.reader(f1)]
print(ListOfTuples,'\n')

#------------------------------------------------------

#Input the cutoff salary from the user

Cut_Off_Salary = int(input('enter the cutoff salary : '))
print('The Cutoff salary is :  ',Cut_Off_Salary)
print('\n')

#-------------------------------------------------------


def cut_off(data,salary):
    
    '''function that takes 2 arguments, a list of
           tuples and a integer denoting a salary'''
    
    Ran_dom = ((int(salary),Name,Title) for salary, Name,Title in ListOfTuples)
    list_ele = []
    for j in Ran_dom:                             #creating a list with elements having salary above cutoff value                   
        if j[0] >= Cut_Off_Salary:
            list_ele.append(j[0:3])        
    if list_ele == []:
        print('Data not found for the given cutoff salary')
    else:
        SortedList = sorted(list_ele, key=lambda tup: tup[0],reverse=True)     #sorting the list based on the salary
        print('Employees that have salary above the given value: ', '\n')
        print(tabulate(SortedList,headers=['Salary', 'Name','Job Title'], tablefmt='orgtbl')) 
        print('\n')
    print('Do you wishes to quit or to supply the name of another department??')
        
    return 
cut_off(data,salary)


#End
#---------------------------------------------------------------------------
    


# In[ ]:





# In[ ]:


C:\Users\renji\OneDrive\Documents\python dataset.csv

