#!/usr/bin/env python
# -*- coding: utf-8 -*-
__module_name__ = "Colors"
__module_version__ = "1.0"
__module_description__ = "Green text and black background"
__module_author_ = "Mroik"

import xchat

def colors(word, word_eol, userdata):
    newcol = str(chr(3)+"4,15 ✘✔✘ "+chr(3)+"9,1 "+word_eol[1]+" "+chr(3)+"4,15 ✘✔✘ ")
    xchat.command("say "+newcol)
    return xchat.EAT_ALL

def colors2(word, word_eol, userdata):
    newcol = " ✘✔✘ "+word_eol[1]+" ✘✔✘ "
    xchat.command("say "+newcol)
    return xchat.EAT_ALL

xchat.hook_command("FAINA",colors,help="Colors the text before sending")
xchat.hook_command("MIRKO",colors2,help="Same format of FAINA but without colors")
xchat.prnt("Color script loaded")
