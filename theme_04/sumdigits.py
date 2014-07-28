"""This module performs a counting the sum of digits in the number of number!.

Usage:
    factorial.py [-h] number [...]

Description:
    factorial.py receivers one or more values number. For each values of
    number is number! and calculated the sum of digits in the number
    number! Value of nunber! is only natural numbers.

Options:
    -h Print help on the module and exit.

"""

import sys


class FactorialException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def str_to_int(numbers):
    """This function converts the number represented as a string in int.
    If this is not possible, the value doesn't change.
    """
    for number in numbers:
        try:
            yield int(number)
        except ValueError:
            yield number


def factorial(number):
    """This function finds the value of number!
    """
    if not isinstance(number, int):
        raise FactorialException('invalid literal for factorial(): ' +
                                 '\'{}\' not int'.format(number))
    if number < 0:
        raise FactorialException('invalid literal for factorial(): ' +
                                 '\'{}\' negative int'.format(number))

    res = 1
    for i in range(1, number + 1):
        res *= i

    return res


def sum_digits(number):
    """This function calculates the sum of the digits for number
    """
    return sum([int(i) for i in str(number)]) if number else None


def main():
    """The main function
    """
    errorstr = 'factorial.py: missing operand specifiels the file.\n' + \
        'Get more information on the command: factorial.py -h\n'

    if len(sys.argv) == 1:
        sys.stderr.write(errorstr)
        sys.exit(1)

    if sys.argv[1] == '-h':
        sys.stdout.write(__doc__)
        sys.exit(0)

    for number in str_to_int(sys.argv[1:]):
        try:
            sum_ = sum_digits(factorial(number))
            sys.stdout.write('Sum of digits {}!: {}\n'.format(number, sum_))
        except FactorialException as error:
            sys.stderr.write('FactorialException: {}\n'.format(error.value))


if __name__ == '__main__':
    main()
