print("########################### Loja de Tintas ###########################")

tamanho_area = float(input('Bem vindo!\nPor favor, informe a área total a ser pintada: ').replace(',','.'))
litros_tinta = (tamanho_area // 3) + 1
lata_tinta = (litros_tinta // 18) + 1
custo_pintura = lata_tinta * 80

print(f'Para pintar uma área de {tamanho_area:.2f} m² será necessário {lata_tinta} latas de tintas.\nO custo total será de R${custo_pintura:.2f}')
