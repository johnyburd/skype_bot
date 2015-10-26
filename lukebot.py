#lukebot.py
import pickle,random
def generate_response(msg):
    a=open('lexicon-luke','rb')
    successorlist=pickle.load(a)
    a.close()
    def nextword(a):
        if a in successorlist:
            return random.choice(successorlist[a])
        else:
            return 'the'
    #speech='':
    speech=msg
    while 1:
        s=random.choice(speech.split())
        if len(s) > 3 and s != "jonbot":
            break
    response=''
    while True:
        neword=nextword(s)
        response+=' '+neword
        s=neword
        if neword[-1] in '?!.':
            break
    return response
