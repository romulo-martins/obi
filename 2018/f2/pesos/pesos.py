#!/usr/bin/env python3

def calcular(pesos):
    elevador = { 'sobe': 0, 'desce': 0 }
    for p in pesos:
        elevador['sobe'] = p
        if abs(elevador['sobe'] - elevador['desce']) > 8:
            return 'N'
        elevador['desce'] = p
    return 'S'

def main():
    n = int(input())
    # p = []
    # for i in range(0, n):
    #     p.append(int(input()))
    p = list(map(int, input().split()))
    print(calcular(p))

if __name__ == '__main__':
    main()
