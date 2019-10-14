#!/usr/bin/env python3

import pytest
from batalha import calcular

def test_ex1():
    j1 = { 'ataque': 21, 'defesa': 7 }
    j2 = { 'ataque': 7, 'defesa': 12 }
    assert calcular(j1, j2) == 1

def test_ex2():
    j1 = { 'ataque': 2, 'defesa': 5 }
    j2 = { 'ataque': 71, 'defesa': 18 }
    assert calcular(j1, j2) == -1

def test_ex3():
    j1 = { 'ataque': 14, 'defesa': 8 }
    j2 = { 'ataque': 8, 'defesa': 14 }
    assert calcular(j1, j2) == -1

def test_ex4():
    j1 = { 'ataque': 1, 'defesa': 19 }
    j2 = { 'ataque': 32, 'defesa': 1 }
    assert calcular(j1, j2) == 2
