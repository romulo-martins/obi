#!/usr/bin/env python3

import pytest
from copa import calcular_fase

def test_ex1():
    assert calcular_fase(10, 14) == 'semifinal'

def test_ex2():
    assert calcular_fase(7, 8) == 'oitavas'

def test_ex3():
    assert calcular_fase(3, 13) == 'final'

def test_ex4():
    assert calcular_fase(5, 8) == 'quartas'