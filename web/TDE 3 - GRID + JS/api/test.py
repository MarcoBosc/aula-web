from PIL import Image, ImageDraw, ImageFont
import uuid

# gera um id para a nova imagem
random_uuid = uuid.uuid4()
random_uuid_str = str(random_uuid)
# Palavras para sobrepor na imagem
top_word = "Olá"
bottom_word = "Mundo"
# Abre a imagem
image = Image.open("dogeRainbow.jpg")
# Abre para sobreposição
draw = ImageDraw.Draw(image)
# Seta a fonte a ser usada
font = ImageFont.truetype('IMPACT.TTF', 50)
# Sobrepõe (escreve por cima) da imagem os textos inseridos
draw.text((310, 62), top_word, font=font)
draw.text((310, 533), bottom_word, font=font)
# salva a Imagem
image.save(f'imagem{random_uuid_str}.jpg')