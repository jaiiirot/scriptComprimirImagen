from PIL import Image
import os
import zipfile

# Carpeta de origen
carpeta_origen = "./images/"

# Crea una lista de archivos en la carpeta de origen
archivos = os.listdir(carpeta_origen)

# Crea el archivo zip
nombre_zip = "imagenesComprimidas.zip"
with zipfile.ZipFile(nombre_zip, 'w') as zip_file:
    # Itera sobre cada archivo en la carpeta de origen
    for archivo in archivos:
        # Verifica si el archivo es una imagen (puedes ajustar esta condición según tus necesidades)
        if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Ruta completa del archivo de origen
            ruta_origen = os.path.join(carpeta_origen, archivo)

            # Carga la imagen
            imagen = Image.open(ruta_origen)

            # Especifica la calidad de compresión deseada (valores entre 0 y 100)
            calidad = 50

            # Guarda la imagen comprimida directamente en el archivo zip con su nombre original
            zip_file.writestr(archivo, imagen.tobytes(), optimize=True, quality=calidad)

print(f"Todas las imágenes han sido comprimidas y guardadas en {nombre_zip}")
