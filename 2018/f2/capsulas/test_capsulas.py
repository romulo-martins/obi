#!/usr/bin/env python3

import pytest
from capsulas import calcular

def test_ex1():
    f = 12
    c = [3, 7, 2]
    assert calcular(f, c) == 14

def test_ex2():
    f = 100
    c = [17, 13, 20, 10, 12, 16, 10, 13, 13, 10]
    assert calcular(f, c) == 130
