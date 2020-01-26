d1 = {'id':2,
     'name':"waleed",
     'course': 'A.I',
     'admission date':'2019-12-15',
      'DOB':'1998-10-01'
      }
print(d1)

d2 = {}
d2['id']=2
d2['name']="waleed"
d2['course']='A.I'
d2['admission date']='2019-12-15'
d2['DOB']='1998-10-01'
print(d1)

d3 = {}
d3["id"] = input("Enter Your id: ")
d3["name"] = input("Enter Your Name: ")
l1 =input("Enter Your Skills with ',': ")
d3["Skills"] = l1
print(d3.keys())

print(d3.values())

l1 = (d3.values())
print(l1)
# dict_values(['12312', 'waleed', '1231231,java,c++'])
# In[11]:
print(d3["Skills"][12])
# ,
# In[19]:
d4 = {}
d4["id"] = input("Enter Your id: ")
d4["name"] = input("Enter Your Name: ")
d4["Skills"] = ["Python"] + (input("Enter Your Skills with ',': ").split(','))
print(d4)
# Enter
# Your
# id: 123123
# Enter
# Your
# Name: waleed
# Enter
# Your
# Skills
# with ',': java, c + +, c, kotlin, assembly
# {'id': '123123', 'name': 'waleed', 'Skills': ['Python', 'java', 'c++', 'c', 'kotlin', 'assembly']}
# In[27]:
# d4["Skills"][0][0]
# Out[27]:
# 'P'
# In[29]:
d5 = d4
d5["id"] = "xyz"
print(d4)
print(d5)
# {'id': 'xyz', 'name': 'waleed', 'Skills': ['Python', 'java', 'c++', 'c', 'kotlin', 'assembly']}
# {'id': 'xyz', 'name': 'waleed', 'Skills': ['Python', 'java', 'c++', 'c', 'kotlin', 'assembly']}
# In[31]:
d5 = d4.copy()
d5["id"] = "abc"
print(d4)
print(d5)
# {'id': 'xyz', 'name': 'waleed', 'Skills': ['Python', 'java', 'c++', 'c', 'kotlin', 'assembly']}
# {'id': 'abc', 'name': 'waleed', 'Skills': ['Python', 'java', 'c++', 'c', 'kotlin', 'assembly']}
# In[35]:
l1 = ["Waleed", "Butt", "amer", "Butt", "Goes", "murree"]
d6 = dict.fromkeys(l1)
print(d6)
# {'Waleed': None, 'Butt': None, 'amer': None, 'Goes': None, 'murree': None}
# In[2]:
d7 = dict.fromkeys((input("Enter Values: ").split(',')), "NAN")
print(d7)
# Enter
# Values: waleed, qasim, ali, shehzad
# roy
# {'waleed': 'NAN', ' qasim': 'NAN', ' ali': 'NAN', ' shehzad roy': 'NAN'}
# In[8]:
print(dict.fromkeys((input("Enter Values: ").split(',')), (input("Enter Values: ").split(','))))
# Enter
# Values: waleed, tauheed, qasim, waleedagain, talal
# Enter
# Values: 1, 2, 4, 3, 4, 5, 6, 2
# {'waleed': ['1', '2', '4', '3', '4', '5', '6', '2'], 'tauheed': ['1', '2', '4', '3', '4', '5', '6', '2'],
#  'qasim': ['1', '2', '4', '3', '4', '5', '6', '2'], 'waleedagain': ['1', '2', '4', '3', '4', '5', '6', '2'],
#  'talal': ['1', '2', '4', '3', '4', '5', '6', '2']}
# In[14]:
l1 = ['a', 'b', 'c']
l2 = ['x', 'y', 'z']
d8 = dict(zip(l1, l2))
print(d8)
{'a': 'x', 'b': 'y', 'c': 'z'}
# In[16]:
print(dict(zip((input("Enter Keys: ").split(',')), (input("Enter Values: ").split(',')))))
# Enter
# Keys: afasd, fs, df, sd, f, sad, f, asd, f, s, df
# Enter
# Values: a, f, sdf, s, df, s, df, sad, f, sd, f
# {'afasd': 'a', 'fs': 'f', 'df': 'f', 'sd': 's', 'f': 'f', 'sad': 's', 'asd': 'sad', 's': 'sd'}
# In[19]:
#

def func1(a, b):
    try:
        print(a[b])
    except:
        print("No Key")


d9 = {"Python": "Beginner"}
func1(d9, "Java")
# No
# Value
# In[22]:
d10 = {'a': 1, 'c': 9, 'f': 11, 'g': 10, 'h': 13, 'q': 7}
l1 = list(d10.keys())
l2 = list(d10.values())
l1.sort()
l2.sort()
d10 = dict(zip(l1, l2))
print(d10)
# {'a': 1, 'c': 7, 'f': 9, 'g': 10, 'h': 11, 'q': 13}
# In[24]:


def func2(a, b):
    a[b] = "NEW"


d11 = {"Python": "Beginner"}
func2(d11, "Java")
print(d11)
# {'Python': 'Beginner', 'Java': 'NEW'}
# In[4]:
d12 = {'a': 1, 'c': 9, 'f': 11, 'g': 10, 'h': 13, 'q': 7}
keys = list(d12.keys())
key = 0
values = list(d12.values())
values.sort()
d13 = {}
for value in values:
    for j in keys:
        if d12[j] == value:
            key = j
    d13[key] = value

print(d13)