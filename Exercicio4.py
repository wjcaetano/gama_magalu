print("########################### Calculadora de Soma ###########################")
nota1 = float(input('Digite a nota do primeiro bimestre: ').replace(',','.'))
nota2 = float(input('Digite a nota do segundo bimestre: ').replace(',','.'))
nota3 = float(input('Digite a nota do terceiro bimestre: ').replace(',','.'))
nota4 = float(input('Digite a nota do quarto bimestre: ').replace(',','.'))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A média final é: {media:.2f}')