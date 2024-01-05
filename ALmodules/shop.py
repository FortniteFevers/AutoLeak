import requests
from PIL import Image, ImageFont, ImageDraw
from datetime import date
from datetime import datetime
import os
import time
import tweepy
from colorama import *
import shutil

#===============#
loadFont = 'fonts/BurbankBigRegular-BlackItalic.otf'
showItems = False
botDelay = 5

backgroundColor = 0x000000
#===============#

def genshop():
    print('Starting the generation process.'+Fore.CYAN)
    start = time.time()

    response = requests.get('https://fortnite-api.com/v2/shop/br/combined')

    data = response.json()['data']

    currentdate = response.json()['data']['date']
    currentdate = currentdate[:10]

    # --- FEATURED GEN --- #
    print('\nGenerating Featured Section...')
    featured = data['featured']
    count = 0
    for i in featured['entries']:

        if i['newDisplayAssetPath'] != None:
            try:
                url = i['newDisplayAsset']['materialInstances'][0]['images']['Background']
            except:
                url = i['newDisplayAsset']['materialInstances'][0]['images']['OfferImage']
        else:
            url = i['items'][0]['images']['icon']

        name = i['items'][0]['id']
        last_seen = i['items'][0]['shopHistory']
        try:
            last_seen = last_seen[-2][:10]
        except:
            last_seen = 'NEW!'
        price = i['finalPrice']

        if i['bundle'] != None:
            url = i['bundle']['image']
            name = f"zzz{i['bundle']['name']}"
        
        if last_seen != 'NEW!':
            dateloop = datetime.strptime(last_seen, "%Y-%m-%d")
            current = datetime.strptime(currentdate, "%Y-%m-%d")
            diff = str(current.date() - dateloop.date())
            diff = diff.replace('days, 0:00:00', '')
            if diff == '0:00:00':
                diff = '1'
        else:
            diff = 'NEW!'


        open(f'icons/{name}.png', 'wb').write(requests.get(url).content)
        background = Image.open(f'icons/{name}.png').resize((512, 512))
        background.save(f'icons/{name}.png')

        img=Image.new("RGB",(512,512))
        img.paste(background)

        # OTHER ITEMS GEN
        try:
            if i['bundle'] == None:
                if i['items'][1]:
                    url = i['items'][1]['images']['icon']
                    open(f'icons/temp{name}.png', 'wb').write(requests.get(url).content)
                    background = Image.open(f'icons/temp{name}.png').resize((80, 80))
                    background.save(f'icons/temp{name}.png')
                
                    background = Image.open(f'icons/temp{name}.png')
                    img.paste(background, (0, 0), background)

                    os.remove(f'icons/temp{name}.png')
                if i['items'][2]:
                    url = i['items'][2]['images']['icon']
                    open(f'icons/temp{name}.png', 'wb').write(requests.get(url).content)
                    background = Image.open(f'icons/temp{name}.png').resize((80, 80))
                    background.save(f'icons/temp{name}.png')
                
                    background = Image.open(f'icons/temp{name}.png')
                    img.paste(background, (0, 100), background)

                    os.remove(f'icons/temp{name}.png')

                if i['items'][3]:
                    url = i['items'][3]['images']['icon']
                    open(f'icons/temp{name}.png', 'wb').write(requests.get(url).content)
                    background = Image.open(f'icons/temp{name}.png').resize((80, 80))
                    background.save(f'icons/temp{name}.png')
                
                    background = Image.open(f'icons/temp{name}.png')
                    img.paste(background, (0, 200), background)

                    os.remove(f'icons/temp{name}.png')
        except:
            pass



        overlay = Image.open('assets/overlay.png').convert('RGBA')
        img.paste(overlay, (0,0), overlay)

        img.save(f'icons/{name}.png')

        background = Image.open(f'icons/{name}.png')

        itemname = i['items'][0]['name']
        if i['bundle'] != None:
            itemname = f"{i['bundle']['name']}"
        
        font=ImageFont.truetype(loadFont,35)
        draw=ImageDraw.Draw(background)
        draw.text((256,420),itemname,font=font,fill='white', anchor='ms') # Writes name

        if 'NEW!' in diff:
            diff_text = 'NEW!'
        else:
            diff = diff.replace(' ', '')
            diff_text = f'LAST SEEN: {diff} days ago'

        if '0:00' in diff_text:
            diff_text = 'LAST SEEN: 1 day ago'

        font=ImageFont.truetype(loadFont,15)
        draw=ImageDraw.Draw(background)
        draw.text((256,450),diff_text,font=font,fill='white', anchor='ms') # Writes date last seen

        font=ImageFont.truetype(loadFont,40)
        draw=ImageDraw.Draw(background)
        draw.text((256,505),f'{price}',font=font,fill='white', anchor='ms') # Writes price

        background.save(f'icons/{name}.png')

        if showItems != False:
            print(f'Last Seen: {diff} days ago\n{name} - {price}\n')

        count += 1

    print(f'Done generating "{count}" items in the Featured section.')
    featrued_num = count
    print('')

    # --- DAILY GEN --- #
    print('Generating Daily Section...')
    daily = data['daily']
    count = 0
    if daily != None:
        for i in daily['entries']:

            if i['newDisplayAssetPath'] != None:
                try:
                    url = i['newDisplayAsset']['materialInstances'][0]['images']['Background']
                except:
                    url = i['newDisplayAsset']['materialInstances'][0]['images']['OfferImage']
            else:
                url = i['items'][0]['images']['icon']


            name = i['items'][0]['id']
            last_seen = i['items'][0]['shopHistory']
            try:
                last_seen = last_seen[-2][:10]
            except:
                last_seen = 'NEW!'
            price = i['finalPrice']

            if i['bundle'] != None:
                url = i['bundle']['image']
                name = f"zzz{i['bundle']['name']}"
            
            if last_seen != 'NEW!':
                dateloop = datetime.strptime(last_seen, "%Y-%m-%d")
                current = datetime.strptime(currentdate, "%Y-%m-%d")
                diff = str(current.date() - dateloop.date())
                diff = diff.replace('days, 0:00:00', '')
                if diff == '0:00:00':
                    diff = '1'
            else:
                diff = 'NEW!'


            open(f'icons/{name}.png', 'wb').write(requests.get(url).content)
            background = Image.open(f'icons/{name}.png').resize((512, 512))
            background.save(f'icons/{name}.png')

            img=Image.new("RGB",(512,512))
            img.paste(background)

            # OTHER ITEMS GEN
            try:
                if i['bundle'] == None:
                    if i['items'][1]:
                        url = i['items'][1]['images']['icon']
                        open(f'icons/temp{name}.png', 'wb').write(requests.get(url).content)
                        background = Image.open(f'icons/temp{name}.png').resize((80, 80))
                        background.save(f'icons/temp{name}.png')
                    
                        background = Image.open(f'icons/temp{name}.png')
                        img.paste(background, (0, 0), background)

                        os.remove(f'icons/temp{name}.png')
                    if i['items'][2]:
                        url = i['items'][2]['images']['icon']
                        open(f'icons/temp{name}.png', 'wb').write(requests.get(url).content)
                        background = Image.open(f'icons/temp{name}.png').resize((80, 80))
                        background.save(f'icons/temp{name}.png')
                    
                        background = Image.open(f'icons/temp{name}.png')
                        img.paste(background, (0, 100), background)

                        os.remove(f'icons/temp{name}.png')

                    if i['items'][3]:
                        url = i['items'][3]['images']['icon']
                        open(f'icons/temp{name}.png', 'wb').write(requests.get(url).content)
                        background = Image.open(f'icons/temp{name}.png').resize((80, 80))
                        background.save(f'icons/temp{name}.png')
                    
                        background = Image.open(f'icons/temp{name}.png')
                        img.paste(background, (0, 200), background)

                        os.remove(f'icons/temp{name}.png')
            except:
                pass

            overlay = Image.open('assets/overlay.png').convert('RGBA')
            img.paste(overlay, (0,0), overlay)

            img.save(f'icons/{name}.png')

            background = Image.open(f'icons/{name}.png')


            itemname = i['items'][0]['name']
            if i['bundle'] != None:
                itemname = f"{i['bundle']['name']}"
            font=ImageFont.truetype(loadFont,35)
            draw=ImageDraw.Draw(background)
            draw.text((256,420),itemname,font=font,fill='white', anchor='ms') # Writes name

            if 'NEW!' in diff:
                diff_text = 'NEW!'
            else:
                diff = diff.replace(' ', '')
                diff_text = f'LAST SEEN: {diff} days ago'

            if '0:00' in diff_text:
                diff_text = 'LAST SEEN: 1 day ago'

            font=ImageFont.truetype(loadFont,15)
            draw=ImageDraw.Draw(background)
            draw.text((256,450),diff_text,font=font,fill='white', anchor='ms') # Writes date last seen

            font=ImageFont.truetype(loadFont,40)
            draw=ImageDraw.Draw(background)
            draw.text((256,505),f'{price}',font=font,fill='white', anchor='ms') # Writes price

            background.save(f'icons/{name}.png')

            if showItems != False:
                print(f'Last Seen: {diff} days ago\n{name} - {price}\n')

            count += 1
    else:
        print("Daily section does not exist.")

    print(f'Done generating "{count}" items in the Daily section.')
    daily_num = count
    
    #########################

    totalnum = daily_num + featrued_num
    print(f'\nGenerated {totalnum} items from the {currentdate} Item Shop.')


    end = time.time()

    print(f"IMAGE GENERATING COMPLETE - Generated image in {round(end - start, 2)} seconds!")
    

response = requests.get('https://fortnite-api.com/v2/shop/br/combined')
currentdate = response.json()['data']['date']
currentdate = currentdate[:10]
# Credits to https://github.com/MyNameIsDark01 for the original Merger code.
# This merger is under rights, you may not take this code and use it in your own project without proper credits to Fevers and Dark.
from math import ceil, sqrt
from typing import Union
import glob
from PIL import Image, ImageFont, ImageDraw
import PIL
import requests
import glob
from math import ceil, sqrt
from typing import Union
import os

# Credits to https://github.com/MyNameIsDark01 for the original Merger code.
# This merger is under rights, you may not take this code and use it in your own project without proper credits to Fevers and Dark.

def shopmerge(datas: Union[list, None] = None, save_as: str = f'merged/shop {currentdate}.jpg'):
    response = requests.get('https://fortnite-api.com/v2/shop/br/combined')
    currentdate = response.json()['data']['date']
    currentdate = currentdate[:10]
    if not datas:
        datas = [Image.open(i) for i in glob.glob('icons/*.png')]

    list_ = []
    num = 0
    for file in os.listdir('icons'):
        num += 1
        
        if file.startswith('tempzzz'):
            pass
        else:
            list_.append(f'icons/{file}')

    row_n = num
        
    rowslen = ceil(sqrt(row_n))
    columnslen = round(sqrt(row_n))

    mode = "RGB"
    px = 512

    rows = rowslen * px
    columns = columnslen * px
    image = Image.new(mode, (rows, columns))

    i = 0

    datas = [Image.open(i) for i in sorted(list_)]

    for card in datas:
        image.paste(
            card,
            ((0 + ((i % rowslen) * card.width)),
                (0 + ((i // rowslen) * card.height)))
        )

        i += 1

    image.save(f"{save_as}")

    img = PIL.Image.open(f"{save_as}")
    width, height = img.size

    img=Image.new("RGB",(width,height+322), backgroundColor)

    shopimage = Image.open(f"{save_as}")
    img.paste(shopimage, (0, 322))
    
    font=ImageFont.truetype('fonts/BurbankBigRegular-BlackItalic.otf',150)
    draw=ImageDraw.Draw(img)
    draw.text((width/2,190),'FORTNITE ITEM SHOP',font=font,fill='white', anchor='ms') # Writes name

    font=ImageFont.truetype('fonts/BurbankBigRegular-BlackItalic.otf',50)
    draw.text((width/2,240),currentdate,font=font,fill='white', anchor='ms') # Writes name

    img.save(f'{save_as}')

    return image

def update(api):
    apiurl = f'https://fortnite-api.com/v2/shop/br/combined'

    response = requests.get(apiurl)
    shopData = response.json()['data']['hash']
    currentdate = response.json()['data']['date']
    currentdate = currentdate[:10]

    count = 1

    while 1:
        
        response = requests.get(apiurl)
        if response:
            try:
                shopDataLoop = response.json()['data']['hash']
            except:
                return update()
            print("Checking for change in the Shop... ("+str(count)+")")
            count = count + 1
            
            if shopData != shopDataLoop: # Now run program as normal. Shop has changed.
                print('\nTHE SHOP HAS UPDATED!')
                try:
                    shutil.rmtree('cache')
                    os.makedirs('cache')
                except:
                    os.makedirs('cache')
                genshop()
                shopmerge()
                api.update_with_media(f'merged/shop {currentdate}.jpg', f'#Fortnite Item Shop update for {currentdate}!\n\nConsider using code "Fevers" to support me! #EpicPartner')
                print('')
                update(api)
        
        else:
            print("FAILED TO GRAB SHOP DATA: URL DOWN")

        time.sleep(botDelay)
