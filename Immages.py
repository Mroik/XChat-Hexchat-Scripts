#!/usr/bin/env python
# -*- coding: utf-8 -*-
__module_name__ = "Image"
__module_version__ = "1.0"
__module_description__ = "Sends Ascii arts"
__module_author__ = "Mroik"
import xchat
import string

def coloring(listlin3):
    for x in listlin3:
        x = x.replace("+", chr(3)+"9,9+")
        x = x.replace("-", chr(3)+"1,1+")
        xchat.command("say " + x)

def hello(word,word_eol,userdata):
    status = 0
    line1 = "+----+---++++++---+------+-----++++++"
    line2 = "+----+---+--------+------+-----+----+"
    line3 = "++++++---+++------+------+-----+----+"
    line4 = "+----+---+--------+------+-----+----+"
    line5 = "+----+---++++++---+++++--+++++-++++++"
    listline = [line1,line2,line3,line4,line5]
    coloring(listline)
    return xchat.EAT_ALL
xchat.hook_command("HELLO",hello)

def gays(word,word_eol,userdata):
    line1 = "--------------+++++++---++++++---+++-----+++---------------"
    line2 = "-------------+++---+++------+++---+++---+++----------------"
    line3 = "-------------+++---+++--+++++++----+++-+++-----------------"
    line4 = "--------------++++++++-+++--+++-----+++++------------------"
    line5 = "-------------------+++--++++++++-----+++-------------------"
    line6 = "--------------+++++++---------------+++--------------------"
    line7 = "-----------------------------------------------------------"
    line8 = "-----------------------------+++---------------------------"
    line9 = "---------------------------------------------+++-----------"
    line10 = "---++++++---++++++--++++++--++++---+++++++--++++++---++++++"
    line11 = "--+++------+++-----+++--+++--+++--+++---+++--+++----+++----"
    line12 = "---+++++--+++------+++-------+++--+++---+++--+++-----+++++-"
    line13 = "------+++--+++-----+++-------+++--++++++++---++++++-----+++"
    line14 = "--++++++----++++++-+++------+++++-+++---------++++--++++++-"
    line15 = "----------------------------------+++----------------------"
    listline = [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15]
    coloring(listline)
    return xchat.EAT_ALL
xchat.hook_command("GAYS",gays)

def fuck(word,word_eol,userdata):
    line1 = "++++++---+-----+----++++++++----+----+-"
    line2 = "+--------+-----+----+-----------+--++--"
    line3 = "++++++---+-----+----+-----------+++----"
    line4 = "+--------+-----+----+-----------+--+++-"
    line5 = "+--------+++++++----++++++++----+-----+"
    listline = [line1,line2,line3,line4,line5]
    coloring(listline)
    return xchat.EAT_ALL
xchat.hook_command("FUCK",fuck)

def goodnight(word,word_eol,userdata):
    line1 = "++++++++---++++++++---++++++++---++++++---++----+--+++--+++++++++---+-------+---+++++++++"
    line2 = "+----------+------+---+------+---+-----+--+-+---+--+++--+-----------+-------+-------+----"
    line3 = "+---++++---+------+---+------+---+-----+--+--+--+--+++--+----++++---+++++++++-------+----"
    line4 = "+------+---+------+---+------+---+-----+--+---+-+--+++--+-------+---+-------+-------+----"
    line5 = "++++++++---++++++++---++++++++---++++++---+----++--+++--+++++++++---+-------+-------+----"
    listline = [line1,line2,line3,line4,line5]
    coloring(listline)
    return xchat.EAT_ALL
xchat.hook_command("GOODNIGHT",goodnight)

def bikini(word,word_eol,userdata):
    line1 = "                           _"
    line2 = "                         .-\" `."
    line3 = "                         ;:\":  \"\"--.."
    line4 = "                .-+. ,gpd$L\:._      \"\"-._"
    line5 = "               /  //;$SS$$$$SS$$t--.      \"-._"
    line6 = "             .'  `.//SS$P^\"\"\"TS$$S. \"-.       \"-,"
    line7 = "           .'    _ \"-S^\"      TS$$Sb   \"-.       `."
    line8 = "         .'    .':S$Y      _.. SS$$Sb-'   \"-.      ;"
    line9 = "       .'    .'  SS$;,=-.  ._.`:S$$SS;       j     ;"
    line10 = "     .'    .'   :SS$$.-'        SS$$SS\     /     /"
    line11 = "   .'     /     SS$$S;    -     SS$$SS ;   /     /"
    line12 = " .'      /   ._dSS$$SS   .--.  :SS$$$S\;  /     /"
    line13 = "/       /     :SS$$SS$b. `--'  $$SS$$S ) /     /"
    line14 = "\      :      ;SS$$SS$$SS.___.'$$SS$$Sb /     /"
    line15 = " \      \"-.   SS$$SS$$$SS      $$SS$$SS';    /"
    line16 = "  `.       \"-dSS$$SS$$SS:;     :$$SSSP      /"
    line17 = "    `.              \"^S^':     '^TSS'      /"
    line18 = "      \"-.      `.     ::-.   _ .-\"\\      /"
    line19 = "         \"-.  -._\    ;;           \\\\  : :"
    line20 = "            \"-.   \  ::             \\\\ ; ;"
    line21 = "               $.  `.;;       ,      \\\\;:"
    line22 = "              dS$\  / '-._    :  _.-"" \;"
    line23 = "           `-:S$^$t'      \"\"--:\"\"       ;"
    line24 = "              TP :$$ ;        ::        :"
    line25 = "                d$S$_:        ;-\       ;"
    line26 = "               :$SS$; `.____.'   `.___.j"
    line27 = "               $$SS$$                  ;"
    line28 = "              / T$S$$;  ;      ;    ; :"
    line29 = "             :   `TS$$  :      :    : ;"
    line30 = "                   `T$         :     :"
    line31 = "                bug  ;         ;     ;"
    line32 = "                    /                ;"
    line33 = "                  .'                 :"
    line34 = "                 /      :           ;:"
    line35 = "                /       ;     c     ::"
    line36 = "               :`.      ;           : ;"
    line37 = "               ;  \"-.   :           ; :"
    line38 = "              :_     \"-.            .' ;"
    line39 = "              ; \"-.     \"\"--..__..-\"   :"
    line40 = "             :     `.                _.-;"
    line41 = "             ;       `.           .-\"   ;"
    line42 = "             ;         `.       .'      ;"
    line43 = "             ;           \     /        :"
    line44 = "             ;            \   /         :"
    line45 = "             ;             \_/          :"
    line46 = "             ;             ::           :"
    line47 = "             ;             :;           ;"
    line48 = "             :             :;           ;"
    line49 = "              ;            ;;          :"
    line50 = "              |            ;;          |"
    line51 = "              :           : ;          ;"
    line52 = "               ;          : ;         :"
    line53 = "               :          ; :         |"
    line54 = "                ;         ; :         ;"
    line55 = "                :         ; :        :"
    line56 = "                 ;        ; :        |"
    line57 = "                 :        ; :        ;"
    line58 = "                  ;       : :       :"
    line59 = "                  : ;   : :  ;  ;   |"
    line60 = "                   ;:   ; ;  :  :   :"
    line61 = "                   : \    ;   \      \"-."
    line62 = "                   :      ;    \        \\"
    line63 = "                   ;      :     \      .d$b"
    line64 = "                  db.___.d$b     \__.g$$$$$b"
    line65 = "                  $$$$$$$$$$     :$$$$$$$$$$b"
    line66 = "                  $$$$$$$$$$      T$$$$$$$$$$;"
    line67 = "                  :$$$$$$$$$       T$$$$$$$$$$"
    line68 = "                   $$$$$$$$$        `T$$$$$$$$b"
    line69 = "                   $$$$$$$$;          T$$$$$$$$;"
    line70 = "                   :$$$$$$$            T$$$$$$$$"
    line71 = "                   :$$$$$$$             T$$$$$$$;"
    line72 = "                    $$$$$$$              T$$$$$$$"
    line73 = "                    $$$$$$$               T$$$$$$;"
    line74 = "                    $$$$$$$                T$$$$$$"
    line75 = "                    :$$$$$;                 T$$$$$b"
    line76 = "                    :$$$$$;                  T$$$S$b."
    line77 = "                    :$$$$S;                   SSS$$$$bp."
    line78 = "                    :$$$$S;                   :S$$$$$S$$;"
    line79 = "                    $S$$SS;                    S$$$$$$SP"
    line80 = "                   :$SSSSS;                    :$$$$$$S"
    line81 = "                   $$$$$$$;                     $$$$$$$"
    line82 = "                   $$$$$$$$                     :$$SS$$"
    line83 = "                   $$$$$$$$                      SSS$$$"
    line84 = "                   $$$$$$$$                      :$$$$;"
    line85 = "                   :$$$$SS;                       `^^'"
    line86 = "                    TSSSSP"
    linelist = [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line28,line29,line30,line31,line32,line33,line34,line35,line36,line37,line38,line39,line40,line41,line42,line43,line44,line45,line46,line47,line48,line49,line50,line51,line52,line53,line54,line55,line56,line57,line58,line59,line60,line61,line62,line63,line64,line65,line66,line67,line68,line69,line70,line71,line72,line73,line74,line75,line76,line77,line78,line79,line80,line81,line82,line83,line84,line85,line86]
    for x in linelist:
        xchat.command("say "+x)
    return xchat.EAT_ALL
xchat.hook_command("BIKINI",bikini)

def shrek(word,word_eol,userdata):
    line1 = "                      _____"
    line2 = "                   ,-'     `._"
    line3 = "                 ,'           `.        ,-."
    line4 = "               ,'               \       ),.\\"
    line5 = "     ,.       /                  \     /(  \;"
    line6 = "    /'\\\\     ,o.        ,ooooo.   \  ,'  `-')"
    line7 = "    )) )`. d8P\"Y8.    ,8P\"\"\"\"\"Y8.  `'  .--\"'"
    line8 = "   (`-'   `Y'  `Y8    dP       `'     /"
    line9 = "    `----.(   __ `    ,' ,---.       ("
    line10 = "           ),--.`.   (  ;,---.        )"
    line11 = "          / \O_,' )   \  \O_,'        |"
    line12 = "         ;  `-- ,'       `---'        |"
    line13 = "         |    -'         `.           |"
    line14 = "        _;    ,            )          :"
    line15 = "     _.'|     `.:._   ,.::\" `..       |"
    line16 = "  --'   |   .'     \"\"\"         `      |`."
    line17 = "        |  :;      :   :     _.       |`.`.-'--."
    line18 = "        |  ' .     :   :__.,'|/       |  \\"
    line19 = "        `     \--.__.-'|_|_|-/        /   )"
    line20 = "         \     \_   `--^\"__,'        ,    |"
    line21 = "   -hrr- ;  `    `--^---'          ,'     |"
    line22 = "          \  `                    /      /"
    line23 = "           \   `    _ _          /"
    line24 = "            \           `       /"
    line25 = "             \           '    ,'"
    line26 = "              `.       ,   _,'"
    line27 = "                `-.___.---'"
    listline = [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27]
    for x in listline:
        xchat.command("say "+x)
    return xchat.EAT_ALL
xchat.hook_command("SHREK",shrek)

def nerd(word,word_eol,userdata):
    line1 = "    /)))))))))"
    line2 = "   //) __   __\\"
    line3 = "   C==/_o|^|o_\\"
    line4 = "   |      _\  )"
    line5 = "    \   .--- /"
    line6 = "   _/`-. __.'_"
    line7 = " /` \`'-,._./|\\"
    line8 = "/    \ /`\_/\/ \\"
    listline = [line1,line2,line3,line4,line5,line6,line7,line8]
    for x in listline:
        xchat.command("say "+x)
    return xchat.EAT_ALL
xchat.hook_command("NERD",nerd)

def gayaward(word,word_eol,userdata):
    line1 = chr(3)+"9,1        ___"
    line2 = chr(3)+"9,1       /\__\\"
    line3 = chr(3)+"9,1      / / _/_"
    line4 = chr(3)+"9,1     / / /\  \\"
    line5 = chr(3)+"9,1    / / /  \  \\"
    line6 = chr(3)+"9,1   / /__\/\ \__\\"
    line7 = chr(3)+"9,1   \ \  \ / /  /"
    line8 = chr(3)+"9,1    \ \  / /  /"
    line9 = chr(3)+"9,1     \ \/ /  /"
    line10 = chr(3)+"9,1      \  /  /"
    line11 = chr(3)+"9,1       \/__/"
    line12 = chr(3)+"9,1       |  \|"
    line13 = chr(3)+"9,1       |\  |"
    line14 = chr(3)+"9,1       | \ |"
    line15 = chr(3)+"9,1       )  \("
    line16 = chr(3)+"9,1       |\  |mga"
    line17 = chr(3)+"9,1 .-----'---'-----."
    line18 = chr(3)+"9,1 |'Your very own'|"
    line19 = chr(3)+"9,1 |G A Y A W A R D|"
    line20 = chr(3)+"9,1 |.   Wear it   .|"
    line21 = chr(3)+"9,1 ||   proudly   ||"
    line22 = chr(3)+"9,1 ||             ||"
    line23 = chr(3)+"9,1 ||__ May 1999 _||"
    line24 = chr(3)+"9,1 '---------------'"
    linelist = [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24]
    for x in linelist:
        xchat.command("say "+x)
    return xchat.EAT_ALL
xchat.hook_command("GAYAWARD",gayaward)

def thefrog(word,word_eol,userdata):
    line1 = chr(3)+"9,1_________█░░░░░░░░██_██░░░░░░█"
    line2 = chr(3)+"9,1________█░░░░░░░░░░░█░░░░░░░░░█"
    line3 = chr(3)+"9,1_______█░░░░░░░███░░░█░░░░░░░░░█"
    line4 = chr(3)+"9,1_______█░░░░███░░░███░█░░░████░█"
    line5 = chr(3)+"9,1______█░░░██░░░░░░░░███░██░░░░██"
    line6 = chr(3)+"9,1_____█░░░░░░░░░░░░░░░░░█░░░░░░░░███"
    line7 = chr(3)+"9,1____█░░░░░░░░░░░░░██████░░░░░████░░█"
    line8 = chr(3)+"9,1____█░░░░░░░░░█████░░░████░░██░░██░░█"
    line9 = chr(3)+"9,1___██░░░░░░░███░░░░░░░░░░█░░░░░░░░███"
    line10 = chr(3)+"9,1__█░░░░░░░░░░░░░░█████████░░█████████"
    line11 = chr(3)+"9,1_█░░░░░░░░░░█████_████___████_█████___█"
    line12 = chr(3)+"9,1_█░░░░░░░░░░█______█_███__█_____███_█___█"
    line13 = chr(3)+"9,1█░░░░░░░░░░░░█___████_████____██_██████"
    line14 = chr(3)+"9,1░░░░░░░░░░░░░█████████░░░████████░░░█"
    line15 = chr(3)+"9,1░░░░░░░░░░░░░░░░█░░░░░█░░░░░░░░░░░░█"
    line16 = chr(3)+"9,1░░░░░░░░░░░░░░░░░░░░██░░░░█░░░░░░██"
    line17 = chr(3)+"9,1░░░░░░░░░░░░░░░░░░██░░░░░░░███████"
    line18 = chr(3)+"9,1░░░░░░░░░░░░░░░░██░░░░░░░░░░█░░░░░█"
    line19 = chr(3)+"9,1░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█"
    line20 = chr(3)+"9,1░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█"
    line21 = chr(3)+"9,1░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█"
    line22 = chr(3)+"9,1░░░░░░░░░░░█████████░░░░░░░░░░░░░░██"
    line23 = chr(3)+"9,1░░░░░░░░░░█▒▒▒▒▒▒▒▒███████████████▒▒█"
    line24 = chr(3)+"9,1░░░░░░░░░█▒▒███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█"
    line25 = chr(3)+"9,1░░░░░░░░░█▒▒▒▒▒▒▒▒▒█████████████████"
    line26 = chr(3)+"9,1░░░░░░░░░░████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█"
    line27 = chr(3)+"9,1░░░░░░░░░░░░░░░░░░██████████████████"
    line28 = chr(3)+"9,1░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█"
    line29 = chr(3)+"9,1██░░░░░░░░░░░░░░░░░░░░░░░░░░░██"
    line30 = chr(3)+"9,1▓██░░░░░░░░░░░░░░░░░░░░░░░░██"
    line31 = chr(3)+"9,1▓▓▓███░░░░░░░░░░░░░░░░░░░░█"
    line32 = chr(3)+"9,1▓▓▓▓▓▓███░░░░░░░░░░░░░░░██"
    line33 = chr(3)+"9,1▓▓▓▓▓▓▓▓▓███████████████▓▓█"
    line34 = chr(3)+"9,1▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"
    listline = [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line28,line29,line30,line31,line32,line33,line34]
    for x in listline:
        xchat.command("say "+x)
    return xchat.EAT_ALL
xchat.hook_command("THEFROG",thefrog)

def shrug(word,word_eol,userdata):
    line1 = chr(3)+"9,1¯\_(ツ)_/¯"
    xchat.command("say "+line1)
    return xchat.EAT_ALL
xchat.hook_command("SHRUG",shrug)

print("Image script loaded")
