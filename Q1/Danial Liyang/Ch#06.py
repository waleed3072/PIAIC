# Question 6.3
def lengthOfInteger(number):
    count = 1
    i = 10
    while ((number - (number % i)) != 0):
        count += 1
        i *= 10
    return count


def palindrome(number):
    # Alternate Method
    # return int(str(number)[-1:-(len(str(number))+1):-1])
    list_1 = []
    i = 10
    j = 1
    x = 0
    while number != 0:
        mod = number % i
        list_1.append((mod // j))
        number -= mod
        i *= 10
        j *= 10
    j = 0
    for i in range(len(list_1), 0, -1):
        x += list_1[j] * (10 ** (i - 1))
        j += 1
    return x


print(palindrome(856348658976298375))

