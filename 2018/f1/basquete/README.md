# Basquete de robôs

A organização da OIBR, Olimpíada Internacional de Basquete de Robô, está começando a ter problemas com dois times: os Bit Warriors e os Byte Bulls. É que os robôs desses times acertam quase todos os lançamentos, de qualquer posição na quadra! Pensando bem, o jogo de basquete ficaria mesmo sem graça se jogadores conseguissem acertar qualquer lançamento, não é mesmo? Uma das medidas que a OIBR está implantando é uma nova pontuação para os lançamentos, de acordo com a distância do robô para o início da quadra. A quadra tem 2000 centímetros de comprimento, como na figura.

Dada a distância D do robô até o início da quadra, onde está a cesta, a regra é a seguinte:

* Se D ≤ 800, a cesta vale 1 ponto;
* Se 800 < D ≤ 1400, a cesta vale 2 pontos;
* Se 1400 < D ≤ 2000, a cesta vale 3 pontos.

A organização da OIBR precisa de ajuda para automatizar o placar do jogo. Dado o valor da distância D, você deve escrever um programa para calcular o número de pontos do lançamento.

## Entrada

A primeira e única linha da entrada contém um inteiro D indicando a distância do robô para o início da quadra, em centímetros, no momento do lançamento.

## Saída

Seu programa deve produzir uma única linha, contendo um inteiro, 1, 2 ou 3, indicando a pontuação do lançamento.

## Restrições

* 0 ≤ D ≤ 2000

## Exemplos

|Entrada | Saída|
|--------|------|
| 1720   | 3    |
| 250    | 1    |
| 1400   | 2    |

https://olimpiada.ic.unicamp.br/pratique/pj/2018/f1/basquete/
