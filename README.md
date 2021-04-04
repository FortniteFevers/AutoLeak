# AutoLeak

A program made by [Fevers](https://twitter.com/itsfevers__) and [Thomas Keig](https://twitter.com/thomaskeig_).

AutoLeak is a utility to generate all of the latest leaks in Fortnite, with some bonus features as well.

---

#### AutoLeak 1.3.8 has just been released!
# Whats new in version 1.3.5?
1. NEW ICONS!
- You can use these by changing your type of icons to 'new' in settings.json!
- You can search, generate, and grab paks with these new icons!
- The new icons are BenBot ONLY so if you want to use Fortnite-API, switch over to the standard icons.

2. Added notices command
- Checks for a change or a added Fortnite notice. If it detects one, it will post it to your twitter.
- REQUIRED You need Twitter API keys for this command.
- (API LINK: https://developer.twitter.com/en/portal/dashboard)

3. Added Staging Servers command
- Checks for a change in the Fortnite Staging Servers. If it detects one, it will post it to your twitter.
- REQUIRED You need Twitter API keys for this command.
- (API LINK: https://developer.twitter.com/en/portal/dashboard)

4. Weapons command!
- Search for any weapon you want, and it can generate icons for it.
- UPCOMING Loot pool command. Generate an image of the current loot pool!

5. BUG FIXES! (And small changes)
- Fixed Item Shop, News, and Shop Sections command
- Faster icon generation
- Added language support for BenBot
- Fixed the Footer to not work
- Item Shop command now compresses the image if it is too big to tweet out.
- Fixed a lot more things, but I forget what they are so uh it should just be better

6. UPCOMING FEATURES:
- Custom Item Shop generation (Haven't really started but I will soon)
- Merge all detection commands into one (I will be doing this but in a different program separate from AutoLeak)
- Playlist command (I kind of got it done, but it is really spammy)

7. SETTINGS.JSON CHANGES:
- Added 'apikey' (An API key provided by fortniteapi.io ONLY USED FOR THE WEAPONS COMMAND, NOT REQUIRED!)
- Added 'CreatorCode' (Your creator code goes here. This is used for Item Shop posts, news posts, etc. NOT REQUIRED!)
- Added 'MergeWatermarkUrl' (When merging images it will add a watermark to the merged image NOT REQUIRED!)

### Version Bugs:
- When merging cosmetics from a specific pak, if the number of items merged is equal to "5", it will not work for some reason.


# Features
AutoLeak is a program with many features.
Currently, the program features these options:
- Custom icon generation
- Update mode to detect for a new update and leak the contents, saving every one into the image format
- Generate new cosmetics, which can generate all new cosmetics in an update
- Search for a cosmetic and generate an image
- Tweet out current AES
- Tweet out current build
- Automaticlly Tweet AES and Build if on update mode
- Automaticlly Tweet out news feed and detect for a change
- BenBot Support for searching cosmetics
- Merge images by using the new 'Merge Images' command in AutoLeak
- Checking for Shop Sections
- Grab cosmetics from a specific pak
(Merging images automatically saves to the new "merged" folder!)

And MANY more!

**Sample Image:**

<p align="left">
    <img src="https://i.ibb.co/gth5ggC/CID-703-Athena-Commando-M-Cyclone.png" width="400" draggable="false">
</p>

# Running AutoLeak
To run AutoLeak, you have to have [Python 3.9](https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7) installed on your computer.

After you have succesfully installed Python, you can go to this repl and save the repl as a .zip file.

After you have done this, extract the folder, and open up **INSTALL PACKAGES** and follow the steps.

Now, go into 'settings.json' and edit the content to your liking.

After this, run 'startprogram.bat' and enter in a number (Each number correlates to a command) and enjoy!

# Languages
The following languages are supported: ar / de / en / es / es-419 / fr / it / ja / ko / pl / pt-BR / ru / tr / zh-CN / zh-Hant
- Change these within your settings.json file!
