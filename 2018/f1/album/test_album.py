#!/usr/bin/env python3

import pytest
from album import calcular_figurinhas

def test_ex1():
    figs = [5, 8, 3]
    assert calcular_figurinhas(10, 3, figs) == 7

def test_ex2():
    figs = [3, 3, 2, 3, 3, 3]
    assert calcular_figurinhas(5, 6, figs) == 3

def test_ex3():
    figs = [ 2, 1, 3, 3]
    assert calcular_figurinhas(3, 4, figs) == 0

