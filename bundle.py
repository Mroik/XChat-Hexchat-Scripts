import xchat
import time

__module_name__ = "Bundle"
__module_version__ = "1.1"
__module_description__ = "Bundle of commands"

flood_message = ""

def color_spam(word,word_eol,userdata):
	cspam_msg=""
	for x in range(30):
		if x%2==0:
			cspam_msg=cspam_msg+chr(3)+word[1]+","+word[2]+word_eol[3]
		else:
			cspam_msg=cspam_msg+chr(3)+word[2]+","+word[1]+word_eol[3]
	xchat.command("SAY "+cspam_msg)
	return xchat.EAT_ALL

def allctcp(word,word_eol,userdata):
	nicks = xchat.get_list("users")
	for x in nicks:
		xchat.command("CTCP "+x.nick+" "+word[1])
	return xchat.EAT_ALL

def flooding(userdata):
	if flood_message=="":
		return 0
	else:
		xchat.command("SAY "+flood_message)
		return 1

def flood_start(word,word_eol,userdata):
	global flood_message
	flood_message=word_eol[2]
	global myflooder
	print("Starting the flooder...")
	myflooder=xchat.hook_timer(int(float(word[1])*1000),flooding)
	return xchat.EAT_ALL

def flood_stop(word,word_eol,userdata):
	global flood_message
	flood_message=""
	print("Stopping the flooder...")
	return xchat.EAT_ALL

def hello(word,word_eol,userdata):
	nicks = xchat.get_list("users")
	for x in nicks:
		xchat.command("FAINA "+str(x.nick)+": "+word_eol[1])
	return xchat.EAT_ALL

def hello2(word,word_eol,userdata):
	saying=""
	nicks = xchat.get_list("users")
	for x in nicks:
		saying=saying+str(x.nick)+" "
	xchat.command("FAINA "+saying)
	return xchat.EAT_ALL

def what_time(word,word_eol,userdata):
	xchat.command("SAY It's "+str(time.localtime()[3])+":"+str(time.localtime()[4])+" GMT+2")
	return xchat.EAT_ALL

def msg_color(word,word_eol,userdata):
	msg_input=xchat.get_info('inputbox')
	if (word[0] == "65293") and (msg_input!=None) and (msg_input[0]!="/"): #65293 is the return key
		xchat.command("SAY "+chr(3)+"4,15 ✘✔✘ "+chr(3)+"9,1 "+msg_input+" "+chr(3)+"4,15 ✘✔✘ ")
		xchat.command("SETTEXT "+"")
		return xchat.EAT_XCHAT
	else:
		return

def not_msg_color(word,word_eol,userdata):
	xchat.unhook(color_hook)
	global color_hook
	color_hook="OFF"
	print("uncoloring")
	return xchat.EAT_ALL

def is_msg_color(word,word_eol,userdata):
	if color_hook=="OFF":
		global color_hook
		color_hook=xchat.hook_print("Key Press",msg_color)
		print("coloring")
		return xchat.EAT_ALL
	return

color_hook=xchat.hook_print("Key Press",msg_color) #notice that the coloring of the text is already enabled after loading the script
xchat.hook_command("CACTIVE",is_msg_color,help="enables coloring text before sending the message")
xchat.hook_command("DACTIVE",not_msg_color,help="turns off coloring of the text")
xchat.hook_command("PHRASE",hello,help="PHRASE <string>")
xchat.hook_command("HIGHLIGHT",hello2,help="hilights every user")
xchat.hook_command("FLOOD",flood_start,help = "FLOOD <seconds> <msg>")
xchat.hook_command("UNFLOOD",flood_stop)
xchat.hook_command("TIME",what_time) #quite useless, no one actually needs a command like this on a IRC client
xchat.hook_command("CTCPALL",allctcp,help="CTCPALL <command>")
xchat.hook_command("CSPAM",color_spam,help="CSPAM <color 1> <color 2> string to spam")

print("bundle script loaded")
