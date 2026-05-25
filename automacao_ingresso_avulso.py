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

    ing_avulso = ing_avulso.resize((1488,698))
    posicao = (mesa-1) % 6
    if posicao == 0 :
        folha = Image.new('RGB',(3508,2480),(255,255,255))
    
    coordenadas = {
    0: (0, 0), #1
    1: (1488, 0), #2
    2: (0, 698), #3
    3: (1488, 698), #4
    4: (0, 1396), #5
    5: (1488, 1396) #6
}

    folha.paste(ing_avulso, coordenadas[posicao])

    if posicao == 5 or mesa == 200:
        num_folha += 1
        nome_folha = f'ing_avulso_{num_folha}.png'
        folha.save(nome_folha)
        arquivos_folha.append(nome_folha)

with open("ingressos_avulsos.pdf", "wb") as f:
    f.write(img2pdf.convert(arquivos_folha))

print(f"pronto, a quantidade de folhas geradas foi {num_folha}")