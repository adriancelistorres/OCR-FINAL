from flask import Flask, request, jsonify
import base64
from PIL import Image
import io
import cv2
import numpy as np
import pytesseract
import os

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

        ## Servicios ##
        ###Primera Fila###
        coordenadas_corte1 = (0, 0, 395, 130)
        parte_cortada1 = imagen_recortada_pil.crop(coordenadas_corte1)
        #parte_cortada1.save('parte_cortada1.png')

        coordenadas_corte2 = (382, 0, 650, 130)
        parte_cortada2 = imagen_recortada_pil.crop(coordenadas_corte2)
        #parte_cortada2.save('parte_cortada2.png')

        coordenadas_corte3 = (770, 0, 1150, 130)
        parte_cortada3 = imagen_recortada_pil.crop(coordenadas_corte3)

        coordenadas_corte4 = (1150, 0, 1400, 130)
        parte_cortada4 = imagen_recortada_pil.crop(coordenadas_corte4)
        
        ###Segunda Fila###
        coordenadas_corte5 = (0, 132, 380, 230)
        parte_cortada5 = imagen_recortada_pil.crop(coordenadas_corte5)

        coordenadas_corte6 = (382, 132, 650, 230)
        parte_cortada6 = imagen_recortada_pil.crop(coordenadas_corte6)
        
        coordenadas_corte7 = (770, 132, 1080, 230)
        parte_cortada7 = imagen_recortada_pil.crop(coordenadas_corte7)

        ## Equipos ##
        ###Primera Fila###
        coordenadas_corte8 = (0, 232, 380, 362)
        parte_cortada8 = imagen_recortada_pil.crop(coordenadas_corte8)

        coordenadas_corte9 = (382, 232, 650, 362)
        parte_cortada9 = imagen_recortada_pil.crop(coordenadas_corte9)

        coordenadas_corte10 = (770, 232, 1150, 362)
        parte_cortada10 = imagen_recortada_pil.crop(coordenadas_corte10)

        coordenadas_corte11 = (1150, 232, 1500, 362)
        parte_cortada11 = imagen_recortada_pil.crop(coordenadas_corte11)

        ###Segunda Fila###
        coordenadas_corte12 = (0, 364, 220, 440)
        parte_cortada12 = imagen_recortada_pil.crop(coordenadas_corte12)

        coordenadas_corte13 = (382, 364, 650, 440)
        parte_cortada13 = imagen_recortada_pil.crop(coordenadas_corte13)

        ## Servicios Adicionales ##
        ###Primera Fila###
        coordenadas_corte14 = (0, 422, 365, 540)
        parte_cortada14 = imagen_recortada_pil.crop(coordenadas_corte14)

        coordenadas_corte15 = (382, 422, 650, 552)
        parte_cortada15 = imagen_recortada_pil.crop(coordenadas_corte15)

        coordenadas_corte16 = (770, 422, 1080, 552)
        parte_cortada16 = imagen_recortada_pil.crop(coordenadas_corte16)

        coordenadas_corte17 = (1150, 422, 1500, 552)
        parte_cortada17 = imagen_recortada_pil.crop(coordenadas_corte17)

        # Realizar otras operaciones con la imagen recortada si es necesario...

          # Crea una lista para almacenar el texto de cada imagen
        texto_imagenes = []

        # Crea tres nuevas imágenes vacías con el tamaño deseado (el tamaño de la imagen original)
        nueva_imagen1 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen2 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen3 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen4 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen5 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen6 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen7 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen8 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen9 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen10 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen11 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen12 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen13 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen14 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen15 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen16 = Image.new('RGB', imagen_recortada_pil.size)
        nueva_imagen17 = Image.new('RGB', imagen_recortada_pil.size)

        nueva_imagen1.paste(parte_cortada1.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen2.paste(parte_cortada2.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen3.paste(parte_cortada3.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen4.paste(parte_cortada4.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen5.paste(parte_cortada5.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen6.paste(parte_cortada6.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen7.paste(parte_cortada7.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen8.paste(parte_cortada8.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen9.paste(parte_cortada9.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen10.paste(parte_cortada10.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen11.paste(parte_cortada11.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen12.paste(parte_cortada12.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen13.paste(parte_cortada13.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen14.paste(parte_cortada14.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen15.paste(parte_cortada15.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen16.paste(parte_cortada16.resize(imagen_recortada_pil.size), (0, 0))
        nueva_imagen17.paste(parte_cortada17.resize(imagen_recortada_pil.size), (0, 0))

        nueva_imagen1.save('imagen_rearmada1.jpg')
        nueva_imagen2.save('imagen_rearmada2.jpg')
        nueva_imagen3.save('imagen_rearmada3.jpg')
        nueva_imagen4.save('imagen_rearmada4.jpg')
        nueva_imagen5.save('imagen_rearmada5.jpg')
        nueva_imagen6.save('imagen_rearmada6.jpg')
        nueva_imagen7.save('imagen_rearmada7.jpg')
        nueva_imagen8.save('imagen_rearmada8.jpg')
        nueva_imagen9.save('imagen_rearmada9.jpg')
        nueva_imagen10.save('imagen_rearmada10.jpg')
        nueva_imagen11.save('imagen_rearmada11.jpg')
        nueva_imagen12.save('imagen_rearmada12.jpg')
        nueva_imagen13.save('imagen_rearmada13.jpg')
        nueva_imagen14.save('imagen_rearmada14.jpg')
        nueva_imagen15.save('imagen_rearmada15.jpg')
        nueva_imagen16.save('imagen_rearmada16.jpg')
        nueva_imagen17.save('imagen_rearmada17.jpg')

        imagen_recortada_pil.close()

        imagen1 = Image.open('imagen_rearmada1.jpg')
        imagen2 = Image.open('imagen_rearmada2.jpg')
        imagen3 = Image.open('imagen_rearmada3.jpg')
        imagen4 = Image.open('imagen_rearmada4.jpg')
        imagen5 = Image.open('imagen_rearmada5.jpg')
        imagen6 = Image.open('imagen_rearmada6.jpg')
        imagen7 = Image.open('imagen_rearmada7.jpg')
        imagen8 = Image.open('imagen_rearmada8.jpg')
        imagen9 = Image.open('imagen_rearmada9.jpg')
        imagen10 = Image.open('imagen_rearmada10.jpg')
        imagen11 = Image.open('imagen_rearmada11.jpg')
        imagen12 = Image.open('imagen_rearmada12.jpg')
        imagen13 = Image.open('imagen_rearmada13.jpg')
        imagen14 = Image.open('imagen_rearmada14.jpg')
        imagen15 = Image.open('imagen_rearmada15.jpg')
        imagen16 = Image.open('imagen_rearmada16.jpg')
        imagen17 = Image.open('imagen_rearmada17.jpg')

        texto_imagen1 = pytesseract.image_to_string(imagen1)
        texto_imagen2 = pytesseract.image_to_string(imagen2)
        texto_imagen3 = pytesseract.image_to_string(imagen3)
        texto_imagen4 = pytesseract.image_to_string(imagen4)
        texto_imagen5 = pytesseract.image_to_string(imagen5)
        texto_imagen6 = pytesseract.image_to_string(imagen6)
        texto_imagen7 = pytesseract.image_to_string(imagen7)
        texto_imagen8 = pytesseract.image_to_string(imagen8)
        texto_imagen9 = pytesseract.image_to_string(imagen9)
        texto_imagen10 = pytesseract.image_to_string(imagen10)
        texto_imagen11 = pytesseract.image_to_string(imagen11)
        texto_imagen12 = pytesseract.image_to_string(imagen12)
        texto_imagen13 = pytesseract.image_to_string(imagen13)
        texto_imagen14 = pytesseract.image_to_string(imagen14)
        texto_imagen15 = pytesseract.image_to_string(imagen15)
        texto_imagen16 = pytesseract.image_to_string(imagen16)
        texto_imagen17 = pytesseract.image_to_string(imagen17)

        texto_imagenes.append(texto_imagen1.strip().split('\n'))
        texto_imagenes.append(texto_imagen2.strip().split('\n'))
        texto_imagenes.append(texto_imagen3.strip().split('\n'))
        texto_imagenes.append(texto_imagen4.strip().split('\n'))
        texto_imagenes.append(texto_imagen5.strip().split('\n'))
        texto_imagenes.append(texto_imagen6.strip().split('\n'))
        texto_imagenes.append(texto_imagen7.strip().split('\n'))
        texto_imagenes.append(texto_imagen8.strip().split('\n'))
        texto_imagenes.append(texto_imagen9.strip().split('\n'))
        texto_imagenes.append(texto_imagen10.strip().split('\n'))
        texto_imagenes.append(texto_imagen11.strip().split('\n'))
        texto_imagenes.append(texto_imagen12.strip().split('\n'))
        texto_imagenes.append(texto_imagen13.strip().split('\n'))
        texto_imagenes.append(texto_imagen14.strip().split('\n'))
        texto_imagenes.append(texto_imagen15.strip().split('\n'))
        texto_imagenes.append(texto_imagen16.strip().split('\n'))
        texto_imagenes.append(texto_imagen17.strip().split('\n'))

        imagen1.close()
        imagen2.close()
        imagen3.close()
        imagen4.close()
        imagen5.close()
        imagen6.close()
        imagen7.close()
        imagen8.close()
        imagen9.close()
        imagen10.close()
        imagen11.close()
        imagen12.close()
        imagen13.close()
        imagen14.close()
        imagen15.close()
        imagen16.close()
        imagen17.close()

        # Elimina las imágenes del disco duro
        imagenes_a_eliminar = [
        'imagen_rearmada1.jpg', 'imagen_rearmada2.jpg', 'imagen_rearmada3.jpg', 'imagen_rearmada4.jpg',
        'imagen_rearmada5.jpg', 'imagen_rearmada6.jpg', 'imagen_rearmada7.jpg',
        'imagen_rearmada8.jpg', 'imagen_rearmada9.jpg', 'imagen_rearmada10.jpg', 'imagen_rearmada11.jpg',
        'imagen_rearmada12.jpg', 'imagen_rearmada13.jpg',
        'imagen_rearmada14.jpg', 'imagen_rearmada15.jpg', 'imagen_rearmada16.jpg', 'imagen_rearmada17.jpg'
        ]

        for imagen in imagenes_a_eliminar:
                try:
                        os.remove(imagen)
                        print(f"Imagen {imagen} eliminada.")
                except FileNotFoundError:
                        print(f"La imagen {imagen} no se encontró.")
                except Exception as e:
                        print(f"Error al eliminar la imagen {imagen}: {e}")

        # Eliminar elementos en blanco de cada sublista
        texto_imagenes_sin_en_blanco = [
            [elemento for elemento in sublista if elemento != ""] for sublista in texto_imagenes
        ]

        for i, texto in enumerate(texto_imagenes_sin_en_blanco):
          print(f"Texto de imagen {i}:\n{texto}\n")

        # Presentación JSON
        data = {
            "Servicios": {},
            "Equipos": {},
            "Servicios_Adicionales": {}
        }

        
        # data["Servicios"] = {
        #     texto_imagenes_sin_en_blanco[0][1]: texto_imagenes_sin_en_blanco[0][2],
        #     texto_imagenes_sin_en_blanco[1][0]: texto_imagenes_sin_en_blanco[1][1],
        #     texto_imagenes_sin_en_blanco[2][0]: texto_imagenes_sin_en_blanco[2][1],
        #     texto_imagenes_sin_en_blanco[3][0]: texto_imagenes_sin_en_blanco[3][1],
        #     texto_imagenes_sin_en_blanco[4][0]: texto_imagenes_sin_en_blanco[4][2] if len(texto_imagenes_sin_en_blanco[4]) > 2 else texto_imagenes_sin_en_blanco[4][1],
        #     texto_imagenes_sin_en_blanco[5][0]: texto_imagenes_sin_en_blanco[5][1] if len(texto_imagenes_sin_en_blanco[5]) > 1 else "-",
        #     texto_imagenes_sin_en_blanco[6][0]: texto_imagenes_sin_en_blanco[6][1]
        # }

        # data["Equipos"] = {
        #     texto_imagenes_sin_en_blanco[7][1]: texto_imagenes_sin_en_blanco[7][2],
        #     texto_imagenes_sin_en_blanco[8][0]: texto_imagenes_sin_en_blanco[8][1],
        #     texto_imagenes_sin_en_blanco[9][0]: texto_imagenes_sin_en_blanco[9][2] if len(texto_imagenes_sin_en_blanco[9]) > 2 else texto_imagenes_sin_en_blanco[9][1],
        #     texto_imagenes_sin_en_blanco[10][0]: texto_imagenes_sin_en_blanco[10][2] if len(texto_imagenes_sin_en_blanco[10]) > 2 else texto_imagenes_sin_en_blanco[10][1],
        #     texto_imagenes_sin_en_blanco[11][0]: texto_imagenes_sin_en_blanco[11][1],
        #     texto_imagenes_sin_en_blanco[12][0]: texto_imagenes_sin_en_blanco[12][1]
        # }

        # data["Servicios_Adicionales"] = {
        #     texto_imagenes_sin_en_blanco[13][1]: texto_imagenes_sin_en_blanco[13][2],
        #     texto_imagenes_sin_en_blanco[14][0]: texto_imagenes_sin_en_blanco[14][1],
        #     texto_imagenes_sin_en_blanco[15][0]: texto_imagenes_sin_en_blanco[15][1],
        #     texto_imagenes_sin_en_blanco[16][0]: texto_imagenes_sin_en_blanco[16][1]
        # }

        data["Servicios"] = {
            # "CantidadLineasMovilesDisponibles": texto_imagenes_sin_en_blanco[0][2] if texto_imagenes_sin_en_blanco[0][2] == "l" else "1",
            "CantidadLineasMovilesDisponibles": "1" if texto_imagenes_sin_en_blanco[0][2] == "l" else texto_imagenes_sin_en_blanco[0][2],
            "CargoFijoMaximoPorLineaPack": texto_imagenes_sin_en_blanco[1][1],""
            "MetodoDeFacturacionAdelantado": texto_imagenes_sin_en_blanco[2][1],
            "TipoDePlan": texto_imagenes_sin_en_blanco[3][1],
            "CargoFijoMaximoPorLineaMovilSinEquipoFinanciado": texto_imagenes_sin_en_blanco[4][2] if len(texto_imagenes_sin_en_blanco[4]) > 2 else texto_imagenes_sin_en_blanco[4][1],
            "TipoCliente": texto_imagenes_sin_en_blanco[5][1] if len(texto_imagenes_sin_en_blanco[5]) > 1 else "-",
            "MontoMaximoEasyPack": texto_imagenes_sin_en_blanco[6][1]
        }

        data["Equipos"] = {
            "MontoMaximoFinanciarEquipoAccesorios": texto_imagenes_sin_en_blanco[7][2],
            "MontoOcupadoEnFinanciamiento": texto_imagenes_sin_en_blanco[8][1],
            "MontoDisponibleFinanciamientoAccesorios": texto_imagenes_sin_en_blanco[9][2] if len(texto_imagenes_sin_en_blanco[9]) > 2 else texto_imagenes_sin_en_blanco[9][1],
            "CantidadMesesFinanciamientoAccesorios": texto_imagenes_sin_en_blanco[10][2] if len(texto_imagenes_sin_en_blanco[10]) > 2 else texto_imagenes_sin_en_blanco[10][1],
            "RatioDeFinanciamiento": texto_imagenes_sin_en_blanco[11][1],
            "TipoClienteVEP": texto_imagenes_sin_en_blanco[12][1] if len(texto_imagenes_sin_en_blanco[12]) > 1 else "-"
        }

        data["Servicios_Adicionales"] = {
            "MontoDisponibleContratarServiciosAdicionales": texto_imagenes_sin_en_blanco[13][2],
            "MontoDisponiblePrimasDeSeguros": texto_imagenes_sin_en_blanco[14][1],
            "CupoServiciosComplementarios": texto_imagenes_sin_en_blanco[15][1],
            "MontoAcreditarDeuda": texto_imagenes_sin_en_blanco[16][1]
        }


        return jsonify({'message': data}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
