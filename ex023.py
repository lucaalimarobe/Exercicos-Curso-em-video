'''Separando Digito de um numero'''

numero = int(input('Informe um numero: '))
print(f'Analisando seu numero {numero}')

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')