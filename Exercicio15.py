print("########################### Salario Mensal ###########################")

salario_hora = float(input('Qual o valor que vc recebe por hora?\n').replace(',','.'))
horas_mes = float(input('Quantas horas trabalhou neste mês?\n').replace(',','.'))

salario_bruto = salario_hora * horas_mes
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - (ir + inss + sindicato)


print(f'+ Salário Bruto: R${salario_bruto:.2f}\n- IR (11%): R${ir:.2f}\n- INSS (8%): R${inss}\n- Sindicato: R${sindicato:.2f}\n= Salário Liquido: R${salario_liquido}')