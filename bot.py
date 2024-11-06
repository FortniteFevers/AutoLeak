# If you have any issues with the softwere, please message Fevers#3474 on discord. #

"""
Commons Clause - License Condition v1.0
Copyright Fevers 2024

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

All Rights Reserved. You are not allowed to redistribute this software, or use
the software to build derivative works based upon without prior written permission.
This software is open-source only for Educational Purposes, if you learn\copy-over\edit anything from AutoLeak you must give appropriate credit,
provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner.

Software: AUTOLEAK
"""

currentVersion = 'BETA'

try:
    import requests
    import tweepy
    import time
    import PIL
    import math
    from PIL import Image, ImageFont, ImageDraw, ImageChops
    import os
    import json
    import shutil
    import math
    import datetime
    from datetime import date, datetime
    import random
    from os import listdir
    from colorama import *
    #from googletrans import Translator
    import platform
    import tkinter as tk
    window = tk.Tk()
    window.wm_withdraw()

    from pypresence import Presence
except ModuleNotFoundError as e:
    print(f"Error: {e}")
    print('Please install this module to run the program.')

#translator = Translator()
#init()

try:
    rpc = Presence(
        "916433412376625213"
    )
    rpc.connect()
    rpc.update(details='The easiest way to datamine Fortnite', large_image='autoleak_v2_logo', buttons=[{"label": "Join our Discord!", "url": "https://dsc.gg/autoleak"}, {"label": "Download AutoLeak!", "url": "https://github.com/FortniteFevers/AutoLeak"}])
except Exception as e:
    print(Fore.RED + f'Discord Presense Error:',e)
    print('Loading program anyways...')
    time.sleep(1)

now = datetime.now()
current_time = now.strftime("%H:%M")

from ALmodules.shopsections import shop_sections
from ALmodules.compressor import compressnewcosmetics_normal, compress_brnews, compress_normal, pak_compress, compressnewcosmetics_new
from ALmodules.merger import merger
from ALmodules.largeIconType import largeicontype, largeicontype_search, large_merger, largeicontype_pak, largeicontype_search_banner
from ALmodules.shop import genshop, update, shopmerge

loop = True
count = 1
fontSize = 40
initialCheckDelay = 2


import platform # If softwere is linux, it does not run ctypes
x = platform.system()

if x == 'Windows':
    autoleakcool = """
    

    ░█████╗░██╗░░░██╗████████╗░█████╗░██╗░░░░░███████╗░█████╗░██╗░░██╗
    ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██║░░░░░██╔════╝██╔══██╗██║░██╔╝
    ███████║██║░░░██║░░░██║░░░██║░░██║██║░░░░░█████╗░░███████║█████═╝░
    ██╔══██║██║░░░██║░░░██║░░░██║░░██║██║░░░░░██╔══╝░░██╔══██║██╔═██╗░
    ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝███████╗███████╗██║░░██║██║░╚██╗
    ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝

    """
    print(Fore.CYAN + autoleakcool + Fore.RESET)
    print('                              Loading...')
    time.sleep(2)
    os.system("cls")
    os.system(
    "TITLE AutoLeak / Created by Fevers.")
    os.system('cls' if os.name=='nt' else 'clear')

# Used to communicate with updates
try:
    response = requests.get('https://raw.githubusercontent.com/FortniteFevers/AutoLeak/beta/notices.json')
    ln1 = response.json()["1"]
    ln2 = response.json()["2"]
    ln3 = response.json()["3"]
    ln4 = response.json()["4"]
    ln5 = response.json()["5"]
    ln6 = response.json()["6"]
    ln7 = response.json()["7"]
    latestVersion = response.json()["latestVersion"]
    betaText = response.json()['betatext']
    seasonnum = response.json()['currentFortniteVersionNumber']
except:
    response = None
    ln1 = 'Thank you for using AutoLeak - Created by Fevers.'
    ln2 = ''
    ln3 = 'Want to create rarity backgrounds? Feel free to send us any via discord to maybe be featured in AutoLeak!'
    ln4 = '(Please keep it in the same format!) My discord @: @Fevers#3474'
    ln5 = 'AutoLeak beta is now public! Check it out on my GitHub under the beta branch!'
    ln6 = ''
    ln7 = 'Make sure you join our discord server!  -  https://dsc.gg/AutoLeak'
    latestVersion = '1.3.8'
    betaText = 'Welcome to AutoLeak Beta! Thanks for signing up and helping us with developing this program!\nIf there are any errors, make sure to tell us in our Discord server.'
    seasonnum = '0000'
print("")
print("------------------------------------------------------------------------------------------------")
print("")
print(ln1)
print(ln2)
print(ln3)
print(ln4)
print(ln5)
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
    if currentVersion != 'BETA':
        print(Fore.RED + '--> You are currently running v'+currentVersion+' of AutoLeak, v'+latestVersion+' is now avaliable - Please check #updates in the AutoLeak discord server for the update!')
        #Mbox("VERSION ERROR", f"Hey there!\n\nWe have noticed you are running a pervious version of AutoLeak!\n\nYou are on version {currentVersion}, and {latestVersion} is now avalible!\nPlease check #updates in the AutoLeak discord server for the update!\n\nYou can still use this version, but make sure to download the latest version after!", 0)
    else:
        print(Fore.CYAN + f"{betaText}")
print("")
print(Style.RESET_ALL + "------------------------------------------------------------------------------------------------")
print("")
# Used to communicate with settings.json, grab all user inputs from it.

with open("settings.json") as settings:
    data = json.load(settings)
    TwitterSupport = data['TwitterSupport']
    if data['ShowValues_AtStart'] == True:

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
            global language
            language = data["language"]
            if language == 'ar' or language == 'de' or language == 'en' or language == 'es' or language == 'es-419' or language == 'fr' or language == 'it' or language == 'ja' or language == 'ko' or language == 'pl' or language == 'pt-BR' or language == 'de' or language == 'ru' or language == 'tr' or language == 'zh-CN' or language == 'zh-Hant':
                print(Fore.GREEN + 'Loaded "language" as "'+language+'"')
            else:
                language = 'en'
                print(Fore.YELLOW + 'Incorrect value for language was given so I have loaded "language" as "en"')

        except:
            language = 'en'
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
            if iconType == 'standard' or iconType == 'clean' or iconType == 'new' or iconType == 'cataba' or iconType == 'large':
                print(Fore.GREEN + 'Loaded "iconType" as "'+iconType+'"')
            else:
                iconType = 'cataba'
                print(Fore.YELLOW + 'Incorrect value for iconType was given so I have loaded "iconType" as "cataba"')
        except:
            iconType = 'cataba'
            print(Fore.RED + 'Failed to load "iconType", defaulted to "cataba"')

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
            global showitemsource
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
            loc1 = ''
            mergewatermark = data['MergeWatermarkUrl']
            if 'image' in mergewatermark:
                loc1 = mergewatermark.replace('image/', '')
                print(Fore.GREEN+f'Detected "MergeWatermark" to be an image file. Image is located in assets/{loc1}')

                def addwatermark():
                    img=Image.open(f'assets/{loc1}')
                    img=img.resize((512,512),PIL.Image.ANTIALIAS)
                    img.save(f'icons/zzz{loc1}')
                #addwatermark()
            else:
                if mergewatermark != "":
                    print(Fore.GREEN+f'Loaded "MergeWatermark" as "{mergewatermark}')
                else:
                    print(Fore.GREEN+f'Loaded "MergeWatermark" as None.')
                    mergewatermark = ""
        except:
            print(Fore.YELLOW+'Incorrect value for "mergewatermark", defaulting to None.')
            mergewatermark = ""

        try:
            automergetweet = data['AutoTweetMerged']
            automergetweet = automergetweet.title()
            if automergetweet == 'True' or 'False':
                print(Fore.GREEN+f'Loaded "Auto Tweet Merged Images" as "{automergetweet}"')
            else:
                print(Fore.YELLOW+'Incorrect value for "Auto Tweet Merged Images", defaulting to False.')
                automergetweet = 'False'
        except:
            print(Fore.YELLOW+'Incorrect value for "Auto Tweet Merged Images", defaulting to False.')
            automergetweet = "False"

        try:
            showDescription = data['ShowDescOnNPCs']
            if showDescription == 'True' or 'False':
                print(Fore.GREEN+f'Loaded "Show Description on NPCs" as "{showDescription}"')
            else:
                print(Fore.YELLOW+'Incorrect value for "Show Description on NPCs", defaulting to False.')
                showDescription = 'False'
        except:
            print(Fore.YELLOW+'Incorrect value for "Show Description on NPCs", defaulting to False.')
            showDescription = "False"

        try:
            sections_image = data['ShopSections_Image']
            if sections_image == 'True' or 'False':
                print(Fore.GREEN+f'Loaded "Shop Sections Image" as "{sections_image}"')
            else:
                print(Fore.YELLOW+f'Incorrect value for "Shop Sections Image", defaulting to True."')
                sections_image = 'False'
        except:
            print(Fore.RED+f'Incorrect value for "Shop Sections Image", defaulting to True."')
            sections_image = 'True'

        try:
            BG_Color = data['ImageColor']
            if BG_Color == "":
                print(Fore.YELLOW+f'Incorrect value for "Background Color", defaulting to "Blue"')
                BG_Color = '394ff7'
            else:
                print(Fore.GREEN+f'Loaded "Background Color" as "{BG_Color}"')
                
        except:
            print(Fore.RED+f'Incorrect value for "Background Color", defaulting to "Blue"')
            BG_Color = '394ff7'

        try:
            sideFont = data['sideFont']
            if sideFont != '':
                print(Fore.GREEN+f'Loaded "Side Font" as "{sideFont}"')
            else:
                print(Fore.YELLOW+'Incorrect value for "Side Font", defaulting to OpenSans-Regular.ttf.')
                sideFont = 'OpenSans-Regular.ttf'
        except:
            print(Fore.YELLOW+'Incorrect value for "Side Font", defaulting to OpenSans-Regular.ttf.')
            sideFont = "OpenSans-Regular.ttf"

    else:
        
        try:
            name = data["name"]
            namelol = data["name"]
        except:
            name = 'AutoLeak'
            print(Fore.RED + 'Failed to load "name", defaulted to "AutoLeak"')

        try:
            footer = data["footer"]
        except:
            footer = '#Fortnite'
            print(Fore.RED + 'Failed to load "footer", defaulted to "#Fortnite"')

        try:
            language = data["language"]
            if language == 'ar' or language == 'de' or language == 'en' or language == 'es' or language == 'es-419' or language == 'fr' or language == 'it' or language == 'ja' or language == 'ko' or language == 'pl' or language == 'pt-BR' or language == 'de' or language == 'ru' or language == 'tr' or language == 'zh-CN' or language == 'zh-Hant':
                pass
            else:
                language = 'en'
                print(Fore.YELLOW + 'Incorrect value for language was given so I have loaded "language" as "en"')

        except:
            language = 'en'
            print(Fore.RED + 'Failed to load "language", defaulted to "en"')

        try:
            imageFont = data["imageFont"]
        except:
            imageFont = 'BurbankBigCondensed-Black.otf'
            print(Fore.RED + 'Failed to load "imageFont", defaulted to "BurbankBigCondensed-Black.otf"')

        try:
            placeholderUrl = data["placeholderUrl"]
        except:
            placeholderUrl = 'https://i.imgur.com/W22Foja.png'
            print(Fore.RED + 'Failed to load "placeholderUrl", set to default placeholder url.')

        try:
            watermark = data["watermark"]
        except:
            watermark = ''
            print(Fore.RED + 'Failed to load "watermark", ignored, program will be ran without a watermark.')

        try:
            useFeaturedIfAvaliable = data["useFeaturedIfAvaliable"]
            if useFeaturedIfAvaliable == 'True' or useFeaturedIfAvaliable == 'False':
                pass
            else:
                useFeaturedIfAvaliable = 'False'
                print(Fore.YELLOW + 'Incorrect value for useFeaturedIfAvaliable was given so I have loaded "useFeaturedIfAvaliable" as "False"')
        except:
            useFeaturedIfAvaliable = 'False'
            print(Fore.RED + 'Failed to load "useFeaturedIfAvaliable", defaulted to "False"')

        try:
            iconType = data["iconType"]
            if iconType == 'standard' or iconType == 'clean' or iconType == 'new' or iconType == 'cataba' or iconType == 'large':
                pass
            else:
                iconType = 'cataba'
                print(Fore.YELLOW + 'Incorrect value for iconType was given so I have loaded "iconType" as "cataba"')
        except:
            iconType = 'cataba'
            print(Fore.RED + 'Failed to load "iconType", defaulted to "cataba"')

        try:
            twitAPIKey = data["twitAPIKey"]
            if twitAPIKey == '':
                twitAPIKey = 'XXX'
        
        except:
            twitAPIKey = 'XXX'
            print(Fore.RED + 'Failed to load "twitAPIKey", defaulted to "XXX"')

        try:
            twitAPISecretKey = data["twitAPISecretKey"]
           
        except:
            twitAPISecretKey = 'XXX'
            print(Fore.RED + 'Failed to load "twitAPISecretKey", defaulted to "XXX"')

        try:
            twitAccessToken = data["twitAccessToken"]

        except:
            twitAccessToken = 'XXX'
            print(Fore.RED + 'Failed to load "twitAccessToken", defaulted to "XXX"')

        try:
            twitAccessTokenSecret = data["twitAccessTokenSecret"]

        except:
            twitAccessTokenSecret = 'XXX'
            print(Fore.RED + 'Failed to load "twitAccessTokenSecret", defaulted to "XXX"')

        try:
            tweetUpdate = data["tweetUpdate"]
            if tweetUpdate == 'True' or tweetUpdate == 'False':
                pass
            else:
                tweetUpdate = 'False'
                print(Fore.YELLOW + 'Incorrect value for tweetUpdate was given so I have loaded "tweetUpdate" as "False"')
        except:
            tweetUpdate = 'False'
            print(Fore.RED + 'Failed to load "tweetUpdate", defaulted to "False"')

        try:
            tweetAes = data["tweetAes"]
            if tweetAes == 'True' or tweetAes == 'False':
                pass
            else:
                tweetAes = 'False'
                print(Fore.YELLOW + 'Incorrect value for tweetAes was given so I have loaded "tweetAes" as "False"')
        except:
            tweetAes = 'False'
            print(Fore.RED + 'Failed to load "tweetAes", defaulted to "False"')

        try:
            BotDelay = data['BotDelay']
            
        except:
            BotDelay = 30
            print(Fore.RED + 'Failed to load "BotDelay", defaulted to 30 seconds.')
            
        try:
            twitsearch = data['TweetSearch']
            if twitsearch == 'True' or twitsearch == 'False':
                pass
            else:
                twitsearch = 'True'
                print(Fore.YELLOW + 'Incorrect value for "Twitter Search", defaulting to "True"...')
        except:
            twitsearch = 'False'
            print(Fore.RED + 'Failed to load "Tweet Search", defaulting to "False"...')
            
        try:
            MergeImagesAuto = data['MergeImages']
            if MergeImagesAuto == 'True' or MergeImagesAuto == 'False':
                pass
            else:
                MergeImagesAuto = 'True'
        except:
            print(Fore.YELLOW + 'Incorrect value for "MergeImages", defaulting to "True"...')
            MergeImagesAuto = 'True'

        try:
            CreatorCode = data['CreatorCode']
            if CreatorCode != '':
                pass
            else:
                CreatorCode = ''
        except:
            CreatorCode = ''
            print(Fore.YELLOW + 'Incorrect value for "CreatorCode", defaulting to none.')
            
        try:
            apikey = data['apikey']
            if apikey != "":
                pass
            else:
                print(Fore.GREEN + 'Loaded API Key as none.')
                CreatorCode = ''
        except:
            apikey = ''
            print(Fore.YELLOW + 'Incorrect value for "apikey", defaulting to none.')   
        
        try:
            showitemsource = data['showitemsource']
            showitemsource = showitemsource.title()
        except:
            print(Fore.YELLOW+'Incorrect value for "ShowItemSource", defaulting to True.')
            showitemsource = 'True'
            
        try:
            loc1 = ''
            mergewatermark = data['MergeWatermarkUrl']
            if 'image' in mergewatermark:
                loc1 = mergewatermark.replace('image/', '')

                def addwatermark():
                    img=Image.open(f'assets/{loc1}')
                    img=img.resize((512,512),PIL.Image.ANTIALIAS)
                    img.save(f'icons/zzz{loc1}')
                #addwatermark()
            else:
                if mergewatermark != "":
                    pass
                else:
                    #print(Fore.GREEN+f'Loaded "MergeWatermark" as None.')
                    mergewatermark = ""
        except:
            print(Fore.YELLOW+'Incorrect value for "mergewatermark", defaulting to None.')
            mergewatermark = ""

        try:
            automergetweet = data['AutoTweetMerged']
            automergetweet = automergetweet.title()
            if automergetweet == 'True' or 'False':
                pass
            else:
                print(Fore.YELLOW+'Incorrect value for "Auto Tweet Merged Images", defaulting to False.')
                automergetweet = 'False'
        except:
            print(Fore.YELLOW+'Incorrect value for "Auto Tweet Merged Images", defaulting to False.')
            automergetweet = "False"

        try:
            showDescription = data['ShowDescOnNPCs']
            if showDescription == 'True' or 'False':
                pass
            else:
                print(Fore.YELLOW+'Incorrect value for "Show Description on NPCs", defaulting to False.')
                showDescription = 'False'
        except:
            print(Fore.YELLOW+'Incorrect value for "Show Description on NPCs", defaulting to False.')
            showDescription = "False"

        try:
            sections_image = data['ShopSections_Image']
            if sections_image == 'True' or 'False':
                pass
            else:
                print(Fore.YELLOW+f'Incorrect value for "Shop Sections Image", defaulting to True."')
                sections_image = 'False'
        except:
            print(Fore.RED+f'Incorrect value for "Shop Sections Image", defaulting to True."')
            sections_image = 'True'

        try:
            BG_Color = data['ImageColor']
            if BG_Color == "":
                BG_Color = '394ff7'
            else:
                print(Fore.GREEN+f'Loaded "Background Color" as "{BG_Color}"')
                
        except:
            print(Fore.RED+f'Incorrect value for "Background Color", defaulting to "Blue"')
            BG_Color = '394ff7'

        try:
            sideFont = data['sideFont']
            if sideFont != '':
                pass
            else:
                print(Fore.YELLOW+'Incorrect value for "Side Font", defaulting to OpenSans-Regular.ttf.')
                sideFont = 'OpenSans-Regular.ttf'
        except:
            print(Fore.YELLOW+'Incorrect value for "Side Font", defaulting to OpenSans-Regular.ttf.')
            sideFont = "OpenSans-Regular.ttf"
    
    sections_image = sections_image.title()


# Sets up Twitter API keys        
auth = tweepy.OAuthHandler(twitAPIKey, twitAPISecretKey)
auth.set_access_token(twitAccessToken, twitAccessTokenSecret)
api = tweepy.API(auth)

# Sets up fortniteapi.io API key
headers = {'Authorization': apikey}

#-------------------#-------------------#

# Defines update mode
def update_mode():
    print(Fore.CYAN)
    apitype = 'Fortnite-API'
    print(f'\n-- Starting Update Mode --\n   IconType = {iconType}\n   Delay = {BotDelay} seconds\n   API = {apitype}\n'+Fore.GREEN)
    
    response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/new?lange={language}')
    if response:
        oldhash = response.json()['data']['hash']
    else:
        return update_mode()

    count = 1

    while 1:
        response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/new?lange={language}')
        if response:
            try:
                newhash = response.json()['data']['hash'] 
            except:
                return update_mode()
            print(f'Checking for a change in cosmetics... ({count})')
            count = count + 1
            if newhash != oldhash:
                print('A new update has been pushed. Generating cosmetics.')
                
                if iconType == 'standard':
                    return generate_cosmetics()
                elif iconType == 'clean':
                    return generate_cosmetics()
                elif iconType == 'cataba':
                    catabaicons()
                    
                elif iconType == 'large':
                    largeicontype(useFeaturedIfAvaliable, language)
                
                if automergetweet == 'True':
                    try:
                        api.update_with_media('merged/merge.jpg', 'A new update has been pushed out, heres all of the new cosmetics:')
                    except:
                        compressnewcosmetics_new()
                        api.update_with_media('merged/merge.jpg', 'A new update has been pushed out, heres all of the new cosmetics:')
                    print('Tweeted new cosmetics')
                print('Done generating cosmetics.')
                return update_mode()
        else:
            print("FAILED TO GRAB NOTICES DATA: URL DOWN")
        time.sleep(BotDelay)

def generate_cosmetics():

    if iconType == 'cataba':
        return catabaicons()
    
    if iconType == 'large':
        return largeicontype(useFeaturedIfAvaliable, language)

    if iconType == 'new':
        return newcnew_fnbrapi()

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
    
    if automergetweet != 'False':                  
        if MergeImagesAuto != 'False':
            print('\nMerging images...')
            if 'image' in mergewatermark:
                addwatermark()
            merger(mergewatermark, loc1)
            
            xlol = len(os.listdir('icons'))
            if mergewatermark == '':
                xlol = xlol-1
            print('\nSaved image!')
            
            if twitAPIKey != 'XXX':
                print('\nTweeting out image....')
                print('What text do you want the Tweet to say?')
                text = input()
                try:
                    api.update_with_media(f'merged/MERGED {xlol}.png', f'[{namelol}] {text}')
                except:
                    print(Fore.RED + 'File size is too big, compressing')
                    try:
                        compressnewcosmetics_normal(xlol)
                        api.update_with_media(f'merged/MERGED {xlol}.png', f'[{namelol}] {text}')
                    except:
                        compressnewcosmetics_normal(xlol)
                        api.update_with_media(f'merged/MERGED {xlol}.png', f'[{namelol}] {text}')
                print('\nTweeted image successfully!')
                time.sleep(5)
            else:
                print('Not Tweeting.')
        else:
            print(Fore.RED + '\nNot merging images.')
            time.sleep(5)
    else:
        print('Exiting...')
        exit()

def newcnew_fnbrapi():
    delete_contents()
    print('Cleared Contents\nLoaded New Icons | API = Fortnite-API')
    
    centerline = 256
    response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/new?language={language}')
    new = response.json()['data']
    print(f"Version = {new['build']}\n")
 
    print(f"Generating {len(new['items'])} new cosmetics from Fortnite-API...\n")

    counter = 1
    start1 = time.time()
    iconType = 'new'

    # Gets season number
    data = requests.get('https://benbot.app/api/v1/status')
    seasonnum = data.json()['currentFortniteVersionNumber']

    for i in new['items']:
        start = time.time()
        print(Fore.BLUE + f"Loading image for {i['id']}")
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
        try:
            r = requests.get(url)
        except:
            print('a')
        open('cache/icontemp.png', 'wb').write(r.content)
        iconImg = Image.open('cache/icontemp.png')
        iconImg.resize((512,512),PIL.Image.ANTIALIAS)


        rarity = i["rarity"]['value']
        rarity = rarity.lower()
        
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
        foreground= Image.open('cache/icontemp.png').resize((512, 512), Image.ANTIALIAS).convert('RGBA')
        img.paste(foreground, (0, 0), foreground)
        img.save('cache/temp.png')
        img.paste(border, (0, 0), border)
        img.save('cache/temp.png')
        background = Image.open('cache/temp.png')

        # Loads Name
        if i['name'] != None:
            name = i['name']
        else:
            name = 'TBD'
        
        loadFont = 'fonts/'+imageFont

        x = len(name)

        if x>17:
            font=ImageFont.truetype(loadFont,45)
            movedescup = 'true'
            loc = 440 # Puts location at a higher level
        else:
            font=ImageFont.truetype(loadFont,60) 
            movedescup = 'false'
            loc = 450 # Puts location at a lower level

        name = name.upper() 
        w,h=font.getsize(name)
        draw=ImageDraw.Draw(background)
        w1, h1 = draw.textsize(name, font=font)
        draw.text((centerline,loc),name,font=font,fill='white', anchor='ms') # Writes name

        # Loads Desc
        if i['description'] != None:
            desc = i['description']
        else:
            desc = 'TBD'

        loadFont = f'fonts/{sideFont}'
        
        try:
            set = i['set']['text']
        except:
            set = None
        if set == None:
            set = None
        else:
            set = set

        x = len(desc)
        if x>95:
            font=ImageFont.truetype(loadFont,10)
            draw=ImageDraw.Draw(background)
            line = 470
            draw.text(
                (centerline,line),
                desc,
                font=font,
                fill='white', 
                anchor='ms') # Writes name
        else:
            if x>45:
                #print('above')
                font=ImageFont.truetype(loadFont,14)
                draw=ImageDraw.Draw(background)
                if set != None:
                    line = 474
                else:
                    line = 480
                if movedescup == 'true':
                    line = line-8
                draw.text(
                    (centerline,line),
                    desc,
                    font=font,
                    fill='white', 
                    anchor='ms') # Writes name
            else:
                #print('below')
                font=ImageFont.truetype(loadFont,16)
                draw=ImageDraw.Draw(background)
                if set != None:
                    line = 475
                else:
                    line = 480

                if movedescup == 'true':
                    line = line-2
                draw.text(
                    (centerline,line),
                    desc,
                    font=font,
                    fill='white', 
                    anchor='ms') # Writes name   

        # Loads Item Set Text
        if set != None:
            font=ImageFont.truetype(loadFont, 15)
            draw=ImageDraw.Draw(background)
            draw.text(
                (centerline, 500),
                set,
                font=font,
                fill='white',
                anchor='ms') # Writes set

        # Loads watermark
        loadFont = 'fonts/'+imageFont # Puts font back to original
        if watermark != '':
            font=ImageFont.truetype(loadFont,25)
            draw=ImageDraw.Draw(background)
            draw.text((10,9),watermark,font=font,fill='white')

        # Loads gameplay tag
        if showitemsource != 'False':
            text = ''
            try:
                for x in i['gameplayTags']:
                    if 'Cosmetics.Source.ItemShop' in x:
                        text = 'Cosmetics.Source.ItemShop'
                        break
                    if '.BattlePass.Paid' in x:
                        text = f'Cosmetics.Source.Season{seasonnum}.BattlePass.Paid'
                        break
                    if 'Cosmetics.Set.' in x:
                        # Creates Set
                        try:
                            set = i['set']['value'].replace(' ', '')
                        except:
                            pass
                        text = f'Cosmetics.Set.{set}'
                        break
            except:
                pass
            font=ImageFont.truetype(loadFont, 15)
            if watermark != '':
                draw=ImageDraw.Draw(background)
                draw.text((10,30),text,font=font,fill='white')
            else:
                if text != None or text != '':
                    draw=ImageDraw.Draw(background)
                    draw.text((10,10),text,font=font,fill='white')
        background.save('icons/'+i["id"]+'.png')
        end = time.time()

        # Finishing Time
        percentage = counter/len(new['items'])
        realpercentage = percentage * 100
        print(Fore.CYAN + f"Generated image for {i['id']}")
        print(Fore.CYAN + f"{counter}/{len(new['items'])} - {round(realpercentage)}%\n")
        counter = counter + 1

    end1 = time.time()
    print("!  !  !  !  !  !  !")
    print(f"IMAGE GENERATING COMPLETE - Generated image in {round(end1 - start1, 2)} seconds!")
    if MergeImagesAuto != 'False':
        print('SAVED MERGED IMAGE!')
    print("!  !  !  !  !  !  !")


    if MergeImagesAuto != 'False':
        print('\nMerging images...')
        if 'image' in mergewatermark:
            addwatermark()
        merger(mergewatermark, loc1)

        version = new['build'].replace('++Fortnite+Release-', '').replace('-CL-17328477-Windows', '')
        #print(x)
        lol = len(os.listdir('icons'))
        if mergewatermark == '':
            lol = lol-1
        print('\nSaved image!')
        if automergetweet != 'False':
            if twitAPIKey != 'XXX':
                print('\nTweeting out image....')
                try:
                    api.update_with_media(f'merged/merge.jpg', f'[{namelol}] Found {lol} Leaked cosmetics from Patch {version}.')
                except:
                    print(Fore.YELLOW + '\nFile size is too big, compressing image.')
                    compressnewcosmetics_new(lol)
                    api.update_with_media(f'merged/merge.jpg', f'[{namelol}] Found {lol} Leaked cosmetics from Patch {version}.')
                    time.sleep(5)
                print(Fore.GREEN + '\nTweeted image successfully!')
        else:
            print(Fore.YELLOW+'Not tweeting images.')
            time.sleep(2)
            exit()
    else:
        print('Not auto merging images.')
        print('Exiting...')
        time.sleep(2)
        exit()

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
    if iconType == 'cataba':
        return catabasearch()
    elif iconType == 'large':
        print('Loaded Large Icon Type')
        print('API = Fortnite-API')
        return largeicontype_search(useFeaturedIfAvaliable, language)
    else:
        pass
    fontSize = 40
    print(Fore.GREEN +'\nWhat cosmetic do you want to grab?')
    ask = input()

    response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?name={ask}&language={language}')

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
    #print('Deleting contents of the Icons folder...')
    try:
        shutil.rmtree('icons')
        os.makedirs('icons')
    except:
        os.makedirs('icons')
    #print('Cleared contents!')
                     
def news_feed():
    count = 1
    apiurl = 'https://fortnite-api.com/v2/news/br?language={language}'

    jsondata = requests.get(apiurl)
    data = jsondata.json()

    response = requests.get(apiurl)
    newsData = response.json()["data"]["hash"]

    while 1:
        response = requests.get(apiurl)
        if response:
            try:
                newsDataLoop = response.json()["data"]["hash"]
            except:
                news_feed()
            print("Checking for change in news feed... ("+str(count)+")")
            count = count + 1
    
            if newsData != newsDataLoop:
            
                print(f"News Feed has changed at {current_time}...")
                response = requests.get(apiurl)
                print("Saving image")
                #url = response.json()["image"]

                xx = response.json()['data']['motds'][0]
                url = xx['tileImage']
                r = requests.get(url, allow_redirects=True)
                open('brnews.png', 'wb').write(r.content)
                print("Saved image!")

                today = date.today()
                d = today.strftime("%m/%d/%Y")
                response = requests.get(apiurl)

                title = xx['title']
                desc = xx['body']

                try:
                    api.update_with_media("brnews.png",f"#Fortnite News Update: {title}\n\n'{desc}'\n[{namelol}]")
                except:
                    print('\nImage could not post, compressing image.')
                    compress_brnews()
                    api.update_with_media("Compressed_news.png",f"#Fortnite News Update: {title}\n\n'{desc}'\n[{namelol}]")
                print("Tweeted image!")
                
                response = requests.get(apiurl)
                newsData = response.json()["data"]["hash"]
                news_feed()
    
        else:
            print("FAILED TO GRAB NEWS DATA: URL DOWN")

        time.sleep(BotDelay)
                         
def merge_images():
    print('\nMerging images...')
    merger(mergewatermark, loc1)
    print('\nSaved image!')
    if automergetweet != 'False':
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
                compress_normal(x)
                api.update_with_media(f'merged/MERGED {x}.png', f'[{namelol}] {text}')
                time.sleep(5)
            print('\nTweeted image successfully!')
        else:
            print(Fore.RED + 'Not Tweeting.')

def shop():
    delete_contents()
    if TwitterSupport != False:
        print('\nDo you want to generate a shop image or use the Shop Update mode for twitter?\n(1) Generate shop\n(2) Update mode')
        ask = input('>> ')
        if ask == '1':
            genshop()

            print('\nMerging images...')
            shopmerge()
            print('Done! The image is now saved in the "merged" folder.')
            time.sleep(10)
        else:
            update(api)
    else:
        genshop()

        print('\nMerging images...')
        shopmerge()
        print('Done! The image is now saved in the "merged" folder.')
        time.sleep(10)

def dynamic_pak():
    
    if iconType == 'large':
        return largeicontype_pak(useFeaturedIfAvaliable, language)

    if iconType == 'cataba':
        return cataba_pak()

    print("Please set the icon type to either; 'large', or 'cataba'")

def notices():
    count = 1
    apiurl = 'https://fn-api.com/api/emergencyNotices'
    
    response = requests.get(apiurl)
    noticesData = response.json()['data']
    while 1:
        response = requests.get(apiurl)
        if response:
            try:
                noticesDataLoop = response.json()['data']
            except:
                notices()
            print("Checking for change in Notices... ("+str(count)+")")
            count = count + 1
            response = requests.get(apiurl)
            if noticesData != noticesDataLoop:
                print(f"A new notice has changed/been added at {current_time}...")
                message = response.json()['data']
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
    apiurl = 'https://fortnite-public-service-stage.ol.epicgames.com/fortnite/api/version' # Epic Games Staging URL
    response = requests.get(apiurl)
    oldVersion = response.json()['version']

    while 1:
        try:
            response = requests.get(apiurl)
        except:
            return staging_servers()
        if response:
            try:
                newVersion = response.json()['version']
            except:
                return staging_servers()
            print("Checking for change in Staging Servers... ("+str(count)+")")
            count = count + 1
            response = requests.get(apiurl)

            if newVersion != oldVersion:

                print(f'\nThe staging servers  have been updated and are on {newVersion}.')
                api = tweepy.API(auth)
                api.update_status(f'#Fortnite Version Uptate:\n\nPatch v{newVersion} has been added to the pre-release staging servers. Epic is currently testing this update version, and will most likely release within the upcoming week(s).')
                print('\nSuccesfully tweeted the staging servers.')
                staging_servers()
        else:
            print("FAILED TO GRAB STAGING SERVERS DATA: URL DOWN")

        time.sleep(BotDelay)

def weapons():
    #print('\nWhat weapon do you want to grab?')
    response = requests.get(f'https://fortniteapi.io/v1/loot/list?lang={language}', headers=headers)

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
    #arg = arg.title()
    if ask1 == '2':
        for i in weapons:
            if i['name'].lower() == arg.lower():
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


def newiconsfnapi():
    print('Loaded New Icons | API = Fortnite-API\n')
    start = time.time()
    print(Fore.YELLOW+'Type the name of the cosmetic you want to grab below:\n')
    ask = input(Fore.GREEN + '>> ')

    response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?name={ask}&language={language}')

    idsearch = ask.find('Athena_Commando')
    if idsearch != -1:
        # Detected an ID
        response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={ask}&language={language}')

    fontSize = 40
    # Making icon type new to get the new icons lol #
    iconType = 'new'
    if ask == 'exit':
        exit()
    try:
        i = response.json()['data']
        # Item Successfully grabbed
    except:
        print(Fore.RED + f'Unable to retreive {ask}.')
        time.sleep(5)
        exit()
    centerline = 256
    print(Fore.BLUE + f"Loading image for {i['id']}")
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
    try:
        r = requests.get(url)
    except:
        print('a')
    open('cache/icontemp.png', 'wb').write(r.content)
    iconImg = Image.open('cache/icontemp.png')
    iconImg.resize((512,512),PIL.Image.ANTIALIAS)


    rarity = i["rarity"]['value']
    rarity = rarity.lower()
    
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
    foreground= Image.open('cache/icontemp.png').resize((512, 512), Image.ANTIALIAS).convert('RGBA')
    img.paste(foreground, (0, 0), foreground)
    img.save('cache/temp.png')
    img.paste(border, (0, 0), border)
    img.save('cache/temp.png')
    background = Image.open('cache/temp.png')

    # Loads Name
    if i['name'] != None:
        name = i['name']
    else:
        name = 'TBD'
    
    loadFont = 'fonts/'+imageFont

    x = len(name)

    if x>17:
        font=ImageFont.truetype(loadFont,45)
        movedescup = 'true'
        loc = 440 # Puts location at a higher level
    else:
        font=ImageFont.truetype(loadFont,60) 
        movedescup = 'false'
        loc = 450 # Puts location at a lower level

    name = name.upper() 
    w,h=font.getsize(name)
    draw=ImageDraw.Draw(background)
    w1, h1 = draw.textsize(name, font=font)
    draw.text((centerline,loc),name,font=font,fill='white', anchor='ms') # Writes name

    # Loads Desc
    if i['description'] != None:
        desc = i['description']
    else:
        desc = 'TBD'

    loadFont = f'fonts/{sideFont}'
    
    try:
        set = i['set']['text']
    except:
        set = None
    if set == None:
        set = None
    else:
        set = set

    x = len(desc)
    if x>95:
        font=ImageFont.truetype(loadFont,10)
        draw=ImageDraw.Draw(background)
        line = 470
        draw.text(
            (centerline,line),
            desc,
            font=font,
            fill='white', 
            anchor='ms') # Writes name
    else:
        if x>45:
            #print('above')
            font=ImageFont.truetype(loadFont,14)
            draw=ImageDraw.Draw(background)
            if set != None:
                line = 474
            else:
                line = 480
            if movedescup == 'true':
                line = line-8
            draw.text(
                (centerline,line),
                desc,
                font=font,
                fill='white', 
                anchor='ms') # Writes name
        else:
            #print('below')
            font=ImageFont.truetype(loadFont,16)
            draw=ImageDraw.Draw(background)
            if set != None:
                line = 475
            else:
                line = 480

            if movedescup == 'true':
                line = line-2
            draw.text(
                (centerline,line),
                desc,
                font=font,
                fill='white', 
                anchor='ms') # Writes name   

    # Loads Item Set Text
    if set != None:
        font=ImageFont.truetype(loadFont, 15)
        draw=ImageDraw.Draw(background)
        draw.text(
            (centerline, 500),
            set,
            font=font,
            fill='white',
            anchor='ms') # Writes set

    # Loads watermark
    loadFont = 'fonts/'+imageFont # Puts font back to original
    if watermark != '':
        font=ImageFont.truetype(loadFont,25)
        draw=ImageDraw.Draw(background)
        draw.text((10,9),watermark,font=font,fill='white')

    # Loads gameplay tag
    if showitemsource != 'False':
        text = ''
        try:
            for x in i['gameplayTags']:
                if 'Cosmetics.Source.ItemShop' in x:
                    text = 'Cosmetics.Source.ItemShop'
                    break
                elif '.BattlePass.Paid' in x:
                    text = f'Cosmetics.Source.Season{seasonnum}.BattlePass.Paid'
                    break
                elif 'Cosmetics.Set.' in x:
                    # Creates Set
                    try:
                        set = i['set']['value'].replace(' ', '')
                    except:
                        pass
                    text = f'Cosmetics.Set.{set}'
                    break
        except:
            pass
        font=ImageFont.truetype(loadFont, 15)
        if watermark != '':
            draw=ImageDraw.Draw(background)
            draw.text((10,30),text,font=font,fill='white')
        else:
            if text != None or text != '':
                draw=ImageDraw.Draw(background)
                draw.text((10,10),text,font=font,fill='white')
    background.save('icons/'+i["id"]+'.png')
    end = time.time()

    # Finishing Time
    print(Fore.CYAN + f"Generated image for {i['id']} in {round(end - start, 2)} seconds.")
        
        
    background.show()
    end = time.time()
    print(Fore.GREEN+"")
    newiconsfnapi()


def newcnew_fnbrapi():
    delete_contents()
    print('Cleared Contents\nLoaded New Icons | API = Fortnite-API')
    
    centerline = 256
    response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/new?language={language}')
    new = response.json()['data']
    print(f"Version = {new['build']}\n")
 
    print(f"Generating {len(new['items'])} new cosmetics from Fortnite-API...\n")

    counter = 1
    start1 = time.time()
    iconType = 'new'

    # Gets season number
    data = requests.get('https://fortnite-api.com/v2/aes')
    seasonnum = data.json()['data']['build']
    seasonnum = seasonnum[19:24]

    for i in new['items']:
        start = time.time()
        print(Fore.BLUE + f"Loading image for {i['id']}")
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
        try:
            r = requests.get(url)
        except:
            print('a')
        open('cache/icontemp.png', 'wb').write(r.content)
        iconImg = Image.open('cache/icontemp.png')
        iconImg.resize((512,512),PIL.Image.ANTIALIAS)


        rarity = i["rarity"]['value']
        rarity = rarity.lower()
        
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
        foreground= Image.open('cache/icontemp.png').resize((512, 512), Image.ANTIALIAS).convert('RGBA')
        img.paste(foreground, (0, 0), foreground)
        img.save('cache/temp.png')
        img.paste(border, (0, 0), border)
        img.save('cache/temp.png')
        background = Image.open('cache/temp.png')

        # Loads Name
        if i['name'] != None:
            name = i['name']
        else:
            name = 'TBD'
        
        loadFont = 'fonts/'+imageFont

        x = len(name)

        if x>17:
            font=ImageFont.truetype(loadFont,45)
            movedescup = 'true'
            loc = 440 # Puts location at a higher level
        else:
            font=ImageFont.truetype(loadFont,60) 
            movedescup = 'false'
            loc = 450 # Puts location at a lower level

        name = name.upper() 
        w,h=font.getsize(name)
        draw=ImageDraw.Draw(background)
        w1, h1 = draw.textsize(name, font=font)
        draw.text((centerline,loc),name,font=font,fill='white', anchor='ms') # Writes name

        # Loads Desc
        if i['description'] != None:
            desc = i['description']
        else:
            desc = 'TBD'

        loadFont = f'fonts/{sideFont}'
        
        try:
            set = i['set']['text']
        except:
            set = None
        if set == None:
            set = None
        else:
            set = set

        x = len(desc)
        if x>95:
            font=ImageFont.truetype(loadFont,10)
            draw=ImageDraw.Draw(background)
            line = 470
            draw.text(
                (centerline,line),
                desc,
                font=font,
                fill='white', 
                anchor='ms') # Writes name
        else:
            if x>45:
                #print('above')
                font=ImageFont.truetype(loadFont,14)
                draw=ImageDraw.Draw(background)
                if set != None:
                    line = 474
                else:
                    line = 480
                if movedescup == 'true':
                    line = line-8
                draw.text(
                    (centerline,line),
                    desc,
                    font=font,
                    fill='white', 
                    anchor='ms') # Writes name
            else:
                #print('below')
                font=ImageFont.truetype(loadFont,16)
                draw=ImageDraw.Draw(background)
                if set != None:
                    line = 475
                else:
                    line = 480

                if movedescup == 'true':
                    line = line-2
                draw.text(
                    (centerline,line),
                    desc,
                    font=font,
                    fill='white', 
                    anchor='ms') # Writes name   

        # Loads Item Set Text
        if set != None:
            font=ImageFont.truetype(loadFont, 15)
            draw=ImageDraw.Draw(background)
            draw.text(
                (centerline, 500),
                set,
                font=font,
                fill='white',
                anchor='ms') # Writes set

        # Loads watermark
        loadFont = 'fonts/'+imageFont # Puts font back to original
        if watermark != '':
            font=ImageFont.truetype(loadFont,25)
            draw=ImageDraw.Draw(background)
            draw.text((10,9),watermark,font=font,fill='white')

        # Loads gameplay tag
        if showitemsource != 'False':
            text = ''
            try:
                for x in i['gameplayTags']:
                    if 'Cosmetics.Source.ItemShop' in x:
                        text = 'Cosmetics.Source.ItemShop'
                        break
                    if '.BattlePass.Paid' in x:
                        text = f'Cosmetics.Source.Season{seasonnum}.BattlePass.Paid'
                        break
                    if 'Cosmetics.Set.' in x:
                        # Creates Set
                        try:
                            set = i['set']['value'].replace(' ', '')
                        except:
                            pass
                        text = f'Cosmetics.Set.{set}'
                        break
            except:
                pass
            font=ImageFont.truetype(loadFont, 15)
            if watermark != '':
                draw=ImageDraw.Draw(background)
                draw.text((10,30),text,font=font,fill='white')
            else:
                if text != None or text != '':
                    draw=ImageDraw.Draw(background)
                    draw.text((10,10),text,font=font,fill='white')
        background.save('icons/'+i["id"]+'.png')
        end = time.time()

        # Finishing Time
        percentage = counter/len(new['items'])
        realpercentage = percentage * 100
        print(Fore.CYAN + f"Generated image for {i['id']}")
        print(Fore.CYAN + f"{counter}/{len(new['items'])} - {round(realpercentage)}%\n")
        counter = counter + 1

    end1 = time.time()
    print("!  !  !  !  !  !  !")
    print(f"IMAGE GENERATING COMPLETE - Generated image in {round(end1 - start1, 2)} seconds!")
    if MergeImagesAuto != 'False':
        print('SAVED MERGED IMAGE!')
    print("!  !  !  !  !  !  !")


    if MergeImagesAuto != 'False':
        print('\nMerging images...')
        if 'image' in mergewatermark:
            addwatermark()
        merger(mergewatermark, loc1)

        version = new['build'].replace('++Fortnite+Release-', '').replace('-CL-17328477-Windows', '')
        #print(x)
        lol = len(os.listdir('icons'))
        if mergewatermark == '':
            lol = lol-1
        print('\nSaved image!')
        if automergetweet != 'False':
            if twitAPIKey != 'XXX':
                print('\nTweeting out image....')
                try:
                    api.update_with_media(f'merged/merge.jpg', f'[{namelol}] Found {lol} Leaked cosmetics from Patch {version}.')
                except:
                    print(Fore.YELLOW + '\nFile size is too big, compressing image.')
                    compressnewcosmetics_new(lol)
                    api.update_with_media(f'merged/merge.jpg', f'[{namelol}] Found {lol} Leaked cosmetics from Patch {version}.')
                    time.sleep(5)
                print(Fore.GREEN + '\nTweeted image successfully!')
        else:
            print(Fore.YELLOW+'Not tweeting images.')
            time.sleep(2)
            exit()
    else:
        print('Not auto merging images.')
        print('Exiting...')
        time.sleep(2)
        exit()

def set_search():
    try:
        shutil.rmtree('icons')
        os.makedirs('icons')
    except:
        os.makedirs('icons')
    print(Fore.GREEN + '\nCleared Content\nWhat set do you want to grab?' + Fore.CYAN)
    ask = input('>> ')
    fontSize = 40
    response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search/all?set={ask}&language={language}')
    if response.json()['status'] == 404:
        print(Fore.RED + 'Item Set does not exist.')
        set_search()
    new = response.json()['data']

    print(Fore.GREEN + f'\nLoaded set [{ask}] with Fortnite-API')
    print(f'Loaded [{len(new)}] cosmetics in set\n')
    loop = False
    counter = 1
    start = time.time()
    iconType = 'new'
    for i in new:
        start = time.time()
        try:
            print(Fore.BLUE + "Loading image for "+i["id"])
        except:
            print(Fore.RED + f'Unable to retreive item.')
            time.sleep(5)
            exit()
        if useFeaturedIfAvaliable == 'True':
            if i["images"]["featured"] != None:
                url = i["images"]["featured"]
            else:
                if i['images']['icon'] != None:
                    url = i["images"]["icon"]
                else:
                    url = 'https://i.ibb.co/KyvMydQ/do-Not-Delete.png'
        elif useFeaturedIfAvaliable == 'False':
            if i['images']['icon'] != None:
                url = i["images"]["icon"]
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

        rarity = i["rarity"]['value']
        rarity = rarity.lower()
        
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
        foreground= Image.open('cache/icontemp.png').resize((512, 512), Image.ANTIALIAS).convert('RGBA')
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
    
            loadFont = f'fonts/{sideFont}'
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
            try:
                if i['set']['text'] != None:
                    if desc1 != '':
                        if descup != 'true':
                            if desc1 == 'aaaa':
                                # IF DESC IS BIG AF THEN DO THIS #
                                bigaf = '1'
                                pass
                            else:
                                # This means it is not big af
                                #print('a')
                                draw.text(((512-w1)/2,455),desc,font=font,fill='white')
                        else:
                            # This means if it equals none then it 
                            #print('bc')
                            if xx>70:
                                font=ImageFont.truetype(loadFont,14)
                            else:
                                font=ImageFont.truetype(loadFont,20)
                                w,h=font.getsize(desc)
                                draw=ImageDraw.Draw(background)
                                w1, h1 = draw.textsize(desc, font=font)
                            draw.text(((512-w1)/2,448),desc,font=font,fill='white')
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
                            print('aaaa')
                            draw.text(((512-w1)/2,465),desc,font=font,fill='white')
                    else:
                        print('bbb')
                        draw.text(((512-w1)/2,470),desc,font=font,fill='white')
            except:
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
                        #print('aab')
                        draw.text(((512-w1)/2,465),desc,font=font,fill='white')
                else:
                    #print('beb')
                    desc1 = 'nope'
                    draw.text(((512-w1)/2,470),desc,font=font,fill='white')

            if desc1 == '':
                #print('b')
                if xx1>17:
                    draw.text(((512-w1)/2,440),desc,font=font,fill='white')
                else:
                    draw.text(((512-w1)/2,457),desc,font=font,fill='white')

            try:
                if i['set']['text'] != None:
                    set = i["set"]['text']
                    font=ImageFont.truetype(loadFont,16)
                    w,h=font.getsize(set)
                    draw=ImageDraw.Draw(background)
                    w1, h1 = draw.textsize(set, font=font)
                    if desc1 != '':
                        if bigaf == '1':
                            print('AAAAAAAAA')
                            draw.text(((512-w1)/2,465),set,font=font,fill='white')
                        else:
                            # Alright, this should be if the description is too big then it does this i guess #
                            draw.text(((512-w1)/2,480),set,font=font,fill='white')
                    else:
                        # Same thing as the one above but just adding an else because if its normal its not '' #
                        draw.text(((512-w1)/2,480),set,font=font,fill='white')
            except:
                pass
    
    
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
            #if i['gameplayTags'] == None:
            #    showitemsource = 'False'

            if showitemsource != 'False':
                bruh = ''
                if i['gameplayTags'] == None:
                    bruh = 'no tags'
                if bruh != 'no tags':
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
            else:
                pass
            
            if showitemsource == 'True':
                font=ImageFont.truetype(loadFont,15)
                thing1 = source.replace('Cosmetics.Source.', '')
                #x = len(thing1)
                if shop == '1':
                    thing1 = 'Cosmetics.Source.ItemShop'
                elif shop == '2':
                    try:
                        thing1 = f'Season{seasonnum}.BattlePass.Paid'
                    except:
                        thing1 = f'SeasonTBD.BattlePass.Paid'
                elif shop == '0':
                    thing1 = ''
                elif shop == '3':
                    set = i['set']['value']
                    try:
                        set1 = set.replace(' ', '')
                    except:
                        pass
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
        i = response.json()['data']
        percentage = counter/len(i)
        realpercentage = percentage * 100
        print(Fore.CYAN + f"Generated image for {id}")
        print(Fore.CYAN + f"{counter}/{len(i)} - {round(realpercentage)}%")
        print("")
        counter = counter + 1
        end = time.time()

    if MergeImagesAuto != 'False':
        print('\nMerging images...')
        merger(mergewatermark, loc1)
        response = requests.get('https://fortnite-api.com/v2/aes')
        version = response.json()['data']['build']
        version = version[19:24]
        lol = len(os.listdir('icons'))
        if mergewatermark == '':
            lol = lol-1
        print('\nSaved image!')
        if automergetweet != 'False':
            if twitAPIKey != 'XXX':
                print('\nTweeting out image....')
                try:
                    api.update_with_media(f'merged/MERGED {lol}.png', f'[{namelol}] Found {lol} Leaked cosmetics from Patch {version}.')
                except:
                    print(Fore.YELLOW + '\nFile size is too big, compressing image.')
                    compressnewcosmetics_new(lol)
                    api.update_with_media(f'merged/MERGED {lol}.png', f'[{namelol}] Found {lol} Leaked cosmetics from Patch {version}.')
                    time.sleep(5)
                print(Fore.GREEN + '\nTweeted image successfully!')
            else:
                print(Fore.YELLOW+'Not tweeting images.')
        else:
            print('not tweeting')
    else:
        print('Not auto merging images.')

    set_search()

def catabaupdate():
    response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/new?language={language}')
    oldhash = response.json()['data']['hash']

    count = 1

    while 1:
        response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/new?language={language}')
        if response:
            try:
                newhash = response.json()['data']['hash'] 
            except:
                catabaupdate()
            print(f'Checking for a change in cosmetics... ({count})')
            count = count + 1
            if newhash != oldhash:
                print('A new update has been pushed. Generating cosmetics.')
                catabaicons()
                try:
                    api.update_with_media('merged/merge.jpg', 'A new update has been pushed out, heres all of the new cosmetics:')
                except:
                    compressnewcosmetics_new()
                    api.update_with_media('merged/merge.jpg', 'A new update has been pushed out, heres all of the new cosmetics:')
                print('Done :)')
                return catabaupdate()
        else:
            print("FAILED TO GRAB NOTICES DATA: URL DOWN")
        time.sleep(5)

def catabaicons():
    delete_contents()
    print(Fore.YELLOW + 'THIS IS A WORK IN PROGRESS, NOT FULLY FINISHED YET.' + Fore.GREEN)
    
    response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/new?language={language}')
    version = response.json()['data']['build']
    print('\nGenerating cosmetics for version',version)
    counter = 0
    itemnum = 0
    for i in response.json()['data']['items']:
        name = i['name']
        id = i['id']
        description = i['description']
        backendtype = i['type']['value']
        backendtype = backendtype.upper()

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
        try:
            r = requests.get(url)
        except:
            print('a')
        open(f'cache/{id}temp.png', 'wb').write(r.content)
        iconImg = Image.open(f'cache/{id}temp.png')
        iconImg.resize((512,512),PIL.Image.ANTIALIAS)


        rarity = i["rarity"]['value']
        rarity = rarity.lower()

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

        varaints_icon = Image.open('rarities/cataba/PlusSign.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
        if i['variants'] != None:
            img.paste(varaints_icon, (0,0), varaints_icon)

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

        font=ImageFont.truetype(loadFont,14)
        draw=ImageDraw.Draw(background)
        draw.text((6,495),backendtype,font=font,fill='white') # Writes backend type        

        background.save(f'icons/{id}.png')
        os.remove(f'cache/{id}temp.png')
        os.remove(f'cache/{id}.png')
        counter = counter + 1
        i = response.json()['data']['items']
        percentage = counter/len(i)
        realpercentage = percentage * 100
        print(f"{counter}/{len(i)} - {round(realpercentage)}%")
        itemnum = itemnum + 1
    
    print('Done!')
    if MergeImagesAuto != 'False':
        print('\nMerging images...')
        if 'image' in mergewatermark:
            addwatermark()
        merger(mergewatermark, loc1)
        if automergetweet != 'False':
            api.update_with_media(f'merged/merge.jpg', f'[{namelol}] Found {itemnum} Leaked cosmetics from Patch {version}.')
            print('Tweeted')


def catabasearch():
    print(Fore.GREEN+'\nWhat cosmetic do you want to lookup? (Enter name or enter an ID by doing ID:CID_Example_ID)')
    name = input('>> ')
    if 'ID:' in name:
        name = name.replace('ID:','')
        response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?language={language}&id={name}')
    else:
        response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?language={language}&name={name}')
    if response.json()['status'] == 404:
        print('ERROR: 404')
        catabasearch()
    i = response.json()['data']
    start = time.time()
    name = i['name']
    id = i['id']
    description = i['description']
    backendtype = i['type']['value']
    backendtype = backendtype.upper()

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
    try:
        r = requests.get(url)
    except:
        print('a')
    open(f'cache/{id}temp.png', 'wb').write(r.content)
    iconImg = Image.open(f'cache/{id}temp.png')
    iconImg.resize((512,512),PIL.Image.ANTIALIAS)


    rarity = i["rarity"]['value']
    rarity = rarity.lower()

    try:
        raritybackground = Image.open(f'rarities/cataba/{rarity}.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
    except:
        raritybackground = Image.open(f'rarities/cataba/common.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")

    try:
        background = Image.open(f'rarities/cataba/{rarity}_background.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
    except:
        background = Image.open(f'rarities/cataba/common_background.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")

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

    varaints_icon = Image.open('rarities/cataba/PlusSign.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
    if i['variants'] != None:
        img.paste(varaints_icon, (0,0), varaints_icon)

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

    font=ImageFont.truetype(loadFont,14)
    draw=ImageDraw.Draw(background)
    draw.text((6,495),backendtype,font=font,fill='white') # Writes backend type        

    background.save(f'icons/{id}.png')
    os.remove(f'cache/{id}temp.png')
    os.remove(f'cache/{id}.png')
    end = time.time()
    print(Fore.CYAN+"")
    print("!  !  !  !  !  !  !")
    print(f"IMAGE GENERATING COMPLETE - Generated image in {round(end - start, 2)} seconds!")
    print("!  !  !  !  !  !  !")
    time.sleep(2)
    img = Image.open(f'icons/{id}.png')
    img.show()
    if twitsearch == 'True':
        api.update_with_media(f'icons/{id}.png', f'{name} - {backendtype}')
    catabasearch()


def cataba_pak():
    print(Fore.GREEN+'\nWhat pak do you wanna grab')
    pak = input('>> ')
    response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search/all?dynamicPakId={pak}&language={language}')
    if response.json()['status'] == 404:
        print('ERROR: 404')
        cataba_pak()
    data = response.json()['data']
    start = time.time()
    counter = 0
    for i in data:
        name = i['name']
        id = i['id']
        description = i['description']
        backendtype = i['type']['value']
        backendtype = backendtype.upper()

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
        try:
            r = requests.get(url)
        except:
            print('a')
        open(f'cache/{id}temp.png', 'wb').write(r.content)
        iconImg = Image.open(f'cache/{id}temp.png')
        iconImg.resize((512,512),PIL.Image.ANTIALIAS)


        rarity = i["rarity"]['value']
        rarity = rarity.lower()

        try:
            raritybackground = Image.open(f'rarities/cataba/{rarity}.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
        except:
            raritybackground = Image.open(f'rarities/cataba/common.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")

        try:
            background = Image.open(f'rarities/cataba/{rarity}_background.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
        except:
            background = Image.open(f'rarities/cataba/common_background.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")

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

        varaints_icon = Image.open('rarities/cataba/PlusSign.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
        if i['variants'] != None:
            img.paste(varaints_icon, (0,0), varaints_icon)

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

        font=ImageFont.truetype(loadFont,14)
        draw=ImageDraw.Draw(background)
        draw.text((6,495),backendtype,font=font,fill='white') # Writes backend type        

        background.save(f'icons/{id}.png')
        os.remove(f'cache/{id}temp.png')
        os.remove(f'cache/{id}.png')
        end = time.time()
        counter = counter + 1
        i = response.json()['data']
        percentage = counter/len(i)
        realpercentage = percentage * 100
        print(f"{counter}/{len(i)} - {round(realpercentage)}%")
    #time.sleep(2)
    #img = Image.open(f'icons/{id}.png')
    #img.show()
    print('done')
    merger(mergewatermark, loc1)
    if twitsearch == 'True':
        api.update_with_media(f'icons/{id}.png', f'{name} - {backendtype}')
    cataba_pak()

def reset_settings():
    print('')
    print('Are you sure you want to reset settings.json?\n(y) Yes\n(n) No')
    ask = input('>> ')
    ask = ask.lower()
    if ask == 'y':
        print('\nClearing settings.json...')
        response = requests.get('https://raw.githubusercontent.com/FortniteFevers/AutoLeak/beta/settings.json')

        with open(f'test.json', 'w') as x:
            json.dump(response.json(), x, indent = 2)
        
        print('Dumped json to file')

    else:
        print('\nNot clearing settings.json.')

    exit()

##############################################
print(Fore.GREEN + "\n- - - - - MENU - - - - -")
print("")

if response != None:
    notice = response.json()['notice']
    if notice == None or notice == '':
        pass
    else:
        print(Fore.RED+'!!NOTICE!! '+Fore.GREEN+f'{notice}\n')
else:
    print(Fore.RED+'!!NOTICE!! '+Fore.GREEN+f'For some reason, Pastebin did not work. Try to relaunch AutoLeak!\n')

print(Fore.RED+'- IMPORTANT COMMANDS -'+Fore.GREEN)
print(Fore.YELLOW + "(reset)" +Fore.GREEN + " - Reset settings.json")

print('')
print(Fore.CYAN+'- MAIN COMMANDS -'+Fore.GREEN)
print(Fore.YELLOW + "(1)" +Fore.GREEN + " - Start update mode")
print(Fore.YELLOW + "(2)" +Fore.GREEN + " - Generate new cosmetics")
print(Fore.YELLOW + "(3)" +Fore.GREEN + " - Search for a cosmetic")
print(Fore.YELLOW + "(4)" +Fore.GREEN + " - Grab all cosmetics from a specific pak")
print(Fore.YELLOW + "(5)" +Fore.GREEN + " - Generate a custom Fortnite Item Shop image")

print('')
print(Fore.CYAN+'- OTHER COMMANDS -'+Fore.GREEN)
print("(6) - Tweet current build")
print("(7) - Tweet current AES key")
print("(8) - Clear contents of the icon folder")
print("(9) - Check for a change in News Feed")
print("(10) - Merge images in icons folder (512x512)")
print("(11) - Check for a change in Shop Sections")
print("(12) - Checks for a change in notices")
print("(13) - Checks for a change in staging servers") # staging_servers
print("(14) - Search for any weapon of choice.") # weapons

print('')
print(Fore.CYAN+'- BETA COMMANDS -'+Fore.GREEN)
print("(15) - Search by set") # set_search

#print("(16) - Merge large icon images")

###

print("")
option_choice = input(">> ")
option_choice = option_choice.lower()

# IMPORTANT COMMANDS
if option_choice == 'reset':
    reset_settings()


# MAIN COMMANDS
if option_choice == "1":
    update_mode()
elif option_choice == "2":
    generate_cosmetics()
elif option_choice == "3":
    search_cosmetic()
elif option_choice == "4":
    dynamic_pak()
elif option_choice == "5":
    shop()

# OTHER COMMANDS
elif option_choice == "6":
    tweet_build()
elif option_choice == "7":
    tweet_aes()
elif option_choice == "8":
    delete_contents()
elif option_choice == "9":
    news_feed()
elif option_choice == "10":
    merge_images()
elif option_choice == "11":
    shop_sections(sections_image, BotDelay, BG_Color, api, namelol, watermark, language)
elif option_choice == "12":
    notices()
elif option_choice == "13":
    staging_servers()
elif option_choice == "14":
    weapons()
elif option_choice == "69":
    largeicontype_search_banner(useFeaturedIfAvaliable, language)

# BETA COMMANDS
elif option_choice == '15':
    set_search()
elif option_choice == '16':
    large_merger()

else:
    print(Fore.RED+"\nPlease enter a number between 1 and 16")
    time.sleep(2)
    
# Search for a cosmetic (NEW ICONS)") - newcbeta()
# Generate new cosmetics (NEW ICONS)') - newcnew()
# Grab all cosmetics from a specific pak (NEW ICONS)') - dynpak2()

#print('(L1) - '+Fore.YELLOW+'**IN BETA** '+Fore.GREEN+'Large Icon Type Gen (new cosmetics)')
#print('(L2) - '+Fore.YELLOW+'**IN BETA** '+Fore.GREEN+'Large Icon Type Gen (search cosmetic)')
#print('(L3) - '+Fore.YELLOW+'**IN BETA** '+Fore.GREEN+'Large Icon Type Gen (pak search)')
#print('(LM) - '+Fore.YELLOW+'**IN BETA** '+Fore.GREEN+'Large Icon Type Gen (Merge cosmetics)')

# If you have any issues with the softwere, please message Fevers#3474 on discord. #
