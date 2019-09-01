#!/usr/bin/env python3

import pytest
from basquete import calcular_pontos

def test_ex1():
    assert calcular_pontos(1720) == 3

def test_ex2():
    assert calcular_pontos(250) == 1

def test_ex3():
    assert calcular_pontos(1400) == 2
