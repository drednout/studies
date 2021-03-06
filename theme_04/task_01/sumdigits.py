"""This module performs a counting the sum of digits in the number of number!.

Usage:
    factorial.py [-h] number [...]

Description:
    factorial.py receivers one or more values number. For each values of
    number is number! and calculated the sum of digits in the number
    number! Value of number! is only natural numbers.

Options:
    -h Print help on the module and exit.

"""

import sys


class ModuleBaseException(Exception):
    """The base class for all exceptions in this module
    """
    pass


class FactorialException(ModuleBaseException):
    """Exceptions generated by the transmission of incorrect data
    """
    pass


class SumDigitsException(ModuleBaseException):
    """Exceptions generated by the transmission of incorrect data
    """
    pass


def is_integer(number):
    """This function checks whether a number is an int or long type
    """
    return False if not isinstance(number, int) and \
        not isinstance(number, long) else True


def str_to_int(number):
    """This function converts the number represented as a string in int.
    If this is not possible, the value doesn't change.
    """
    result = None
    try:
        result = int(number)
    except (ValueError, TypeError):
        pass
    return result


def factorial(number):
    """This function finds the value of number!
    """
    if not is_integer(number):
        raise FactorialException('invalid literal for factorial(): ' +
                                 '\'{}\' not int'.format(number))
    if number < 0:
        raise FactorialException('invalid literal for factorial(): ' +
                                 '\'{}\' negative int'.format(number))

    result = 1
    for i in range(1, number + 1):
        result *= i

    return result


def sum_digits(number):
    """This function calculates the sum of the digits for number
    """
    if not is_integer(number):
        raise SumDigitsException('invalid literal for factorial(): ' +
                                 '\'{}\' not int'.format(number))

    return sum([int(i) for i in str(abs(number))])


def main():
    """The main function
    """
    error_message = 'factorial.py: missing operand specifiers the file.\n' + \
        'Get more information on the command: factorial.py -h\n'

    if len(sys.argv) == 1:
        sys.stderr.write(error_message)
        sys.exit(1)

    if sys.argv[1] == '-h':
        sys.stdout.write(__doc__)
        sys.exit(0)

    for arg in sys.argv[1:]:
        number = str_to_int(arg)
        try:
            if number is None:
                sys.stderr.write('FactorialException: invalid literal for ' +
                                 'factorial(): \'{}\' not int\n'.format(arg))
                continue

            sum_ = sum_digits(factorial(number))
            sys.stdout.write('Sum of digits {}!: {}\n'.format(number, sum_))
        except ModuleBaseException as error:
            sys.stderr.write('FactorialException: {}\n'.format(error))


if __name__ == '__main__':
    main()
