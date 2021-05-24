# If you have any issues with the softwere, please message Fevers#3474 on discord. #

"""
Commons Clause - License Condition v1.0
Copyright Fevers 2021
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

Please note: You also do not have the right to edit this program
and distribute it to others. You are allowed to edit the program
for personal use, but if you do edit it, you are not allowed
to distribute to others.

Software: AUTOLEAK
"""

import requests
import tweepy
import time
import urllib.request
import PIL
import math
from PIL import Image, ImageFont, ImageDraw, ImageChops
import os
import json
import glob
import shutil
import math
import datetime
import webbrowser
from datetime import date
from datetime import datetime
import random

now = datetime.now()

current_time = now.strftime("%H:%M")

from os import listdir
from colorama import *
init()

loop = True
count = 1
fontSize = 40
initialCheckDelay = 2
currentVersion = '1.3.8'

os.system("cls")
os.system(
    "TITLE AutoLeak / Created by Fevers.")

# Starting Popup
import ctypes

rannumber = random.randint(1, 2)
if rannumber == 1:
    def Mbox(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    Mbox('AutoLeak - Created by Fevers.', f'Hey There! Welcome to AutoLeak, the easiest way to Auto-Leak Fortnite. \nMake sure to join our discord by clicking the OK button!\n\n\nYou are on AutoLeak version v{currentVersion}!', 0)
    webbrowser.open_new('https://discord.gg/UZgHArwp4f')
else:
    pass

# Used to communicate with updates
response = requests.get('https://pastebin.com/raw/zku0yz9q')
ln1 = response.json()["1"]
ln2 = response.json()["2"]
ln3 = response.json()["3"]
ln4 = response.json()["4"]
ln5 = response.json()["5"]
ln6 = response.json()["6"]
ln7 = response.json()["7"]
latestVersion = response.json()["latestVersion"]
print("")
print("------------------------------------------------------------------------------------------------")
print("")
print(ln1)                 #############################################################################
print(ln2)                 #  DO NOT REMOVE THESE LINES OF CODE!                                       #
print(ln3)                 #  IT IS UESD TO COMMUNICATE UPDATES WITH YOU WHEN YOU LAUNCH THE PROGRAM!  #
print(ln4)                 #  IF YOU REMOVE IT YOU WILL NOT BE ALERTED WITH NEWS AND NEW UPDATES!      #
print(ln5)                 #############################################################################
print(ln6)
print(ln7)
print("")
print("------------------------------------------------------------------------------------------------")
print("")
print("Version info:")
print("")

if latestVersion == currentVersion:
    print(Fore.GREEN + '--> This version of AUTOLEAK is up to date!')
else:
    print(Fore.RED + '--> You are currently running v'+currentVersion+' of AutoLeak, v'+latestVersion+' is now avaliable - Please check #updates in the AutoLeak discord server for the update!')
print("")
print(Style.RESET_ALL + "------------------------------------------------------------------------------------------------")
print("")

# Used to communicate with settings.json, grab all user inputs from it.

with open("settings.json") as settings:
    data = json.load(settings)

    try:
        name = data["name"]
        namelol = data["name"]
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
        if iconType == 'standard' or iconType == 'clean' or iconType == 'new':
            print(Fore.GREEN + 'Loaded "iconType" as "'+iconType+'"')
        else:
            iconType = 'standard'
            print(Fore.YELLOW + 'Incorrect value for iconType was given so I have loaded "iconType" as "standard"')
    except:
        iconType = 'standard'
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
        if twitAPIKey == '':
            twitAPIKey = 'XXX'
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

    try:
        BotDelay = data['BotDelay']
        print(Fore.GREEN + f'Loaded "BotDelay" as {BotDelay} seconds.')
    except:
        BotDelay = 30
        print(Fore.RED + 'Failed to load "BotDelay", defaulted to 30 seconds.')
        
    try:
        twitsearch = data['TweetSearch']
        if twitsearch == 'True' or twitsearch == 'False':
            print(Fore.GREEN + f'Loaded "Tweet Search" as {twitsearch}.')
        else:
            twitsearch = 'True'
            print(Fore.YELLOW + 'Incorrect value for "Twitter Search", defaulting to "True"...')
    except:
        twitsearch = 'False'
        print(Fore.RED + 'Failed to load "Tweet Search", defaulting to "False"...')
        
    try:
        MergeImagesAuto = data['MergeImages']
        if MergeImagesAuto == 'True' or MergeImagesAuto == 'False':
            print(Fore.GREEN + f'Loaded "MergeImages" as "{MergeImagesAuto}"')
        else:
            MergeImagesAuto = 'True'
            print(Fore.YELLOW + f'Incorrect value for MergeImages was given so I have loaded "MergeImages" as "True"')
    except:
        print(Fore.YELLOW + 'Incorrect value for "MergeImages", defaulting to "True"...')
        MergeImagesAuto = 'True'

    try:
        CreatorCode = data['CreatorCode']
        if CreatorCode != '':
            print(Fore.GREEN + f'Loaded "CreatorCode" as "{CreatorCode}')
        else:
            print(Fore.GREEN + 'Loaded Creator Code as none.')
            CreatorCode = ''
    except:
        CreatorCode = ''
        print(Fore.YELLOW + 'Incorrect value for "CreatorCode", defaulting to none.')
        
    try:
        apikey = data['apikey']
        if apikey != "":
            print(Fore.GREEN + f'Loaded "API Key" as "{apikey}"')
        else:
            print(Fore.GREEN + 'Loaded API Key as none.')
            CreatorCode = ''
    except:
        apikey = ''
        print(Fore.YELLOW + 'Incorrect value for "apikey", defaulting to none.')   
    
    try:
        showitemsource = data['showitemsource']
        showitemsource = showitemsource.title()
        if showitemsource != "":
            print(Fore.GREEN+f'Loaded "showitemsource" as "{showitemsource}"')
        else:
            print(Fore.GREEN+f'Loaded showitemsource as False.')
    except:
        print(Fore.YELLOW+'Incorrect value for "ShowItemSource", defaulting to True.')
        showitemsource = 'True'
        
    try:
        mergewatermark = data['MergeWatermarkUrl']
        if mergewatermark != "":
            print(Fore.GREEN+f'Loaded "MergeWatermark" as "{mergewatermark}')
        else:
            print(Fore.GREEN+f'Loaded "MergeWatermark" as None.')
            mergewatermark = ""
    except:
        print(Fore.YELLOW+'Incorrect value for "mergewatermark", defaulting to None.')
        mergewatermark = ""

# Sets up Twitter API keys        
auth = tweepy.OAuthHandler(twitAPIKey, twitAPISecretKey)
auth.set_access_token(twitAccessToken, twitAccessTokenSecret)
api = tweepy.API(auth)

# Sets up fortniteapi.io API key
headers = {'Authorization': apikey}

#-------------------#-------------------#


# Defines update mode
def update_mode():

    #Grabs Build
    response = requests.get('https://fortnite-api.com/v2/aes')
    updateCompare = response.json()['data']['build']

    # Grabes AES
    aesCompare = response.json()['data']['mainKey']

    count = 1
    initialCheckDelay = 2
    while 1: # While 1 checks for a Fortnite Update
        response = requests.get('https://fortnite-api.com/v2/aes')
        if response:
            print(Fore.YELLOW+ f'Waiting for Fortnite update -> [Count: {count}] BenBot = {benbot}')
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
                    while 2: # If it detects an update, THEN post build and map.
                        print("")
                        print(Fore.GREEN+"Detected windows update! Starting "+name+"...")

                        if tweetUpdate == 'True':
                            api.update_status('['+name+'] New Update Detected!\n\n'+str(versionLoop)+'\n\n'+footer)
                            print(Fore.GREEN+"Tweeted 'Status 1' (Includes: Update notification)")

                        #==========#

                        if tweetUpdate == 'True':
                            #=== MAP ===#
                            print('\nTweeting map...')
                            response = requests.get('https://fortnite-api.com/v1/map')
                            map = response.json()['data']['images']['blank']
                            r = requests.get(map, allow_redirects=True)
                            open('map.png', 'wb').write(r.content)
                            print("Opened map.png")
                            img=Image.open('map.png')
                            img=img.resize((1200,1200),PIL.Image.ANTIALIAS)
                            img.save('map.png')
                            response = requests.get('https://benbotfn.tk/api/v1/status')
                            version = response.json()['currentFortniteVersionNumber']
                            api.update_with_media('smallmap.png', f'#Fortnite Map Update:\n\nBattle Royale map for v{version}0.')
                            #=== MAP ===#

                            #=== VERSIONBOT ===#
                            response = requests.get('https://benbotfn.tk/api/v1/aes')
                            aes = response.json()['mainKey']
                            response = requests.get('https://benbotfn.tk/api/v1/status')
                            version = response.json()['currentFortniteVersionNumber']
                            build = response.json()['currentFortniteVersion']
                            paks = response.json()['totalPakCount']
                            dynamicpaks = response.json()['dynamicPakCount']
                            print(f'\nThe current version v'+str(version)+'0'+' has been succesfully retrived!')
                            print('The AES key, Paks, and Build have now been retreived also.')
                            time.sleep(1)
                            api.update_status('A #Fortnite update has been detected... \n\nVersion Number: v'+str(version)+'0'+'\n\nBuild: '+str(build)+':\n\n'+str(paks)+' - Pak Files\n\n'+str(dynamicpaks)+' - Dynamic Pak Files'+'\n\n'+str(aes)+' - AES key')
                            #=== VERSIONBOT ===#
                            
                        count = 1 
                        while 3: # While 3 posts the AES key.
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

                                    print(Fore.YELLOW+ f"Waiting for AES update -> [Count: "+str(count)+"]")
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
                                        while 4: # While 4 checks if BenBot and/or Fortnite-API has updated with the new cosmetics.
                                            if benbot == 'False' or 'false':
                                                print('Loaded Fortnite-API.')
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
                                            else: # Then loads BenBot to generate the new cosmetics.
                                                print('Loaded BenBot.')
                                                response = requests.get('https://benbotfn.tk/api/v1/newCosmetics')
                                                if response:
                                                    currentVersion = response.json()["currentVersion"]
                                                    oldVersion = response.json()['previousVersion']

                                                    # If the old version does NOT equal the current version, then an error has occured as the API should of updated already.

                                                    if oldVersion != currentVersion:
                                                        if currentVersion == oldVersion:
                                                            error = response.json()["error"]
                                                            print(Fore.RED + f"ERROR: {error} please wait...")
                                                        else:
                                                            print(Fore.RED + "Error in Cosmetics Endpoint (Status is not 200 or 503) - Retrying... (This is an error with BenBot...)")
                                                        time.sleep(initialCheckDelay)
                                                    
                                                    # Everything went to plan, so do this now.
                                                    else:
                                                        print(Fore.YELLOW+ "Waiting for endpoint update -> [Count: "+str(count)+"]")

                                                        response = requests.get('https://benbotfn.tk/api/v1/newCosmetics')
                                                        newBuild = response.json()["currentVersion"]

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
    if iconType == 'new':
        newcnew()
        return
    else:
        pass
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
    
                    name1= i["name"]
                    loadFont = 'fonts/'+imageFont
    
                    if len(name1) > 20:
                        fontSize = 30
                    if len(name1) > 30:
                        fontSize = 20
    
                    if iconType == 'clean':
                        font=ImageFont.truetype(loadFont,fontSize)
                        w,h=font.getsize(name1)
                        draw=ImageDraw.Draw(img)
                        draw.text((25,440),name1,font=font,fill='white')
    
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
                        w,h=font.getsize(name1)
                        draw=ImageDraw.Draw(img)
                        w1, h1 = draw.textsize(name1, font=font)
                        draw.text(((512-w1)/2,390),name1,font=font,fill='white')
    
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
                    print(Fore.YELLOW + f"Ignored due to error: "+i["id"]+"\n")
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
                rarity = rarity.lower()
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
    
                name1= i["name"]
                loadFont = 'fonts/'+imageFont
    
                if len(name1) > 20:
                    fontSize = 30
                if len(name1) > 30:
                    fontSize = 20
    
                if iconType == 'clean':
                    font=ImageFont.truetype(loadFont,fontSize)
                    w,h=font.getsize(name1)
                    draw=ImageDraw.Draw(img)
                    draw.text((25,440),name1,font=font,fill='white')
    
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
                    w,h=font.getsize(name1)
                    draw=ImageDraw.Draw(img)
                    w1, h1 = draw.textsize(name1, font=font)
                    draw.text(((512-w1)/2,390),name1,font=font,fill='white')
    
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
                      
    if MergeImagesAuto != 'False':
        print('\nMerging images...')
        if mergewatermark != '':
            r = requests.get(mergewatermark, allow_redirects=True)
            open('icons/zzzwatermark.png', 'wb').write(r.content)
        else:
            pass
        images = [file for file in listdir('icons')]
        count = int(round(math.sqrt(len(images)+0.5), 0))
        #print(len(images), count)
        xlol = len(images)
        print(f'\nFound {xlol} images in "Icons" folder.')
        finalImg = Image.new("RGBA", (512*count, 512*count))
        #draw = ImageDraw.Draw(finalImg)
        x = 0
        y = 0
        counter = 0
        for img in images:
            tImg = Image.open(f"icons/{img}")
            if counter >= count:
                y += 512
                x = 0
                counter = 0
            finalImg.paste(tImg, (x, y), tImg)
            x += 512
            counter += 1
        finalImg.show()
        finalImg.save(f'merged/MERGED {xlol}.png')
        print('\nSaved image!')
        if twitAPIKey != 'XXX':
            print('\nTweeting out image....')
            print('What text do you want the Tweet to say?')
            text = input()
            try:
                api.update_with_media(f'merged/MERGED {xlol}.png', f'[{namelol}] {text}')
            except:
                print(Fore.RED + 'File size is too big.')
                time.sleep(5)
            print('\nTweeted image successfully!')
            time.sleep(5)
        else:
            print('Not Tweeting.')
    else:
        print(Fore.RED + '\nNot merging images.')
        time.sleep(5)

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
        api.update_status(f'[{namelol}] Current Fortnite AES Key:\n\n0x{str(twitaes)}\n\n{footer}')
        print(Fore.GREEN+"Tweeted current aes key!")
        time.sleep(5)
    except:
        print(Fore.RED+"Failed to tweet current aes key!")

def tweet_build():
    try:
        response = requests.get('https://fortnite-api.com/v2/aes')
        twitbuild = response.json()["data"]["build"]
        api.update_status(f'[{namelol}] Current Fortnite build:\n\n{str(twitbuild)}\n\n{footer}')
        print(Fore.GREEN+"Tweeted current build!")
        time.sleep(5)
    except:
        print(Fore.RED+"Failed to tweet current build!")

def search_cosmetic():
    if iconType == 'new':
        newcbeta()
    else:
        pass
    fontSize = 40
    print(Fore.GREEN +'\nWhat cosmetic do you want to grab?')
    ask = input()
    if benbot == 'False':
        response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?name={ask}')

        print(f'\nGenerating {ask}...')
        print('')
        start = time.time()

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

        try:
            diff = ImageChops.difference(placeholderImg, iconImg)
        except:
            print(Fore.RED + 'Could not grab icon as there is an error with the image. (Hint: Try using BenBot instead!)')
            time.sleep(5)
            exit()

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

        name1= i["name"]
        loadFont = 'fonts/'+imageFont

        if len(name1) > 20:
            fontSize = 30
        if len(name1) > 30:
            fontSize = 20

        if iconType == 'clean':
            font=ImageFont.truetype(loadFont,fontSize)
            w,h=font.getsize(name1)
            draw=ImageDraw.Draw(img)
            draw.text((25,440),name1,font=font,fill='white')

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
            w,h=font.getsize(name1)
            draw=ImageDraw.Draw(img)
            w1, h1 = draw.textsize(name1, font=font)
            draw.text(((512-w1)/2,390),name1,font=font,fill='white')

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

        img.show()

        os.remove('cache/F'+i["id"]+'.png')
        print(Fore.GREEN + "Done loading image!")

        end = time.time()

        print(Fore.GREEN+"")
        print("!  !  !  !  !  !  !")
        print(f"IMAGE GENERATING COMPLETE - Generated image in {round(end - start, 2)} seconds!")
        print("!  !  !  !  !  !  !")
        time.sleep(2)
    if benbot == 'True':
        print(Fore.CYAN + 'Loaded BenBot.')
        print(Fore.GREEN)
        response = requests.get(f'https://benbotfn.tk/api/v1/cosmetics/br/search?lang={language}&searchLang=en&matchMethod=full&name={ask}')

        print(f'Generating {ask}...')
        print('')
        start = time.time()

        try:
            i = response.json()
            # Item Successfully grabbed
        except:
            print(Fore.RED + f'Unable to retreive {ask}.')
            time.sleep(5)
            exit()
        
        try:
            print(Fore.BLUE + "Loading image for "+i["id"])
        except:
            print(Fore.RED + f'Unable to retreive {ask}.')
            time.sleep(5)
            exit()


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

        try:
            diff = ImageChops.difference(placeholderImg, iconImg)
        except:
            print(Fore.RED + 'Could not grab icon as there is an error with the image.')
            time.sleep(5)
            exit()

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

        rarity = i["rarity"]
        rarity = rarity.lower()

        try:
            series = i['series']['name']

            if series == 'Icon Series':
                rarity = 'icon'
            elif series == 'MARVEL SERIES':
                rarity = 'marvel'
            elif series == 'Gaming Legends Series':
                rarity = 'gaminglegends'
            elif series == 'DC SERIES':
                rarity = 'dc'
        except:
            pass

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


        img=Image.open('cache/BLANK'+i["id"]+'.png')

        name1= i["name"]
        loadFont = 'fonts/'+imageFont

        if len(name1) > 20:
            fontSize = 30
        if len(name1) > 30:
            fontSize = 20

        if iconType == 'clean':
            font=ImageFont.truetype(loadFont,fontSize)
            w,h=font.getsize(name1)
            draw=ImageDraw.Draw(img)
            draw.text((25,440),name1,font=font,fill='white')

            fontSize = 40
            id = i["id"]
            font=ImageFont.truetype(loadFont,30)
            w,h=font.getsize(rarity)
            draw=ImageDraw.Draw(img)
            draw.text((25,402),rarity,font=font,fill='white')

            if watermark != '':
                font=ImageFont.truetype(loadFont,25)
                w,h=font.getsize(watermark)
                draw=ImageDraw.Draw(img)
                draw.text((30,30),watermark,font=font,fill='white')

        elif iconType == 'standard':
            font=ImageFont.truetype(loadFont,fontSize)
            w,h=font.getsize(name1)
            draw=ImageDraw.Draw(img)
            w1, h1 = draw.textsize(name1, font=font)
            draw.text(((512-w1)/2,390),name1,font=font,fill='white')

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
            w,h=font.getsize(rarity)
            draw=ImageDraw.Draw(img)
            w1, h1 = draw.textsize(rarity, font=font)
            draw.text(((512-w1)/2,430),rarity,font=font,fill='white')

            if watermark != '':
                font=ImageFont.truetype(loadFont,25)
                w,h=font.getsize(watermark)
                draw=ImageDraw.Draw(img)
                draw.text((10,9),watermark,font=font,fill='white')
        os.remove('cache/BLANK'+i["id"]+'.png')

        img.save('icons/'+i["id"]+'.png')

        img.show()

        os.remove('cache/F'+i["id"]+'.png')
        print(Fore.GREEN + "Done loading image!")

        end = time.time()

        print(Fore.GREEN+"")
        print("!  !  !  !  !  !  !")
        print(f"IMAGE GENERATING COMPLETE - Generated image in {round(end - start, 2)} seconds!")
        print("!  !  !  !  !  !  !")
        time.sleep(2)

    if twitsearch == 'True':
        print('\nAre you sure you want to Tweet this? - y/n')
        ask2 = input('>> ')
        if ask2 == 'y':
            print(Fore.CYAN + '')
            print('Tweeting icon...')

            try:
                lol = 'True'
                data = response.json()['data']
                itemname = data['name']
                itemdesc = data['description']
                itemrarity = data['rarity']["displayValue"]
                introduction = data['introduction']["season"]
                type = data['type']['displayValue']
            except:
                lol = 'False'
                data = response.json()
                itemname = data['name']
                itemdesc = data['description']
                itemrarity = data['rarity']

            print('Cosmetic info retreived! Printing icon details...')
            print('\nItem Name:',itemname)
            try:
                print('\nItem Type:',type)
            except:
                print('\nUnable to retrive Item Type, as you are using BenBot.')
            print('\nItem Description:',itemdesc)
            print('\nItem Rarity:',itemrarity)
            try:
                print('\nIntroduced in season',introduction)
            except:
                print('\nUnable to retrive Item Introducion, as you are using BenBot.')

            itemid = 'icons/'+i["id"]+'.png'

            print('\nTweeting out',ask+'.')

            if lol == 'True':
                api.update_with_media(f'{itemid}', f'[{namelol}] {itemname} {type}:\n\nDescription of {itemname}: \n{itemdesc}\n\nItem Rarity: {itemrarity}\n\nIntroduced in Season {introduction}')
            else:
                api.update_with_media(f'{itemid}', f'[{namelol}] {itemname}:\n\nDescription of {itemname}: \n{itemdesc}\n\nItem Rarity: {itemrarity}')

            print("\nTweeted",ask+' successfully!')
            search_cosmetic()
        else:
            print(Fore.RED + '\nNot tweeting icon.')
            search_cosmetic()
    else:
        print(Fore.RED + '\nNot tweeting icon.')
        search_cosmetic()

def delete_contents():
    print('Deleting contents of the Icons folder...')
    try:
        shutil.rmtree('icons')
        os.makedirs('icons')
    except:
        os.makedirs('icons')
    print('Cleared contents!')
                     
def news_feed():
    count = 1
    apiurl = 'https://fn-api.com/api/brnews'

    jsondata = requests.get(apiurl)
    data = jsondata.json()

    response = requests.get(apiurl)
    newsData = response.json()["update"]

    while 1:
        response = requests.get(apiurl)
        if response:
            newsDataLoop = response.json()["update"]
            print("Checking for change in news feed... ("+str(count)+")")
            count = count + 1
    
            if newsData != newsDataLoop:
            
                print(f"News Feed has changed at {current_time}...")
                response = requests.get(apiurl)
                print("Saving image")
                #url = response.json()["image"]

                url = 'https://fn-api.com/api/media/brnews.png'
                r = requests.get(url, allow_redirects=True)
                open('brnews.png', 'wb').write(r.content)
                print("Saved image!")

                today = date.today()
                d = today.strftime("%m/%d/%Y")
                response = requests.get(apiurl)
                url = response.json()['image']

                bruh = response.json()['motds']
                feed = ""
                for feedtext in bruh:
                    feed2 = feedtext['title']
                    feed += f"• {feed2}\n"
                print(feed)
                api = tweepy.API(auth)

                try:
                    api.update_with_media("brnews.png",f"#Fortnite News Update for {d}:\n\n{feed}\n[{namelol}]")
                except:
                    print('\nImage could not post, compressing image.')
                    foo = Image.open("brnews.png")
                    x, y = foo.size
                    x2, y2 = math.floor(x/2), math.floor(y/2)
                    foo = foo.resize((x2,y2),Image.ANTIALIAS)
                    foo.save("Compressed_news.png",quality=65)
                    print('Compressed image!')
                    api.update_with_media("Compressed_news.png",f"#Fortnite News Update for {d}:\n\n{feed}\n[{namelol}]")
                print("Tweeted image!")
                
                response = requests.get(apiurl)
                newsData = response.json()["update"]
                news_feed()
    
        else:
            print("FAILED TO GRAB NEWS DATA: URL DOWN")

        time.sleep(BotDelay)
                         
def merge_images():
    print('\nMerging images...')
    if mergewatermark != '':
        r = requests.get(mergewatermark, allow_redirects=True)
        open('icons/zzzwatermark.png', 'wb').write(r.content)
    else:
        pass
    images = [file for file in listdir('icons')]
    count = int(round(math.sqrt(len(images)+0.5), 0))
    #print(len(images), count)
    x = len(images)
    print(f'\nFound {x} images in "Icons" folder.')
    finalImg = Image.new("RGBA", (512*count, 512*count))
    #draw = ImageDraw.Draw(finalImg)
    x = 0
    y = 0
    counter = 0
    for img in images:
        tImg = Image.open(f"icons/{img}")
        if counter >= count:
            y += 512
            x = 0
            counter = 0
        finalImg.paste(tImg, (x, y), tImg)
        x += 512
        counter += 1
    finalImg.show()
    finalImg.save(f'merged/MERGED {x}.png')
    print('\nSaved image!')
    print('\nDo you want to Tweet this image? - y/n')
    asklol = input()
    if asklol == 'y':
        print('\nTweeting out image....')
        print('What text do you want the Tweet to say?')
        text = input()
        try:
            api.update_with_media(f'merged/MERGED {x}.png', f'[{namelol}] {text}')
        except:
            print(Fore.YELLOW + '\nFile size is too big, compressing image.')
            foo = Image.open(f'merged/MERGED {x}.png')
            x, y = foo.size
            x2, y2 = math.floor(x/2), math.floor(y/2)
            foo = foo.resize((x2,y2),Image.ANTIALIAS)
            foo.save(f'merged/MERGED {x}.png',quality=65)
            print(Fore.GREEN + 'Compressed!')
            api.update_with_media(f'merged/MERGED {x}.png', f'[{namelol}] {text}')
            time.sleep(5)
        print('\nTweeted image successfully!')
    else:
        print(Fore.RED + 'Not Tweeting.')

def shop_sections():
    count = 1
    apiurl = 'https://fn-api.com/api/shop_categories'

    jsondata = requests.get(apiurl)
    data = jsondata.json()

    response = requests.get(apiurl)
    newsData = response.json()['timestamp']

    while 1:
        response = requests.get(apiurl)
        if response:
            newsDataLoop = response.json()['timestamp']
            print("Checking for change in the Shop Sections... ("+str(count)+")")
            count = count + 1
            
            if newsData != newsDataLoop:

                print(Fore.GREEN + '\nShop sections have changed!')
                time.sleep(3)
                response = requests.get('https://fn-api.com/api/shop_categories')
                ss = response.json()['shopCategories']
                sections = ""

                for i in ss:
                    #print(f'{i["sectionName"]} - (x{i["quantity"]})\n')
                    sections += f'{i["sectionName"]} - (x{i["quantity"]})\n'

                print(sections)

                print('\nTweeting out the current shop sections...')
                api.update_status(f'#Fortnite Shop Sections Update:\n\n'+str(sections)+f'\n\n[{namelol}]')
                print('Tweeted out the shop sections!')
                shop_sections()
        else:
            print("FAILED TO GRAB SHOP SECTIONS DATA: URL DOWN")

        time.sleep(BotDelay)

def shop():
    count = 1
    apiurl = 'https://fortnite-api.com/v2/shop/br'

    jsondata = requests.get(apiurl)
    data = jsondata.json
    
    response = requests.get(apiurl)
    shopData = response.json()['data']['hash']

    while 1:
        response = requests.get(apiurl)
        if response:
            shopDataLoop = response.json()['data']['hash']
            print("Checking for change in Item Shop... ("+str(count)+")")
            count = count + 1
            response = requests.get(apiurl)

            if shopData != shopDataLoop:
                
                print(f"Shop have changed at {current_time}...")
                response = requests.get(apiurl)
                print()
                if CreatorCode != '':
                    url = f'https://api.nitestats.com/v1/shop/image?footer=Creator%20Code%3A%20{CreatorCode}'
                else:
                    url = f'https://api.nitestats.com/v1/shop/image?'
                r = requests.get(url, allow_redirects=True)
                open('shop.png', 'wb').write(r.content)
                print('\nSaved Shop!')
                today = date.today()
                d2 = today.strftime("%B %d, %Y")
                try:
                    if CreatorCode != '':
                        api.update_with_media(f"shop.png", f'#Fortnite Item Shop for {d2}.\n\nSupport-a-Creator Code: {CreatorCode}')
                    else:
                        api.update_with_media(f"shop.png", f'#Fortnite Item Shop for {d2}.')
                except:
                    time.sleep(100)
                    open('shop.png', 'wb').write(r.content)
                    print('\nSaved Shop!')
                    try:
                        if CreatorCode != '':
                            api.update_with_media(f"shop.png", f'#Fortnite Item Shop for {d2}.\n\nSupport-a-Creator Code: {CreatorCode}')
                        else:
                            api.update_with_media(f"shop.png", f'#Fortnite Item Shop for {d2}.')
                    except:
                        time.sleep(100)
                        if CreatorCode != '':
                            api.update_with_media(f"shop.png", f'#Fortnite Item Shop for {d2}.\n\nSupport-a-Creator Code: {CreatorCode}')
                        else:
                            api.update_with_media(f"shop.png", f'#Fortnite Item Shop for {d2}.')

        else:
            print("FAILED TO GRAB SHOP DATA: URL DOWN")

        time.sleep(BotDelay)

def dynamic_pak():
    if iconType == 'new':
        dynpak2()
    else:
        pass
    print('\nWhat number pak do you want to grab?')
    ask = input('>> ')

    response = requests.get(f'https://benbotfn.tk/api/v1/cosmetics/br/dynamic/{ask}?lang={language}')
    
    try:
        test = response.json()[0]['id']
        print('\nGrabbed!')
    except:
        print(Fore.RED + '\nAn error had occured; pak not found or API error.')
        time.sleep(2)
        exit()
    
    data = response.json()

    print(f"Generating {len(data)} new cosmetics from pak {ask}...")
    fontSize = 40
    print('')
    loop = False
    counter = 1
    start = time.time()
    shutil.rmtree('icons')
    os.makedirs('icons')
    for i in data:
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

            rarity = rarity.lower()

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
            name1= i["name"]
            loadFont = 'fonts/'+imageFont
            if len(name1) > 20:
                fontSize = 30
            if len(name1) > 30:
                fontSize = 20
            if iconType == 'clean':
                font=ImageFont.truetype(loadFont,fontSize)
                w,h=font.getsize(name1)
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
                w,h=font.getsize(name1)
                draw=ImageDraw.Draw(img)
                w1, h1 = draw.textsize(name1, font=font)
                draw.text(((512-w1)/2,390),name1,font=font,fill='white')
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
            percentage = counter/len(data)
            realpercentage = percentage * 100
            print(Fore.CYAN + f"Generated image for {id}")
            print(Fore.CYAN + f"{counter}/{len(data)} - {round(realpercentage)}%")
            print("")
            counter = counter + 1
        except:
            print(Fore.YELLOW + "Ignored due to error: "+i["id"])
    end = time.time()
    print(Fore.GREEN+"")
    print("!  !  !  !  !  !  !")
    print(f"IMAGE GENERATING COMPLETE - Generated images in {round(end - start, 2)} seconds")
    print("!  !  !  !  !  !  !")
    print('\nMerging images...')
    if mergewatermark != '':
        r = requests.get(mergewatermark, allow_redirects=True)
        open('icons/zzzwatermark.png', 'wb').write(r.content)
        print(Fore.CYAN + f"Added Watermark." + Fore.GREEN)
    else:
        pass
    images = [file for file in listdir('icons')]
    count = int(round(math.sqrt(len(images)+0.5), 0))
    #print(len(images), count)
    x = len(images)
    print(f'\nFound {x} images in "Icons" folder.')
    finalImg = Image.new("RGBA", (512*count, 512*count))
    #draw = ImageDraw.Draw(finalImg)
    x = 0
    y = 0
    counter = 0
    for img in images:
        tImg = Image.open(f"icons/{img}")
        if counter >= count:
            y += 512
            x = 0
            counter = 0
        finalImg.paste(tImg, (x, y), tImg)
        x += 512
        counter += 1
    finalImg.show()
    finalImg.save(f'merged/Pak {ask} Merged.png')
    print('\nSaved image!')
    if twitAPIKey != 'XXX':
        print('\nDo you want to Tweet this image? - y/n')
        asklol = input()
        if asklol == 'y':
            print('\nTweeting out image....')
            try:
                api.update_with_media(f'merged/Pak {ask} Merged.png', f'[{namelol}] Found {len(data)} items in Pak {ask}:')
            except:
                print(Fore.YELLOW + '\nFile size is too big, compressing image.')
                foo = Image.open(f'merged/Pak {ask} Merged.png')
                x, y = foo.size
                x2, y2 = math.floor(x/2), math.floor(y/2)
                foo = foo.resize((x2,y2),Image.ANTIALIAS)
                foo.save(f'merged/MERGED {x}.png',quality=65)
                print(Fore.GREEN + 'Compressed!')
                api.update_with_media(f'merged/MERGED {x}.png', f'[{namelol}] Found {len(data)} items in Pakchunk {ask}:')
                time.sleep(5)
            print('\nTweeted image successfully!')
        else:
            print(Fore.RED + 'Not Tweeting.')
    dynamic_pak()

def notices():
    count = 1
    response = requests.get('https://fn-api.com/api/emergencynotice')
    apiurl = 'https://fn-api.com/api/emergencynotice'
    
    response = requests.get(apiurl)
    noticesData = response.json()['messages']
    while 1:
        response = requests.get(apiurl)
        if response:
            noticesDataLoop = response.json()['messages']
            print("Checking for change in Notices... ("+str(count)+")")
            count = count + 1
            response = requests.get(apiurl)
            if noticesData != noticesDataLoop:
                print(f"A new notice has changed/been added at {current_time}...")
                message = response.json()['messages']
                twme = ''
                try:
                    for i in message:
                        title = i['title']
                        body = i['body']
                        x = len(message)
                        print(f'\nMessage {x}:\n{title}\n{body}\n')
                        tw2 = i
                        twme = f'\n{title}\n{body}\n'
                except:
                    print('Could not grab')
                print('\nTweeting current notices...')
                api.update_status(f'New #Fortnite notice:\n {twme}')
                print('\nDone!')
                notices()
        else:
            print("FAILED TO GRAB NOTICES DATA: URL DOWN")
        time.sleep(BotDelay)

def staging_servers():
    count = 1
    response = requests.get('https://api.peely.de/v1/staging')
    apiurl = 'https://api.peely.de/v1/staging'
    
    response = requests.get(apiurl)
    stagingData = response.json()['data']['staging']

    while 1:
        response = requests.get(apiurl)
        if response:
            stagingDataLoop = response.json()['data']['staging']
            print("Checking for change in Staging Servers... ("+str(count)+")")
            count = count + 1
            response = requests.get(apiurl)

            if stagingData != stagingDataLoop:
                
                print(f"The staging servers have been changed at {current_time}...")

                staging = response.json()['data']['staging']
                print(f'\nThe staging servers are on {staging}.')
                print('\nTweeting the current staging servers.')
                api = tweepy.API(auth)
                api.update_status('#Fortnite Version Uptate:\n\nPatch v'+str(staging)+' has been added to the pre-release staging servers. Epic is currently testing this update version, and will most likely release within the upcoming week(s).')
                print('\nSuccesfully tweeted the staging servers.')
                staging_servers()
        else:
            print("FAILED TO GRAB STAGING SERVERS DATA: URL DOWN")

        time.sleep(BotDelay)

def weapons():
    #print('\nWhat weapon do you want to grab?')
    response = requests.get('https://fortniteapi.io/v1/loot/list?lang={language}', headers=headers)

    if apikey == "":
        print(Fore.RED+'\nNo API Key is defined. Please add a Fortniteapi.io API key in settings.json.')
        time.sleep(5)
        exit()

    print('\nDo you want to input an ID (1) or a name (2)?')
    print(Fore.YELLOW + '(Note: Only the name (2) option works for generating the images atm)')
    ask1 = input()
    weapons = response.json()["weapons"]
    iconType = 'clean'
    if ask1 == '2':
        print(Fore.GREEN + '\nWhat weapon do you want to grab?')
    else:
        print(Fore.GREEN + '\nWhat weapon ID do you want to grab?')

    arg = input('>> ')
    arg = arg.title()
    if ask1 == '2':
        for i in weapons:
            if i['name'] == arg:
                print(Fore.BLUE + f'\nFound the {i["name"]} weapon.')
                print(f'\nID: {i["id"]}')
                print(f'\nDescription: {i["description"]}')
                costype1 = i['rarity']
                costype = costype1.title()
                print(f'\nRarity: {costype}')
                fontSize = 40
                print('')
                data = response.json()["weapons"]
                loop = False
                counter = 1
                start = time.time()
                try:
                    print(Fore.BLUE + "Loading image for "+i["id"]+f' ({i["rarity"]})')
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
                    costype1 = i['rarity']
                    costype = costype1.title()
                    img=Image.open('cache/BLANK'+i["id"]+'.png')
                    name= i["name"]
                    loadFont = 'fonts/'+imageFont
                    if len(name) > 20:
                        fontSize = 30
                    if len(name) > 30:
                        fontSize = 20
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
                    os.remove('cache/BLANK'+i["id"]+'.png')
                    img.save('icons/'+i["id"]+' '+i["rarity"]+'.png')
                    os.remove('cache/F'+i["id"]+'.png')
                    percentage = counter/len(data)
                    realpercentage = percentage * 100
                    print(Fore.CYAN + f"Generated image for {id}")
                    #print(Fore.CYAN + f"{counter}/{len(data)} - {round(realpercentage)}%")
                    counter = counter + 1
                except Exception as e:
                    print(Fore.YELLOW + "Ignored due to error: "+i["id"])
                    print(e)
                end = time.time()
    else:
        for i in weapons:
            if i['id'] == arg:
                print(f'\nFound the {i["name"]} weapon.')
                print(f'\nID: {i["id"]}')
                print(f'\nDescription: {i["description"]}')
                print(f'\nRarity: {i["rarity"]}')
                url = i["images"]["background"]
                r = requests.get(url, allow_redirects=True)
                open(f'icons/{i["id"]}.png', 'wb').write(r.content)
                print('\nSaved Image!')
                time.sleep(4)

def newcbeta():
    print('Loaded New Icons | API = BenBot\n')
    start = time.time()
    print(Fore.YELLOW+'\nType the name of the cosmetic you want to grab below:\n')
    ask = input(Fore.GREEN + '>> ')
    response = requests.get(f'https://benbotfn.tk/api/v1/cosmetics/br/search?lang={language}&searchLang=en&matchMethod=full&name={ask}')
    fontSize = 40
    # Making icon type new to get the new icons lol #
    iconType = 'new'
    if ask == 'exit':
        exit()
    try:
        i = response.json()
        # Item Successfully grabbed
    except:
        print(Fore.RED + f'Unable to retreive {ask}.')
        time.sleep(5)
        exit()

    try:
        print(Fore.BLUE + "Loading image for "+i["id"])
    except:
        print(Fore.RED + f'Unable to retreive {ask}.')
        time.sleep(5)
        exit()
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
    try:
        diff = ImageChops.difference(placeholderImg, iconImg)
    except:
        print(Fore.RED + 'Could not grab icon as there is an error with the image.')
        time.sleep(5)
        exit()
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
    rarity = i["rarity"]
    rarity = rarity.lower()
    try:
        series = i['series']['name']
        if series == 'Icon Series':
            rarity = 'icon'
        elif series == 'MARVEL SERIES':
            rarity = 'marvel'
        elif series == 'Gaming Legends Series':
            rarity = 'gaminglegends'
        elif series == 'DC SERIES':
            rarity = 'dc'
        elif series == 'Lava Series':
            rarity = 'lava'
        elif series == 'Shadow Series':
            rarity = 'shadow'
        elif rarity == 'Star Wars Series':
            rarity = 'starwars'
        elif rarity == 'Slurp Series':
            rarity = 'slurp'
        elif rarity == 'DARK SERIES':
            rarity = 'dark'
    except:
        pass
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
    img=Image.open('cache/BLANK'+i["id"]+'.png')
    name1= i["name"]
    loadFont = 'fonts/'+imageFont
    if len(name1) > 20:
        fontSize = 30
    if len(name1) > 30:
        fontSize = 2
    if iconType == 'new':
        descup = 'undefined'
        xx1 = len(name1)
        if xx1>17:
            font=ImageFont.truetype(loadFont,45) 
            print('Name is greater than 16 characters.\n')
            descup = 'true'
        else:
            font=ImageFont.truetype(loadFont,60) 
            descup = 'false'
        name1 = name1.upper()
        w,h=font.getsize(name1)
        draw=ImageDraw.Draw(img)
        w1, h1 = draw.textsize(name1, font=font)
        draw.text(((512-w1)/2,406),name1,font=font,fill='white')

        fontSize = 4

        loadFont = 'fonts/OpenSans-Regular.ttf'
        desc = i["description"]
        xx = len(desc)
        desc1 = 'a'
        if xx>35:
            desc1 = ''
            # Description is greater than 35. #
        if desc1 != '':
            font=ImageFont.truetype(loadFont,16)
            w,h=font.getsize(desc)
            draw=ImageDraw.Draw(img)
            w1, h1 = draw.textsize(desc, font=font)
        else:
            font=ImageFont.truetype(loadFont,14)
            w,h=font.getsize(desc)
            draw=ImageDraw.Draw(img)
            w1, h1 = draw.textsize(desc, font=font)

            if xx>75:
                desc1 = 'aaaa'
            else:
                pass
        bigaf = ''
        # I should comment some of this stuff #
        if i['setText'] != None:
            if desc1 != '':
                if descup != 'true':
                    if desc1 == 'aaaa':
                        # IF DESC IS BIG AF THEN DO THIS #
                        bigaf = '1'
                        pass
                    else:
                        # This means it is not big af
                        draw.text(((512-w1)/2,455),desc,font=font,fill='white')
                else:
                    # This means if it equals none then it 
                    draw.text(((512-w1)/2,454),desc,font=font,fill='white')
            else:
                if desc1 == 'aaaa':
                    pass
                else:
                   # Idek just do this crap #
                    if name1 != 'PEELY':
                        draw.text(((512-w1)/2,460),desc,font=font,fill='white')
                    else:
                        bigaf = '69'
                        pass
        else:
            if desc1 != '':
                if desc1 == 'aaaa':
                    if xx<80:
                        font=ImageFont.truetype(loadFont,10)
                        w,h=font.getsize(desc)
                        draw=ImageDraw.Draw(img)
                        w1, h1 = draw.textsize(desc, font=font)
                        draw.text(((512-w1)/2,465),desc,font=font,fill='white')
                    else:
                        pass
                else:
                    draw.text(((512-w1)/2,465),desc,font=font,fill='white')
            else:
                draw.text(((512-w1)/2,470),desc,font=font,fill='white')

        if i['setText'] != None:
            set = i["setText"]
            font=ImageFont.truetype(loadFont,16)
            w,h=font.getsize(set)
            draw=ImageDraw.Draw(img)
            w1, h1 = draw.textsize(set, font=font)
            if desc1 != '':
                if bigaf == '1':
                    draw.text(((512-w1)/2,465),set,font=font,fill='white')
                else:
                    # Alright, this should be if the description is too big then it does this i guess #
                    draw.text(((512-w1)/2,480),set,font=font,fill='white')
            else:
                # Same thing as the one above but just adding an else because if its normal its not '' #
                if bigaf != '69':
                    draw.text(((512-w1)/2,480),set,font=font,fill='white')
                else:
                    draw.text(((512-w1)/2,465),set,font=font,fill='white')


        loadFont = 'fonts/'+imageFont

        id = i["id"]

        #showitemsource = 'True'

        if watermark != '':
            font=ImageFont.truetype(loadFont,25)
            w,h=font.getsize(watermark)
            draw=ImageDraw.Draw(img)
            draw.text((10,9),watermark,font=font,fill='white')

        i = response.json()
        
        shop = ''
        if showitemsource != 'False':
            for x in i['gameplayTags']:
                result = x.find('Cosmetics.Source.ItemShop')
                if result != -1:
                    print('Found an Item Shop tag.')
                    shop = '1'
                else:
                    pass

            if shop != '1':
                shop = '69'
                print('did not find an item shop tag')

            if shop == '69':
                for x in i['gameplayTags']:
                    result = x.find('BattlePass.Paid')
                    if result != -1:
                        print('Found a battle pass tag.')
                        shop = '2'
                        resp1 = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?name={ask}')
                        seasonnum = resp1.json()['data']['introduction']['backendValue']
                        break
                if shop != '2':
                    print('Did not find a battle pass tag, skipping')
                    shop = '0'

            if shop == '0':
                for x in i['gameplayTags']:
                    result = x.find('Cosmetics.Set.')
                    if result != -1:
                        print('Found a set tag since the other two tabs dont work lol')
                        shop = '3'
                        break
                if shop != '3':
                    print('could not find ANY tags.')
                    shop = '0'


            source = i['gameplayTags'][0]

            if name1 == 'VENOM':
                source = i['gameplayTags'][2]
        else:
            pass
            
        if showitemsource == 'True':
            font=ImageFont.truetype(loadFont,15)
            thing1 = source.replace('Cosmetics.Source.', '')
            #x = len(thing1)
            if shop == '1':
                thing1 = 'Cosmetics.Source.ItemShop'
            elif shop == '2':
                thing1 = f'Season{seasonnum}.BattlePass.Paid'
            elif shop == '0':
                thing1 = ''
            elif shop == '3':
                set = i['set']
                set1 = set.replace(' ', '')
                set1 = set1.title()
                thing1 = f'Cosmetics.Set.{set1}'
            if thing1 != '0':
                if watermark != '':
                    thing = f'{thing1}'
                    w,h=font.getsize(thing)
                    draw=ImageDraw.Draw(img)
                    draw.text((10,30),thing,font=font,fill='white')
                else:
                    thing = f'{thing1}'
                    w,h=font.getsize(thing)
                    draw=ImageDraw.Draw(img)
                    draw.text((10,10),thing,font=font,fill='white')
            else:
                print('\nNot writing source as there is none.')
        else:
            print('Not writing source.')
        
        
    os.remove('cache/BLANK'+i["id"]+'.png')
    img.save('icons/'+i["id"]+'.png')
    img.show()
    os.remove('cache/F'+i["id"]+'.png')
    print(Fore.GREEN + "\nDone loading image!")
    end = time.time()
    print(Fore.GREEN+"")
    print("!  !  !  !  !  !  !")
    print(f"IMAGE GENERATING COMPLETE - Generated image in {round(end - start, 2)} seconds!")
    print("!  !  !  !  !  !  !")
    newcbeta()

def newcnew():
    print('Loaded New Icons | API = BenBot')
    fontSize = 40
    response = requests.get('https://benbotfn.tk/api/v1/newCosmetics')
    new = response.json()
    print(f"Version: {new['currentVersion']}\n")

    print(f"Generating {len(new['items'])} new cosmetics from BenBot...")
    print('')
    loop = False
    counter = 1
    start = time.time()
    iconType = 'new'
    new = response.json()
    for i in new['items']:
        start = time.time()
        try:
            print(Fore.BLUE + "Loading image for "+i["id"])
        except:
            print(Fore.RED + f'Unable to retreive item.')
            time.sleep(5)
            exit()
        if useFeaturedIfAvaliable == 'True':
            if i["icons"]["featured"] != None:
                url = i["icons"]["featured"]
            else:
                if i['icons']['icon'] != None:
                    url = i["icons"]["icon"]
                else:
                    url = 'https://i.ibb.co/KyvMydQ/do-Not-Delete.png'
        elif useFeaturedIfAvaliable == 'False':
            if i['icons']['icon'] != None:
                url = i["icons"]["icon"]
            else:
                url = 'https://i.ibb.co/KyvMydQ/do-Not-Delete.png'
        placeholderImg = Image.open('assets/doNotDelete.png')
        r = requests.get(url, allow_redirects=True)
        open(f'cache/icontemp.png', 'wb').write(r.content)
        iconImg = Image.open(f'cache/icontemp.png')
        try:
            diff = ImageChops.difference(placeholderImg, iconImg)
        except:
            pass
        if diff.getbbox():
            r = requests.get(url, allow_redirects=True)
            open(f'cache/icontemp.png', 'wb').write(r.content)
            img=Image.open(f'cache/icontemp.png')
            img=img.resize((512,512),PIL.Image.ANTIALIAS)
            img.save(f'cache/temp.png')
        else:
            try:
                r = requests.get(placeholderUrl, allow_redirects=True)
                open(f'cache/icontemp.png', 'wb').write(r.content)
                img=Image.open(f'cache/icontemp.png')
                img=img.resize((512,512),PIL.Image.ANTIALIAS)
                img.save(f'cache/temp.png')
            except:
                pass

        rarity = i["rarity"]
        rarity = rarity.lower()
        try:
            series = i['series']['name']
            if series == 'Icon Series':
                rarity = 'icon'
            elif series == 'MARVEL SERIES':
                rarity = 'marvel'
            elif series == 'Gaming Legends Series':
                rarity = 'gaminglegends'
            elif series == 'DC SERIES':
                rarity = 'dc' 
            elif series == 'Lava Series':
                rarity = 'lava'
            elif series == 'Shadow Series':
                rarity = 'shadow'
            elif rarity == 'Star Wars Series':
                rarity = 'starwars'
            elif rarity == 'Slurp Series':
                rarity = 'slurp'
            elif rarity == 'DARK SERIES':
                rarity = 'dark'
        except:
            pass
            foreground = Image.open('cache/icontemp.png')
        
        # Background making stuff by Swift-nite#3722 - Your a huge help, thanks! :banana:
        try:
            background = Image.open(f'rarities/{iconType}/{rarity}.png')
            border=Image.open(f'rarities/{iconType}/border{rarity}.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
        except:
            background = Image.open(f'rarities/{iconType}/common.png')
            border=Image.open(f'rarities/{iconType}/bordercommon.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
        img=Image.new("RGB",(512,512))
        img.paste(background)
        img.save('cache/temp.png')
        img=Image.open(f'cache/temp.png')
        foreground= Image.open('cache/icontemp.png').resize((512, 512), Image.ANTIALIAS)
        img.paste(foreground, (0, 0), foreground)
        img.save('cache/temp.png')
        img.paste(border, (0, 0), border)
        img.save('cache/temp.png')
        background = Image.open('cache/temp.png')

        if i['name'] != None:
            name = i['name']
        else:
            name = 'TBD'

        name1= name
        loadFont = 'fonts/'+imageFont
        if len(name1) > 20:
            fontSize = 30
        if len(name1) > 30:
            fontSize = 2
        elif iconType == 'new':
            descup = 'undefined'
            xx1 = len(name1)
            if xx1>17:
                font=ImageFont.truetype(loadFont,45) 
                #print('Name is greater than 16 characters.\n')
                descup = 'true'
            else:
                font=ImageFont.truetype(loadFont,60) 
                descup = 'false'
            name1 = name1.upper()
            w,h=font.getsize(name1)
            draw=ImageDraw.Draw(background)
            w1, h1 = draw.textsize(name1, font=font)
            draw.text(((512-w1)/2,406),name1,font=font,fill='white')
    
            fontSize = 4
    
            loadFont = 'fonts/OpenSans-Regular.ttf'
            desc = i["description"]

            if desc != None:
                pass
            else:
                desc = 'TBD'

            xx = len(desc)
            desc1 = 'a'
            if xx>35:
                desc1 = ''
            if desc1 != '':
                font=ImageFont.truetype(loadFont,16)
                w,h=font.getsize(desc)
                draw=ImageDraw.Draw(background)
                w1, h1 = draw.textsize(desc, font=font)
            else:
                font=ImageFont.truetype(loadFont,14)
                w,h=font.getsize(desc)
                draw=ImageDraw.Draw(background)
                w1, h1 = draw.textsize(desc, font=font)
                if xx>70:
                    desc1 = 'aaaa'
                    #print('owo uwu owo uwu')
                else:
                    pass
            bigaf = ''
            # I should comment some of this stuff #
            if i['setText'] != None:
                if desc1 != '':
                    if descup != 'true':
                        if desc1 == 'aaaa':
                            # IF DESC IS BIG AF THEN DO THIS #
                            bigaf = '1'
                            pass
                        else:
                            # This means it is not big af
                            draw.text(((512-w1)/2,455),desc,font=font,fill='white')
                    else:
                        # This means if it equals none then it 
                        draw.text(((512-w1)/2,454),desc,font=font,fill='white')
                else:
                    if desc1 == 'aaaa':
                        pass
                    else:
                        bigaf = '69'
                        pass
            else:
                if desc1 != '':
                    if desc1 == 'aaaa':
                        if xx<80:
                            font=ImageFont.truetype(loadFont,10)
                            w,h=font.getsize(desc)
                            draw=ImageDraw.Draw(background)
                            w1, h1 = draw.textsize(desc, font=font)
                            draw.text(((512-w1)/2,465),desc,font=font,fill='white')
                        else:
                            pass
                    else:
                        draw.text(((512-w1)/2,465),desc,font=font,fill='white')
                else:
                    draw.text(((512-w1)/2,470),desc,font=font,fill='white')
    
            if i['setText'] != None:
                set = i["setText"]
                font=ImageFont.truetype(loadFont,16)
                w,h=font.getsize(set)
                draw=ImageDraw.Draw(background)
                w1, h1 = draw.textsize(set, font=font)
                if desc1 != '':
                    if bigaf == '1':
                        draw.text(((512-w1)/2,465),set,font=font,fill='white')
                    else:
                        # Alright, this should be if the description is too big then it does this i guess #
                        draw.text(((512-w1)/2,480),set,font=font,fill='white')
                else:
                    # Same thing as the one above but just adding an else because if its normal its not '' #
                    draw.text(((512-w1)/2,480),set,font=font,fill='white')
    
    
            loadFont = 'fonts/'+imageFont
    
            id = i["id"]
    
            #showitemsource = 'True'
    
            if watermark != '':
                font=ImageFont.truetype(loadFont,25)
                w,h=font.getsize(watermark)
                draw=ImageDraw.Draw(background)
                draw.text((10,9),watermark,font=font,fill='white')
    
            #i = response.json()
            
            shop = ''
            if showitemsource != 'False':
                for x in i['gameplayTags']:
                    result = x.find('Cosmetics.Source.ItemShop')
                    if result != -1:
                        #print('Found an Item Shop tag.')
                        shop = '1'
                    else:
                        pass
                    
                if shop != '1':
                    shop = '69'
                    #print('did not find an item shop tag')
    
                if shop == '69':
                    for x in i['gameplayTags']:
                        result = x.find('BattlePass.Paid')
                        if result != -1:
                            #print('Found a battle pass tag.')
                            shop = '2'
                            resp1 = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?name={name1}')
                            try:
                                seasonnum = resp1.json()['data']['introduction']['backendValue']
                            except:
                                pass
                            break
                    if shop != '2':
                        #print('Did not find a battle pass tag, skipping')
                        shop = '0'
    
                if shop == '0':
                    for x in i['gameplayTags']:
                        result = x.find('Cosmetics.Set.')
                        if result != -1:
                            #print('Found a set tag since the other two tabs dont work lol')
                            shop = '3'
                            break
                    if shop != '3':
                        #print('could not find ANY tags.')
                        shop = '0'
    
                try:
                    source = i['gameplayTags'][0]
                except:
                    pass
    
                if name1 == 'VENOM':
                    source = i['gameplayTags'][2]
            else:
                pass
                
            if showitemsource == 'True':
                font=ImageFont.truetype(loadFont,15)
                thing1 = source.replace('Cosmetics.Source.', '')
                #x = len(thing1)
                if shop == '1':
                    thing1 = 'Cosmetics.Source.ItemShop'
                elif shop == '2':
                    thing1 = f'Season{seasonnum}.BattlePass.Paid'
                elif shop == '0':
                    thing1 = ''
                elif shop == '3':
                    set = i['set']
                    set1 = set.replace(' ', '')
                    set1 = set1.title()
                    thing1 = f'Cosmetics.Set.{set1}'
                if thing1 != '0':
                    if watermark != '':
                        thing = f'{thing1}'
                        w,h=font.getsize(thing)
                        draw=ImageDraw.Draw(background)
                        draw.text((10,30),thing,font=font,fill='white')
                    else:
                        thing = f'{thing1}'
                        w,h=font.getsize(thing)
                        draw=ImageDraw.Draw(background)
                        draw.text((10,10),thing,font=font,fill='white')
                else:
                    #print('\nNot writing source as there is none.')
                    pass
            else:
                print('Not writing source.')
        
        #os.remove('cache/BLANK'+i["id"]+'.png')
        background.save('icons/'+i["id"]+'.png')
        i = response.json()
        percentage = counter/len(i['items'])
        realpercentage = percentage * 100
        print(Fore.CYAN + f"Generated image for {id}")
        print(Fore.CYAN + f"{counter}/{len(i['items'])} - {round(realpercentage)}%")
        print("")
        counter = counter + 1
        end = time.time()

    if MergeImagesAuto != 'False':
        print('\nMerging images...')
        if mergewatermark != '':
            r = requests.get(mergewatermark, allow_redirects=True)
            open('icons/zzzwatermark.png', 'wb').write(r.content)
        else:
            pass
        images = [file for file in listdir('icons')]
        count = int(round(math.sqrt(len(images)+0.5), 0))
        #print(len(images), count)
        lol = len(images) - 1
        print(f'\nFound {lol} images in "Icons" folder.')
        finalImg = Image.new("RGB", (512*count, 512*count))
        #draw = ImageDraw.Draw(finalImg)
        x = 0
        y = 0
        counter = 0
        for img in images:
            tImg = Image.open(f"icons/{img}").convert("RGBA")
            if counter >= count:
                y += 512
                x = 0
                counter = 0
            finalImg.paste(tImg, (x, y), tImg)
            x += 512
            counter += 1
        finalImg.show()
        finalImg.save(f'merged/MERGED {lol}.png')
        response = requests.get('https://benbotfn.tk/api/v1/status')
        version = response.json()['currentFortniteVersionNumber']
        #print(x)
        lol = len(images) - 1
        print('\nSaved image!')
        if twitAPIKey != 'XXX':
            print('\nTweeting out image....')
            try:
                api.update_with_media(f'merged/MERGED {lol}.png', f'[{namelol}] Found {lol} Leaked cosmetics from Patch {version}.')
            except:
                print(Fore.YELLOW + '\nFile size is too big, compressing image.')
                foo = Image.open(f'merged/MERGED {lol}.png')
                x, y = foo.size
                x2, y2 = math.floor(x/2), math.floor(y/2)
                foo = foo.resize((x2,y2),Image.ANTIALIAS)
                foo.save(f'merged/MERGED {lol}.png',quality=65)
                print(Fore.GREEN + 'Compressed!')
                api.update_with_media(f'merged/MERGED {lol}.png', f'[{namelol}] Found {lol} Leaked cosmetics from Patch {version}.')
                time.sleep(5)
            print(Fore.GREEN + '\nTweeted image successfully!')
        else:
            print(Fore.YELLOW+'Not tweeting images.')
    else:
        print('Not auto merging images.')
        print('Exiting...')
        time.sleep(2)
        exit()



def dynpak2():
    try:
        shutil.rmtree('icons')
        os.makedirs('icons')
    except:
        os.makedirs('icons')
    print('Cleared "icons" folder contents.')
    print('Loaded New Icons | API = BenBot\n')
    print('What pak number do you want to grab?')
    paktrue = input('>> ')
    fontSize = 40
    response = requests.get(f'https://benbotfn.tk/api/v1/cosmetics/br/dynamic/{paktrue}?lang={language}')
    new = response.json()

    print(f"\nGenerating {len(new)} new cosmetics from BenBot...")
    print('')
    loop = False
    counter = 1
    start = time.time()
    iconType = 'new'
    new = response.json()
    for i in new:
        start = time.time()
        try:
            print(Fore.BLUE + "Loading image for "+i["id"])
        except:
            print(Fore.RED + f'Unable to retreive item.')
            time.sleep(5)
            exit()
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
        try:
            diff = ImageChops.difference(placeholderImg, iconImg)
        except:
            print(Fore.RED + 'Could not grab icon as there is an error with the image.')
            time.sleep(5)
            exit()
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
        rarity = i["rarity"]
        rarity = rarity.lower()
        try:
            series = i['series']['name']
            if series == 'Icon Series':
                rarity = 'icon'
            elif series == 'MARVEL SERIES':
                rarity = 'marvel'
            elif series == 'Gaming Legends Series':
                rarity = 'gaminglegends'
            elif series == 'DC SERIES':
                rarity = 'dc' 
            elif series == 'Lava Series':
                rarity = 'lava'
            elif series == 'Shadow Series':
                rarity = 'shadow'
            elif rarity == 'Star Wars Series':
                rarity = 'starwars'
            elif rarity == 'Slurp Series':
                rarity = 'slurp'
            elif rarity == 'DARK SERIES':
                rarity = 'dark'
        except:
            pass 
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
        img=Image.open('cache/BLANK'+i["id"]+'.png')
        name1= i["name"]
        loadFont = 'fonts/'+imageFont
        if len(name1) > 20:
            fontSize = 30
        if len(name1) > 30:
            fontSize = 2
        elif iconType == 'new':
            descup = 'undefined'
            xx1 = len(name1)
            if xx1>17:
                font=ImageFont.truetype(loadFont,45) 
                #print('Name is greater than 16 characters.\n')
                descup = 'true'
            else:
                font=ImageFont.truetype(loadFont,60) 
                descup = 'false'
            name1 = name1.upper()
            w,h=font.getsize(name1)
            draw=ImageDraw.Draw(img)
            w1, h1 = draw.textsize(name1, font=font)
            draw.text(((512-w1)/2,406),name1,font=font,fill='white')
    
            fontSize = 4
    
            loadFont = 'fonts/OpenSans-Regular.ttf'
            desc = i["description"]
            xx = len(desc)
            desc1 = 'a'
            if xx>35:
                desc1 = ''
            if desc1 != '':
                font=ImageFont.truetype(loadFont,16)
                w,h=font.getsize(desc)
                draw=ImageDraw.Draw(img)
                w1, h1 = draw.textsize(desc, font=font)
            else:
                font=ImageFont.truetype(loadFont,14)
                w,h=font.getsize(desc)
                draw=ImageDraw.Draw(img)
                w1, h1 = draw.textsize(desc, font=font)
                if xx>70:
                    desc1 = 'aaaa'
                    #print('owo uwu owo uwu')
                else:
                    pass
            bigaf = ''
            # I should comment some of this stuff #
            if i['setText'] != None:
                if desc1 != '':
                    if descup != 'true':
                        if desc1 == 'aaaa':
                            # IF DESC IS BIG AF THEN DO THIS #
                            bigaf = '1'
                            pass
                        else:
                            # This means it is not big af
                            draw.text(((512-w1)/2,455),desc,font=font,fill='white')
                    else:
                        # This means if it equals none then it 
                        draw.text(((512-w1)/2,454),desc,font=font,fill='white')
                else:
                    if desc1 == 'aaaa':
                        pass
                    else:
                        bigaf = '69'
                        pass
            else:
                if desc1 != '':
                    if desc1 == 'aaaa':
                        if xx<80:
                            font=ImageFont.truetype(loadFont,10)
                            w,h=font.getsize(desc)
                            draw=ImageDraw.Draw(img)
                            w1, h1 = draw.textsize(desc, font=font)
                            draw.text(((512-w1)/2,465),desc,font=font,fill='white')
                        else:
                            pass
                    else:
                        draw.text(((512-w1)/2,465),desc,font=font,fill='white')
                else:
                    draw.text(((512-w1)/2,470),desc,font=font,fill='white')

            if i['setText'] != None:
                set = i["setText"]
                font=ImageFont.truetype(loadFont,16)
                w,h=font.getsize(set)
                draw=ImageDraw.Draw(img)
                w1, h1 = draw.textsize(set, font=font)
                if desc1 != '':
                    if bigaf == '1':
                        draw.text(((512-w1)/2,465),set,font=font,fill='white')
                    else:
                        # Alright, this should be if the description is too big then it does this i guess #
                        draw.text(((512-w1)/2,480),set,font=font,fill='white')
                else:
                    # Same thing as the one above but just adding an else because if its normal its not '' #
                    draw.text(((512-w1)/2,480),set,font=font,fill='white')
    
    
            loadFont = 'fonts/'+imageFont
    
            id = i["id"]
    
            #showitemsource = 'True'
    
            if watermark != '':
                font=ImageFont.truetype(loadFont,25)
                w,h=font.getsize(watermark)
                draw=ImageDraw.Draw(img)
                draw.text((10,9),watermark,font=font,fill='white')
    
            #i = response.json()
            
            shop = ''
            if showitemsource != 'False':
                for x in i['gameplayTags']:
                    result = x.find('Cosmetics.Source.ItemShop')
                    if result != -1:
                        #print('Found an Item Shop tag.')
                        shop = '1'
                    else:
                        pass
                    
                if shop != '1':
                    shop = '69'
                    #print('did not find an item shop tag')
    
                if shop == '69':
                    for x in i['gameplayTags']:
                        result = x.find('BattlePass.Paid')
                        if result != -1:
                            #print('Found a battle pass tag.')
                            shop = '2'
                            resp1 = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?name={name1}')
                            try:
                                seasonnum = resp1.json()['data']['introduction']['backendValue']
                            except:
                                pass
                            break
                    if shop != '2':
                        #print('Did not find a battle pass tag, skipping')
                        shop = '0'
    
                if shop == '0':
                    for x in i['gameplayTags']:
                        result = x.find('Cosmetics.Set.')
                        if result != -1:
                            #print('Found a set tag since the other two tabs dont work lol')
                            shop = '3'
                            break
                    if shop != '3':
                        #print('could not find ANY tags.')
                        shop = '0'
    
                try:
                    source = i['gameplayTags'][0]
                except:
                    pass
    
                if name1 == 'VENOM':
                    source = i['gameplayTags'][2]
            else:
                pass
                
            if showitemsource == 'True':
                font=ImageFont.truetype(loadFont,15)
                thing1 = source.replace('Cosmetics.Source.', '')
                #x = len(thing1)
                if shop == '1':
                    thing1 = 'Cosmetics.Source.ItemShop'
                elif shop == '2':
                    thing1 = f'Season{seasonnum}.BattlePass.Paid'
                elif shop == '0':
                    thing1 = ''
                elif shop == '3':
                    set = i['set']
                    set1 = set.replace(' ', '')
                    set1 = set1.title()
                    thing1 = f'Cosmetics.Set.{set1}'
                if thing1 != '0':
                    if watermark != '':
                        thing = f'{thing1}'
                        w,h=font.getsize(thing)
                        draw=ImageDraw.Draw(img)
                        draw.text((10,30),thing,font=font,fill='white')
                    else:
                        thing = f'{thing1}'
                        w,h=font.getsize(thing)
                        draw=ImageDraw.Draw(img)
                        draw.text((10,10),thing,font=font,fill='white')
                else:
                    #print('\nNot writing source as there is none.')
                    pass
            else:
                print('Not writing source.')
        
        
        os.remove('cache/BLANK'+i["id"]+'.png')
        img.save('icons/'+i["id"]+'.png')
        os.remove('cache/F'+i["id"]+'.png')
        i = response.json()
        percentage = counter/len(i)
        realpercentage = percentage * 100
        print(Fore.CYAN + f"Generated image for {id}")
        print(Fore.CYAN + f"{counter}/{len(i)} - {round(realpercentage)}%")
        print("")
        counter = counter + 1
        end = time.time()

    if MergeImagesAuto != 'False':
        print('\nMerging images...')
        if mergewatermark != '':
            r = requests.get(mergewatermark, allow_redirects=True)
            open('icons/zzzwatermark.png', 'wb').write(r.content)
            print(Fore.CYAN + f"Added Watermark to image."+Fore.GREEN)
        else:
            pass
        images = [file for file in listdir('icons')]
        count = int(round(math.sqrt(len(images)+0.5), 0))
        #print(len(images), count)
        lol = len(images) - 1
        print(f'\nFound {lol} images in "Icons" folder.')
        finalImg = Image.new("RGBA", (512*count, 512*count))
        #draw = ImageDraw.Draw(finalImg)
        x = 0
        y = 0
        counter = 0
        for img in images:
            tImg = Image.open(f"icons/{img}")
            if counter >= count:
                y += 512
                x = 0
                counter = 0
            finalImg.paste(tImg, (x, y), tImg)
            x += 512
            counter += 1
        finalImg.show()
        finalImg.save(f'merged/MERGED {lol}.png')
        response = requests.get('https://benbotfn.tk/api/v1/status')
        version = response.json()['currentFortniteVersionNumber']
        #print(x)
        print('\nSaved image!')
        if twitAPIKey != 'XXX':
            print('\nDo you want to Tweet out this image? - y/n')
            ask = input('>> ')
            if ask == 'y':
                print('\nTweeting out image....')
                lol = len(images) - 1
                try:
                    api.update_with_media(f'merged/MERGED {lol}.png', f'[{namelol}] Found {lol} Cosmetics in Pak {paktrue}.')
                except:
                    print(Fore.YELLOW + '\nFile size is too big, compressing image.')
                    foo = Image.open(f'merged/MERGED {lol}.png')
                    x, y = foo.size
                    x2, y2 = math.floor(x/2), math.floor(y/2)
                    foo = foo.resize((x2,y2),Image.ANTIALIAS)
                    foo.save(f'merged/MERGED {x}.png',quality=65)
                    print(Fore.GREEN + 'Compressed!')
                    api.update_with_media(f'merged/MERGED {lol}.png', f'[{namelol}] Found {lol} Cosmetics in Pak {paktrue}.')
                    time.sleep(5)
                print(Fore.GREEN + '\nTweeted image successfully!')
            else:
                print('Not tweeting.')
    else:
        print('Not auto merging images.')
        

print(Fore.GREEN + "\n- - - - - MENU - - - - -")
print("")
print(Fore.RED+'!!NOTICE!! '+Fore.GREEN+'We have just introduced new icons into AutoLeak! These are in beta, but you\ncan test them out by changing the iconType in settings.json to "new"!\n')
print(Fore.YELLOW + "(1)" +Fore.GREEN + " - Start update mode")
print(Fore.YELLOW + "(2)" +Fore.GREEN + " - Generate new cosmetics")
print("(3) - Tweet current build")
print("(4) - Tweet current AES key")
print("(5) - Search for a cosmetic")
print("(6) - Clear contents of the icon folder")
print("(7) - Check for a change in News Feed")
print("(8) - Merge images in icons folder")
print("(9) - Check for a change in Shop Sections")
print("(10) - Check for a change in Item Shop")
print("(11) - Grab all cosmetics from a specific pak")
print("(12) - Checks for a change in notices")
print("(13) - Checks for a change in staging servers")
print("(14) - Search for any weapon of choice.")

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
elif option_choice == "7":
    news_feed()
elif option_choice == "8":
    merge_images()
elif option_choice == "9":
    shop_sections()
elif option_choice == "10":
    shop()
elif option_choice == "11":
    dynamic_pak()
elif option_choice == "12":
    notices()
elif option_choice == "13":
    staging_servers()
elif option_choice == "14":
    weapons()
else:
    print(Fore.RED+"\nPlease enter a number between 1 and 14")
    time.sleep(2)
    
# Search for a cosmetic (NEW ICONS)") - newcbeta()
# Generate new cosmetics (NEW ICONS)') - newcnew()
# Grab all cosmetics from a specific pak (NEW ICONS)') - dynpak2()

# If you have any issues with the softwere, please message Fevers#3474 on discord. #
