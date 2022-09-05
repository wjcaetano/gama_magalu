print("########################### Calculadora de Tempo de Download ###########################")

tamanho_arquivo = int(input('Informe o tamanho do arquivo (em Mb): '))
velocidade_download = int(input('Informe a velocidade de download (em Mbps): '))

tempo_download = (tamanho_arquivo / (velocidade_download / 8)) /60

print(f'Para baixar um arquivo de {tamanho_arquivo} Megabites (Mb) em uma conexão de {velocidade_download} Mb/s, em {tempo_download:.1f} minutos o download será concluido.')