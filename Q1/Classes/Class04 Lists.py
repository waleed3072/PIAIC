dir(list)

names = ["Waleed","Butt","Hamza",7,4,3]
print(names)

check = True
record = []
while(check):
    name = input("Enter Student Name: ")
    fname = input("Enter Father Name: ")
    contact = input("Enter Contact Number: ")
    record.append("Name: "+name+" Father Name: "+fname+" Contact: "+contact)
    inp = input("Enter More Record?\nEnter Y to add ")
    if inp == "Y":
        continue
    else:
        check=False
print(record)

i = 1000
while(i>=990):
    print(i)
    i -=1
for i in range(1000,989,-1):
    print(i)

j=48
for i in range(65,91,1):
    print(chr(i)+" "+chr(i+32)+" "+chr(j))
    j +=1
    if(j == 57):
        j = 48

inp = eval(input("Enter Number: "))
for i in range (1,11,1):
    for j in range (1,(inp+1),1):
        print("{} X {} = {}".format(j,i,i*j),end="\t")
    print()


matrix = [[2,5,9],[8,9,10],[20,30,27],[35,9,20]]

for i in range(0,3,1):
    for j in range(0,3,1):
        if matrix[i][j] % 5 == 0:
            print("{}\tis on Row {} Column {}".format(matrix[i][j],(i+1),(j+1)))

for i in range(1,1001,1):
    if i%5==0 and i%7==0 and i%20==0:
        print(i,end=" ")

inp = input("You go to a gorgeous girl and say Marry Me: ")
if inp == "yes":
    print("Direct Marketig")
else:
    inp = input("Your friend went to a gorgeous girl and said Marry Him: ")
    if inp == "yes":
        print("Advertising")
    else:
        inp = input("Gorgeous girl walks to you and said Marry Me: ")
        if inp == "yes":
            print("Brand Recognition")
        else:
            inp = input("You went to a gorgeous girl and said Marry Him and She slaps: ")
            if inp == "yes":
                print("Customer Feedback")
            else:
                inp = input("You say to gorgeous girl Marry Him and Her husband comes: ")
                if inp == "yes":
                    print("Demand and supply")
                else:
                    inp = input("Your wife came before all this: ")
                    if inp == "yes":
                        print("Interruption")
                    else:
                        print("Something must have happened")