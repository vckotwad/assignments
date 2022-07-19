import os
from PIL import Image
import imagehash


hash0 = imagehash.average_hash(Image.open('querry.jpg')) 
cutoff = 9

filename='database'
database_directory=(os.listdir(os.path.join(os.getcwd(), filename)))

for file in database_directory:
   hash1 = imagehash.average_hash(Image.open("database/"+file)) 
   if hash0 - hash1 < cutoff:
      print(f'{file} is similar to query image')
   


