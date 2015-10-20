import Skype4Py

skype = Skype4Py.Skype()
skype.Attach()

def onMsg(msg, status):
  if status == Skype4Py.cmsReceived:
    msg.Chat.SendMessage(msg.Body)
    print(msg.Body)


skype.RegisterEventHandler('MessageStatus', onMsg)
while 1: pass
