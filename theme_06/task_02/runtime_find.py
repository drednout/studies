"""The module displays information about the runtime to sort a list
of arbitrary length by the bubble and the built-in sorted().

Usage:
    runtime_sorting.py LIMIT ITERATION

Description:
    The module take from one to several LIMIT values. The list of
    values with ','.

Parameters:
    LIMIT
        Sets the maximum number of values in the list.

    ITERATION
       Sets the number of executions of sorts.

Options:
    -h
        Print help on the module and exit.

    --help
        Print detailed help on the module and exit.

Examples:
    To run the module is necessary for it to pass parameters LIMIT
    and ITERATION:
        runtime_sorting.py LIMIT ITERATION

"""

import sys
import argparse
import time


# ------------
# Unit classes
# ------------
class ModuleProfiler(object):
    """This class is necessary to measure the runtime of the
    algorithm and print this values to the stdout.
    """

    def __enter__(self):
        self._start_time = time.time()

    def __exit__(self, type, value, traceback):
        sys.stdout.write('{:<15.5f}|'.format(time.time() - self._start_time))


class ModuleHelpAction(argparse._HelpAction):
    """The class for overriding method __call__
    """
    def __call__(self, parser, namespace, values, option_string=None):
        if 'help' in option_string:
            parser.print_help_detailed()
            parser.exit()
        parser.print_help()
        parser.exit()


class ModuleParser(argparse.ArgumentParser):
    """The class add method print_help_detailed
    """
    def print_help_detailed(self):
        """Print help documentation
        """
        sys.stdout.write(__doc__)


# --------------------------
# Print function information
# --------------------------
def print_separation_line(iteration):
    """The function formation and print the separation line
    for a table total information.
    """
    sys.stdout.write('+{:9}+{:9}+'.format('-'*9, '-'*9))
    for index in range(iteration):
        sys.stdout.write('{:15}+'.format('-'*15))
    sys.stdout.write('\n')


def print_cap_table(iteration):
    """The function formation and print the cap for a table
    total information.
    """
    sys.stdout.write('|{:<9}|{:<9}|'.format('Limit', 'Type'))
    for index in range(iteration):
        sys.stdout.write('{:<15}|'.format(index))
    sys.stdout.write('\n')


def parse_arg():
    """parse command line parameters passed to the module.
    """
    parser = ModuleParser(add_help=False)

    parser.add_argument('limits', type=str, help='Lengths list')
    parser.add_argument('iteration', type=int,
                        help='The number of repetitions.')
    parser.add_argument('-h', '--help', action=ModuleHelpAction,
                        help='Show help message and exit')

    return parser.parse_args()


def find_linear(list_, value):
    for index in range(len(list_)):
        if value == list_[index]:
            return index


def find_binary(list_, value):
    first = 0
    last = len(list_) - 1

    while first <= last:
        middle = first + (last - first) // 2
        if value == list_[middle]:
            return middle
        elif value < list_[middle]:
            last = middle
        else:
            first = middle + 1


def find_index(list_, value):
    return list_.index(value)


def init_list(limit):
    """The function returns a list of length 'limit' made up of
    random numbers.
    """
    return [index for index in range(limit)]


def runtime(func, *argv):
    """The function runtime calculates and print it on the stdout.
    """
    with ModuleProfiler() as profiler:
        func(*argv)


def main():
    """The main function.
    """
    options = parse_arg()
    limits = [int(limit) for limit in options.limits.split(',')]

    print_separation_line(options.iteration)
    print_cap_table(options.iteration)

    for limit in limits:
        print_separation_line(options.iteration)
        sys.stdout.write('|{:<9}|{:<9}|'.format(limit, 'linear'))

        list_ = init_list(limit)

        for i in range(options.iteration):
            runtime(find_linear, list_, limit - 1)

        sys.stdout.write('\n|{:<9}|{:<9}|'.format('', 'binary'))

        for i in range(options.iteration):
            runtime(find_binary, list_, limit - 1)

        sys.stdout.write('\n|{:<9}|{:<9}|'.format('', 'index'))

        for i in range(options.iteration):
            runtime(find_index, list_, limit - 1)

        sys.stdout.write('\n')

    print_separation_line(options.iteration)


if __name__ == '__main__':
    main()