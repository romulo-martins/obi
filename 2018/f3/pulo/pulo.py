#!/usr/bin/env python3

def calcular(lajotas):
    num_pulos = 0
    pos = 0
    num_lajotas = len(lajotas) 
    while pos != num_lajotas-1:
        if pos+2 < num_lajotas and lajotas[pos+2] == 1:
            pos += 2
        elif pos+1 < num_lajotas and lajotas[pos+1] == 1:
            pos += 1
        else:
            return -1
        num_pulos += 1
    return num_pulos

def main():
    c = int(input())
    lajotas = list(map(int, input().split()))
    print(calcular(lajotas))

if __name__ == '__main__':
    main()