# Pesos

Uma fábrica instalou um elevador composto de duas cabines ligadas por uma roldana, como na figura. Quando uma cabine sobe, a outra desce. No primeiro andar da fábrica existem algumas caixas de pesos diversos e precisamos levar todas as caixas para o segundo andar, usando o elevador. Apenas uma caixa pode ser colocada por vez dentro de uma cabine. Além disso, existe uma restrição de segurança importante: durante uma viagem do elevador, a diferença de peso entre as cabines pode ser no máximo de 8 unidades. De forma mais rigorosa, P-Q ≤ 8, onde P é o peso da cabine mais pesada e Q, o peso da cabine mais leve. O gerente da fábrica não está preocupado com o número de viagens que o elevador vai fazer. Ele apenas precisa saber se é possível ou não levar todas as caixas para o segundo andar. No exemplo da figura, podemos levar todas as três caixas usando a seguinte sequência de seis viagens do elevador:

1. Sobe a caixa de peso 4, desce a outra cabine vazia; (diferença de 4)
2. Sobe a caixa de peso 10, desce a caixa de peso 4; (diferença de 6)
3. Sobe a caixa de peso 15, desce a caixa de peso 10; (diferença de 5)
4. Sobe a caixa de peso 4, desce a outra cabine vazia; (diferença de 4)
5. Sobe a caixa de peso 10, desce a caixa de peso 4; (diferença de 6)
6. Sobe a caixa de peso 4, desce a outra cabine vazia (diferença de 4).

Dados os pesos de N caixas no primeiro andar, em ordem crescente, seu programa deve determinar se é possível ou não levar todas as N caixas para o segundo andar.

## Entrada

A primeira linha da entrada contém um inteiro N indicando o número de caixas. A segunda linha da entrada contém N inteiros representando os pesos das caixas, em ordem crescente.

## Saída

Imprima uma linha na saída. A linha deve conter o caracter S caso seja possível, ou N caso não seja possível levar todas as caixas até o segundo andar da fábrica.

## Restrições
* 1 ≤ N ≤ 104
* O peso das caixas está entre 1 e 105, inclusive.

## Exemplos
```
Entrada | Saída
--------+-------
3       | S
4 10 15 |
```
```
Entrada               | Saída
----------------------+-------
8                     | N
2 6 15 20 25 35 35 40 |
```
```
Entrada     | Saída
------------+--------
4           | N
10 14 20 23 |
```
```
Entrada | Saída
--------+-------
1       | S
8       |
```

https://olimpiada.ic.unicamp.br/pratique/pj/2018/f2/pesos/