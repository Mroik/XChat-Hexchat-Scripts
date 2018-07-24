import xchat
import time

__module_name__ = "Bundle"
__module_version__ = "1.2"
__module_description__ = "Bundle of commands"

flood_message = ""
flood_context= []
join_flood_e = -1
join_flood_time = 0

def join_flood(word,word_eol,userdata):
	global join_flood_e
	global join_flood_time
	join_flood_e = join_flood_e + 1
	if join_flood_e==1:
		join_flood_time = time.localtime()[4]*60+time.localtime()[5]
	if join_flood_e>3:
		if (time.localtime()[4]*60+time.localtime()[5])-join_flood_time<10:
			xchat.command("QUIT")
		join_flood_time = 0
		join_flood_e = 0
	return xchat.EAT_NONE

def join_flood_en(word,word_eol,userdata):
	global join_flood_hook
	global join_flood_e
	if join_flood_e==-1:
		join_flood_e = 0
		join_flood_hook = xchat.hook_print("You Join",join_flood)
		print("Join flood enabled")
	return xchat.EAT_ALL

def join_flood_dis(word,word_eol,userdata):
	global join_flood_e
	global join_flood_time
	if join_flood_e>-1:
		join_flood_e = -1
		join_flood_time = 0
		xchat.unhook(join_flood_hook)
		print("Join flood disabled")
	return xchat.EAT_ALL

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
                for x in flood_context:
                        x.command("SAY "+flood_message)
		return 1

def flood_start(word,word_eol,userdata):
	global flood_message
	flood_message=word_eol[2]
	global myflooder
	global flood_context
	flood_context = flood_context+[xchat.get_context()]
	print("Starting the flooder...")
	if len(flood_context) == 1:
                myflooder=xchat.hook_timer(int(float(word[1])*1000),flooding)
	return xchat.EAT_ALL

def flood_stop(word,word_eol,userdata):
        global flood_context
        flood_context=[]
	global flood_message
	flood_message=""
	print("Stopping the flooder...")
	return xchat.EAT_ALL

def hello(word,word_eol,userdata):
	nicks = xchat.get_list("users")
	if color_hook != "OFF":
		for x in nicks:
			xchat.command("FAINA "+str(x.nick)+": "+word_eol[1])
	else:
		for x in nicks:
			xchat.command("SAY "+str(x.nick)+": "+word_eol[1])
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
	if (word[0] == "65293") and (msg_input!=""): #65293 is the return key
		if msg_input[0]!="/":
			xchat.command("SAY "+chr(3)+"4,15 ✘✔✘ "+chr(3)+"9,1 "+msg_input+" "+chr(3)+"4,15 ✘✔✘ ")
			xchat.command("SETTEXT "+"")
			return xchat.EAT_XCHAT
	else:
		return

def not_msg_color(word,word_eol,userdata):
	global color_hook
	xchat.unhook(color_hook)
	color_hook="OFF"
	print("uncoloring")
	return xchat.EAT_ALL

def is_msg_color(word,word_eol,userdata):
	global color_hook
	if color_hook=="OFF":
		color_hook=xchat.hook_print("Key Press",msg_color)
		print("coloring")
		return xchat.EAT_ALL
	return xchat.EAT_ALL

xchat.hook_command("JOINFE",join_flood_en,help="Enables join flood")
xchat.hook_command("JOINFD",join_flood_dis,help="Disables join flood")
#color_hook=xchat.hook_print("Key Press",msg_color) uncomment to enable coloring on load
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
