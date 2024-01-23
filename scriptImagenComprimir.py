from PIL import Image

# Carga la imagen
image = Image.open("./images/luna.jpg")

#Especifica la calidad de compresión deseada (valores entre 0 y 100)
quality = 50

# Guarda la imagen comprimida
image.save("./images/luna_comprimida.jpg",optimize=True, quality=quality)
