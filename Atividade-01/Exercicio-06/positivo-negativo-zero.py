# Crie um programa que receba um número do usuário e diga se ele é positivo, negativo ou igual a zero.

# Para usuario inserir um valor
number = float(input("Insira um número: "))
if number > 0:
    print("O número é positivo")
elif number < 0:
    print("O número é negativo")
else: 
    print("O número é zero")