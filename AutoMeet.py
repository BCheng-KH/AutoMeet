import time, webbrowser
import pyautogui as pag

f = open("MeetInfo.txt", "r")
text = f.read()
f.close()

info = eval(text)

acted = False

before = False



def conMeet(info):
    for i in range(info["tries"]):
        if i != 0:
            time.sleep(info["delay"]*60)
        webbrowser.open(info["link"])
        time.sleep(10)
        if info["mute"]:
            pag.hotkey('ctrl', 'd')
        time.sleep(5)
        if info["camOff"]:
            pag.hotkey('ctrl', 'e')
        time.sleep(5)
        pag.click(x=int(pag.size()[0]*(info["x"])), y=int(pag.size()[1]*(info["y"])))
    return

def main(info, acted, before):
    
    while True:
        time.sleep(5)
        #print(time.localtime()[4] < info["min"])
        if not before and (time.localtime()[3] < info["hour"] or (time.localtime()[3] == info["hour"] and time.localtime()[4] < info["min"])):
            before = True
            print(before)
            if info["repeat"]:
                acted = False
        if (before and not acted) and ((time.localtime()[3] == info["hour"] and time.localtime()[4] >= info["min"]) or time.localtime()[3] > info["hour"]):
            print("connect")
            conMeet(info)
            
            acted = True
            before = False
            if not info["repeat"]:
                break
            

print("started")
main(info, acted, before)
