from PIL import Image,ImageDraw, ImageFont
import img2pdf

template = Image.open("id_mesas.png")
color = (70,41,10) 

num_folha = 0
arquivos_folhas = []

for mesa in range(1, 115):
    number = str(mesa).zfill(2)
    id_mesa = template.copy()
    draw = ImageDraw.Draw(id_mesa)
    if mesa >=100:
        fnt_main = ImageFont.truetype('Hertical Sans Texture/Hertical Sans Texture.ttf', 500)
    else:
        fnt_main = ImageFont.truetype('Hertical Sans Texture/Hertical Sans Texture.ttf', 500)    

    #numero debaixo
    draw.text((690, 1600), number, color, fnt_main, anchor='mm')

    #imagem temporaria
    temp = Image.new('RGBA', id_mesa.size, (0,0,0,0))
    #numero invertido
    draw_temp = ImageDraw.Draw(temp)
    draw_temp.text((690,1600), number, color, fnt_main, anchor='mm')
    temp = temp.rotate(180)
    id_mesa.paste(temp, (0, 0), temp)

    num_folha += 1
    nome_arquivo = f"id_mesas_{num_folha}.png"
    id_mesa.save(nome_arquivo)
    arquivos_folhas.append(nome_arquivo)

with open("id_mesa.pdf","wb") as f:
    f.write(img2pdf.convert(arquivos_folhas))

print(f"pronto, a quantidade de folhas geradas foi {num_folha}")