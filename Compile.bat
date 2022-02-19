echo off

pip install --upgrade pip
pip install pyinstaller
pip install requests
pip install pywin32
pip install opencv-python
pip install Pillow
pip install pyTelegramBotAPI
pip install psutil
pip install GPUtil
pip install tabulate
pip install pycryptodome

pyinstaller -F -w -i vk.ico code.py


rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null