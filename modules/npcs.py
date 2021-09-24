from colorama import *
init()
import time
import requests
import PIL
from PIL import Image, ImageFont, ImageDraw, ImageChops, ImageOps
import os
import shutil

def add_border(input_image, output_image, border, color=0): # Adds border to image
    img = Image.open(input_image)
    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border, fill=color)
    else:
        raise RuntimeError('Border is not an integer or tuple!') # This shouldnt occur, but doing to be safe
    bimg.save(output_image)

def npcsdef(showDescription, imageFont, apikey, loadFont):
    print('How do you want to use the NPC bot?\n')
    print('a = Generate all NPCs icons\nc = Generate current NPCs icons\nloc = Generate a image of NPC locations')
    ask = input('>> ')
    if ask == 'a':
        print(Fore.CYAN + '\nGenerating all current NPCs...\n')

        start = time.time()
        response = requests.get('https://benbot.app/api/v1/files')

        counter = 0

        if showDescription == 'True' or 'False':
            pass
        else:
            showDescription = 'False'

        for i in response.json():
            if i.startswith('FortniteGame/Plugins/GameFeatures/NPCLibrary/Content/NPCs/'):
                if 'NPCCharacterData' in i:
                    response = requests.get(f'https://benbot.app/api/v1/assetProperties?path={i}')
                    x = response.json()['export_properties'][0]

                    loc = x['POILocations']
                    loc = str(loc)
                    loc = loc.replace('Athena.Location.', '').replace("['", '').replace("']", '')
                    name = x['DisplayName']['finalText']

                    try:
                        icon = x['SidePanelIcon']['assetPath']
                    except:
                        icon = ""

                    if icon == "":
                        icon = x['EntryListIcon']['assetPath']

                    r = requests.get(f'https://benbot.app/api/v1/exportAsset?path={icon}&lang=en&noVariants=false&rawIcon=false', allow_redirects=True)
                    open(f'cache/{name} icon.png', 'wb').write(r.content)

                    print(
                        f'{name} NPC:\n',
                        f' - Found in {loc}'
                    )

                    h = f'{name} NPC:\n - Found in {loc}\n\n'

                    background = Image.open(f'rarities/npc/background.png')
                    border=Image.open(f'rarities/npc/border.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")

                    img=Image.new("RGB",(512,512))
                    img.paste(background)
                    img.save('cache/temp.png')
                    img=Image.open(f'cache/temp.png')

                    foreground= Image.open(f'cache/{name} icon.png').resize((512, 512), Image.ANTIALIAS)
                    img.paste(foreground, (0, 0), foreground)
                    img.save('cache/temp.png')
                    img.paste(border, (0, 0), border)
                    img.save('cache/temp.png')

                    #os.remove(f'cache/{name} icon.png')

                    background = Image.open('cache/temp.png')

                    loadFont = f'fonts/'+ imageFont

                    if len(name) > 18:
                        font=ImageFont.truetype(loadFont,51) 
                    else:
                        font=ImageFont.truetype(loadFont,57) 
                    name1 = name.upper()
                    namereal = f'{name1} NPC'

                    w,h=font.getsize(namereal)
                    draw=ImageDraw.Draw(background)
                    w1, h1 = draw.textsize(namereal, font=font)
                    draw.text(((512-w1)/2,406),namereal,font=font,fill='white')

                    if showDescription != 'False':
                        try:
                            description = x['GeneralDescription']['finalText']
                            font=ImageFont.truetype(loadFont,15)
                            w,h=font.getsize(description)
                            draw=ImageDraw.Draw(background)
                            draw.text((10,9),description,font=font,fill='white')
                        except:
                            pass
                    else:
                        pass

                    loc = f'Found in {loc}'

                    loadFont = 'fonts/OpenSans-Regular.ttf'

                    if len(loc) > 75:
                        font = ImageFont.truetype(loadFont,9)
                    else:
                        font = ImageFont.truetype(loadFont,14)
                    w,h=font.getsize(loc)
                    draw=ImageDraw.Draw(background)
                    w1, h1 = draw.textsize(loc, font=font)
                    draw.text(((512-w1)/2,470),loc,font=font,fill='white')

                    counter = counter + 1
                    background.save(f'icons/{name} NPC.png')

                    print('  - Loaded image!\n')

        end = time.time()

        print(f'Done loading images in {round(end - start, 2)} seconds!')
        try:
            shutil.rmtree('cache')
            os.makedirs('cache')
        except:
            os.makedirs('cache')

        time.sleep(5)
    if ask == 'c':
        response = requests.get('https://benbot.app/api/v1/status')
        currentfnversion = response.json()['currentFortniteVersion']
        currentfnversion = currentfnversion.replace('++Fortnite+Release-', '').replace('-CL-16593740-Windows', '')
        print(Fore.CYAN + f'\nGenerating all new NPCs from the latest Fortnite Version ({currentfnversion})...\n')

        start = time.time()
        response = requests.get(f'https://benbot.app/api/v1/files/added')

        counter = 0

        if showDescription == 'True' or 'False':
            pass
        else:
            showDescription = 'False'

        for i in response.json():
            if i.startswith('FortniteGame/Plugins/GameFeatures/NPCLibrary/Content/NPCs/'):
                if 'NPCCharacterData' in i:
                    response = requests.get(f'https://benbot.app/api/v1/assetProperties?path={i}')
                    x = response.json()['export_properties'][0]

                    loc = x['POILocations']
                    loc = str(loc)
                    loc = loc.replace('Athena.Location.', '').replace("['", '').replace("']", '')
                    name = x['DisplayName']['finalText']

                    try:
                        icon = x['SidePanelIcon']['assetPath']
                    except:
                        icon = ""

                    if icon == "":
                        icon = x['EntryListIcon']['assetPath']

                    r = requests.get(f'https://benbot.app/api/v1/exportAsset?path={icon}&lang=en&noVariants=false&rawIcon=false', allow_redirects=True)
                    open(f'cache/{name} icon.png', 'wb').write(r.content)

                    print(
                        f'{name} NPC:\n',
                        f' - Found in {loc}'
                    )

                    h = f'{name} NPC:\n - Found in {loc}\n\n'

                    background = Image.open(f'rarities/npc/background.png')
                    border=Image.open(f'rarities/npc/border.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")

                    img=Image.new("RGB",(512,512))
                    img.paste(background)
                    img.save('cache/temp.png')
                    img=Image.open(f'cache/temp.png')

                    foreground= Image.open(f'cache/{name} icon.png').resize((512, 512), Image.ANTIALIAS)
                    img.paste(foreground, (0, 0), foreground)
                    img.save('cache/temp.png')
                    img.paste(border, (0, 0), border)
                    img.save('cache/temp.png')

                    #os.remove(f'cache/{name} icon.png')

                    background = Image.open('cache/temp.png')

                    loadFont = f'fonts/'+ imageFont

                    if len(name) > 18:
                        font=ImageFont.truetype(loadFont,51) 
                    else:
                        font=ImageFont.truetype(loadFont,57) 
                    name1 = name.upper()
                    namereal = f'{name1} NPC'

                    w,h=font.getsize(namereal)
                    draw=ImageDraw.Draw(background)
                    w1, h1 = draw.textsize(namereal, font=font)
                    draw.text(((512-w1)/2,406),namereal,font=font,fill='white')

                    if showDescription != 'False':
                        try:
                            description = x['GeneralDescription']['finalText']
                            font=ImageFont.truetype(loadFont,15)
                            w,h=font.getsize(description)
                            draw=ImageDraw.Draw(background)
                            draw.text((10,9),description,font=font,fill='white')
                        except:
                            pass
                    else:
                        pass

                    loc = f'Found in {loc}'

                    loadFont = 'fonts/OpenSans-Regular.ttf'

                    if len(loc) > 75:
                        font = ImageFont.truetype(loadFont,9)
                    else:
                        font = ImageFont.truetype(loadFont,14)
                    w,h=font.getsize(loc)
                    draw=ImageDraw.Draw(background)
                    w1, h1 = draw.textsize(loc, font=font)
                    draw.text(((512-w1)/2,470),loc,font=font,fill='white')

                    counter = counter + 1
                    background.save(f'icons/{name} NPC.png')

                    print('  - Loaded image!\n')

        end = time.time()

        print(f'Done loading images in {round(end - start, 2)} seconds!')

        time.sleep(5)
    if ask == 'loc':
        try:
            os.remove('Assets/plotted_done.png')
        except:
            pass
            if apikey == '':
                print('Please enter an API key from fortniteapi.io to run this function')
                time.sleep(2)
                exit()
        headers = {'Authorization': apikey}
        try:
            mapimage = Image.open('Assets/Apollo_Terrain_Minimap.png')
        except:
            response = requests.get('https://cdn.discordapp.com/attachments/810723511655202826/890775730026340392/Apollo_Terrain_Minimap.png')
            open('Assets/Apollo_Terrain_Minimap.png', 'wb').write(response.content)
            mapimage = Image.open('Assets/Apollo_Terrain_Minimap.png')

        img = Image.new("RGB", (2048, 2048))
        img.paste(mapimage, (0, 0), mapimage)
        img.save('Assets/cache.png')

        print('\nGenerating all current NPC plotted locations... Please give us a moment.')

        response = requests.get('https://fortniteapi.io/v2/game/npc/list?enabled=true&scale=2048', headers=headers) # I could of just exported the assets of the file and scale it but im lazy so yea
        
        point = 0
        for i in response.json()['npc']:
            name = i['displayName']
            namereplace = False
            if ' ' in name:
                name = name.replace(' ', '\n')
                namereplace = True
            try:
                x = int(i['spawnLocations'][0]['locations'][0]['x'])
                y = int(i['spawnLocations'][0]['locations'][0]['y'])
                
                url = i['images']['toast']

                r = requests.get(url, allow_redirects=True)
                open(f'cache/temp.png', 'wb').write(r.content)
                add_border('cache/temp.png', output_image='cache/temp.png', border=15, color='#ff0000')

                #y = ((y+135000)/ (135000*2))*2048 # Calculates Y value
                #x  = (1-(x+135000)/ (135000*2))*2048 # Calculates X value

                mapimage = Image.open('Assets/cache.png')
                point = point + 1
                font=ImageFont.truetype(loadFont,25)
                draw=ImageDraw.Draw(mapimage)
                if namereplace != True:
                    draw.text((x+25,y-12),f'{name}',font=font,fill=(255, 201, 23), stroke_width=3, stroke_fill=(0, 0, 0), anchor='ms')
                else:
                    draw.text((x+25,y-42),f'{name}',font=font,fill=(255, 201, 23), stroke_width=3, stroke_fill=(0, 0, 0), anchor='ms')
                foreground= Image.open('cache/temp.png').resize((60, 60), Image.ANTIALIAS)
                mapimage.paste(foreground, (x, y), foreground)
                mapimage.save('Assets/cache.png')
                #print(f'Point {point} -  {x}, {y}') # Prints Locations
            except:
                print('There was an error with this NPC.')
                
        os.rename('Assets/cache.png', 'Assets/plotted_done.png')
        image = Image.open('Assets/plotted_done.png')
        image.show()
        x = len(response.json()['npc'])
        print(Fore.CYAN + '\nPlotted all {x} NPC points. Saved into assets folder as plotted_done.png')
