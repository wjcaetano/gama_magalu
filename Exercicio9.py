print("########################### Conversor Fahrenheit/Celcius ###########################")

fah = float(input('Digite a temperatura em Fahrenheit: ').replace(',','.'))
cel = 5 * ((fah-32)/9)

print(f'A temperatura em Celcius é: {cel:.2f} graus')