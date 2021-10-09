#!/usr/bin/env python
# coding: utf-8

# # Series -- what it is?

# In[6]:


import numpy as np
import pandas as pd
from pandas import DataFrame, Series

get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


s3 = Series({'Orange':100, 'Kiwi':99 })
s3


# In[27]:


my_dict = {'Orange':100, 'Kiwi':99, 'banana':78.5, 'tomoto':34 }
s4 = Series(my_dict)


# In[19]:


s3 + s4


# # Random variables

# In[21]:


my_rv = np.random.random(20)


# In[23]:


s5 = Series(my_rv)
s5


# In[28]:


s6 = Series(my_dict)
s6


# In[30]:


s6["tomoto"]


# In[32]:


my_indexes = [1,3]


# In[34]:


s6[my_indexes]


# # Dates
# 

# In[45]:


s7 = pd.date_range("August 17, 2021","8/23/2021")
s7


# In[41]:


temperatures = [67,23,103,58,12,100,45]


# In[43]:


s9 = Series(temperatures,index = pd.date_range("August 17, 2021", "8/23/2021"))
s9


# In[44]:


s9["August 21, 2021"]


# In[46]:


s9.median()


# In[47]:


s9.mean()


# ### Things to remembers 
# - Function call () - use paranthesis
# - pandas  to access an index [] - square brackets
# 

# In[48]:


s9.describe()


# # Data frame

# In[49]:


College_df = pd.read_csv('Colleges.csv')


# In[50]:


College_df


# In[51]:


type(College_df)


# In[52]:


College_df.columns


# In[53]:


s10 = College_df['College']
s10


# In[106]:


my_columns = ['College','Pell grad share']
type(my_columns)


# In[132]:


new_df = DataFrame(College_df['College'],College_df['Pell grad share'])
new_df


# In[95]:


boolen_selection = College_df["Pell grad share"] > 31


# In[97]:


College_df.loc[boolen_selection,["College","Freshman class"]]


# In[120]:


toPlot = College_df.loc[College_df["Freshman class"] == "1,500",]


# In[123]:


import matplotlib.pyplot as plt 
plt.plot(College_df["College"],College_df["Freshman class"])


# In[56]:


# File we seleted for practice
new_csv = pd.read_csv('softball.csv')


# In[57]:


new_csv.columns


# In[58]:


new_csv


# In[59]:


one_col = new_csv['Hits'] #to only see one column


# In[133]:


one_col.max() # hiighest number in column


# In[61]:


one_col.min()


# In[63]:


one_col.isna()


# In[65]:


new_csv['Total'] = new_csv['Hits'] + new_csv['Run']


# In[71]:


new_csv.sort_values('Total')


# In[85]:


new_csv[10:] #to print rows from 10


# In[134]:


new_csv.loc[new_csv["Run"]>10,] #for specific condition to get all the values where Run is greter than 10


# In[90]:


new_csv['Errors'].max()


# In[138]:


#for i in new_csv['Errors']:
 #   if i>4:
  #      print('All the errors greater than )

errors_morethan_4 = new_csv['Errors'] >4
type(errors_morethan_4)


# In[142]:


new_csv.loc[errors_morethan_4,['Game','Errors']]


# In[152]:


#To plot the dataframes
df = pd.DataFrame(new_csv,columns=['Game','Errors','Status'])
print (df)


# In[153]:


df.plot(x = 'Game', y ='Errors',kind = 'scatter' )


# In[154]:


df.plot(x = 'Game', y ='Errors',kind = 'line' )


# In[159]:


df.plot(x = 'Errors', y ='Status',kind = 'bar' )


# In[ ]:





# In[ ]:




