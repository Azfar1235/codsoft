import datetime

Time = datetime.datetime.now()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("hi good Morning !")

    elif hour>=12 and hour<15:
        return("hi good afternoon !")
    
    else:
        return("hi good Evening!")

while True:
    print("USER : ",end="")
    query = input()
    print("CHATBOT : ",end="")
    if "hello" in query or "hi" in query:
        print(wishme())
        print("\thow can i help you mate")
    elif "your name" in query or "who are you" in query:
        print("Hi, I am Trevor, a ChatBot")
        print("\tHow can I help you mate")
    elif "time now" in query:
        print("the time is : ",Time)
    elif "bye" in query:
        print("Ok, mate see you soon")
    else:
        print("sorry I didn't get that")