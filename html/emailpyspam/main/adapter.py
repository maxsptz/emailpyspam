import os
from optparse import OptionParser
import time

os.system('xhost +')

from pynput import Key, Controller

keyboard = Controller()


##
# set the display with export DISPLAY=":0" as a command for www-data
##

def getopts():
    parser = OptionParser()
    parser.add_option("-r", "--recipients", dest="reci", help="the poor fucker whos email your spamming")
    parser.add_option("-n", "--number", dest="num", help="the number of emails your sending")

    (options, arguments) = parser.parse_args()
    return options

def keys(key):
    keyboard.press_and_release(key)

def startinitprogram():
    begin()
    mycmd = 'python3 emailspam.py'
    os.system(mycmd)


def begin():
    option = getopts()
    recip = option.reci
    time.sleep(10)
    keys('1')
    keys('1')
    keyboard.press_and_release('\n')
    keyboard.press_and_release('\n')
    keys('y')
    keys(option.num)
    keys('y')
    keys('y')
    keys('1')

startinitprogram()

