# Cálculo do Índice de Massa Corporal
import os
 
altura1 = float(input("Digite sua altura em metros: "))
peso1 = float(input("Digite seu peso em Kg: "))
 
imc = peso1 / altura1 **2
 
print("Seu IMC é: %.4f" % imc)
 