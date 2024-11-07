from PIL import Image
import sys

for arg in sys.argv: 
    print(arg)
    if arg.endswith('.jpeg') or arg.endswith('.jpg'):
        with Image.open(arg) as shittening_image:
            shittening_image.save(arg, "JPEG", quality=250, subsampling=0)
