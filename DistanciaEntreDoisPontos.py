# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e 
# calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

# Distancia =

# Entrada
# O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

# Saída
# Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
import math

numx1, numy1 = map(float, input().split())
numx2, numy2 = map(float, input().split())

distancia = math.sqrt((numx2 - numx1) ** 2 + (numy2- numy1) ** 2)

print(f"{distancia:.4f}")