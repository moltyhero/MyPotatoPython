# coding=utf-8
import math

# חיבור +
def add():
    x = int(input("Enter 1st Number"))
    y = int(input("Enter 2nd Number"))
    return x + y

# חיסור -
def dec():
    x = int(input("Enter 1st Number"))
    y = int(input("Enter 2nd Number"))
    return x - y

# כפל *
def multiply():
    x = int(input("Enter 1st Number"))
    y = int(input("Enter 2nd Number"))
    return x * y


# חילוק /
def devide():
    x = int(input("Enter 1st Number"))
    y = int(input("Enter 2nd Number"))
    if y != 0:
        return x / y

# נוסחת שורשים
def qEquation():
    a = int(input("Enter a"))
    b = int(input("Enter b"))
    c = int(input("Enter b"))


    if a != 0:
        num1 = (b + math.sqrt(b * b - 2 * a * c)) / 2 * a
        num2 = (b - math.sqrt(b * b - 2 * a * c)) / 2 * a
        return (num1, num2)
    else:
        return "Error"

# חישוב נגזרת
def derivative():
    pol = input("Enter polynom")
    temp1 = pol.split('+', '-')
    for i in temp1:
        temp2 = i.split('^')
        temp2

# חישוב עצרת
def factorial():
    x = int(input("Enter Number"))
    sum = 1
    for i in range(2, x+1, 1):
        sum *= i

    return sum

# חישובי שטח
def space():
    return 9

# חישוב מהירות
def speed():
    return 0

# חישוב תאוצה
def acceleration():
    return 0

def main():
    selection = int(input("Enter selection"))

    if selection == 1:
        print add()
    elif selection == 2:
        print dec()
    elif selection == 3:
        print multiply()
    elif selection == 4:
        print devide()
    elif selection == 5:
        print dec()
    elif selection == 6:
        print qEquation()
    elif selection == 7:
        print derivative()
    elif selection == 8:
        print factorial()
    elif selection == 9:
        print space()
    elif selection == 10:
        print speed()
    elif selection == 11:
        print  acceleration()


if __name__ == '__main__':
    main()
