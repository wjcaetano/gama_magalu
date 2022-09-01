print("########################### Conversor Celcius/Fahrenheit ###########################")

cel = float(input('Digite a temperatura em Celcius: ').replace(',','.'))
fah = (cel * (9/5)) + 32

print(f'A temperatura em Fahrenheit é: {fah:.2f} graus')