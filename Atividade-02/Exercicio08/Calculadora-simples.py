''' 
Crie um programa que simule uma calculadora simples. 
O usuário deve informar dois números e a operação desejada (+, -, *, /) e o programa
deve exibir o resultado da operação.'''

numb1 = float(input("Digite o primeiro número: "))
numb2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação a ser realizada (+, -, *, /): ")

if operacao == "+":
    resultado = numb1 + numb2
    print(f"O resultado de {numb1} + {numb2} é: {resultado}")
elif operacao == "-":
    resultado = numb1 - numb2
    print(f"O resultado de {numb1} - {numb2} é: {resultado}")
elif operacao == "*":
    resultado = numb1 * numb2
    print(f"O resultado de {numb1} * {numb2} é: {resultado}")
elif operacao == "/":
    if numb2 != 0:        
        resultado = numb1 / numb2
        print(f"O resultado de {numb1} + {numb2} é: {resultado}")
    else:
        print("Erro!!! divisão por zero não permitida.")
else:
    print("Operação inválida.")