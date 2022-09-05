print("########################### Peso Ideal ###########################")

altura = float(input('Digite a sua altura: ').replace(',','.'))
alt_ideal = (72.7*altura)-58

print(f'O seu peso ideal é: {alt_ideal:.2f} kg')