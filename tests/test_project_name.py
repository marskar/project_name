#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from project_name.project_name import fib

__author__ = "AUTHOR_NAME"
__copyright__ = "AUTHOR_NAME"
__license__ = "MIT"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
