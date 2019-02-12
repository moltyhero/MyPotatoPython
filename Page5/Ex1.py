def get_max_group_members(multiplier1, multiplier2):
    while True:
        num = input("Enter number from 2 to 10,000\n")
        if 2 <= num <= 10000:
            break

    my_group = range(1, num+1)  # type: List[int]

    if multiplier1 != 0:
        for x in range((num - 1) / multiplier1):
            my_group[(my_group[x] * multiplier1)-1] = 0

    if multiplier2 != 0:
        for x in range((num - 1) / multiplier2):
            my_group[(my_group[x] * multiplier2)-1] = 0

    str1 = ""
    for x in range(num):
        if my_group[x] != 0:
            str1 += str(my_group[x]) + ","

    print str1


def main():
    get_max_group_members(2, 0)
    print ""
    get_max_group_members(2,3)


if __name__ == '__main__':
    main()
