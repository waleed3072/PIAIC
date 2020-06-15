# Task 1
grade = int(input("Enter Grade: "))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("E")

# Task 2
dayRented = input("Enter the Day on which DVD is rented: ")
daysKept = int(input("Enter the days customer kept the DVD: "))
time = input("Enter the time at which DVD is returned (HH AM/PM): ")
condition = input("Was the DVD scratched? (Y/N): ")
# Checking Time for return
if time[-2:-1] == "P" and int(time[0:2]) >= 8:
    daysKept += 1
# Calculating bill
bill = daysKept * 1.59
# Discount and Extra Charge for Damage
if condition == "Y":
    bill += 1
if dayRented == "Sunday":
    if condition == "Y":
        bill += 1
    bill -= bill * 0.3
elif dayRented == "Thursday":
    bill -= bill * 0.5

print("The bill is: {:.2f} $".format(bill))

# Task 3
list1 =[]
for i in range(0,10,1):
    list1.append(int(input("Enter number {} : ".format(i+1))))
i=0
while i<len(list1):
    if list1[i] == 6:
        print("Index = {}".format(i))
        break
    i +=1
if (i == len(list1)):
    print("Not Found")

# List of Dictionaries of List and Dictionaries
# In [10]:
l1=[
        {"name":"Waleed",
         "Marks":{"math":30,"english":80,"phy":80},
         "hobbies": ["cricket","book reading"]
        },

        {"name":"Bilal",
         "Marks":{"math":45,"english":89,"phy":70},
         "hobbies": ["painting","traveling"]
        }
    ]
print(l1)