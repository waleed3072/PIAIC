#!/usr/bin/env python
# Converting any type of data into numbers is called Vectorization
# First step in Machine Learning
# Py auto GUI
# Selenium
# Filing
# File opening table
# --------------------------------------------------
#                           |r    r+  w   w+  a   a+
# --------------------------------------------------
# read                      |+    +       +       +
# write                     |     +   +   +   +   +
# write after seek          |     +   +   +
# create                    |         +   +   +   +
# turnacate                 |         +   +
# position at start         |+    +   +   +
# position at end           |                 +
# ---------------------------------------------------
file1 = open("abc1.txt")
li = list(file1)
print(li)
file1.close()
# In[2]:
# Write to a file
with open("abc1.txt","w+") as file0:
    for i in range(1,51):
        file0.write("New Line {}\n".format(i))
# In[3]:
# Read a file
with open("abc1.txt") as file2:
    print(file2.readline())
    print(file2.readlines())
# In[4]:
#append
with open("abc1.txt","a") as file0:
    for i in range(1,501):
        file0.write("Line {}\n".format(i))
# In[5]:
# Read a file
with open("abc1.txt") as file2:
    print(file2.readline())
    print(file2.readlines())
# In[31]:
# Write to a file
with open("task.txt","w+") as file0:
    file0.write("1\n2\n3\n")
    file0.write("A\nB\nC\n")
with open("task.txt") as file0:
    s1 = str(file0.read())
    l1 = list(s1)
    print(l1)
    l2 = [l1[0],l1[2],l1[4]]
    l3 = [l1[6],l1[8],l1[10]]
    l2.sort(reverse = True )
    l3.sort(reverse = True )
    l2 = l3 + l2
    print(l2)
    with open("task.txt","w+") as file1:
        for i in l2:
            file1.write(i+",")
# In[1]:
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from plt import image
