"""
Commons Clause - License Condition v1.0
Copyright thomaskeig 2020
The Software is provided to you by the Licensor under the
License, as defined below, subject to the following condition.
Without limiting other conditions in the License, the grant
of rights under the License will not include, and the License
does not grant to you, the right to Sell the Software.
For purposes of the foregoing, “Sell” means practicing any or
all of the rights granted to you under the License to provide
to third parties, for a fee or other consideration (including
without limitation fees for hosting or consulting/ support
services related to the Software), a product or service whose
value derives, entirely or substantially, from the functionality
of the Software. Any license notice or attribution required by
the License must also include this Commons Clause License
Condition notice.
Software: AUTOLEAK
"""

import requests
import tweepy
import time
import urllib.request
import PIL
from PIL import Image, ImageFont, ImageDraw, ImageChops
import os
import json
import glob
import shutil

from colorama import *
init()

loop = True
count = 1
fontSize = 40
initialCheckDelay = 2
currentVersion = '1.2.4'

response = requests.get('https://pastebin.com/raw/zku0yz9q')
ln1 = response.json()["1"]
ln2 = response.json()["2"]
ln3 = response.json()["3"]
ln4 = response.json()["4"]
ln5 = response.json()["5"]
latestVersion = response.json()["latestVersion"]
print("")
print("------------------------------------------------------------------------------------------------")
print("")
print(ln1)                 #############################################################################
print(ln2)                 #  DO NOT REMOVE THESE LINES OF CODE!                                       #
print(ln3)                 #  IT IS UESD TO COMMUNICATE UPDATES WITH YOU WHEN YOU LAUNCH THE PROGRAM!  #
print(ln4)                 #  IF YOU REMOVE IT YOU WILL NOT BE ALERTED WITH NEWS AND NEW UPDATES!      #
print(ln5)                 #############################################################################
print("")
print("------------------------------------------------------------------------------------------------")
print("")
print("Version info:")
print("")
if latestVersion == currentVersion:
    print('--> This version of AUTOLEAK is up to date!')
else:
    print('--> You are currently running v'+currentVersion+' of AutoLeak, v'+latestVersion+' is now avaliable - Please check #autoleak-updates in the discord server for the update!')
print("")
print("------------------------------------------------------------------------------------------------")
print("")

with open("settings.json") as settings:
    data = json.load(settings)

    try:
        name = data["name"]
        print(Fore.GREEN + 'Loaded "name" as "'+name+'"')
    except:
        name = 'AutoLeak'
        print(Fore.RED + 'Failed to load "name", defaulted to "AutoLeak"')

    try:
        footer = data["footer"]
        print(Fore.GREEN + 'Loaded "footer" as "'+footer+'"')
    except:
        footer = '#Fortnite'
        print(Fore.RED + 'Failed to load "footer", defaulted to "#Fortnite"')

    try:
        language = data["language"]
        if language == 'ar' or language == 'de' or language == 'en' or language == 'es' or language == 'es-419' or language == 'fr' or language == 'it' or language == 'ja' or language == 'ko' or language == 'pl' or language == 'pt-BR' or language == 'de' or language == 'ru' or language == 'tr' or language == 'zh-CN' or language == 'zh-Hant':
            print(Fore.GREEN + 'Loaded "language" as "'+language+'"')
        else:
            language = 'en'
            print(Fore.YELLOW + 'Incorrect value for language was given so I have loaded "language" as "en"')

    except:
        language = 'False'
        print(Fore.RED + 'Failed to load "language", defaulted to "en"')

    try:
        imageFont = data["imageFont"]
        print(Fore.GREEN + 'Loaded "imageFont" as "'+imageFont+'"')
    except:
        imageFont = 'BurbankBigCondensed-Black.otf'
        print(Fore.RED + 'Failed to load "imageFont", defaulted to "BurbankBigCondensed-Black.otf"')

    try:
        placeholderUrl = data["placeholderUrl"]
        print(Fore.GREEN + 'Loaded "placeholderUrl" as "'+placeholderUrl+'"')
    except:
        placeholderUrl = 'https://i.imgur.com/W22Foja.png'
        print(Fore.RED + 'Failed to load "placeholderUrl", set to default placeholder url.')

    try:
        watermark = data["watermark"]
        print(Fore.GREEN + 'Loaded "watermark" as "'+watermark+'"')
    except:
        watermark = ''
        print(Fore.RED + 'Failed to load "watermark", ignored, program will be ran without a watermark.')

    try:
        useFeaturedIfAvaliable = data["useFeaturedIfAvaliable"]
        if useFeaturedIfAvaliable == 'True' or useFeaturedIfAvaliable == 'False':
            print(Fore.GREEN + 'Loaded "useFeaturedIfAvaliable" as "'+useFeaturedIfAvaliable+'"')
        else:
            useFeaturedIfAvaliable = 'False'
            print(Fore.YELLOW + 'Incorrect value for useFeaturedIfAvaliable was given so I have loaded "useFeaturedIfAvaliable" as "False"')
    except:
        useFeaturedIfAvaliable = 'False'
        print(Fore.RED + 'Failed to load "useFeaturedIfAvaliable", defaulted to "False"')

    try:
        iconType = data["iconType"]
        if iconType == 'standard' or iconType == 'clean':
            print(Fore.GREEN + 'Loaded "iconType" as "'+iconType+'"')
        else:
            iconType = 'False'
            print(Fore.YELLOW + 'Incorrect value for iconType was given so I have loaded "iconType" as "standard"')
    except:
        iconType = 'False'
        print(Fore.RED + 'Failed to load "iconType", defaulted to "standard"')

    try:
        benbot = data['BenBot']
        if benbot == 'True':
            print(Fore.GREEN + f'Loaded BenBot API.')
        if benbot == 'False':
            print(Fore.GREEN + 'Loaded Fortnite-API.')

    except:
        benbot = 'False'
        print(Fore.RED + 'Failed to load "ApiType", defaulting to "Fortnite-API"...')

    try:
        twitAPIKey = data["twitAPIKey"]
        print(Fore.GREEN + 'Loaded "twitAPIKey" as "'+twitAPIKey+'"')
    except:
        twitAPIKey = 'XXX'
        print(Fore.RED + 'Failed to load "twitAPIKey", defaulted to "XXX"')

    try:
        twitAPISecretKey = data["twitAPISecretKey"]
        print(Fore.GREEN + 'Loaded "twitAPISecretKey" as "'+twitAPISecretKey+'"')
    except:
        twitAPISecretKey = 'XXX'
        print(Fore.RED + 'Failed to load "twitAPISecretKey", defaulted to "XXX"')

    try:
        twitAccessToken = data["twitAccessToken"]
        print(Fore.GREEN + 'Loaded "twitAccessToken" as "'+twitAccessToken+'"')
    except:
        twitAccessToken = 'XXX'
        print(Fore.RED + 'Failed to load "twitAccessToken", defaulted to "XXX"')

    try:
        twitAccessTokenSecret = data["twitAccessTokenSecret"]
        print(Fore.GREEN + 'Loaded "twitAccessTokenSecret" as "'+twitAccessTokenSecret+'"')
    except:
        twitAccessTokenSecret = 'XXX'
        print(Fore.RED + 'Failed to load "twitAccessTokenSecret", defaulted to "XXX"')

    try:
        tweetUpdate = data["tweetUpdate"]
        if tweetUpdate == 'True' or tweetUpdate == 'False':
            print(Fore.GREEN + 'Loaded "tweetUpdate" as "'+tweetUpdate+'"')
        else:
            tweetUpdate = 'False'
            print(Fore.YELLOW + 'Incorrect value for tweetUpdate was given so I have loaded "tweetUpdate" as "False"')
    except:
        tweetUpdate = 'False'
        print(Fore.RED + 'Failed to load "tweetUpdate", defaulted to "False"')

    try:
        tweetAes = data["tweetAes"]
        if tweetAes == 'True' or tweetAes == 'False':
            print(Fore.GREEN + 'Loaded "tweetAes" as "'+tweetAes+'"')
        else:
            tweetAes = 'False'
            print(Fore.YELLOW + 'Incorrect value for tweetAes was given so I have loaded "tweetAes" as "False"')
    except:
        tweetAes = 'False'
        print(Fore.RED + 'Failed to load "tweetAes", defaulted to "False"')

    auth = tweepy.OAuthHandler(twitAPIKey, twitAPISecretKey)
    auth.set_access_token(twitAccessToken, twitAccessTokenSecret)
    api = tweepy.API(auth)



#-------------------#-------------------#



def update_mode():

    response = requests.get('https://fortnite-api.com/v2/aes')
    updateCompare = response.json()['data']['build']

    response = requests.get('https://fortnite-api.com/v2/aes')
    aesCompare = response.json()['data']['mainKey']

    count = 1
    initialCheckDelay = 2
    while 1:
        response = requests.get('https://fortnite-api.com/v2/aes')
        if response:
            print(Fore.YELLOW+ "Waiting for Fortnite update -> [Count: "+str(count)+"]")
            status = response.json()["status"]
            if status != 200:
                if status == 503:
                    error = response.json()["error"]
                    print(Fore.RED + f"ERROR: {error} please wait...")
                else:
                    print(Fore.RED + "Error in AES Endpoint (Status is not 200 or 503) - Retrying... (This is an error with fortnite-api.com)")
                time.sleep(initialCheckDelay)
            else:
                versionLoop = response.json()["data"]["build"]
                count = count + 1
                if updateCompare != versionLoop:
                    while 2:
                        print("")
                        print(Fore.GREEN+"Detected windows update! Starting "+name+"...")

                        if tweetUpdate == 'True':
                            api.update_status('['+name+'] New Update Detected!\n\n'+str(versionLoop)+'\n\n'+footer)
                            print(Fore.GREEN+"Tweeted 'Status 1' (Includes: Update notification)")

                        count = 1
                        while 3:
                            response = requests.get('https://fortnite-api.com/v2/aes')
                            if response:
                                status = response.json()["status"]
                                if status != 200:
                                    if status == 503:
                                        error = response.json()["error"]
                                        print(Fore.RED + f"ERROR: {error} please wait...")
                                    else:
                                        print(Fore.RED + "Error in AES Endpoint (Status is not 200 or 503) - Retrying... (This is an error with fortnite-api.com)")
                                    time.sleep(initialCheckDelay)
                                else:

                                    print(Fore.YELLOW+ "Waiting for AES update -> [Count: "+str(count)+"]")
                                    mainKey = response.json()["data"]["mainKey"]
                                    mainKeyVersion1 = response.json()["data"]["build"].replace('++Fortnite+Release-', '')
                                    mainKeyVersion = mainKeyVersion1.replace('-Windows', '')
                                    count = count + 1

                                    if aesCompare != mainKey:

                                        print(Fore.GREEN+"Detected aes update!")

                                        if tweetAes == 'True':
                                            api.update_status('['+name+'] AES Key for v'+str(mainKeyVersion)+':\n\n0x'+str(mainKey)+'\n\n'+footer)
                                            print(Fore.GREEN + "Tweeted 'Status 2' (Includes: AES Key)")

                                        count = 1
                                        while 4:
                                            response = requests.get('https://fortnite-api.com/v2/cosmetics/br/new?language='+language)
                                            if response:
                                                status = response.json()["status"]
                                                if status != 200:
                                                    if status == 503:
                                                        error = response.json()["error"]
                                                        print(Fore.RED + f"ERROR: {error} please wait...")
                                                    else:
                                                        print(Fore.RED + "Error in Cosmetics Endpoint (Status is not 200 or 503) - Retrying... (This is an error with fortnite-api.com)")
                                                    time.sleep(initialCheckDelay)
                                                else:

                                                    print(Fore.YELLOW+ "Waiting for endpoint update -> [Count: "+str(count)+"]")

                                                    response = requests.get('https://fortnite-api.com/v2/cosmetics/br/new?language='+language)
                                                    newBuild = response.json()["data"]["build"]

                                                    count = count + 1
                                                    if versionLoop == newBuild:
                                                        generate_cosmetics()
                                                        return

                                                    else:
                                                        time.sleep(initialCheckDelay)

                                            else:
                                                print(Fore.RED + "Error in COSMETICS Endpoint (Page Down) - Retrying... (This is an error with fortnite-api.com)")
                                                time.sleep(initialCheckDelay)

                                    time.sleep(initialCheckDelay)
                            else:
                                print(Fore.RED + "Error in AES Endpoint 2 (Page Down) - Retrying... (This is an error with fortnite-api.com)")
                                time.sleep(initialCheckDelay)

                time.sleep(initialCheckDelay)
        else:
            print(Fore.RED + "Error in AES Endpoint 1 (Page Down) - Retrying... (This is an error with fortnite-api.com)")
            time.sleep(initialCheckDelay)

def generate_cosmetics():

    if benbot == 'False':
            print('Loading Fortnite-API...\n')
            fontSize = 40
            response = requests.get('https://fortnite-api.com/v2/cosmetics/br/new?language='+language)
            new = response.json()
    
            print(f"Generating {len(new['data']['items'])} new cosmetics from Fortnite-API...")
            print('')
            loop = False
            counter = 1
            start = time.time()
            for i in new["data"]["items"]:
                try:
                
                    print(Fore.BLUE + "Loading image for "+i["id"])
    
                    if useFeaturedIfAvaliable == 'True':
                        if i["images"]["featured"] != None:
                            url = i["images"]["featured"]
                        else:
                            url = i["images"]["icon"]
                    elif useFeaturedIfAvaliable == 'False':
                        url = i["images"]["icon"]
    
                    placeholderImg = Image.open('assets/doNotDelete.png')
    
    
                    r = requests.get(url, allow_redirects=True)
                    open(f'cache/{i["id"]}.png', 'wb').write(r.content)
                    iconImg = Image.open(f'cache/{i["id"]}.png')
    
                    diff = ImageChops.difference(placeholderImg, iconImg)
    
                    if diff.getbbox():
                        r = requests.get(url, allow_redirects=True)
                        open(f'cache/{i["id"]}.png', 'wb').write(r.content)
    
                        img=Image.open(f'cache/{i["id"]}.png')
                        img=img.resize((512,512),PIL.Image.ANTIALIAS)
                        img.save(f'cache/{i["id"]}.png')
                    else:
                        try:
                            r = requests.get(placeholderUrl, allow_redirects=True)
                            open(f'cache/{i["id"]}.png', 'wb').write(r.content)
    
                            img=Image.open(f'cache/{i["id"]}.png')
                            img=img.resize((512,512),PIL.Image.ANTIALIAS)
                            img.save(f'cache/{i["id"]}.png')
                        except:
                            continue
                        
                        
                        
                    rarity = i["rarity"]["value"]
                    foreground = Image.open('cache/'+i["id"]+'.png')
                    try:
                        background = Image.open(f'rarities/{iconType}/{rarity}.png')
                        border = Image.open(f'rarities/{iconType}/border{rarity}.png')
                    except:
                        background = Image.open(f'rarities/{iconType}/common.png')
                        border = Image.open(f'rarities/{iconType}/bordercommon.png')
    
    
                    Image.alpha_composite(background, foreground).save('cache/F'+i["id"]+'.png')
                    os.remove('cache/'+i["id"]+'.png')
    
    
                    background = Image.open('cache/F'+i["id"]+'.png')
                    Image.alpha_composite(background, border).save('cache/BLANK'+i["id"]+'.png')
    
    
                    costype = i["type"]["displayValue"]
    
    
                    img=Image.open('cache/BLANK'+i["id"]+'.png')
    
                    name= i["name"]
                    loadFont = 'fonts/'+imageFont
    
                    if len(name) > 20:
                        fontSize = 30
                    if len(name) > 30:
                        fontSize = 20
    
                    if iconType == 'clean':
                        font=ImageFont.truetype(loadFont,fontSize)
                        w,h=font.getsize(name)
                        draw=ImageDraw.Draw(img)
                        draw.text((25,440),name,font=font,fill='white')
    
                        fontSize = 40
                        id = i["id"]
                        font=ImageFont.truetype(loadFont,30)
                        w,h=font.getsize(costype)
                        draw=ImageDraw.Draw(img)
                        draw.text((25,402),costype,font=font,fill='white')
    
                        if watermark != '':
                            font=ImageFont.truetype(loadFont,25)
                            w,h=font.getsize(watermark)
                            draw=ImageDraw.Draw(img)
                            draw.text((30,30),watermark,font=font,fill='white')
    
                    elif iconType == 'standard':
                        font=ImageFont.truetype(loadFont,fontSize)
                        w,h=font.getsize(name)
                        draw=ImageDraw.Draw(img)
                        w1, h1 = draw.textsize(name, font=font)
                        draw.text(((512-w1)/2,390),name,font=font,fill='white')
    
                        fontSize = 40
    
                        desc = i["description"]
                        font=ImageFont.truetype(loadFont,15)
                        w,h=font.getsize(desc)
                        draw=ImageDraw.Draw(img)
                        w1, h1 = draw.textsize(desc, font=font)
                        draw.text(((512-w1)/2,455),desc,font=font,fill='white')
    
                        id = i["id"]
                        font=ImageFont.truetype(loadFont,15)
                        w,h=font.getsize(id)
                        draw=ImageDraw.Draw(img)
                        w1, h1 = draw.textsize(id, font=font)
                        draw.text(((512-w1)/2,475),id,font=font,fill='white')
    
                        font=ImageFont.truetype(loadFont,20)
                        w,h=font.getsize(costype)
                        draw=ImageDraw.Draw(img)
                        w1, h1 = draw.textsize(costype, font=font)
                        draw.text(((512-w1)/2,430),costype,font=font,fill='white')
    
                        if watermark != '':
                            font=ImageFont.truetype(loadFont,25)
                            w,h=font.getsize(watermark)
                            draw=ImageDraw.Draw(img)
                            draw.text((10,9),watermark,font=font,fill='white')
                    os.remove('cache/BLANK'+i["id"]+'.png')
    
                    img.save('icons/'+i["id"]+'.png')
                    os.remove('cache/F'+i["id"]+'.png')
    
                    percentage = counter/len(new['data']['items'])
                    realpercentage = percentage * 100
    
                    print(Fore.CYAN + f"Generated image for {id}")
                    print(Fore.CYAN + f"{counter}/{len(new['data']['items'])} - {round(realpercentage)}%")
                    print("")
                    counter = counter + 1
                except:
                    print(Fore.YELLOW + "Ignored due to error: "+i["id"])
            end = time.time()
            print("")
    
            print(Fore.GREEN+"")
            print("!  !  !  !  !  !  !")
            print(f"IMAGE GENERATING COMPLETE - Generated images in {round(end - start, 2)} seconds")
            print("!  !  !  !  !  !  !")
    
    if benbot == 'True':
        print('Loading BenBot...\n')
        fontSize = 40
        response = requests.get('https://benbotfn.tk/api/v1/newCosmetics')
        new = response.json()
    
        print(f"Generating {len(new['items'])} new cosmetics from BenBot...")
        print('')
        loop = False
        counter = 1
        start = time.time()
        for i in new["items"]:
            try:
            
                print(Fore.BLUE + "Loading image for "+i["id"])
    
                if useFeaturedIfAvaliable == 'True':
                    if i["icons"]["featured"] != None:
                        url = i["icons"]["featured"]
                    else:
                        url = i["icons"]["icon"]
                elif useFeaturedIfAvaliable == 'False':
                    url = i["icons"]["icon"]
    
                placeholderImg = Image.open('assets/doNotDelete.png')
    
    
                r = requests.get(url, allow_redirects=True)
                open(f'cache/{i["id"]}.png', 'wb').write(r.content)
                iconImg = Image.open(f'cache/{i["id"]}.png')
    
                diff = ImageChops.difference(placeholderImg, iconImg)
    
                if diff.getbbox():
                    r = requests.get(url, allow_redirects=True)
                    open(f'cache/{i["id"]}.png', 'wb').write(r.content)
    
                    img=Image.open(f'cache/{i["id"]}.png')
                    img=img.resize((512,512),PIL.Image.ANTIALIAS)
                    img.save(f'cache/{i["id"]}.png')
                else:
                    try:
                        r = requests.get(placeholderUrl, allow_redirects=True)
                        open(f'cache/{i["id"]}.png', 'wb').write(r.content)
    
                        img=Image.open(f'cache/{i["id"]}.png')
                        img=img.resize((512,512),PIL.Image.ANTIALIAS)
                        img.save(f'cache/{i["id"]}.png')
                    except:
                        continue
                    
                    
                    
                rarity = i["rarity"]
                foreground = Image.open('cache/'+i["id"]+'.png')
                try:
                    background = Image.open(f'rarities/{iconType}/{rarity}.png')
                    border = Image.open(f'rarities/{iconType}/border{rarity}.png')
                except:
                    background = Image.open(f'rarities/{iconType}/common.png')
                    border = Image.open(f'rarities/{iconType}/bordercommon.png')
    
    
                Image.alpha_composite(background, foreground).save('cache/F'+i["id"]+'.png')
                os.remove('cache/'+i["id"]+'.png')
    
    
                background = Image.open('cache/F'+i["id"]+'.png')
                Image.alpha_composite(background, border).save('cache/BLANK'+i["id"]+'.png')
    
    
                costype = i['rarity']
    
    
                img=Image.open('cache/BLANK'+i["id"]+'.png')
    
                name= i["name"]
                loadFont = 'fonts/'+imageFont
    
                if len(name) > 20:
                    fontSize = 30
                if len(name) > 30:
                    fontSize = 20
    
                if iconType == 'clean':
                    font=ImageFont.truetype(loadFont,fontSize)
                    w,h=font.getsize(name)
                    draw=ImageDraw.Draw(img)
                    draw.text((25,440),name,font=font,fill='white')
    
                    fontSize = 40
                    id = i["id"]
                    font=ImageFont.truetype(loadFont,30)
                    w,h=font.getsize(costype)
                    draw=ImageDraw.Draw(img)
                    draw.text((25,402),costype,font=font,fill='white')
    
                    if watermark != '':
                        font=ImageFont.truetype(loadFont,25)
                        w,h=font.getsize(watermark)
                        draw=ImageDraw.Draw(img)
                        draw.text((30,30),watermark,font=font,fill='white')
    
                elif iconType == 'standard':
                    font=ImageFont.truetype(loadFont,fontSize)
                    w,h=font.getsize(name)
                    draw=ImageDraw.Draw(img)
                    w1, h1 = draw.textsize(name, font=font)
                    draw.text(((512-w1)/2,390),name,font=font,fill='white')
    
                    fontSize = 40
    
                    desc = i["description"]
                    font=ImageFont.truetype(loadFont,15)
                    w,h=font.getsize(desc)
                    draw=ImageDraw.Draw(img)
                    w1, h1 = draw.textsize(desc, font=font)
                    draw.text(((512-w1)/2,455),desc,font=font,fill='white')
    
                    id = i["id"]
                    font=ImageFont.truetype(loadFont,15)
                    w,h=font.getsize(id)
                    draw=ImageDraw.Draw(img)
                    w1, h1 = draw.textsize(id, font=font)
                    draw.text(((512-w1)/2,475),id,font=font,fill='white')
    
                    font=ImageFont.truetype(loadFont,20)
                    w,h=font.getsize(costype)
                    draw=ImageDraw.Draw(img)
                    w1, h1 = draw.textsize(costype, font=font)
                    draw.text(((512-w1)/2,430),costype,font=font,fill='white')
    
                    if watermark != '':
                        font=ImageFont.truetype(loadFont,25)
                        w,h=font.getsize(watermark)
                        draw=ImageDraw.Draw(img)
                        draw.text((10,9),watermark,font=font,fill='white')
                os.remove('cache/BLANK'+i["id"]+'.png')
    
                img.save('icons/'+i["id"]+'.png')
                os.remove('cache/F'+i["id"]+'.png')
    
                percentage = counter/len(new['items'])
                realpercentage = percentage * 100
    
                print(Fore.CYAN + f"Generated image for {id}")
                print(Fore.CYAN + f"{counter}/{len(new['items'])} - {round(realpercentage)}%")
                print("")
                counter = counter + 1
            except:
                print(Fore.YELLOW + "Ignored due to error: "+i["id"])
        end = time.time()
        print("")
    
        print(Fore.GREEN+"")
        print("!  !  !  !  !  !  !")
        print(f"IMAGE GENERATING COMPLETE - Generated images in {round(end - start, 2)} seconds")
        print("!  !  !  !  !  !  !")

def check_version():
    response = requests.get('https://pastebin.com/raw/zku0yz9q')
    latestVersion = response.json()["latestVersion"]

    if currentVersion == latestVersion:
        app.info("AutoLeak v"+currentVersion, "You already have the latest version")
    else:
        app.info("AutoLeak v"+currentVersion, f"Alert! You are using v{currentVersion} but version v{latestVersion} is avaliable!\nHead to the discord server to download the update!")

def edit_function():
    os.startfile('settings.json')

def tweet_aes():
    try:
        response = requests.get('https://fortnite-api.com/v2/aes')
        twitaes = response.json()["data"]["mainKey"]
        api.update_status(f'[{name}] Current Fortnite AES Key:\n\n0x{str(twitaes)}\n\n{footer}')
        print(Fore.GREEN+"Tweeted current aes key!")
    except:
        print(Fore.RED+"Failed to tweet current aes key!")

def tweet_build():
    try:
        response = requests.get('https://fortnite-api.com/v2/aes')
        twitbuild = response.json()["data"]["build"]
        api.update_status(f'[{name}] Current Fortnite build:\n\n{str(twitbuild)}\n\n{footer}')
        print(Fore.GREEN+"Tweeted current build!")
    except:
        print(Fore.RED+"Failed to tweet current build!")

def search_cosmetic():
    fontSize = 40
    print('\nWhat cosmetic do you want to grab?')
    ask = input()
    response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?name={ask}')

    print(f'\nGenerating {ask}...')
    print('')

    try:
        i = response.json()['data']
        # Item Successfully grabbed
    except:
        print(Fore.RED + f'Unable to retreive {ask}.')
        time.sleep(5)
        exit()

    print(Fore.BLUE + "Loading image for "+i["id"])


    if useFeaturedIfAvaliable == 'True':
        if i["images"]["featured"] != None:
            url = i["images"]["featured"]
        else:
            url = i["images"]["icon"]
    elif useFeaturedIfAvaliable == 'False':
        url = i["images"]["icon"]

    placeholderImg = Image.open('assets/doNotDelete.png')


    r = requests.get(url, allow_redirects=True)
    open(f'cache/{i["id"]}.png', 'wb').write(r.content)
    iconImg = Image.open(f'cache/{i["id"]}.png')

    diff = ImageChops.difference(placeholderImg, iconImg)

    if diff.getbbox():
        r = requests.get(url, allow_redirects=True)
        open(f'cache/{i["id"]}.png', 'wb').write(r.content)

        img=Image.open(f'cache/{i["id"]}.png')
        img=img.resize((512,512),PIL.Image.ANTIALIAS)
        img.save(f'cache/{i["id"]}.png')
    else:
        try:
            r = requests.get(placeholderUrl, allow_redirects=True)
            open(f'cache/{i["id"]}.png', 'wb').write(r.content)

            img=Image.open(f'cache/{i["id"]}.png')
            img=img.resize((512,512),PIL.Image.ANTIALIAS)
            img.save(f'cache/{i["id"]}.png')
        except:
            print('')

    rarity = i["rarity"]["value"]
    foreground = Image.open('cache/'+i["id"]+'.png')
    try:
        background = Image.open(f'rarities/{iconType}/{rarity}.png')
        border = Image.open(f'rarities/{iconType}/border{rarity}.png')
    except:
        background = Image.open(f'rarities/{iconType}/common.png')
        border = Image.open(f'rarities/{iconType}/bordercommon.png')


    Image.alpha_composite(background, foreground).save('cache/F'+i["id"]+'.png')
    os.remove('cache/'+i["id"]+'.png')


    background = Image.open('cache/F'+i["id"]+'.png')
    Image.alpha_composite(background, border).save('cache/BLANK'+i["id"]+'.png')


    costype = i["type"]["displayValue"]


    img=Image.open('cache/BLANK'+i["id"]+'.png')

    name= i["name"]
    loadFont = 'fonts/'+imageFont

    if len(name) > 20:
        fontSize = 30
    if len(name) > 30:
        fontSize = 20

    if iconType == 'clean':
        font=ImageFont.truetype(loadFont,fontSize)
        w,h=font.getsize(name)
        draw=ImageDraw.Draw(img)
        draw.text((25,440),name,font=font,fill='white')

        fontSize = 40
        id = i["id"]
        font=ImageFont.truetype(loadFont,30)
        w,h=font.getsize(costype)
        draw=ImageDraw.Draw(img)
        draw.text((25,402),costype,font=font,fill='white')

        if watermark != '':
            font=ImageFont.truetype(loadFont,25)
            w,h=font.getsize(watermark)
            draw=ImageDraw.Draw(img)
            draw.text((30,30),watermark,font=font,fill='white')

    elif iconType == 'standard':
        font=ImageFont.truetype(loadFont,fontSize)
        w,h=font.getsize(name)
        draw=ImageDraw.Draw(img)
        w1, h1 = draw.textsize(name, font=font)
        draw.text(((512-w1)/2,390),name,font=font,fill='white')

        fontSize = 40

        desc = i["description"]
        font=ImageFont.truetype(loadFont,15)
        w,h=font.getsize(desc)
        draw=ImageDraw.Draw(img)
        w1, h1 = draw.textsize(desc, font=font)
        draw.text(((512-w1)/2,455),desc,font=font,fill='white')

        id = i["id"]
        font=ImageFont.truetype(loadFont,15)
        w,h=font.getsize(id)
        draw=ImageDraw.Draw(img)
        w1, h1 = draw.textsize(id, font=font)
        draw.text(((512-w1)/2,475),id,font=font,fill='white')

        font=ImageFont.truetype(loadFont,20)
        w,h=font.getsize(costype)
        draw=ImageDraw.Draw(img)
        w1, h1 = draw.textsize(costype, font=font)
        draw.text(((512-w1)/2,430),costype,font=font,fill='white')

        if watermark != '':
            font=ImageFont.truetype(loadFont,25)
            w,h=font.getsize(watermark)
            draw=ImageDraw.Draw(img)
            draw.text((10,9),watermark,font=font,fill='white')
    os.remove('cache/BLANK'+i["id"]+'.png')

    img.save('icons/'+i["id"]+'.png')
    os.remove('cache/F'+i["id"]+'.png')

    print(Fore.CYAN + f"Generated image for {id}")

    print('Saving file...')

    print(Fore.GREEN+"\nFinished successfully!")

def delete_contents():
    print('Deleting contents of the Icons folder...')
    try:
        shutil.rmtree('icons')
        os.makedirs('icons')
    except:
        os.makedirs('icons')
    print('Cleared contents!')

print("- - - - - MENU - - - - -")
print("")
print("(1) - Start update mode")
print("(2) - Generate new cosmetics")
print("(3) - Tweet current build")
print("(4) - Tweet current AES key")
print("(5) - Search for a cosmetic")
print("(6) - Clear contents of the icon folder")
print("")
option_choice = input(">> ")
if option_choice == "1":
    update_mode()
elif option_choice == "2":
    generate_cosmetics()
elif option_choice == "3":
    tweet_build()
elif option_choice == "4":
    tweet_aes()
elif option_choice == "5":
    search_cosmetic()
elif option_choice == "6":
    delete_contents()
else:
    print("Please enter a number between 1 and 6")

# ALL STUFF BELOW IS FOR THE OLD GUI AUTOLEAK, KEEPING AS A COMMENT TO SAVE FOR FURTHER NOTICE

#app = App(title="AutoLeak v"+currentVersion, bg='#36393f', width=400, height=750)
# menubar = MenuBar(app,
#                   toplevel=["AutoLeak", "Settings"],
#                   options=[
#                       [ ["Check for update", check_version] ],
#                       [ ["Open settings in JSON", edit_function] ]
#                   ])
#
# picture = Picture(app, image="assets/al-white.png")
# label = Text(app, size=40, text="AutoLeak", color='white', font='BurbankBigCondensed-Black')
# label = Text(app, size=20, text=f'v{currentVersion}', color='white', font='BurbankBigCondensed-Black')
# picture = Picture(app, image="assets/Images/autoleak-options.png")
# button = PushButton(app, image='assets/Buttons/update-button.png', command=update_mode)
# label = Text(app, text="")
# button = PushButton(app, image='assets/Buttons/generate-button.png', command=generate_cosmetics)
# picture = Picture(app, image="assets/Images/twitter-options.png")
# button = PushButton(app, image='assets/Buttons/twitbuild-button.png', command=tweet_build)
# label = Text(app, text="")
# button = PushButton(app, image='assets/Buttons/twitaes-button.png', command=tweet_aes)
# picture = Picture(app, image="assets/Images/general-options.png")
# label = Text(app, text="COMING SOON", color='white')
# label = Text(app, text="")
# label = Text(app, size=10, text="Developed by @thomaskeig#0001", color='white')
#
# app.display()
