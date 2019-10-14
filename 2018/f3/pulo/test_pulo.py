#!/usr/bin/env python3

import pytest
from pulo import calcular

def test_ex1():
    lajotas = [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1]
    assert calcular(lajotas) == 8

def test_ex2():
    lajotas = [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1]
    assert calcular(lajotas) == -1

def test_ex3():
    lajotas = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert calcular(lajotas) == 6

def test_ex4():
    lajotas = [1, 0, 1, 1, 0, 1, 1, 0, 1]
    assert calcular(lajotas) == 5
