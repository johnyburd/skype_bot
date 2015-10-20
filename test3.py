import Skype4Py
import time
import re

skype = Skype4Py.Skype()
skype.Attach()
chat = skype.Chat("#johnyburd/$jonbot66;620ceca73ef48d0e") #johnyburd
#chat = skype.Chat("#johnyburd/$b5b2fea895ecb6f9") #public

for m in chat.Members:
    print(m)

def reply(msg, sender):
    if msg == "hello jonbot" or msg == "Hello jonbot":
        reply = "hi, "+sender+"!"
    elif msg == "jonbot quit":
        chat.SendMessage("Okay Bye :'(")
        exit()
    else:
        return
    chat.SendMessage(reply)

def on_message_status(message, status):
    #chat = message.Chat
    sender = message.Sender.Handle

    if 1:
        if status == "RECEIVED":
            if message.Type == "SAID":
                #print(skype.ActiveChats)
                #chat.SendMessage("this is a test")
                message.MarkAsSeen()
                for line in message.Body.split('\n'):
                    print(line)
                    reply(line, sender)
            elif message.Type == "EMOTED":
                print("idk")
            elif message.Type == "SETTOPIC":
                print("idk")
        else:
            print(message, status)
skype.OnMessageStatus = on_message_status


while 1:
    time.sleep(1)
 #   skype.RegisterEventHandler('MessageStatus', on_message_status)
