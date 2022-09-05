print("########################### Peso Ideal ###########################")

altura = float(input('Digite a sua altura: ').replace(',','.'))
alt_ideal_H = (72.7*altura)-58
alt_ideal_M = (62.1*altura)-44.7

print(f'O peso ideal para o sexo masculino é: {alt_ideal_H:.2f} kg\nO peso ideal para o sexo feminino é: {alt_ideal_M:.2f}')