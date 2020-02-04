lines = int(input("Enter number of lines: "))

for i in range(0, lines, 1):
    for j in range(lines, 1, -1):
        print(" ", end=" ")

    for j in range(i + 1, 1, -1):
        print(j, end=" ")

    print("1", end=" ")

    for j in range(2, i + 2, 1):
        print(j, end=" ")
    lines -= 1
    print()

# Enter number of lines: 11
#                     1
#                   2 1 2
#                 3 2 1 2 3
#               4 3 2 1 2 3 4
#             5 4 3 2 1 2 3 4 5
#           6 5 4 3 2 1 2 3 4 5 6
#         7 6 5 4 3 2 1 2 3 4 5 6 7
#       8 7 6 5 4 3 2 1 2 3 4 5 6 7 8
#     9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9
#   10 9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9 10
# 11 10 9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9 10 11

print("Patter A")

for i in range(1,7,1):
    for j in range(1,i+1,1):
        print(j,end=" ")
    print()
# Patter A
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# In [6]:
print("Patter B")

for i in range(6,0,-1):
    for j in range(1,i+1,1):
        print(j,end=" ")
    print()
# Patter B
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# In [10]:
print("Patter C")

for i in range(1,7,1):
    for j in range(7,i,-1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
# Patter C
#             1
#           2 1
#         3 2 1
#       4 3 2 1
#     5 4 3 2 1
#   6 5 4 3 2 1

# (Display prime numbers between 2 and 1,000) Modify Listing 5.13 to display all
# the prime numbers between 2 and 1,000, inclusive. Display eight prime numbers
# per line.
def isPrime(i):
    for j in range(2,(i//2)+1):
        if i % j == 0:
            return False
    return True
for i in range(2,1001):
    if isPrime(i):
        print(i,end=" ")

# 2 3 5 7 11 13 17 19 23 29 31 

# In[17]:


# (Find the factors of an integer) Write a program that reads an integer and displays
# all its smallest factors, also known as prime factors. For example, if the input integer
# is 120, the output should be as follows:
# 2, 2, 2, 3, 5
inp1 = int(input("Enter an Integer: " ))
l1 = []
while inp1 > 1:
    
    for i in range(2,inp1+1):
        if inp1 % i == 0:
            break
    print("{} | {}\n___________".format(i,inp1))
    l1.append(i)
    inp1 //= i

print(l1)


# In[11]:


# (Demonstrate cancellation errors) A cancellation error occurs when you are
# manipulating a very large number with a very small number. The large number
# may cancel out the smaller number. For example, the result of 100000000.0 +
# 0.000000001 is equal to 100000000.0. To avoid cancellation errors and obtain
# more accurate results, carefully select the order of computation. For example, in
# computing the following series, you will obtain more accurate results by computing
# from right to left rather than from left to right:
# 1 +1/2 +1/3 + .... +1/n
# Write a program that compares the results of the summation of the preceding
# series, computing both from left to right and from right to left with n 50000.
inp1 = int(input("Enter an Integer: " ))
r=0
for i in range(inp1,0,-1):
    r+=1/i
print("Right to left: ",r)
r=0
for i in range(1,inp1,1):
    r+=1/i
print("Left to right: ",r)


# In[12]:


# (Sum a series) Write a program to sum the following series:
# 1/3 +3/5 +5/7 +7/9 +9/11 +11/13 + .... + 95/97 +97/99
inp1 = int(input("Enter an Integer: " ))
r=0
for i in range(1,inp1+1,2):
    r+=i/(i+2)
print(r)


# In[26]:


# (Compute ) You can approximate by using the following series:
# p = 4(1 -1/3 + 1/5 - 1/7 + 1/9 -1/11 + .... + (-1)i+1/2i - 1)
inp1 = int(input("Enter Accuracy Limit: " ))
r=0
for i in range(inp1,0,-1):
    r += ((-1)**(i+1))/((2*i)-1)
r *= 4
print("Pie is: ",r)


# In[39]:


# **5.30 (Display the first days of each month) Write a program that prompts the user
# to enter the year and first day of the year, and displays the first day of each month
# in the year on the console. For example, if the user entered year 2013, and 2 for
# Tuesday, January 1, 2013, your program should display the following output:
# January 1, 2013 is Tuesday
# ...
# December 1, 2013 is Sunday
def getDay(number):
    number %= 7
    if number == 0:
        return "Sunday"
    elif number == 1:
        return "Monday"
    elif number == 2:
        return "Tuesday"
    elif number == 3:
        return "Wednesday"
    elif number == 4:
        return "Thursday"
    elif number == 5:
        return "Friday"
    else:
        return "Saturday"
def getMonth(number):
    number %= 12
    if number == 0:
        return "January"
    elif number == 1:
        return "February"
    elif number == 2:
        return "March"
    elif number == 3:
        return "April"
    elif number == 4:
        return "May"
    elif number == 5:
        return "June"
    elif number == 6:
        return "July"
    elif number == 7:
        return "Augest"
    elif number == 8:
        return "September"
    elif number == 9:
        return "October"
    elif number == 10:
        return "Novemer"
    else:
        return "December"

inp0 = int(input("Enter Starting Year: " ))
inp1 = int(input("Enter Ending Year: " ))
inp2 = int(input("Enter Day\n(0->Sunday,6->Saturday): " ))
l1 = [0,2,4,6,7,9,11]

for year in range(inp0,inp1+1,1):
    for i in range(12):
        print("{} 1 of {} is {}".format(getMonth(i),year,getDay(inp2)))
        if i == 1:
            if inp1 % 4 == 0:
                inp2 += 28
            else:
                inp2 += 27
        elif i in l1:
            inp2 += 31
        else:
            inp2 +=30


# In[79]:


# **5.31 (Display calendars) Write a program that prompts the user to enter the year
# and first day of the year, and displays on the console the calendar table for the
# year. For example, if the user entered year 2005, and 6 for Saturday, January 1,
# 2005, your program should display the calendar for each month in the year, as
# follows:
inp0 = int(input("Enter Starting Year: " ))
inp1 = int(input("Enter Ending Year: " ))
inp2 = int(input("Enter Day\n(0->Sunday,6->Saturday): " ))

for year in range(inp0,inp1+1,1):
    for i in range(12):
        s = str(getMonth(i))+" "+str(year)
        print(s.center(20))
        print("--------------------")
        print("Su Mo Tu We Th Fr Sa")
        print("--------------------")
        
        counter=0
        for j in range(inp2):
            counter+=1
            print("{:>2s}".format(" "),end=" ")
        limit=0
        if i == 1:
            if inp1 % 4 == 0:
                limit= 29
            else:
                limit= 28
        elif i in l1:
            limit= 31
        else:
            limit=30
        inp2= (inp2+limit)%7    
        for j in range(1,limit+1,1):
            print("{:>2s}".format(str(j)),end=" ")
            counter+=1
            if counter == 7:
                counter=0
                print()
        print("\n--------------------")


# In[85]:


# **5.35 (Perfect number) A positive integer is called a perfect number if it is equal to the
# sum of all of its positive divisors, excluding itself. For example, 6 is the first perfect
# number, because The next is
# There are four perfect numbers less than 10,000. Write a program to find these
# four numbers.
def getDivisors(number):
    l1=[]
    for i in range(1,(number//2)+1,1):
        if number % i == 0:
            l1.append(i)
    return l1
def isPerfect(number):
    s=0
    divisors = getDivisors(number)
    for i in divisors:
        s +=i
    return number==s
for i in range(1,10001):
    if isPerfect(i):
        print("{} is perfect (Divisors {})".format(i,getDivisors(i)))


# In[86]:


8128/4064


# In[94]:


# ***5.36 (Game: scissor, rock, paper) Programming Exercise 4.17 gives a program that
# plays the scissor, rock, paper game. Revise the program to let the user play continuously
# until either the user or the computer wins more than two times.
from random import randint
def rockPaperSccissor(number):
    if number == 1:
        return "Rock"
    elif number == 2:
        return "Papers"
    elif number == 3:
        return "Scissors"
    else:
        return None
while True:
    inp1 = int(input("Enter your choice\n1:Rock\n2:Papers\n3:Scissors\n0:Quit\n-> "))
    if inp1 == 0:
        break
    if inp1 > 3:
        print("Wrong Choice enter 1,2,3 only!!")
        continue
    compChoice = randint(1,3)
    if compChoice == inp1:
        print("Draw {}".format(rockPaperSccissor(inp1)))
    elif (compChoice == 1 and inp1 == 3) or (compChoice == 2 and inp1 == 1) or (compChoice == 3 and inp1 == 2):
        print("Computer Won\nCPU={},You={}".format(rockPaperSccissor(compChoice),rockPaperSccissor(inp1)))
    else:
        print("You Won\nCPU={},You={}".format(rockPaperSccissor(compChoice),rockPaperSccissor(inp1)))    


# In[96]:


# *5.38 (Simulation: clock countdown) You can use the time.sleep(seconds) function
# in the time module to let the program pause for the specified seconds. Write a
# program that prompts the user to enter the number of seconds, displays a message
# at every second, and terminates when the time expires. Here is a sample run:
# Enter the number of seconds:
# 2 seconds remaining
# 1 second remaining
# Stopped
import time
inp1 = int(input("Enter Time in seconds:"))
for i in range(inp1-1,-1,-1):
    print(i)
    time.sleep(1)
print("Program Terminated")


# In[ ]:




