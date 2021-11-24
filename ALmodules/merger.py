from PIL import Image
import PIL
import requests
import glob
from math import ceil, sqrt
from typing import Union

# Credits to https://github.com/MyNameIsDark01 for the original Merger code.
# This merger is under rights, you may not take this code and use it in your own project without proper credits to Fevers and Dark.

def merger(loc1, mergewatermark, datas: Union[list, None] = None, save_as: str = 'merge.jpg'):
    if not datas:
        datas = [Image.open(i) for i in glob.glob('icons/*.png')]

    row_n = len(datas)
    if mergewatermark != '':
        row_n += 1
        
    rowslen = ceil(sqrt(row_n))
    columnslen = round(sqrt(row_n))

    mode = "RGB"
    px = 512

    rows = rowslen * px
    columns = columnslen * px
    image = Image.new(mode, (rows, columns))

    i = 0

    for card in datas:
        image.paste(
            card,
            ((0 + ((i % rowslen) * card.width)),
                (0 + ((i // rowslen) * card.height)))
        )

        i += 1
    
    if loc1 == '':
        if mergewatermark != '':
            r = requests.get(mergewatermark, allow_redirects=True)
            open('icons/zzzwatermark.png', 'wb').write(r.content)
            card = Image.open(f'icons/zzzwatermark.png')
            card = card.resize((512,512),PIL.Image.ANTIALIAS)
            image.paste(
                card,
                ((0 + ((i % rowslen) * card.width)),
                    (0 + ((i // rowslen) * card.height)))
            )

            i += 1

    if save_as and len(save_as) > 4:
        image.save(f"merged/{save_as}")
        image.show()

    return image
