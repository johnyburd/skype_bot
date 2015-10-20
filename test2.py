def sendGroupChatMessage(topic):
    """
    Send Group Chat Messages.
    """
    import Skype4Py as skype
    skypeClient = skype.Skype()
    skypeClient.Attach()
    messageSent = False
    print (topic)
    for elem in skypeClient.ActiveChats:
        print (elem)
        print (len(elem._GetMembers()))
        if len(elem._GetMembers()) == 2 and elem.Topic == topic:
            elem.SendMessage("testmessage")
            messageSent = True

    if not messageSent:
        for chat in skypeClient.BookmarkedChats:
            if chat.Topic == topic:
                chat.SendMessage("testmessage")
                messageSent = True

    return messageSent
print(sendGroupChatMessage("The Chat"))
