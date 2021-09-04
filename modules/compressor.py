import PIL
import math
from PIL import Image
from colorama import Fore

def compressnewcosmetics_normal(xlol):
    foo = Image.open(f"merged/MERGED {xlol}.png")
    x, y = foo.size
    x2, y2 = math.floor(x/2), math.floor(y/2)
    foo = foo.resize((x2,y2),Image.ANTIALIAS)
    foo.save(f"merged/MERGED {xlol}.png",quality=65)
    print('Compressed image!')

def compress_brnews():
    foo = Image.open("brnews.png")
    x, y = foo.size
    x2, y2 = math.floor(x/2), math.floor(y/2)
    foo = foo.resize((x2,y2),Image.ANTIALIAS)
    foo.save("Compressed_news.png",quality=65)
    print('Compressed image!')

def compress_normal(x):
    foo = Image.open(f'merged/MERGED {x}.png')
    x, y = foo.size
    x2, y2 = math.floor(x/2), math.floor(y/2)
    foo = foo.resize((x2,y2),Image.ANTIALIAS)
    foo.save(f'merged/MERGED {x}.png',quality=65)
    print(Fore.GREEN + 'Compressed!')

def pak_compress(ask, x):
    foo = Image.open(f'merged/Pak {ask} Merged.png')
    x, y = foo.size
    x2, y2 = math.floor(x/2), math.floor(y/2)
    foo = foo.resize((x2,y2),Image.ANTIALIAS)
    foo.save(f'merged/MERGED {x}.png',quality=65)
    print(Fore.GREEN + 'Compressed!' + Fore.CYAN)

def compressnewcosmetics_new(lol):
    foo = Image.open(f'merged/MERGED {lol}.png')
    x, y = foo.size
    x2, y2 = math.floor(x/2), math.floor(y/2)
    foo = foo.resize((x2,y2),Image.ANTIALIAS)
    foo.save(f'merged/MERGED {lol}.png',quality=65)
    print(Fore.GREEN + 'Compressed!' + Fore.CYAN)