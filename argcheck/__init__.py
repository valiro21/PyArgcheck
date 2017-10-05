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

from .argcheck import (throw_on_none,
                       throw_on_negative,
                       throw_on_non_positive,
                       throw_on_positive,
                       throw_on_non_negative,
                       throw_if_not_in_range,
                       throw_on_greater_than,
                       throw_on_lower_than,
                       throw_on_nan,
                       throw_on_inf,
                       throw_on_nan_or_inf,
                       throw_on_equal,
                       throw_on_close,
                       throw_on_not_close,
                       throw_on_non_iterable,
                       throw_on_empty,
                       throw_on_none_or_empty,
                       throw_if_false,
                       throw_if_true)

__all__ = [
    "throw_on_none",
    "throw_on_negative",
    "throw_on_non_positive",
    "throw_on_positive",
    "throw_on_non_negative",
    "throw_if_not_in_range",
    "throw_on_greater_than",
    "throw_on_lower_than",
    "throw_on_nan",
    "throw_on_inf",
    "throw_on_nan_or_inf",
    "throw_on_equal",
    "throw_on_close",
    "throw_on_not_close",
    "throw_on_non_iterable",
    "throw_on_empty",
    "throw_on_none_or_empty",
    "throw_if_false",
    "throw_if_true"
]
