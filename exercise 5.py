#!/usr/bin/env python
# coding: utf-8

# In[318]:


#-------------------------------------------------------------------------------

#importing the libreries

import numpy as np
import pandas as pd
import csv
import collections

#----------------------------------------------------------------------------------

#read the text file

data_file1 = np.loadtxt(r"C:\Users\renji\OneDrive\Documents\exercise 5 datafile.txt",skiprows=1,dtype =int)
data_file2 = np.genfromtxt(r"C:\Users\renji\OneDrive\Documents\exercise 5 datafile.txt", delimiter=" ", max_rows = 1, dtype=int)

#-----------------------------------------------------------------------------------

#calculating the no of students and marks

n = data_file2[0]                 #no of students
Course_Mrk = (data_file2[1]/100)
Exam_Mrk = 1- Course_Mrk

#-----------------------------------------------------------------------------------

#creating the 2 arrays

n_array_1=np.array([[0,0,0,0]]*n)
n_array_2 = np.array([[int,int,int,int,str]]*n)

#-----------------------------------------------------------------------------------

#creating the 2D and 1d array

for i in range(0,n):
        Raw_Data = data_file1[i]
        Exam = Raw_Data[1]*Exam_Mrk
        course = Raw_Data[2]*Course_Mrk       
        Ovrl_Mrk = round(Exam + course)
        for j in range(0,3):
            array_1[j] = Raw_Data[j]
            array_1[3] = Ovrl_Mrk
            n_array_1[i] =array_1  #2D -ARRAY
            
            clas_s = ' '
            if Raw_Data[1] < 40 or Raw_Data[2] < 40:
                clas_s = 'failed'
            elif 40 <= Ovrl_Mrk <=49:        # Condition for grades
                clas_s = 'Third class'
            elif 50 <= Ovrl_Mrk <=69:
                clas_s = 'second class'
            else:
                clas_s = 'first class'
            for s in range(0,3):
                array_2[s] = Raw_Data[s]
                array_2[3] = Ovrl_Mrk
                array_2[4] = clas_s
                n_array_2[i] =array_2 

#--------------------------------------------------------------------

#sorting the array and store as one dimentional array
sorted_array_2 =n_array_2[n_array_2[:,3].argsort()]
sorted_1D_array_2 = sorted_array_2.flatten()        #1D ARRAY

#---------------------------------------------------------------------

#writng output in a txt file

f = open("OutputTextFile.txt", 'w')
print(sorted_1D_array_2, file=f)

#----------------------------------------------------------------------

#calculating the no of students in each grades

clss_lst=[]
def class_count():
    '''calculating the no of students in each grades'''
    
    for raw in range(0,n):
        clss_lst.append(sorted_array_2[raw][4])
    

    counter=collections.Counter(clss_lst)
    print('The no of students in each grades')
    print(counter,'\n')
    return

class_count()

#----------------------------------------------------------------------

#printing the register no of failed students

df = pd.DataFrame(n_array_2,columns =['register no','exam mark','course work','overral','grade'])
df2= df.loc[df['grade'] == 'failed', 'register no']
df_reg = df2.to_string(index=False)
print('The registration numbers of the students who have failed.','\n')
print(df_reg)
    
    
#-------------------------------------------------------------------------

#End

#---------------------------------------------------------------------------
  



# #array_1 = data_file.read().splitlines()
# #print(array_0)
# #array2 =np.array(['',0,0,0,0,]*n)
# #print(array2)
# 
# #print(data_file.read())
# array_0 = data_file.read().splitlines()
# print(array_0)
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




