import numpy as np

#np.random.seed(1337)

import random

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

# ÖVNING 2***************************
import requests 
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plot

image_url = 'https://images.unsplash.com/photo-1615751072497-5f5169febe17?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y3V0ZSUyMGRvZ3xlbnwwfHwwfHx8MA%3D%3D'

response = requests.get(image_url)
image_content = response.content

# Gör bilden läsbar med bytesio och Image.open
image = Image.open(BytesIO(image_content))
image_array = np.array(image)
image_array[10:1323, 10:990] = (255,0,0)
print(image_array.shape)

# spara bild
Image.fromarray(image_array).save("dog.png")

# Visa bilden:
#plot.imshow(image_array)
#plot.show()


