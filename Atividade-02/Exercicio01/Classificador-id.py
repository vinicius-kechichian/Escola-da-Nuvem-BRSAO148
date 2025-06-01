# Crie um programa que solicite a idade do usuário e classifique-o 
# em uma das seguintes categorias: 


# Criança (0-12 anos) 
# Adolescente (13-17 anos) 
# Adulto (18-59 anos) 
# Idoso (60 anos ou mais)

id = int(input("Digite sua idade: "))
if id >= 0 and id <= 12:
    print("Classificação: Criança")
elif id >= 13 and id <= 17:
    print("Classificação: Adolescente")
elif id >= 18 and id <= 59:
    print("Classificação: Adulto")
elif id >= 60:
    print("Classificação: Idoso")
else:
    print("Idade inválida!")