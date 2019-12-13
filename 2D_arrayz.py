#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: December 2019
# This is a program which generates numbers and finds the average of them.

import random


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def sum_of_numbers(list_of_numbers):

    total = 0
    for counter_1 in list_of_numbers:
        for counter_2 in counter_1:
            total += counter_2

    return total


def main():
    # this is what runs the program

    list_of_numbers = []

    # input
    rows_as_string = input(color.YELLOW + 'Input number of rows you want: '
                           + color.END)
    columns_as_string = input(color.YELLOW + 'Input number of columns' +
                              ' you want: ' + color.END)

    try:
        rows = int(rows_as_string)
        columns = int(columns_as_string)

        for loop_counter_r in range(0, rows):
            temporary_column = []
            for loop_counter_c in range(0, columns):
                random_number = random.randint(1, 50+1)
                temporary_column.append(random_number)
                print("{0} ".format(random_number), end="")
            list_of_numbers.append(temporary_column)
            print("")

        total_sum = sum_of_numbers(list_of_numbers)
        average = total_sum/(rows*columns)
        print(color.GREEN + 'Average of numbers = {0} '.format(average) +
              color.END)

    except Exception:
        print('')
        print(color.PURPLE + color.UNDERLINE + 'That is not a valid'
              ' number...' + color.END)
        print("")
        print("")


if __name__ == "__main__":
    main()
