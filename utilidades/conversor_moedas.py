from utilidades import calcula

def multiplicar(a, b, c, d):
 return a * b, a * c, a * d

a = float(input('Digite o valor em Reais:'))
b = float(input('Digite o valor em Dolar:'))
c = float(input('Digite o valor em Euro:'))
d = float(input('Digite o valor em Libra esterlina:'))

print(f'{a}*{b} = {calcula.multiplicar(a, b)}')
print(f'{a}*{c} = {calcula.multiplicar(a, c)}')
print(f'{a}*{d} = {calcula.multiplicar(a, d)}')
