#!/usr/bin/env python3

def remover_repetidas(figs):
    uniq_figs = []
    for f in figs:
        if f not in uniq_figs:
            uniq_figs.append(f)
    return uniq_figs

def calcular_figurinhas(n, m, figs):
    uniq_figs = remover_repetidas(figs)
    return (n - len(uniq_figs))

def main():
    n = int(input())
    m = int(input())
    figs = []
    for i in range(0, m):
        fig = int(input())
        figs.append(fig)
    resp = calcular_figurinhas(n, m, figs)
    print(resp)

if __name__ == '__main__':
    main()
    