# coding=utf-8
import math


# חיבור +
def add():
    x = int(input("Enter 1st Number\n"))
    y = int(input("Enter 2nd Number\n"))
    return x + y


# חיסור -
def dec():
    x = int(input("Enter 1st Number\n"))
    y = int(input("Enter 2nd Number\n"))
    return x - y


# כפל *
def multiply():
    x = int(input("Enter 1st Number\n"))
    y = int(input("Enter 2nd Number\n"))
    return x * y


# חילוק /
def divide():
    x = float(input("Enter 1st Number\n"))
    y = float(input("Enter 2nd Number\n"))
    if y != 0:
        return x / y


# נוסחת שורשים
def q_equation():
    a = int(input("Enter a\n"))
    b = int(input("Enter b\n"))
    c = int(input("Enter b\n"))

    if a != 0:
        num1 = (b + math.sqrt(b * b - 2 * a * c)) / 2 * a
        num2 = (b - math.sqrt(b * b - 2 * a * c)) / 2 * a
        return num1, num2
    else:
        return "Error"


# חישוב נגזרת
def derivative():
    pol = raw_input("Enter polynom\n")
    temp1 = pol.split('+')
    direct = ""
    print temp1
    for i in temp1:
        temp2 = i.split('^')
        direct += temp2[1]
        direct += temp2[0]
        direct += "^"
        direct += str(int(temp2[1]) - 1)
        direct += "+"

    return direct


# חישוב עצרת
def factorial():
    x = int(input("Enter Number\n"))
    total = 1
    for i in range(2, x+1, 1):
        total *= i

    return total


# חישובי שטח
def space():
    choice = input("Which shape do you want to get the space of?\n")
    if choice == "Rectangle":
        side = input("Enter 1 side\n")
        height = input("Enter the height to the side\n")
        return side*height
    elif choice == "Triangle":
        side = input("Enter 1 side\n")
        height = input("Enter the height to the side\n")
        return side * height / 2


# חישוב מהירות
def speed():
    distance = input("Enter distance\n")
    time = input("Enter time\n")
    return distance/time


# חישוב תאוצה
def acceleration():
    speed = input("Enter speed\n")
    time = input("Enter time\n")
    return speed * time


def main():
    selection = int(input("Enter selection\n"))

    while selection != -1:
        if selection == 1:
            print add()
        elif selection == 2:
            print dec()
        elif selection == 3:
            print multiply()
        elif selection == 4:
            print divide()
        elif selection == 5:
            print q_equation()
        elif selection == 6:
            print derivative()
        elif selection == 7:
            print factorial()
        elif selection == 8:
            print space()
        elif selection == 9:
            print speed()
        elif selection == 10:
            print acceleration()

        selection = int(input("Enter selection:"
                              "1 Add"
                              "2 Decrease"
                              "3 Multiply"
                              "4 Divide"
                              "5 quadratic equation"
                              "6 Directive"
                              "7 Factorial"
                              "8 Space"
                              "9 Speed"
                              "10 Acceleration\n"))


if __name__ == '__main__':
    main()
