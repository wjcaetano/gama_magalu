print("########################### Coversor (metro/centímetro) ###########################")

metro = float(input("Digite o valor em metros: ").replace(',','.'))
centimetro = metro * 100

print(f'{metro:.2f} metro(s) = {centimetro:.2f} centímetros')
