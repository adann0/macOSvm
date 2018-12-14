#!/usr/bin/env python3

"""
./macOSvm "/Applications/Install macOS <version>.app" /out/path
"""

import sys
import os

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

def guard(msg) :
    print(msg)
    print('=== man macOSvm ===\n./macOSvm "/Applications/Install macOS <version>.app" /out/path')
    exit()

if len(sys.argv) < 3 : guard('You miss the input or output path.\n')

if sys.argv[1].endswith('.app') is False : guard("Your 'Install macOS.app' Path seems to be wrong.\n")

if os.path.isdir(sys.argv[2]) is False : guard("Your Out Path seems to be wrong.\n")

i = sys.argv[1].find('Install macOS') + 14
j = sys.argv[1].find('.app')

if i == -1 or j == -1 : guard("Your 'Install macOS.app' Path seems to be wrong.\n")

versionname = sys.argv[1][i:j]
print (bcolors.WARNING + "$ hdiutil create -o '/tmp/" + versionname + ".cdr' -size 7316m -layout SPUD -fs HFS+J" + bcolors.ENDC)
os.system("hdiutil create -o '/tmp/" + versionname + ".cdr' -size 7316m -layout SPUD -fs HFS+J")
print (bcolors.WARNING + "$ hdiutil attach '/tmp/" + versionname + ".cdr.dmg' -noverify -nobrowse -mountpoint /Volumes/install_build" + bcolors.ENDC)
os.system("hdiutil attach '/tmp/" + versionname + ".cdr.dmg' -noverify -nobrowse -mountpoint /Volumes/install_build")
print (bcolors.WARNING + "$ asr restore -source '" + sys.argv[1] + "/Contents/SharedSupport/BaseSystem.dmg' -target /Volumes/install_build -noprompt -noverify -erase" + bcolors.ENDC)
os.system("asr restore -source '" + sys.argv[1] + "/Contents/SharedSupport/BaseSystem.dmg' -target /Volumes/install_build -noprompt -noverify -erase")
print (bcolors.WARNING + "$ hdiutil detach /Volumes/OS\ X\ Base\ System" + bcolors.ENDC)
os.system("hdiutil detach /Volumes/OS\ X\ Base\ System")
print (bcolors.WARNING + "$ hdiutil convert '/tmp/" + versionname + ".cdr.dmg' -format UDTO -o '/tmp/" + versionname + ".iso'" + bcolors.ENDC)
os.system("hdiutil convert '/tmp/" + versionname + ".cdr.dmg' -format UDTO -o '/tmp/" + versionname + ".iso'")
print (bcolors.WARNING + "$ mv '/tmp/" + versionname + ".iso.cdr' '" + sys.argv[2] + "'" + bcolors.ENDC)
os.system("mv '/tmp/" + versionname + ".iso.cdr' '" + sys.argv[2] + "'")
print (bcolors.OKGREEN + "DONE !" + bcolors.ENDC)
