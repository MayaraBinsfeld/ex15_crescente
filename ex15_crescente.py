"""
Programa: ex15_crescente
Descrição: Este programa ordena os números fornecidos pelo usuário em ordem crescente.
Autor: Mayara Binsfeld
Data: 27/02/2025
Versão: 0.0.1

"""

# Alocação de memória
numero1 = 0
numero2 = 0
numero3 = 0

# Entrada de dados 
numero1 = float(input("Digite o primeiro número"))
numero2 = float(input("Digite o segundo número"))
numero3 = float(input("Digite o terceiro número"))

# Processamento de dados
numeros = [numero1, numero2, numero3]
numeros.sort ()

# Saída de dados
print(f"Os números em ordem crescente são:{numeros} ")