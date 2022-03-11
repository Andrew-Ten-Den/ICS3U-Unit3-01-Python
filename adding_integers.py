#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: March 11 2022
# This program calculates the sum of two integers


def main():
    # This program calculates the sum of two integers

    # input
    integer1 = int(input("Enter first integer: "))
    integer2 = int(input("Enter second integer: "))

    # process
    total = integer1 + integer2

    # output
    print("")
    print("{} + {} = {}".format(integer1, integer2, total))
    print("")
    print("Done")


if __name__ == "__main__":
    main()
