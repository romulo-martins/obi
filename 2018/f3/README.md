# Batalha

Todo mundo está jogando um novo game de realidade aumentada no celular, com batalhas entre monstrinhos! Nas primeiras fases do jogo as batalhas são bem simples, mas ainda assim bastante divertidas. Dois jogadores vão escolher um monstrinho cada, na sua coleção de monstrinhos. Cada monstrinho tem um tipo de ataque e um tipo de defesa, que são identificados por números naturais. A regra da batalha, que consiste em cada monstrinho usar seu respectivo ataque ao mesmo tempo, é que se o número da defesa de um monstrinho é igual ao número do ataque do seu oponente, então ele não sofre nenhum dano; caso contrário, se o número da defesa dele é diferente do ataque do oponente, então ele sofre dano total e desmaia! Por exemplo, o monstrinho do primeiro jogador tem o ataque 21 e a defesa 7; enquanto que o monstrinho do segundo jogador tem o ataque 7 e a defesa 12. Nesse caso, o primeiro jogador vence, pois não desmaiou, enquanto que o segundo jogador desmaiou. Assim, o resultado da batalha, que seu programa deve determinar, pode ser:

* Jogador 1 vence: se o jogador 1 não desmaia e o jogador 2 desmaia;
* Jogador 2 vence: se o jogador 2 não desmaia e o jogador 1 desmaia;
* Empate: em qualquer caso contrário; quer dizer, os dois desmaiam, ou nenhum desmaia.

## Entrada

A primeira linha da entrada contém um inteiro A1 indicando o ataque do primeiro jogador. A segunda linha contém um inteiro D1 indicando a defesa do primeiro jogador. A terceira linha contém um inteiro A2 representando o ataque do segundo jogador. A quarta, e última linha, contém um inteiro D2 representando a defesa do segundo jogador.

## Saída

Imprima uma linha contendo um inteiro, 1 ou 2, indicando qual jogador ganhou a batalha. Se a batalha resultou em empate, imprima -1.

## Restrições
* 1 ≤ A1 ≤ 100
* 1 ≤ D1 ≤ 100
* 1 ≤ A2 ≤ 100
* 1 ≤ D2 ≤ 100

## Exemplos

```
Entrada | Saída
--------+-------
21      | 1
7       |
7       |
12      |
```
```
Entrada | Saída
--------+-------
2       |
5       |
71      |
18      |
```
```
Entrada | Saída
--------+-------
14      | -1
8       |
8       |
14      |
```
```
Entrada | Saída
--------+-------
1       | 2
19      |
32      |
1       |
```
https://olimpiada.ic.unicamp.br/pratique/pj/2018/f3/batalha/