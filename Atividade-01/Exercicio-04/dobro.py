# Crie uma função em Python que receba um número como parâmetro e retorne o dobro desse número.
#  Depois, chame essa função com um número fornecido pelo usuário.

def dobro(number):
    return number * 2
valor = float(input("Insira um número: "))
resultado = dobro (valor)
print("O dobro do número inserido é: ", resultado)
