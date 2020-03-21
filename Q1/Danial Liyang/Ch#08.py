#!/usr/bin/env python
# coding: utf-8

# In[2]:


# *8.1 (Check SSN) Write a program that prompts the user to enter a Social Security
# number in the format ddd-dd-dddd, where d is a digit. The program displays
# Valid SSN for a correct Social Security number or Invalid SSN otherwise.
ssn = input("Enter SSN (format ddd-dd-dddd)")
if ssn[0:2].isdigit and ssn[3] == '-' and ssn[6] == '-' and ssn[4:5].isdigit and ssn[7:10].isdigit:
    print("OK")
else:
    print("No OK !")


# In[30]:


# **8.2 (Check substrings) You can check whether a string is a substring of another string
# by using the find method in the str class. Write your own function to implement
# find. Write a program that prompts the user to enter two strings and then checks
# whether the first string is a substring of the second string.
def find(string,subString):
    gap  = len(subString)
    x = 0
    while x < len(string):
        y = x + gap
        if string[x:y] == subString:
            return True
        x += 1
    return False
string = "Waleed Butt Son of Amer Butt"
subString = "Butt"
print(find(string,subString))


# In[27]:


# **8.3 (Check password) Some Web sites impose certain rules for passwords. Write a
# function that checks whether a string is a valid password. Suppose the password
# rules are as follows:
# ■ A password must have at least eight characters.
# ■ A password must consist of only letters and digits.
# ■ A password must contain at least two digits.
# Write a program that prompts the user to enter a password and displays valid
# password if the rules are followed or invalid password otherwise.
def isValid(password):
    digits = 0
    if len(password) < 8:
        return False
    for i in password:
        if not ((ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57)):
            return False
        if (ord(i) >= 48 and ord(i) <= 57):
            digits += 1
    return digits >= 2
print(isValid("abcdefgh34"))


# In[35]:


# **8.5 (Occurrences of a specified string) Write a function that counts the occurrences of a
# specified non-overlapping string s2 in another string s1 using the following header:
# def count(s1, s2):
# For example, count("system error, syntax error", "error") returns
# 2. Write a test program that prompts the user to enter two strings and displays the
# number of occurrences of the second string in the first string.
def count(string,subString):
    gap  = len(subString)
    x = 0
    count = 0
    while x < len(string):
        y = x + gap
        if string[x:y] == subString:
            count +=1
        x += 1
    return count
string = "Waleed Butt Son of AmerButt"
subString = "Butt"
print(count(string,subString))


# In[ ]:




