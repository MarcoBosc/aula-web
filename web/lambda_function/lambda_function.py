import json
import os
import base64
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

def lambda_handler(event, context):
    try:
        # Decodifica os dados da requisição
        request_data = json.loads(event['body'])
        top_word = request_data.get('top_word', 'Olá')  # Palavra superior padrão
        bottom_word = request_data.get('bottom_word', 'Mundo')  # Palavra inferior padrão
        
        # Abre a imagem
        image_path = os.path.join(os.path.dirname(__file__), 'dogeRainbow.jpg')
        image = Image.open(image_path)

        # Seta a fonte a ser usada
        font_path = os.path.join(os.path.dirname(__file__), 'IMPACT.TTF')
        font = ImageFont.truetype(font_path, 50)

        # Abre para sobreposição
        draw = ImageDraw.Draw(image)

        # Sobrepõe (escreve por cima) da imagem os textos inseridos
        draw.text((310, 62), top_word, font=font)
        draw.text((310, 533), bottom_word, font=font)

        # Salva a imagem editada em memória
        edited_image_io = BytesIO()
        image.save(edited_image_io, format='JPEG')
        edited_image_io.seek(0)

        # Codifica a imagem editada em base64
        edited_image_base64 = base64.b64encode(edited_image_io.getvalue()).decode('utf-8')

        # Formata a resposta
        response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "image/jpeg"
            },
            "body": edited_image_base64,
            "isBase64Encoded": True
        }
    except Exception as e:
        # Se ocorrer algum erro, retorna uma resposta de erro
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

    return response
