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