#!/usr/bin/env python3

def calcular(f, c):
    dia = 1
    contador = 0
    while contador < f:
        for i in range(0, len(c)):
            if dia % c[i] == 0:
                contador += 1
        if contador >= f:
            break
        dia += 1  
    return dia

def main():
    # n = int(input())
    # f = int(input())
    # c = []
    # for i in range(0, n):
    #     capsula = int(input())
    #     c.append(capsula)
    n, f = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(calcular(f, c))

if __name__ == '__main__':
    main()