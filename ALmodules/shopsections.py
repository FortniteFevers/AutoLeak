import requests
from colorama import *
import time
from PIL import Image, ImageFont, ImageDraw, ImageChops, ImageColor
import os

from googletrans import Translator
translator = Translator()

# DEFAULT LANG = EN

def shop_sections(sections_image, BotDelay, BG_Color, api, namelol, watermark, language):
    if sections_image != 'True':
        count = 1
        apiurl = f'https://fn-api.com/api/shop/sections?lang={language}'

        response = requests.get(apiurl)
        newsData = response.json()['data']['hash']

        while 1:
            response = requests.get(apiurl)
            if response:
                newsDataLoop = response.json()['data']['hash']
                print("Checking for change in the Shop Sections... ("+str(count)+")")
                count = count + 1
                
                if newsData != newsDataLoop:

                    print(Fore.GREEN + '\nShop sections have changed!')
                    time.sleep(3)
                    response = requests.get(f'https://fn-api.com/api/shop/sections?lang={language}')
                    ss = response.json()['data']['sections']
                    sections = ""

                    for i in ss:
                        #print(f'{i["sectionName"]} - (x{i["quantity"]})\n')
                        sections += f'{i["name"]} - (x{i["quantity"]})\n'

                    print(sections)

                    print('\nTweeting out the current shop sections...')
                    
                    api.update_status(f'#Fortnite Shop Sections Update:\n\n'+str(sections)+f'\n\n[{namelol}]')
                    print('Tweeted out the shop sections!')
                    shop_sections()
            else:
                print("FAILED TO GRAB SHOP SECTIONS DATA: URL DOWN")

            time.sleep(BotDelay)
    else:
        count = 1
        apiurl = f'https://fn-api.com/api/shop/sections?lang={language}'

        response = requests.get(apiurl)
        newsData = response.json()['data']['hash']

        while 1:
            response = requests.get(apiurl)
            if response:
                newsDataLoop = response.json()['data']['hash']
                print("Checking for change in the Shop Sections... ("+str(count)+") - Image is on")
                count = count + 1
                
                if newsData != newsDataLoop:

                    print(Fore.GREEN + '\nShop sections have changed!')
                    time.sleep(3)
                    response = requests.get(f'https://fn-api.com/api/shop/sections?lang={language}')
                    ss = response.json()['data']['sections']
                    sections = ""

                    for i in ss:
                        #print(f'{i["sectionName"]} - (x{i["quantity"]})\n')
                        sections += f'{i["sectionName"]} - (x{i["quantity"]})\n'

                    print(sections)

                    # Converts hex to RGB

                    color = BG_Color.replace('#', '')
                    color = ImageColor.getcolor(f'#{color}', "RGB")

                    # Creates background with color
                    img=Image.new("RGB",(512,512), (color))
                    img.save('temp.png')
                    background = Image.open('temp.png')

                    # Loads font
                    loadFont = 'fonts/BurbankBigCondensed-Black.otf'

                    # Writes Title

                    cap = 'SHOP SECTIONS'
                    cap = translator.translate(cap, dest=language)
                    print(cap.text)
                    w,h=font.getsize(cap.text)
                    draw=ImageDraw.Draw(background)
                    w1, h1 = draw.textsize(cap.text, font=font)
                    draw.text(((512-w1)/2,20),cap.text,font=font,fill='white')

                    # Writes timestamps
                    
                    timestamp = response.json()['data']['timestamp']
                    timestamp = timestamp.replace('T00:00:00Z', '')

                    font=ImageFont.truetype(loadFont,16)
                    w,h=font.getsize(timestamp)
                    draw=ImageDraw.Draw(background)
                    w1, h1 = draw.textsize(timestamp, font=font)
                    draw.text(((512-w1)/2,76),timestamp,font=font,fill='white')


                    background.save('temp.png')

                    full = ''

                    # Grabs current sections
                    for i in response.json()['data']['sections']:
                        name = i['name']
                        quantity = i['quantity']

                        full += f'{name} - (x{quantity})\n\n'

                    background = Image.open('temp.png')

                    # Writes sections
                    font=ImageFont.truetype(loadFont,20)
                    w,h=font.getsize(full)
                    draw=ImageDraw.Draw(background)
                    w1, h1 = draw.textsize(full, font=font)
                    draw.text(((512-w1)/2,120),full,font=font,fill='white')

                    # Watermark
                    w,h=font.getsize(watermark)
                    draw=ImageDraw.Draw(background)
                    draw.text((5,490),watermark,font=font,fill='white')

                    os.remove('temp.png')

                    background.save('done.png')

                    print('\nTweeting out the current shop sections...')
                    api.update_with_media('sections.png', f'#Fortnite Shop Sections Update')
                    print('Tweeted out the shop sections!')
                    shop_sections()
            else:
                print("FAILED TO GRAB SHOP SECTIONS DATA: URL DOWN")

            time.sleep(BotDelay)