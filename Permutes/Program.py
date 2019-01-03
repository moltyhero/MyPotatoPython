# coding=utf-8
import itertools


def permNum():
    num = input("Enter number")
    while num < 2:
        num = input("Enter number bigger than 1")
    permutes = list(itertools.permutations(range(1, num + 1), num))
    sum = len(permutes)

    for i in range(len(permutes)):
        for x in range(num-1):
            if permutes[i][x] + permutes[i][x+1] <= num:
                sum -= 1
                break

    print sum
    print permutes

def max2():
    far2 = False
    isOK = True
    count = 0
    num = input("Enter number")
    test = range(1, num + 1)
    permutes = list(itertools.permutations(range(1, num+1), num))
    for i in range(len(permutes)):
        for x in range(num):
            if abs(permutes[i][x] - x)-1 > 1:
                if not far2:
                    far2 = True
                else:
                    isOK = False
        if isOK:
            count += 1
        isOK = True

    print count

def main():
    permNum()


if __name__ == '__main__':
    main()
