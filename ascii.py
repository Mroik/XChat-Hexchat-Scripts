#!/usr/bin/env python
# -*- coding: utf-8 -*-

__module_name__ = "Ascii"
__module_version__ = "beta"
__module_author__ = "Mroik"
__module_description__ = "Imports ascii art from https://github.com/Mroik/myascii.git"

import xchat
import string
import os

def coloring(text):
    text = text.replace("+",chr(3)+"9,9+")
    text = text.replace("-",chr(3)+"1,1-")
    xchat.command("say "+text)

def asciilist(word,word_eol,userdata):
    lista=os.listdir("/home/mirko/myascii/ascii")
    for x in lista:
        print(x)
    lista=os.listdir("/home/mirko/myascii/ascii2")
    for x in lista:
        print(x)
    return xchat.EAT_ALL
xchat.hook_command("ASCLIST",asciilist)

def update(word,word_eol,userdata):
    os.system("git clone https://github.com/Mroik/myascii.git")
    print("Ascii database updated")
    return xchat.EAT_ALL
xchat.hook_command("ASCUP",update)

def ascii(word,word_eol,userdata):
    if os.path.exists("/home/mirko/myascii/ascii/"+word[1]+".txt"):
        text = open("/home/mirko/myascii/ascii/"+word[1]+".txt")
        for line in text:
            xchat.command("say "+chr(3)+"9,1"+line)
        text.close
    else:
        print("This file doesn't exist")
    return xchat.EAT_ALL
xchat.hook_command("ASCII",ascii)

def ascii2(word,word_eol,userdata):
    text = open("/home/mirko/myascii/ascii2/"+word[1]+".txt")
    for line in text:
        line = line.replace("+",chr(3)+"9,9+")
        line = line.replace("-",chr(3)+"1,1-")
        xchat.command("say "+chr(3)+"9,1"+line)
    text.close
    return xchat.EAT_ALL
xchat.hook_command("ASCIIC",ascii2)

print("Ascii script loaded")
