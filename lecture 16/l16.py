import numpy as np
import random

#np.random.seed(1337)

''' övning 1 '''
# skapa matris med python-kod
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        value = random.randint(1, 10)
        row.append(value)
    matrix.append(row)

# Skriv ut matrisen
i = 0
for row in matrix:
    print(f"matrix row {i}: {row}")
    i += 1


# skapa array 1-9, 3x3 via numpy
arr = np.arange(1,10).reshape(3,3)
arr.dtype="uint64"
print(f"\nShape: {arr.shape}\ndtype: {arr.dtype}\nSize: {arr.size}\n\nArr: {arr}\n")

# Skapa en 3x3 matris med randomiserade heltalsvärden mellan 1 till 10
matris = np.random.randint(1, 11, size=(3, 3))
print(f"matris 3x3: \n{matris}\n")

m2 = matris * 2
print(f"Matris 3x3 * 2:\n{m2}\n")

medelvardet = np.mean(m2)
print(f"Medelvärdet på hela matrisen är:, {medelvardet:.3f}")

m3 = m2 + matrix
print(f"\nm2: \n{m2}\nmatrix: \n{matrix}\n2 matriser adderas: \n{m3}\n---\n\n")


''' övning 2 '''
import requests 
from PIL import Image
from io import BytesIO
#import matplotlib.pyplot as plot

image_url = 'https://images.unsplash.com/photo-1615751072497-5f5169febe17?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y3V0ZSUyMGRvZ3xlbnwwfHwwfHx8MA%3D%3D'

response = requests.get(image_url)
image_content = response.content

# Gör bilden läsbar med bytesio och Image.open
image = Image.open(BytesIO(image_content))
image_array = np.array(image)

# modifiera bilden
new_color = (255,0,0)
image_red = image_array
image_red[::2, 500:1000:2] = new_color
#image_array += image_red

#image_array[31:-31:2, 31:-31:2] = (222,22,222)
image_array[0:31, 0:1000] = new_color

print(image_array.shape)

# spara bild
Image.fromarray(image_array).save("dog.png")

# Visa bilden:
#plot.imshow(image_array)
#plot.show()

''' rita en röd ruta 100x100 pixlar, posistion 100x100 '''
image = Image.open("dog.png")
# pixel_color före:
pixel_value = image.getpixel((101, 101))
print("Pixel färg innan mod ", pixel_value)

for i in range(100):
    for j in range(100):
        image.putpixel((100+i, 100+j), new_color)

image.save("changed_dog.png")
# pixeö_color efter:
pixel_value = image.getpixel((101, 101))
print("Pixel efter mod till röd: ",pixel_value)


## modifiera bilden
#from PIL import Image, ImageDraw
#image_red = image_array.copy().size
#red_mask = np.all(image_array == [255, 0, 0], axis=2)
#image_red[red_mask, :] = [255, 0, 0, 128] 
#
## kombinera de ursprungliga och modifierade bilderna
#image_blend = Image.blend(image, Image.fromarray(image_red.astype(np.uint8)), alpha=0.5) 
#image_blend.save("dog_with_transparent_red.png")