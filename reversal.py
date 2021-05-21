#!/usr/bin/env python3

# Created by: Austin de Mora
# Created on: May 2021
# This program finds the reverse of a number


def main():
    number = print(" I am  going to reverse inputed number")
    number_string = input('Enter a number : ')
    reversed = 0

    # process & output
    try:
        number = int(number_string)

        while (number != 0):
            reverse = int(number % 10)
            reversed = reversed * 10 + reverse
            number = int(number / 10)
        print(reversed)
    except ValueError:
        print("Invalid Input")


if __name__ == "__main__":
    main()
