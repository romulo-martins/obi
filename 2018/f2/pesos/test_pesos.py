#!/usr/bin/env python3

import pytest
from pesos import calcular

def test_ex1():
    p = [4, 10, 15]
    assert calcular(p) == 'S'

def test_ex2():
    p = [2, 6, 15, 20, 25, 35, 35, 40]
    assert calcular(p) == 'N'

def test_ex3():
    p = [10, 14, 20, 23]
    assert calcular(p) == 'N'

def test_ex4():
    p = [8]
    assert calcular(p) == 'S'
