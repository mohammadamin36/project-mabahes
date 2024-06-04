#!/usr/bin/env python
# coding: utf-8

# In[1]:


age=int(input("سال تولد خود را به شمسی وارد کنید "))
month=int(input("ماه تولد خود را به شمسی وارد کنید "))
day=int(input("روز تولد خود را به شمسی وارد کنید "))
birth=int(age*365.25)+month*30+day
tuday=(int(1403*365.25))+(3*31)+(15)
print("تعداد روز های زندگی شما:", tuday-birth)


# In[ ]:




