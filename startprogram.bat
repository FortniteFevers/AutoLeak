@echo off
echo Instaling Packages...
pip3 install -r requirements.txt
pip3 install requests
python bot.py
pause >Nul
