#run first : pip install imagehash
import os, imagehash
from PIL import Image

files = os.listdir(".")
hashes = []

for file in files:

    # Check the image format
    if file.endswith(".jpg") or file.endswith(".png"): 
        # Read the image data using PIL lib
        image = Image.open(file)
        # Get image hash
        hash = str(imagehash.average_hash(image))
        # if hash already in list (= duplicate photo)    
        if(hash in hashes):
            os.remove(file)
        else:
            hashes.append(hash)
        
    else:
        continue