#!/usr/bin/env python
# coding: utf-8

# In[58]:


#importing all this fun stuff
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[59]:


#plotting for problem 1c. 

#bounding function. always greater than PDF. 
g = 1.01
plt.axhline(y = g, color = 'r', label = 'Bounding Function')

#PDF
x = (0, .2, .4, .6, .8, 1, 1.2, 1.4)
p = np.sin(x)
plt.plot(x,p, label = 'PDF')

#piecewise function, CDF
plt.plot([0, .2],[.2, .2], color = 'g' , label = 'CDF')
plt.plot([.2, .4],[.4, .4], color = 'g')
plt.plot([.4, .6],[.6, .6], color = 'g')
plt.plot([0.6, .8],[.7, .7], color = 'g')
plt.plot([0.8, 1],[.84,.84], color = 'g')
plt.plot([1, 1.2],[.93, .93], color = 'g')
plt.plot([1.2, 1.4],[.98, .98], color = 'g')
plt.plot([1.4, 1.6],[1, 1], color = 'g')

plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Rejection Sampling')


# In[60]:


#Problem 3. 
import collections
from numpy.random import seed
from numpy.random import randint

seed(1)
InitialLocation = randint(0, 49, 100000)

seed(2)
FinalLocation = randint(0, 107, 100000)

Capture = collections.Counter(57 > FinalLocation)
Capture


# In[61]:


ForwardScatter = collections.Counter((InitialLocation - FinalLocation < 0)) - collections.Counter(FinalLocation < 5)  - collections.Counter(FinalLocation > 49)
ForwardScatter

