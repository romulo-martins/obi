#!/usr/bin/env python3

def calcular_pontos(d):
    if d <= 800:
        return 1
    elif 800 < d and d <= 1400:
        return 2
    elif 1400 < d and d <= 2000:
        return 3
    else: 
        return 0

def main():
    d = int(input())
    print(calcular_pontos(d))

if __name__ == '__main__':
    main()