#!/usr/bin/env python3

def calcular(jogador1, jogador2):
    desmaia1 = jogador1['defesa'] != jogador2['ataque']
    desmaia2 = jogador1['ataque'] != jogador2['defesa']
    
    if (not desmaia1) and desmaia2:
        return 1
    elif desmaia1 and (not desmaia2):
        return 2
    else:
        return -1

def main():
    a1 = int(input())
    d1 = int(input())
    a2 = int(input())
    d2 = int(input())

    j1 = { 'ataque': a1, 'defesa': d1 }
    j2 = { 'ataque': a2, 'defesa': d2 }
    
    print(calcular(j1, j2))

if __name__ == '__main__':
    main()