import requests
from PIL import Image, ImageFont, ImageDraw
import os
import PIL

def genshopbenbot():
    response = requests.get('https://benbot.app/api/v1/shop/br')
    version = response.json()
    print('\nGenerating shop for',version['date'])
    counter = 0

    print('Generating featured...')
    for i in version['featured']:
        
        for i in i['entries']:
            price = str(i['finalPrice'])
            for i in i['items']:
                name = i['name']
                rarity = i['rarity']
                backendtype = i['shortDescription']
                if backendtype == None:
                    backendtype = i['backendType']
                id = i['id']
                url = f'https://fortnite-api.com/images/cosmetics/br/{id}/icon.png'
                description = i['description']
                

                r = requests.get(url)
                open(f'cache/{id}temp.png', 'wb').write(r.content)
                iconImg = Image.open(f'cache/{id}temp.png')
                iconImg.resize((512,512),PIL.Image.ANTIALIAS)


                raritybackground = Image.open(f'rarities/cataba/{rarity}.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                background = Image.open(f'rarities/cataba/{rarity}_background.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")

                img=Image.new("RGB",(512,512))
                img.paste(raritybackground)
                try:
                    overlay = Image.open(f'rarities/cataba/{rarity}_overlay.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                except:
                    overlay = Image.open(f'rarities/cataba/common_overlay.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                img.paste(overlay, (0,0), overlay)
                iconImg= Image.open(f'cache/{id}temp.png').resize((512, 512), Image.ANTIALIAS).convert('RGBA')
                img.paste(iconImg, (0,0), iconImg)
                img.paste(background, (0,0), background)
                try:
                    rarityoverlay = Image.open(f'rarities/cataba/{rarity}_rarity.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                except:
                    rarityoverlay = Image.open(f'rarities/cataba/placeholder_rarity.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                img.paste(rarityoverlay, (0,0), rarityoverlay)

                vbucksoverlay = Image.open(f'rarities/cataba/vbuck.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                img.paste(vbucksoverlay, (0,0), vbucksoverlay)
                img.save(f'cache/{id}.png')

                loadFont = 'fonts/BurbankBigRegular-BlackItalic.otf'
                font=ImageFont.truetype(loadFont,31)


                background = Image.open(f'cache/{id}.png')
                name=name.upper()
                draw=ImageDraw.Draw(background)
                draw.text((256,472),name,font=font,fill='white', anchor='ms') # Writes name

                description=description.upper()
                font=ImageFont.truetype(loadFont,10)
                draw=ImageDraw.Draw(background)
                draw.text((256,501),description,font=font,fill='white', anchor='ms') # Writes description
            
                font=ImageFont.truetype(loadFont,15)
                draw=ImageDraw.Draw(background)
                draw.text((445,500),price,font=font,fill='white', anchor='ms') # Writes description

                backendtype = backendtype.upper()
                font=ImageFont.truetype(loadFont,14)
                draw=ImageDraw.Draw(background)
                draw.text((6,495),backendtype,font=font,fill='white') # Writes backend type        

                background.save(f'icons/{id}.png')
                os.remove(f'cache/{id}temp.png')
                os.remove(f'cache/{id}.png')

    print('Generated featured')


    print('\nGenerating daily...')
    for i in version['daily']:
        
        for i in i['entries']:
            price = str(i['finalPrice'])
            for i in i['items']:
                name = i['name']
                rarity = i['rarity']
                backendtype = i['shortDescription']
                if backendtype == None:
                    backendtype = i['backendType']
                id = i['id']
                url = f'https://fortnite-api.com/images/cosmetics/br/{id}/icon.png'
                description = i['description']
                

                r = requests.get(url)
                open(f'cache/{id}temp.png', 'wb').write(r.content)
                iconImg = Image.open(f'cache/{id}temp.png')
                iconImg.resize((512,512),PIL.Image.ANTIALIAS)


                raritybackground = Image.open(f'rarities/cataba/{rarity}.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                background = Image.open(f'rarities/cataba/{rarity}_background.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")

                img=Image.new("RGB",(512,512))
                img.paste(raritybackground)
                try:
                    overlay = Image.open(f'rarities/cataba/{rarity}_overlay.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                except:
                    overlay = Image.open(f'rarities/cataba/common_overlay.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                img.paste(overlay, (0,0), overlay)
                iconImg= Image.open(f'cache/{id}temp.png').resize((512, 512), Image.ANTIALIAS).convert('RGBA')
                img.paste(iconImg, (0,0), iconImg)
                img.paste(background, (0,0), background)
                try:
                    rarityoverlay = Image.open(f'rarities/cataba/{rarity}_rarity.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                except:
                    rarityoverlay = Image.open(f'rarities/cataba/placeholder_rarity.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                img.paste(rarityoverlay, (0,0), rarityoverlay)

                vbucksoverlay = Image.open(f'rarities/cataba/vbuck.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                img.paste(vbucksoverlay, (0,0), vbucksoverlay)
                img.save(f'cache/{id}.png')

                loadFont = 'fonts/BurbankBigRegular-BlackItalic.otf'
                font=ImageFont.truetype(loadFont,31)


                background = Image.open(f'cache/{id}.png')
                name=name.upper()
                draw=ImageDraw.Draw(background)
                draw.text((256,472),name,font=font,fill='white', anchor='ms') # Writes name

                description=description.upper()
                font=ImageFont.truetype(loadFont,10)
                draw=ImageDraw.Draw(background)
                draw.text((256,501),description,font=font,fill='white', anchor='ms') # Writes description
            
                font=ImageFont.truetype(loadFont,15)
                draw=ImageDraw.Draw(background)
                draw.text((445,500),price,font=font,fill='white', anchor='ms') # Writes description

                backendtype = backendtype.upper()
                font=ImageFont.truetype(loadFont,14)
                draw=ImageDraw.Draw(background)
                draw.text((6,495),backendtype,font=font,fill='white') # Writes backend type        

                background.save(f'icons/{id}.png')
                os.remove(f'cache/{id}temp.png')
                os.remove(f'cache/{id}.png')

    print('Generated daily.')

    if version['specialFeatured'] == None:
        pass
    else:
        print('\nGenerating special featured...')
        for i in version['specialFeatured']:
            for i in i['entries']:
                price = str(i['finalPrice'])
                for i in i['items']:
                    name = i['name']
                    rarity = i['rarity']
                    backendtype = i['shortDescription']
                    if backendtype == None:
                        backendtype = i['backendType']
                    id = i['id']
                    url = f'https://fortnite-api.com/images/cosmetics/br/{id}/icon.png'
                    description = i['description']
                    

                    r = requests.get(url)
                    open(f'cache/{id}temp.png', 'wb').write(r.content)
                    iconImg = Image.open(f'cache/{id}temp.png')
                    iconImg.resize((512,512),PIL.Image.ANTIALIAS)


                    raritybackground = Image.open(f'rarities/cataba/{rarity}.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                    background = Image.open(f'rarities/cataba/{rarity}_background.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")

                    img=Image.new("RGB",(512,512))
                    img.paste(raritybackground)
                    try:
                        overlay = Image.open(f'rarities/cataba/{rarity}_overlay.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                    except:
                        overlay = Image.open(f'rarities/cataba/common_overlay.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                    img.paste(overlay, (0,0), overlay)
                    iconImg= Image.open(f'cache/{id}temp.png').resize((512, 512), Image.ANTIALIAS).convert('RGBA')
                    img.paste(iconImg, (0,0), iconImg)
                    img.paste(background, (0,0), background)
                    try:
                        rarityoverlay = Image.open(f'rarities/cataba/{rarity}_rarity.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                    except:
                        rarityoverlay = Image.open(f'rarities/cataba/placeholder_rarity.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                    img.paste(rarityoverlay, (0,0), rarityoverlay)

                    vbucksoverlay = Image.open(f'rarities/cataba/vbuck.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                    img.paste(vbucksoverlay, (0,0), vbucksoverlay)
                    img.save(f'cache/{id}.png')

                    loadFont = 'fonts/BurbankBigRegular-BlackItalic.otf'
                    font=ImageFont.truetype(loadFont,31)


                    background = Image.open(f'cache/{id}.png')
                    name=name.upper()
                    draw=ImageDraw.Draw(background)
                    draw.text((256,472),name,font=font,fill='white', anchor='ms') # Writes name

                    description=description.upper()
                    font=ImageFont.truetype(loadFont,10)
                    draw=ImageDraw.Draw(background)
                    draw.text((256,501),description,font=font,fill='white', anchor='ms') # Writes description
                
                    font=ImageFont.truetype(loadFont,15)
                    draw=ImageDraw.Draw(background)
                    draw.text((445,500),price,font=font,fill='white', anchor='ms') # Writes description

                    backendtype = backendtype.upper()
                    font=ImageFont.truetype(loadFont,14)
                    draw=ImageDraw.Draw(background)
                    draw.text((6,495),backendtype,font=font,fill='white') # Writes backend type        

                    background.save(f'icons/{id}.png')
                    os.remove(f'cache/{id}temp.png')
                    os.remove(f'cache/{id}.png')

    print('Generated special featured.')

    print('\nLoading bundles and other things...')
    response = requests.get('https://fortnite-api.com/v2/shop/br/combined')
    version = response.json()['data']
    counter = 0
    for i in version['featured']['entries']:

        if i['bundle'] != None:
            name = i['bundle']['name']
            if 'BUNDLE' not in name:
                name = name + ' BUNDLE'
            url = i['bundle']['image']
            id = i['bundle']['name']
            price = str(i['finalPrice'])
            rarity = 'bundle'
            backendtype = 'BUNDLE'
            try:
                description = i['banner']['value']
            except:
                description = 'N/A'
            if description == None:
                description = 'N/A'
            r = requests.get(url)
            open(f'cache/{id}temp.png', 'wb').write(r.content)
            iconImg = Image.open(f'cache/{id}temp.png')
            iconImg.resize((512,512),PIL.Image.ANTIALIAS)

            rarity = 'common'
            try:
                raritybackground = Image.open(f'rarities/cataba/{rarity}.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
            except:
                raritybackground = Image.open(f'rarities/cataba/common.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")

            try:  
                background = Image.open(f'rarities/cataba/{rarity}_background.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
            except:
                background = Image.open(f'rarities/cataba/{rarity}_background.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")

            img=Image.new("RGB",(512,512))
            img.paste(raritybackground)
            try:
                overlay = Image.open(f'rarities/cataba/{rarity}_overlay.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
            except:
                overlay = Image.open(f'rarities/cataba/common_overlay.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
            img.paste(overlay, (0,0), overlay)
            iconImg= Image.open(f'cache/{id}temp.png').resize((512, 512), Image.ANTIALIAS).convert('RGBA')
            img.paste(iconImg, (0,0), iconImg)
            img.paste(background, (0,0), background)

            rarity = 'bundle'
            try:
                rarityoverlay = Image.open(f'rarities/cataba/{rarity}_rarity.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
            except:
                rarityoverlay = Image.open(f'rarities/cataba/placeholder_rarity.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
            img.paste(rarityoverlay, (0,0), rarityoverlay)

            vbucksoverlay = Image.open(f'rarities/cataba/vbuck.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
            img.paste(vbucksoverlay, (0,0), vbucksoverlay)
            img.save(f'cache/{id}.png')

            loadFont = 'fonts/BurbankBigRegular-BlackItalic.otf'
            font=ImageFont.truetype(loadFont,31)


            background = Image.open(f'cache/{id}.png')
            name=name.upper()
            draw=ImageDraw.Draw(background)
            draw.text((256,472),name,font=font,fill='white', anchor='ms') # Writes name

            description=description.upper()
            font=ImageFont.truetype(loadFont,10)
            draw=ImageDraw.Draw(background)
            draw.text((256,501),description,font=font,fill='white', anchor='ms') # Writes description
        
            font=ImageFont.truetype(loadFont,15)
            draw=ImageDraw.Draw(background)
            draw.text((445,500),price,font=font,fill='white', anchor='ms') # Writes description

            font=ImageFont.truetype(loadFont,14)
            draw=ImageDraw.Draw(background)
            draw.text((6,495),backendtype,font=font,fill='white') # Writes backend type        

            background.save(f'icons/{id}.png')
            os.remove(f'cache/{id}temp.png')
            os.remove(f'cache/{id}.png')
            counter = counter + 1
        else:
            price = str(i['finalPrice'])
            for i in i['items']:
                backendtype = i['type']['value'].upper()
                rarity = i['rarity']['value']
                name = i['name']
                description = i['description']
                if i["images"]["featured"] != None:
                    url = i["images"]["featured"]
                else:
                    if i['images']['icon'] != None:
                        url = i['images']['icon']
                    else:
                        url = 'https://i.ibb.co/KyvMydQ/do-Not-Delete.png'
                id = i['id']
                r = requests.get(url)
                open(f'cache/{id}temp.png', 'wb').write(r.content)
                iconImg = Image.open(f'cache/{id}temp.png')
                iconImg.resize((512,512),PIL.Image.ANTIALIAS)

                rarity = rarity.lower()
                try:
                    raritybackground = Image.open(f'rarities/cataba/{rarity}.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                except:
                    raritybackground = Image.open(f'rarities/cataba/common.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")

                try:  
                    background = Image.open(f'rarities/cataba/{rarity}_background.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                except:
                    background = Image.open(f'rarities/cataba/{rarity}_background.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")

                img=Image.new("RGB",(512,512))
                img.paste(raritybackground)
                try:
                    overlay = Image.open(f'rarities/cataba/{rarity}_overlay.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                except:
                    overlay = Image.open(f'rarities/cataba/common_overlay.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                img.paste(overlay, (0,0), overlay)
                iconImg= Image.open(f'cache/{id}temp.png').resize((512, 512), Image.ANTIALIAS).convert('RGBA')
                img.paste(iconImg, (0,0), iconImg)
                img.paste(background, (0,0), background)

                try:
                    rarityoverlay = Image.open(f'rarities/cataba/{rarity}_rarity.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                except:
                    rarityoverlay = Image.open(f'rarities/cataba/placeholder_rarity.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                img.paste(rarityoverlay, (0,0), rarityoverlay)

                vbucksoverlay = Image.open(f'rarities/cataba/vbuck.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                img.paste(vbucksoverlay, (0,0), vbucksoverlay)
                img.save(f'cache/{id}.png')

                loadFont = 'fonts/BurbankBigRegular-BlackItalic.otf'
                font=ImageFont.truetype(loadFont,31)


                background = Image.open(f'cache/{id}.png')
                name=name.upper()
                draw=ImageDraw.Draw(background)
                draw.text((256,472),name,font=font,fill='white', anchor='ms') # Writes name

                description=description.upper()
                font=ImageFont.truetype(loadFont,10)
                draw=ImageDraw.Draw(background)
                draw.text((256,501),description,font=font,fill='white', anchor='ms') # Writes description

                font=ImageFont.truetype(loadFont,15)
                draw=ImageDraw.Draw(background)
                draw.text((445,500),price,font=font,fill='white', anchor='ms') # Writes description

                font=ImageFont.truetype(loadFont,14)
                draw=ImageDraw.Draw(background)
                draw.text((6,495),backendtype,font=font,fill='white') # Writes backend type        

                background.save(f'icons/{id}.png')
                os.remove(f'cache/{id}temp.png')
                os.remove(f'cache/{id}.png')

    
        #i = response.json()['data']['items']
        #percentage = counter/len(i)
        #realpercentage = percentage * 100
        #print(f"{counter}/{len(i)} - {round(realpercentage)}%")
    print('\nLoaded bundles and other things.')
