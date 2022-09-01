#Faça um Programa que peça 2 números inteiros e um número real.

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segunto número inteiro: '))
num3 = float(input('Digite um número real: ').replace(',','.'))

a = (num1*2) * (num2/2)
b = (num1*3) + num3
c = num3**3

print(f'a. o produto do dobro do primeiro com metade do segundo: {a}')
print(f'b. a soma do triplo do primeiro com o terceiro: {b:.2f}')
print(f'o terceiro elevado ao cubo: {c:.2f}')

