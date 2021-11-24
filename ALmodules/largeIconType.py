"""
Large Icon design license

Copyright (c) Mattheo_

All Rights Reserved. You are not allowed to redistribute this design as your own.

Permission is hereby granted, free of charge, to any person obtaining a verbatim
copy of this design and associated documentation files (the "Design"),
This design is open-source only for Educational Purposes, if you learn/copy-over anything from it you must give appropriate credit,
provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner.

***** This deisgn may be used as long as credit (to MattTheo_) is visible at all times.
***** Please do not modify the original design/copy it- instead keep the design's identity clear.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Design.

THE DESIGN IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE DESIGN OR THE USE OR OTHER DEALINGS IN THE
DESIGN.
"""

import requests
from PIL import Image, ImageFont, ImageDraw
import PIL
import os

import glob
from math import ceil, sqrt
from typing import Union
from colorama import *
init()


def large_merger( datas: Union[list, None] = None, save_as: str = 'merge.jpg'):
    if not datas:
        datas = [Image.open(i) for i in glob.glob('icons/*.png')]

    row_n = len(datas)
        
    rowslen = ceil(sqrt(row_n))
    columnslen = round(sqrt(row_n))

    mode = "RGB"
    px = 512

    rows = rowslen * 1793
    columns = columnslen * 1080
    image = Image.new(mode, (rows, columns))

    i = 0

    for card in datas:
        image.paste(
            card,
            ((0 + ((i % rowslen) * card.width)),
                (0 + ((i // rowslen) * card.height)))
        )

        i += 1

    if save_as and len(save_as) > 4:
        image.save(f"merged/{save_as}")
        #image.show()

    return image

def largeicontype(useFeaturedIfAvaliable, language):
    response = requests.get('https://fortnite-api.com/v2/cosmetics/br/new')

    count = 0
    items = len(response.json()['data']['items'])

    version = response.json()['data']['build']
    print(f'Loaded build {version}')
    print(f'Generating {items} items...\n')
    for i in response.json()['data']['items']:
        id = i['id']

        if useFeaturedIfAvaliable == 'True':
            if i["images"]["featured"] != None:
                url = i["images"]["featured"]
            else:
                if i['images']['icon'] != None:
                    url = i['images']['icon']
                else:
                    url = 'https://i.ibb.co/KyvMydQ/do-Not-Delete.png'
        else:
            if i['images']['icon'] != None:
                url = i['images']['icon']
            else:
                url = 'https://i.ibb.co/KyvMydQ/do-Not-Delete.png'
        r = requests.get(url)
        open(f'cache/{id}temp.png', 'wb').write(r.content)

        # RARITY GEN #
        iconImg = Image.open(f'cache/{id}temp.png')
        iconImg.resize((1083,1083),PIL.Image.ANTIALIAS)

        rarity = i["rarity"]['value']
        rarity = rarity.lower()
        #rarity = 'common'

        try:
            raritybackground = Image.open(f'rarities/cataba/{rarity}.png').resize((1083, 1083), Image.ANTIALIAS).convert("RGBA")
        except:
            raritybackground = Image.open(f'rarities/cataba/common.png').resize((1083, 1083), Image.ANTIALIAS).convert("RGBA")

        img=Image.new("RGB",(1083,1083))
        img.paste(raritybackground)

        iconimg = Image.open(f'cache/{id}temp.png').resize((1083, 1083), Image.ANTIALIAS).convert("RGBA")
        img.paste(iconimg, (0,0), iconimg)
        img.save(f'cache/{id}.png')
        try:
            os.remove(f'cache/{id}temp.png')
        except Exception as e:
            print(e)
            pass
        # RARITY GEN #

        # CARD GEN #
        img=Image.new("RGB",(1793,1080))

        finishedIcon = Image.open(f'cache/{id}.png').resize((1083, 1083), Image.ANTIALIAS).convert("RGBA")
        img.paste(finishedIcon, (710, 0), finishedIcon)

        os.remove(f'cache/{id}.png')

        card = Image.open(f'rarities/large/card.png').convert("RGBA")
        img.paste(card, (0,0), card)

        img.save(f'cache/LargeTemp-{id}.png')

        background = Image.open(f'cache/LargeTemp-{id}.png')

        #Watermark
        watermark = Image.open(f'rarities/large/watermark.png').convert("RGBA")
        background.paste(watermark, (0, 0), watermark)
        #

        loadFont = 'fonts/BurbankBigRegular-Black.ttf'
        font=ImageFont.truetype(loadFont,60)

        name = i['name']
        name=name.upper()
        draw=ImageDraw.Draw(background)
        draw.text((30,55),name,font=font,fill='white')


        loadFont = 'fonts/BurbankBigRegular-BlackItalic.otf'
        font=ImageFont.truetype(loadFont,39)
        desc = i['description']
        desc=desc.upper()
        import textwrap
        newdesc = textwrap.fill(desc, 30)

        draw=ImageDraw.Draw(background)
        draw.text((34,210),newdesc,font=font,fill='white')

        # Button
        rarity = i['rarity']['value']
        raritylen = len(rarity)
        raritywidth = font.getsize(rarity)[0]

        raritytag_w = raritywidth + 40

        raritytag=Image.new("RGB",(raritytag_w,48), color = 0xfffafa).convert('RGBA') # Draws Rarity Button Tag

        background.paste(raritytag, (28, 124), raritytag)

        # RARITY BUTTON TEXT
        rarity=rarity.upper()
        draw=ImageDraw.Draw(background)
        draw.text((32,131),rarity,font=font,fill='black') # Draws Rarity Button Text

        # Backend Value Text

        backend_x = raritytag_w + 28 + 20

        backend = i['type']['value']
        backend=backend.upper()
        draw=ImageDraw.Draw(background)
        draw.text((backend_x,133),backend,font=font,fill='white')


        font=ImageFont.truetype(loadFont,35)
        try:
            set = i['set']['value']
        except:
            set = 'N/A'
        draw.text((20,935),f'Set: {set}',font=font,fill=0xc8c5c4)

        id = i['id']
        font=ImageFont.truetype(loadFont,25)
        draw.text((20,995),f'ID:  {id}',font=font,fill=0xc8c5c4)

        try:
            seasonnum = f"C{i['introduction']['chapter']} S{i['introduction']['season']}"
        except:
            seasonnum = 'N/A'

        otherdesc = f'{seasonnum}'
        try:
            for x in i['gameplayTags']:
                if 'ItemShop' in x:
                    otherdesc = f'{seasonnum} | ITEMSHOP'
                    break
        except:
            pass

        font=ImageFont.truetype(loadFont,35)
        draw.text((20,1035),otherdesc,font=font,fill=0xc8c5c4)

        #Variant Gen
        variants = i['variants']
        variantnum = 0
        if i['variants'] != None:
            plus_sign = Image.open(f'rarities/large/PlusSign.png').convert("RGBA")
            background.paste(plus_sign, (0,0), plus_sign)

            variants_text = Image.open(f'rarities/large/VariantsText.png').convert("RGBA")
            background.paste(variants_text, (0,0), variants_text)

            for x in i['variants'][0]['options']:
                if x['name'] != 'DEFAULT':
                    variantbox=Image.new("RGB",(157,157), color = 0x211f20).convert('RGBA')

                    name = x['name']
                    url = x['image']
                    r = requests.get(url)
                    open(f'cache/variant_{name}.png', 'wb').write(r.content)
                    varianticon = Image.open(f'cache/variant_{name}.png').resize((157, 157), Image.ANTIALIAS).convert("RGBA")
                    variantbox.paste(varianticon, (0,0), varianticon)
                    
                    variantbox.save(f'cache/V_{name}.png')
                    os.remove(f'cache/variant_{name}.png')

                    varianticon = Image.open(f'cache/V_{name}.png').convert("RGBA")
                    
                    variantnum = variantnum + 1
                    
                    xnum = 24
                    if variantnum == 1:
                        xnum = 24
                    elif variantnum == 2:
                        xnum = 204 # 180
                    elif variantnum == 3:
                        xnum = 384 # 180

                    ynum = 390
                    if variantnum == 4:
                        xnum = 24
                        ynum = 570
                    elif variantnum == 5:
                        xnum = 204
                        ynum = 570
                    elif variantnum == 6:
                        xnum = 384
                        ynum = 570
                        
                    background.paste(varianticon, (xnum, ynum), varianticon)
                    os.remove(f'cache/V_{name}.png')


            font=ImageFont.truetype(loadFont,35)
            draw.text((230,340),f'{variantnum}',font=font,fill=0x999999)
            #print(f'Variants: {variantnum}')
        


        # CARD GEN #



        background.save(f'icons/{id}.png')
        os.remove(f'cache/LargeTemp-{id}.png')
        #largeicontype_search(useFeaturedIfAvaliable)
        count = count + 1
        print(f'{count}/{items}')
    print('\nDone generating items! Merging images...')
    large_merger()

def largeicontype_search(useFeaturedIfAvaliable, language):
    print('\nWhat cosmetic do you want to lookup? (Enter name or enter an ID by doing ID:CID_Example_ID)')
    name = input('>> ')
    response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?name={name}&language={language}')

    if 'ID:' in name:
        id = name.replace('ID:', '')
        response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={id}&language={language}')

    status = response.json()['status']
    if status != 200:
        print(f"Error: Status {response.json()['status']}")
        largeicontype_search(useFeaturedIfAvaliable, language)
    i = response.json()['data']
    id = i['id']

    if useFeaturedIfAvaliable == 'True':
        if i["images"]["featured"] != None:
            url = i["images"]["featured"]
        else:
            if i['images']['icon'] != None:
                url = i['images']['icon']
            else:
                url = 'https://i.ibb.co/KyvMydQ/do-Not-Delete.png'
    else:
        if i['images']['icon'] != None:
            url = i['images']['icon']
        else:
            url = 'https://i.ibb.co/KyvMydQ/do-Not-Delete.png'
    r = requests.get(url)
    open(f'cache/{id}temp.png', 'wb').write(r.content)

    # RARITY GEN #
    iconImg = Image.open(f'cache/{id}temp.png')
    iconImg.resize((1083,1083),PIL.Image.ANTIALIAS)

    rarity = i["rarity"]['value']
    rarity = rarity.lower()
    #rarity = 'common'

    try:
        raritybackground = Image.open(f'rarities/cataba/{rarity}.png').resize((1083, 1083), Image.ANTIALIAS).convert("RGBA")
    except:
        raritybackground = Image.open(f'rarities/cataba/common.png').resize((1083, 1083), Image.ANTIALIAS).convert("RGBA")

    img=Image.new("RGB",(1083,1083))
    img.paste(raritybackground)

    iconimg = Image.open(f'cache/{id}temp.png').resize((1083, 1083), Image.ANTIALIAS).convert("RGBA")
    img.paste(iconimg, (0,0), iconimg)
    img.save(f'cache/{id}.png')
    try:
        os.remove(f'cache/{id}temp.png')
    except Exception as e:
        print(e)
        pass
    # RARITY GEN #

    # CARD GEN #
    img=Image.new("RGB",(1793,1080))

    finishedIcon = Image.open(f'cache/{id}.png').resize((1083, 1083), Image.ANTIALIAS).convert("RGBA")
    img.paste(finishedIcon, (710, 0), finishedIcon)

    os.remove(f'cache/{id}.png')

    card = Image.open(f'rarities/large/card.png').convert("RGBA")
    img.paste(card, (0,0), card)

    img.save(f'cache/LargeTemp-{id}.png')

    background = Image.open(f'cache/LargeTemp-{id}.png')

    #Watermark
    watermark = Image.open(f'rarities/large/watermark.png').convert("RGBA")
    background.paste(watermark, (0, 0), watermark)
    #

    loadFont = 'fonts/BurbankBigRegular-Black.ttf'
    font=ImageFont.truetype(loadFont,60)

    name = i['name']
    name=name.upper()
    draw=ImageDraw.Draw(background)
    draw.text((30,55),name,font=font,fill='white')


    loadFont = 'fonts/BurbankBigRegular-BlackItalic.otf'
    font=ImageFont.truetype(loadFont,39)
    desc = i['description']
    desc=desc.upper()
    import textwrap
    newdesc = textwrap.fill(desc, 30)

    draw=ImageDraw.Draw(background)
    draw.text((34,210),newdesc,font=font,fill='white')

    # Button
    rarity = i['rarity']['value']
    raritylen = len(rarity)
    raritywidth = font.getsize(rarity)[0]

    raritytag_w = raritywidth + 40

    raritytag=Image.new("RGB",(raritytag_w,48), color = 0xfffafa).convert('RGBA') # Draws Rarity Button Tag

    background.paste(raritytag, (28, 124), raritytag)

    # RARITY BUTTON TEXT
    rarity=rarity.upper()
    draw=ImageDraw.Draw(background)
    draw.text((32,131),rarity,font=font,fill='black') # Draws Rarity Button Text

    # Backend Value Text

    backend_x = raritytag_w + 28 + 20

    backend = i['type']['value']
    backend=backend.upper()
    draw=ImageDraw.Draw(background)
    draw.text((backend_x,133),backend,font=font,fill='white')


    font=ImageFont.truetype(loadFont,35)
    try:
        set = i['set']['value']
    except:
        set = 'N/A'
    draw.text((20,935),f'Set: {set}',font=font,fill=0xc8c5c4)

    id = i['id']
    font=ImageFont.truetype(loadFont,25)
    draw.text((20,995),f'ID:  {id}',font=font,fill=0xc8c5c4)

    try:
        seasonnum = f"C{i['introduction']['chapter']} S{i['introduction']['season']}"
    except:
        seasonnum = 'N/A'

    otherdesc = f'{seasonnum}'
    try:
        for x in i['gameplayTags']:
            if 'ItemShop' in x:
                otherdesc = f'{seasonnum} | ITEMSHOP'
                break
    except:
        pass

    font=ImageFont.truetype(loadFont,35)
    draw.text((20,1035),otherdesc,font=font,fill=0xc8c5c4)

    #Variant Gen
    variants = i['variants']
    variantnum = 0
    if i['variants'] != None:
        plus_sign = Image.open(f'rarities/large/PlusSign.png').convert("RGBA")
        background.paste(plus_sign, (0,0), plus_sign)

        variants_text = Image.open(f'rarities/large/VariantsText.png').convert("RGBA")
        background.paste(variants_text, (0,0), variants_text)

        for x in i['variants'][0]['options']:
            if x['name'] != 'DEFAULT':
                variantbox=Image.new("RGB",(157,157), color = 0x211f20).convert('RGBA')

                name = x['name']
                url = x['image']
                r = requests.get(url)
                open(f'cache/variant_{name}.png', 'wb').write(r.content)
                varianticon = Image.open(f'cache/variant_{name}.png').resize((157, 157), Image.ANTIALIAS).convert("RGBA")
                variantbox.paste(varianticon, (0,0), varianticon)
                
                variantbox.save(f'cache/V_{name}.png')
                os.remove(f'cache/variant_{name}.png')

                varianticon = Image.open(f'cache/V_{name}.png').convert("RGBA")
                
                variantnum = variantnum + 1
                
                xnum = 24
                if variantnum == 1:
                    xnum = 24
                elif variantnum == 2:
                    xnum = 204 # 180
                elif variantnum == 3:
                    xnum = 384 # 180

                ynum = 390
                if variantnum == 4:
                    xnum = 24
                    ynum = 570
                elif variantnum == 5:
                    xnum = 204
                    ynum = 570
                elif variantnum == 6:
                    xnum = 384
                    ynum = 570
                    
                background.paste(varianticon, (xnum, ynum), varianticon)
                os.remove(f'cache/V_{name}.png')


        font=ImageFont.truetype(loadFont,35)
        draw.text((230,340),f'{variantnum}',font=font,fill=0x999999)
        #print(f'Variants: {variantnum}')
    


    # CARD GEN #



    background.save(f'icons/{id}.png')
    os.remove(f'cache/LargeTemp-{id}.png')
    print(Fore.CYAN+'--Saved image to Icons folder!--'+Fore.GREEN)
    largeicontype_search(useFeaturedIfAvaliable, language)

def largeicontype_pak(useFeaturedIfAvaliable, language):
    print('\nWhat Pak do you want to get cosmetics from?')
    pak = input('>> ')
    print('')

    response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search/all?dynamicPakId={pak}&language={language}')
    if response.json()['status'] != 200:
        print(f"ERROR: {response.json()['error']}")
        largeicontype(useFeaturedIfAvaliable, language)
        

    count = 0
    items = len(response.json()['data'])
    for i in response.json()['data']:
        id = i['id']

        if useFeaturedIfAvaliable == 'True':
            if i["images"]["featured"] != None:
                url = i["images"]["featured"]
            else:
                if i['images']['icon'] != None:
                    url = i['images']['icon']
                else:
                    url = 'https://i.ibb.co/KyvMydQ/do-Not-Delete.png'
        else:
            if i['images']['icon'] != None:
                url = i['images']['icon']
            else:
                url = 'https://i.ibb.co/KyvMydQ/do-Not-Delete.png'
        r = requests.get(url)
        open(f'cache/{id}temp.png', 'wb').write(r.content)

        # RARITY GEN #
        iconImg = Image.open(f'cache/{id}temp.png')
        iconImg.resize((1083,1083),PIL.Image.ANTIALIAS)

        rarity = i["rarity"]['value']
        rarity = rarity.lower()
        #rarity = 'common'

        try:
            raritybackground = Image.open(f'rarities/cataba/{rarity}.png').resize((1083, 1083), Image.ANTIALIAS).convert("RGBA")
        except:
            raritybackground = Image.open(f'rarities/cataba/common.png').resize((1083, 1083), Image.ANTIALIAS).convert("RGBA")

        img=Image.new("RGB",(1083,1083))
        img.paste(raritybackground)

        iconimg = Image.open(f'cache/{id}temp.png').resize((1083, 1083), Image.ANTIALIAS).convert("RGBA")
        img.paste(iconimg, (0,0), iconimg)
        img.save(f'cache/{id}.png')
        try:
            os.remove(f'cache/{id}temp.png')
        except Exception as e:
            print(e)
            pass
        # RARITY GEN #

        # CARD GEN #
        img=Image.new("RGB",(1793,1080))

        finishedIcon = Image.open(f'cache/{id}.png').resize((1083, 1083), Image.ANTIALIAS).convert("RGBA")
        img.paste(finishedIcon, (710, 0), finishedIcon)

        os.remove(f'cache/{id}.png')

        card = Image.open(f'rarities/large/card.png').convert("RGBA")
        img.paste(card, (0,0), card)

        img.save(f'cache/LargeTemp-{id}.png')

        background = Image.open(f'cache/LargeTemp-{id}.png')

        #Watermark
        watermark = Image.open(f'rarities/large/watermark.png').convert("RGBA")
        background.paste(watermark, (0, 0), watermark)
        #

        loadFont = 'fonts/BurbankBigRegular-Black.ttf'
        font=ImageFont.truetype(loadFont,60)

        name = i['name']
        name=name.upper()
        draw=ImageDraw.Draw(background)
        draw.text((30,55),name,font=font,fill='white')


        loadFont = 'fonts/BurbankBigRegular-BlackItalic.otf'
        font=ImageFont.truetype(loadFont,39)
        desc = i['description']
        desc=desc.upper()
        import textwrap
        newdesc = textwrap.fill(desc, 30)

        draw=ImageDraw.Draw(background)
        draw.text((34,210),newdesc,font=font,fill='white')

        # Button
        rarity = i['rarity']['value']
        raritylen = len(rarity)
        raritywidth = font.getsize(rarity)[0]

        raritytag_w = raritywidth + 40

        raritytag=Image.new("RGB",(raritytag_w,48), color = 0xfffafa).convert('RGBA') # Draws Rarity Button Tag

        background.paste(raritytag, (28, 124), raritytag)

        # RARITY BUTTON TEXT
        rarity=rarity.upper()
        draw=ImageDraw.Draw(background)
        draw.text((32,131),rarity,font=font,fill='black') # Draws Rarity Button Text

        # Backend Value Text

        backend_x = raritytag_w + 28 + 20

        backend = i['type']['value']
        backend=backend.upper()
        draw=ImageDraw.Draw(background)
        draw.text((backend_x,133),backend,font=font,fill='white')


        font=ImageFont.truetype(loadFont,35)
        try:
            set = i['set']['value']
        except:
            set = 'N/A'
        draw.text((20,935),f'Set: {set}',font=font,fill=0xc8c5c4)

        id = i['id']
        font=ImageFont.truetype(loadFont,25)
        draw.text((20,995),f'ID:  {id}',font=font,fill=0xc8c5c4)

        try:
            seasonnum = f"C{i['introduction']['chapter']} S{i['introduction']['season']}"
        except:
            seasonnum = 'N/A'

        otherdesc = f'{seasonnum}'
        try:
            for x in i['gameplayTags']:
                if 'ItemShop' in x:
                    otherdesc = f'{seasonnum} | ITEMSHOP'
                    break
        except:
            pass

        font=ImageFont.truetype(loadFont,35)
        draw.text((20,1035),otherdesc,font=font,fill=0xc8c5c4)

        #Variant Gen
        variants = i['variants']
        variantnum = 0
        if i['variants'] != None:
            plus_sign = Image.open(f'rarities/large/PlusSign.png').convert("RGBA")
            background.paste(plus_sign, (0,0), plus_sign)

            variants_text = Image.open(f'rarities/large/VariantsText.png').convert("RGBA")
            background.paste(variants_text, (0,0), variants_text)

            for x in i['variants'][0]['options']:
                if x['name'] != 'DEFAULT':
                    variantbox=Image.new("RGB",(157,157), color = 0x211f20).convert('RGBA')

                    name = x['name']
                    url = x['image']
                    r = requests.get(url)
                    open(f'cache/variant_{name}.png', 'wb').write(r.content)
                    varianticon = Image.open(f'cache/variant_{name}.png').resize((157, 157), Image.ANTIALIAS).convert("RGBA")
                    variantbox.paste(varianticon, (0,0), varianticon)
                    
                    variantbox.save(f'cache/V_{name}.png')
                    os.remove(f'cache/variant_{name}.png')

                    varianticon = Image.open(f'cache/V_{name}.png').convert("RGBA")
                    
                    variantnum = variantnum + 1
                    
                    xnum = 24
                    if variantnum == 1:
                        xnum = 24
                    elif variantnum == 2:
                        xnum = 204 # 180
                    elif variantnum == 3:
                        xnum = 384 # 180

                    ynum = 390
                    if variantnum == 4:
                        xnum = 24
                        ynum = 570
                    elif variantnum == 5:
                        xnum = 204
                        ynum = 570
                    elif variantnum == 6:
                        xnum = 384
                        ynum = 570
                        
                    background.paste(varianticon, (xnum, ynum), varianticon)
                    os.remove(f'cache/V_{name}.png')


            font=ImageFont.truetype(loadFont,35)
            draw.text((230,340),f'{variantnum}',font=font,fill=0x999999)
            #print(f'Variants: {variantnum}')
        


        # CARD GEN #



        background.save(f'icons/{id}.png')
        os.remove(f'cache/LargeTemp-{id}.png')
        #largeicontype_search(useFeaturedIfAvaliable)
        count = count + 1
        print(f'{count}/{items}')
    large_merger()
    print('\nMerged images... opening image')
    img=Image.open('merged/merge.jpg')
    img.show()