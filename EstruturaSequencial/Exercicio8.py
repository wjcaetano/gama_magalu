print("########################### Salário Mensal ###########################")

salario_hora = float(input('Qual o valor que vc recebe por hora?\n').replace(',','.'))
horas_mes = float(input('Quantas horas trabalhou neste mês?\n').replace(',','.'))

salario_mes = salario_hora * horas_mes

print(f'O seu salário neste mês será: R$ {salario_mes:.2f}')