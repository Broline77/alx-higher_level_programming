#!/usr/bin/python3
i = "Fizz"
n = "Buzz"


def fizzbuzz():
    for number in range(1, 101):
        if (number % 3 and number % 5):
            print("%s%s" % (i, n), end=' ')
        elif (number % 3):
            print("%s" % (i), end=' ')
        elif (number % 5):
            print("%s" % (n), end=' ')
        else:
            print("%d" % (number), end=' ')
