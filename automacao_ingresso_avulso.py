from PIL import Image, ImageDraw, ImageFont
import img2pdf

template = Image.open("ingresso_avulso.png")
color = (70,41,10) 

num_folha = 0 
arquivos_folha = []

for mesa in range(1,201):
    number = str(mesa).zfill(2)
    ing_avulso = template.copy()
    draw = ImageDraw.Draw(ing_avulso)
    if mesa >=200:
        fnt_main = ImageFont.truetype('Hertical Sans Texture/Hertical Sans Texture.ttf', 170)
        fnt = ImageFont.truetype('Hertical Sans Texture/Hertical Sans Texture.ttf', 110)      
    elif mesa >=100:
        fnt_main = ImageFont.truetype('Hertical Sans Texture/Hertical Sans Texture.ttf', 200)
        fnt = ImageFont.truetype('Hertical Sans Texture/Hertical Sans Texture.ttf', 135)
    else:
        fnt_main = ImageFont.truetype('Hertical Sans Texture/Hertical Sans Texture.ttf', 230)
        fnt = ImageFont.truetype('Hertical Sans Texture/Hertical Sans Texture.ttf', 170)
    
    draw.text((185,480), number, color, font = fnt, anchor='mm') # slote 1
    draw.text((1250,400), number, color, font=fnt_main, anchor='mm') # main

    ing_avulso = ing_avulso.resize((1169, 620))
    posicao = (mesa-1) % 12
    if posicao == 0 :
        folha = Image.new('RGB',(3508,2480),(255,255,255))
    
    coordenadas = {
    0:  (0, 0),
    1:  (0, 620),
    2:  (0, 1240),
    3:  (0, 1860),
    4:  (1169, 0),
    5:  (1169, 620),
    6:  (1169, 1240),
    7:  (1169, 1860),
    8:  (2338, 0),
    9:  (2338, 620),
    10: (2338, 1240),
    11: (2338, 1860)
}

    folha.paste(ing_avulso, coordenadas[posicao])

    if posicao == 11 or mesa == 200:
        num_folha += 1
        nome_folha = f'ing_avulso_{num_folha}.png'
        folha.save(nome_folha)
        arquivos_folha.append(nome_folha)

with open("ingressos_avulsos.pdf", "wb") as f:
    f.write(img2pdf.convert(arquivos_folha))

print(f"pronto, a quantidade de folhas geradas foi {num_folha}")