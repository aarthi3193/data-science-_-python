
# coding: utf-8

# In[1]:


my_list = [1,2,3,4,5,6,7,8]
print(my_list)


# In[2]:


my_list[1]


# In[6]:


for i in my_list:
    print (i)
    


# In[10]:


for i in my_list: 
    print (i*2)


# In[12]:


for i in my_list: 
    print (i*i)


# In[15]:


#my_list = [1,2,3,4,5,6,7,8]
#odd_list = [1,3,5,7]
#even_list = [2,4,6,8]
even_list = []
odd_list = []
for i in my_list:
    if (i%2 == 0):
        even_list.append(i)
    else: 
        odd_list.append(i)
print (even_list)
print (odd_list)
    


# In[17]:


my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
list_div_3 = [ ]
list_div_4 = [ ]
list_div_5 = [ ]
other = []
for i in my_list:
    if (i%4 == 0):
        list_div_4.append(i)
    elif (i%5 == 0): 
        list_div_5.append(i)
    elif (i%3 == 0):
        list_div_3.append(i)
    else:
        other.append(i)
print (list_div_5)
print (list_div_4)
print (list_div_3)
print (other)

        


# ### FUNCTIONS
# 

# In[22]:


def my_add_function(a,b):
    return(a+b)
p1 = my_add_function (10,20)
print (p1)
p2 = my_add_function (20.2,100.5)
print(p2)


# In[27]:


def my_mult_function(x,y):
    mult = x*y
    print (mult)
    return(x*y)


    


# In[29]:


p4 = my_mult_function(10,10)
print (p4)

