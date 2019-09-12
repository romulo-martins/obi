#!/usr/bin/env python3

def calcular_fase(k, l):
    if (k > l):
        k, l = l, k

    inicio = 1
    fim = 16
    meio = (inicio+fim)/2
    contador = 0
    while not ((k <= meio) and (l > meio)):
        if (k <= meio) and (l < meio):
            fim = meio
        else:
            inicio = meio
        contador += 1
        meio = (inicio+fim)/2
    
    return ['final', 'semifinal', 'quartas', 'oitavas'][contador]


def main():
    k = int(input())
    l = int(input())
    print(calcular_fase(k, l))

if __name__ == '__main__':
    main()
