print("########################### Loja de Tintas ###########################")

tamanho_area = float(input('Bem vindo!\nPor favor, informe a área total a ser pintada: ').replace(',','.'))
litros_tinta = (tamanho_area // 6) + 1
lata_tinta = (litros_tinta // 18) + 1
galao_tinta = (litros_tinta // 3.6) + 1
custo_pintura_lata = lata_tinta * 80
custo_pintura_galao = galao_tinta * 25

print(f'Para pintar uma área de {tamanho_area:.2f} m² será necessário {lata_tinta} latas de tintas.\nO custo total será de R${custo_pintura_lata:.2f}')
print(f'Para pintar uma área de {tamanho_area:.2f} m² será necessário {galao_tinta} galões de tintas.\nO custo total será de R${custo_pintura_galao:.2f}')