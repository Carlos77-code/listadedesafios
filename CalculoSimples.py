# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, 
# o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

# Entrada
# O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

# Saída
# A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". 
# O valor deverá ser apresentado com 2 casas após o ponto.


codigo_peca1, numero_pecas1, valor_unit_pecas1 = input().split()
codigo_peca1 = int(codigo_peca1)
numero_pecas1 = int(numero_pecas1)
valor_unit_pecas1 = float(valor_unit_pecas1)

codigo_peca2, numero_pecas2, valor_unit_pecas2 = input().split()
codigo_peca2 = int(codigo_peca2)
numero_pecas2 = int(numero_pecas2)
valor_unit_pecas2 = float(valor_unit_pecas2)

valor = (numero_pecas1 * valor_unit_pecas1) + (numero_pecas2 * valor_unit_pecas2)

print("VALOR A PAGAR: R$ {:.2f}".format(valor))