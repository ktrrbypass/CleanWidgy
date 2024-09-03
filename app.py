import subprocess
import re
import urllib.request
import os
from exploit.restore import restore_file
from pathlib import Path

def getUUID():
    process = subprocess.Popen(['pymobiledevice3', 'syslog', 'live', '-pn', 'kernel'], 
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    try:
        for line in process.stdout:
            match = re.search(r'/private/var/containers/Bundle/Application/([A-F0-9\-]{36})/', line)
            if match:
                uuid = match.group(1)
                print(f"Got Widgy UUID!: {uuid}")
                process.terminate()
                return uuid
    finally:
        process.terminate()

os.system('cls' if os.name == 'nt' else 'clear')

print(r'''
  _____ __                _      __ _     __           
 / ___// /___  ___ _ ___ | | /| / /(_)___/ /___ _ __ __
/ /__ / // -_)/ _ `// _ \| |/ |/ // // _  // _ `// // /
\___//_/ \__/ \_,_//_//_/|__/|__//_/ \_,_/ \_, / \_, / 
                                          /___/ /___/                                                                      
                    Private Alpha

             Inspired by Codename Nugget and 
                 Written by KTRRBypass
      Special thanks to Lrdsnow, Little_34306 & Skadz
            WARNING THIS ONLY WORKS ON 3.4.2
    ''')
file_path = Path.joinpath(Path.cwd(), 'Info.plist')
if not Path.is_file(file_path):
    print("Info.plist not in this directory, downloading it now...")
    urllib.request.urlretrieve("https://github.com/ktrrbypass/Widgy-Info.plist/releases/download/3.4.2/Info.plist", "Info.plist")
    print("Info.plist successfully downloaded! Run the script again to apply it.")
else:
    input("This script remove the app name for Widgy. To start, hit Enter wait a few seconds and open Widgy on your device.")
    WidgyUUID = getUUID()
    input("The exploit is about to run. Make sure to apply your widgets before running, widgy will not be able to be opened and you will have to reinstall it from the App Store.\n\nPress Enter to apply the exploit...")
    restore_file(fp=file_path, restore_path=f'/var/containers/Bundle/Application/{WidgyUUID}/Widgy.app/', restore_name='Info.plist')
    exit = input("Overwrite completed. Good luck!\nPress Enter to exit...")
    if not exit:
        exit()
