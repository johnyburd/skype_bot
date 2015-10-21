import Skype4Py
import time
import re
import random
import lukebot
import os

skype = Skype4Py.Skype()
skype.Attach()
chat = skype.Chat("#johnyburd/$7f326bf4d6d018d5") #johnyburd
#chat = skype.Chat("#johnyburd/$b5b2fea895ecb6f9") #public
senders = ["my","hands","are typing words"]

for m in chat.Members:
    print(m)

def reply(msg, sender):
    reply = 0
    if re.match(r'(hello|hi|salutations|greetings) jonbot', msg, re.I):
        reply = "hi, "+sender+"!"
    elif re.match(r'(jonbot )?(you\'re|your|youre|you are) .*(jonbot)?', msg, re.I):
        use_name =random.randint(1,2)

        if re.match(r'jonbot (you\'re|your|youre|you are) .*', msg, re.I):
            phrase = re.search('(jonbot (you\'re|your|youre|you are)) (.*)', msg, re.I)
            phrase = phrase.group(3)

            if use_name == 1:
                reply = "you're "+phrase+" too!"
            else:
                reply = "you're "+phrase+" too, "+sender+"!"

        if re.match(r'(you\'re|your|youre|you are) .* jonbot', msg, re.I):
            print("you're ... jonbot")
            phrase = re.match(r'(you\'re|your|youre|you are) (.*) jonbot', msg, re.I)
            phrase = phrase.group(2)

            if use_name == 1:
                reply = "you're "+phrase+" too!"
            else:
                reply = "you're "+phrase+" too, "+sender+"!"
        else:
            print("false alarm")

    elif msg == "!quit":
        if sender == "johnyburd":
            chat.SendMessage("Okay Bye :'(")
            os._exit(0)
        else:
            reply = "you're not the boss of me!"

    elif msg == "!refresh":
            os.system("rm ~/code/python/skype_bot/lexicon-luke")
            os.system("python2 ~/code/python/skype_bot/trainer.py")
            reply = "re-trained."

    else:
        if re.match('.*jonbot.*', msg, re.I):
            reply = lukebot.generate_response(msg)
        else:
            if senders[0]==senders[1] and senders[1]==senders[2] and senders[2]==senders[3]:
                reply = lukebot.generate_response(msg)
            else:
                if random.randint(1,10)==1:
                    reply = lukebot.generate_response(msg)
    if reply !=0:
        chat.SendMessage(reply)
        reply = 0

def save_msg(msg, sender):
    if re.match(r'spygreen_oo', sender, re.I):
        print(sender+" said: "+msg+" >> train.txt")
        text = open("train.txt", "a")
        text.write(msg+"\n")
        text.close()

def on_message_status(message, status):
    #chat = message.Chat
    sender = message.Sender.Handle

    if 1:
        if status == "RECEIVED":

            chat = message.ChatName
            print("chat = "+chat)

            if message.Type == "SAID":
                #print(skype.ActiveChats)
                #chat.SendMessage("this is a test")
                print(message.Chat)
                for line in message.Body.split('\n'):

                    print(sender+": "+line)
                    save_msg(line, sender)
                    reply(line, sender)
                    senders.insert(0,sender)
                    del senders[3]
                    print(senders)

            elif message.Type == "EMOTED":
                print("idk")
            elif message.Type == "SETTOPIC":
                print("idk")
        else:
            print(message, status)
            #message.MarkAsSeen()
skype.OnMessageStatus = on_message_status


while 1:
    time.sleep(1)
 #   skype.RegisterEventHandler('MessageStatus', on_message_status)
