# Pulo do Gato

O gato Obinho gosta de brincar no pátio do colégio, no qual há uma sequência de C lajotas, que podem ser brancas ou pretas. Obinho está na lajota inicial da sequência (a mais à esquerda), e quer ir pulando até a lajota final da sequência (a mais à direita). Mas ele só gosta de pular de uma lajota preta para outra lajota preta, nunca pisando numa lajota branca. Além disso, ele não consegue pular muito longe. A parte esquerda da figura mostra as lajotas que o Obinho pode alcançar com um pulo: uma distância máxima de duas lajotas.

![pulo-do-gato](2018f3pj_pulo.png)

Obinho quer chegar na lajota final com o número mínimo de pulos possível. Por exemplo, na parte direita da figura, para C=14, o menor número de pulos possível é 8. Seu programa deve computar o número mínimo de pulos para o Obinho chegar na lajota final.

## Entrada

A primeira linha da entrada contém um inteiro C, representando o número de lajotas do pátio. A segunda linha contém C inteiros indicando a cor das lajotas, da inicial (mais à esquerda) à final (mais à direita): o valor 1 indica uma lajota preta, o valor 0 indica uma lajota branca.

## Saída

Imprima uma linha contendo o número mínimo de pulos que o gato Obinho precisa dar para ir da lajota inicial até a lajota final. Se não for possível pular até a lajota final, imprima -1.

## Restrições

* 1 ≤ C ≤ 104;
* As lajotas inicial e final são sempre pretas.

## Informações sobre a pontuação

* Para um conjunto de casos de teste valendo 10 pontos, todas as lajotas são pretas;
* Para um conjunto de casos de teste valendo 20 pontos, C ≤ 1000.

## Exemplos

```
Entrada                     | Saída
------------------------------------
14                          | 8
1 1 0 1 1 1 0 1 1 0 1 0 1 1 |
```
```
Entrada                     | Saída
------------------------------------
14                          | -1
1 0 0 1 1 1 0 0 1 0 1 1 0 1 |
```
```
Entrada                 | Saída
--------------------------------                        
12                      | 6
1 1 1 1 1 1 1 1 1 1 1 1 |
```
```
Entrada           | Saída
--------------------------
9                 | 5
1 0 1 1 0 1 1 0 1 |
```

https://olimpiada.ic.unicamp.br/pratique/pj/2018/f3/pulo/