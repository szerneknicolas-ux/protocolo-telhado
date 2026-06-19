from rembg import remove

pasta = r'C:\Users\HP\OneDrive\Área de Trabalho\Projeto do meu pai\public_html'

for nome in ['homem triste', 'homem feliz']:
    with open(f'{pasta}\\{nome}.png', 'rb') as f:
        dados = f.read()
    resultado = remove(dados)
    with open(f'{pasta}\\{nome}-sem-fundo.png', 'wb') as f:
        f.write(resultado)
    print(f'{nome} processado com sucesso!')
