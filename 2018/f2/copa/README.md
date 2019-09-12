# Copa

O sorteio das posições dos jogadores na chave decisiva da copa do mundo de ping-pong está deixando a todos nervosos. É que ninguém quer pegar o jogador mais bem ranqueado, o Mestre Kung, logo nas oitavas de final, ou nas quartas de final. Melhor que só seja possível enfrentar Mestre Kung na semifinal ou na final!

A chave possui 16 posições numeradas de 1 a 16, como na figura abaixo. A organização da copa vai fazer um sorteio para definir em qual posição cada jogador vai iniciar a chave decisiva. Nas oitavas de final, o jogador na posição 1 enfrenta o jogador na posição 2; o da posição 3 enfrenta o da posição 4; e assim por diante, como na figura.

O objetivo deste problema é, dadas as posições de Mestre Kung e Mestre Lu na chave, decidir em que fase da competição Mestre Kung e Mestre Lu vão se enfrentar, caso vençam todas as suas respectivas partidas antes de se enfrentarem. Por exemplo, se o sorteio da chave determinar que Mestre Kung ocupará a posição 1 e Mestre Lu a posição 2 da chave, eles se encontrarão nas oitavas de final; se Mestre Kung ocupar a posição 6 e Mestre Kung ocupar a posição 9 da chave, eles se encontrarão somente na final.

## Entrada

A entrada consiste de duas linhas. A primeira linha da entrada contém um inteiro K que indica a posição de Mestre Kung na chave. A segunda linha da entrada contém um inteiro L que indica a posição de Mestre Lu na chave.

## Saída

Seu programa deve produzir uma linha contendo uma das palavras seguintes, decidindo a fase em que vão se enfrentar os jogadores Mestre Kung e Mestre Lu, se eles chegarem a se enfrentar: oitavas, quartas, semifinal ou final.

## Restrições
* 1 ≤ K ≤ 16
* 1 ≤ L ≤ 16
* K ≠ L

## Informações sobre a pontuação
* Para um conjunto de casos de testes valendo 30 pontos, K = 1.

## Exemplos

```
Entrada | Saída
--------+-----------
10      | semifinal
14      |
```
```
Entrada | Saída
--------+-----------
7       | oitavas
8       |
```
```
Entrada | Saída
--------+-----------
3       | final
13
```
```
Entrada | Saída
--------+-----------
5       | quartas
8       |
```
