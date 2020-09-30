from minha_classe import pessoa

nome = str(input("Digite um nome: "))
idade = int(input("Digite a idade: "))
altura = float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))

p1 = pessoa (nome, idade, altura, peso)
imc = peso / altura **2

print('- -'  *28 )
print("Dados da Pessoa:")
print('- -'  *28 )
print(p1. __repr__(), "Seu IMC é: %.2f" % imc)
print('- -'  *28 )
