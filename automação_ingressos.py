from PIL import Image, ImageDraw, ImageFont #importo a biblioteca Pillow para tratar imagens em python
import img2pdf

template = Image.open("ingresso_template.png") #pego o template
#img_ingresso = template.copy() #criei uma cópia do meu template original para ele nao ficar editado permanentemente na memoria

color=(70, 41, 10) #cor padrao

num_folha = 0 #contadora
arquivos_folha= [] #lista q vai receber a quantidade de folhas

for mesa in range(1,115):
    
    # ajusta tamanho da fonte para numeros de 3 digitos
    if mesa >= 100:
        fnt_main = ImageFont.truetype("Hertical Sans Texture/Hertical Sans Texture.ttf", 150)
        fnt = ImageFont.truetype('Hertical Sans Texture/Hertical Sans Texture.ttf', 100) 

    else:
        fnt_main = ImageFont.truetype('Hertical Sans Texture/Hertical Sans Texture.ttf', 178) 
        fnt = ImageFont.truetype('Hertical Sans Texture/Hertical Sans Texture.ttf', 120) 

    number = str(mesa).zfill(2) #mesa é um número inteiro e o draw.text precisa de uma string e o zfill é para adicionar 0 a esquerda em numeros até ter 2 digitos
    img_ingresso = template.copy() #pego o template
    draw = ImageDraw.Draw(img_ingresso) #criei uma ferramenta de desenho apontando para o img_ingresso

    draw.text((590, 490), number, font=fnt_main, fill=color, anchor='mm') #escrevendo o primeiro numero
    draw.text((190, 920), number, font=fnt, fill=color, anchor='mm') #slote 1
    draw.text((560, 920), number, font=fnt, fill=color, anchor='mm') #slote 2
    draw.text((930, 920), number, font=fnt, fill=color, anchor='mm') #slote 3
    draw.text((1290, 920), number, font=fnt, fill=color, anchor='mm') #slote 4

    img_ingresso = img_ingresso.resize((1754 , 1240)) #to redimensionando ele para a medida q ele vai ser dentro do pdf

    posicao = (mesa-1) % 4 #tentando descobrir qual ingresso meu é

    if posicao == 0: # criando uma folha em branco de 4 em 4
        folha = Image.new('RGB', (3508, 2480), (255, 255,255))

    coordenadas = { #dicionario com as coordenadas de cada posicao
        0 : (0,0),
        1 : (1754,0),
        2 : (0,1240),
        3 : (1754,1240)}
    
    folha.paste(img_ingresso, coordenadas[posicao]) #usando o paste para colar as imagens nas coordenadas de acordo com a posicao de cada uma
    
    # salva a folha quando completa (4 ingressos) ou quando é o último
    if posicao == 3 or mesa == 114:
        num_folha += 1
        nome_folha = f'folha_{num_folha}.png'
        folha.save(nome_folha)
        arquivos_folha.append(nome_folha)

# salva a folha quando completa (4 ingressos) ou quando é o último
with open("ingressos_completo_junto.pdf", "wb") as f:
    f.write(img2pdf.convert(arquivos_folha))

print(f"Pronto! a quantidade de folhas geradas foi {num_folha}")