from flask import Flask, request, jsonify
import base64
from PIL import Image
import io
import cv2
import numpy as np
import pytesseract

app = Flask(__name__)

@app.route('/realizar-ocr', methods=['POST'])
def realizar_ocr():
    try:
        # Obtener la imagen base64 desde la solicitud
        data = request.json
        imagen_base64 = data['imagen_base64']

        # Decodificar la imagen base64
        imagen_bytes = base64.b64decode(imagen_base64)

        # Crear una imagen PIL desde los bytes decodificados
        imagen_pil = Image.open(io.BytesIO(imagen_bytes))

        # Convertir la imagen PIL a una matriz numpy
        imagen_np = cv2.cvtColor(np.array(imagen_pil), cv2.COLOR_RGB2BGR)

        # Convertir la imagen a escala de grises
        gray = cv2.cvtColor(imagen_np, cv2.COLOR_BGR2GRAY)

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Utilizar pytesseract para reconocer texto en la imagen
        text = pytesseract.image_to_string(gray)

        # Dividir el texto en líneas
        lines = text.split('\n')

        # Buscar la línea que contiene "servicios"
        servicios_line = -1
        for i, line in enumerate(lines):
            if "servicios" in line.lower():
                servicios_line = i
                break

        if servicios_line != -1:
            y_position = servicios_line * 20  # Ajusta la cantidad de píxeles a recortar arriba
            x_position = 60  # Ajusta la cantidad de píxeles a recortar a la izquierda
            image_cropped = imagen_np[y_position:, x_position:]
        else:
            # Si no se encuentra "servicios," mantener la imagen original
            image_cropped = imagen_np

        # Guardar la imagen recortada
        cv2.imwrite('imagen_recortada.png', image_cropped)

        # Crear una imagen PIL desde la imagen recortada para hacer más cortes
        imagen_recortada_pil = Image.fromarray(cv2.cvtColor(image_cropped, cv2.COLOR_BGR2RGB))

        # Ejemplo de corte adicional en las coordenadas especificadas
        coordenadas_corte1 = (0, 0, 380, 130)
        parte_cortada1 = imagen_recortada_pil.crop(coordenadas_corte1)
        #parte_cortada1.save('parte_cortada1.png')

        # Ejemplo de corte adicional en las coordenadas especificadas
        coordenadas_corte2 = (382, 0, 650, 130)
        parte_cortada2 = imagen_recortada_pil.crop(coordenadas_corte2)
        #parte_cortada2.save('parte_cortada2.png')
        # Realizar otras operaciones con la imagen recortada si es necesario...

          # Crea una lista para almacenar el texto de cada imagen
        texto_imagenes = []

        # Crea tres nuevas imágenes vacías con el tamaño deseado (el tamaño de la imagen original)
        nueva_imagen1 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen2 = Image.new('RGB', imagen_recortada_pil.size)


        nueva_imagen1.paste(parte_cortada1.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen2.paste(parte_cortada2.resize(imagen_recortada_pil.size), (0, 0))

        nueva_imagen1.save('imagen_rearmada1.jpg')
        nueva_imagen2.save('imagen_rearmada2.jpg')

        imagen1 = Image.open('imagen_rearmada1.jpg')
        imagen2 = Image.open('imagen_rearmada2.jpg')

        texto_imagen1 = pytesseract.image_to_string(imagen1)
        texto_imagen2 = pytesseract.image_to_string(imagen2)

        texto_imagenes.append(texto_imagen1)
        texto_imagenes.append(texto_imagen2)

        for i, texto in enumerate(texto_imagenes):
          print(f"Texto de imagen {i + 1}:\n{texto}\n")



        return jsonify({'message': 'OCR realizado y operaciones adicionales completadas.'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
