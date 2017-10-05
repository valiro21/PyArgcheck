"""
MIT License

Copyright (c) 2017 Valentin-Bogdan Roșca

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import collections

import math


def throw_on_none(argument, parameter_name):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is None.
    """
    if argument is None:
        raise TypeError("The argument {0} was None."
                        .format(parameter_name))


def throw_on_negative(argument, parameter_name):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is negative.
    """
    if argument < 0:
        raise TypeError("The argument {0} was negative."
                        .format(parameter_name))


def throw_on_non_positive(argument, parameter_name):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is not positive.
    """
    if argument <= 0:
        raise TypeError("The argument {0} was not positive."
                        .format(parameter_name))


def throw_on_positive(argument, parameter_name):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is positive.
    """
    if argument > 0:
        raise TypeError("The argument {0} was positive."
                        .format(parameter_name))


def throw_on_non_negative(argument, parameter_name):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is not negative.
    """
    if argument >= 0:
        raise TypeError("The argument {0} was not negative."
                        .format(parameter_name))


def throw_if_not_in_range(argument, parameter_name,
                          min_inclusive, max_inclusive):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is not
    between the interval [min_inclusive, max_inclusive].
    """
    if argument < min_inclusive or argument > max_inclusive:
        raise TypeError(
            "The argument {0} was not between {1} and {2}."
            .format(parameter_name, min_inclusive, max_inclusive))


def throw_on_greater_than(argument, value, parameter_name):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is greater
    than the given value.
    """
    if argument > value:
        raise TypeError("The argument {0} was larger than {1}."
                        .format(parameter_name, value))


def throw_on_lower_than(argument, value, parameter_name):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is lower
    than the given value.
    """
    if argument < value:
        raise TypeError("The argument {0} was lower than {1}."
                        .format(parameter_name, value))


def throw_on_nan(argument, parameter_name):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is nan.
    """
    if math.isnan(argument):
        raise TypeError("The argument {0} was nan."
                        .format(parameter_name))


def throw_on_inf(argument, parameter_name):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is infinity.
    """
    if math.isinf(argument):
        raise TypeError("The argument {0} was inf."
                        .format(parameter_name))

def throw_on_nan_or_inf(argument, parameter_name):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is nan or infinity.
    """
    if math.isnan(argument) or math.isinf(argument):
        raise TypeError("The argument {0} was nan or inf."
                        .format(parameter_name))

def throw_on_equal(argument, value, parameter_name):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is equal
    to the given value.
    """
    if argument == value:
        raise TypeError("The argument {0} was equal to {1}"
                        .format(parameter_name, value))


def throw_on_close(argument, value, parameter_name):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is close
    to the given value.
    """
    if math.isclose(argument, value):
        raise TypeError("The argument {0} was close to {1}"
                        .format(parameter_name, value))


def throw_on_not_close(argument, value, parameter_name):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is not close
    to the given value.
    """
    if not math.isclose(argument, value):
        raise TypeError("The argument {0} was not close to {1}"
                        .format(parameter_name, value))


def throw_on_non_iterable(argument, parameter_name):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is not iterable.
    """
    if not isinstance(argument, collections.Iterable):
        raise TypeError("The argument {0} was not iterable."
                        .format(parameter_name))


def throw_on_empty(argument, parameter_name):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is empty.
    """
    if not argument:
        raise TypeError("The argument {0} was empty."
                        .format(parameter_name))


def throw_on_none_or_empty(argument, parameter_name):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given argument is None or empty.
    """
    if argument is None or not argument == 0:
        raise TypeError("The argument {0} was None or empty."
                        .format(parameter_name))


def throw_if_false(condition, message):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given condition is False.
    """
    if not condition:
        raise TypeError(message)


def throw_if_true(condition, message):
    """
    Throws a TypeError with the parameter_name included
    in the error message if the given condition is True.
    """
    if condition:
        raise TypeError(message)
