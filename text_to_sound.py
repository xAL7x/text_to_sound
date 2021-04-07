import os
os.system("pip install gtts")
os.system("pip install pyfiglet")
os.system("cls")
import pyfiglet
sound = pyfiglet.figlet_format("text -> sound")
print(sound)
print("------- created by alhassanAlharb7 -------")
from gtts import gTTS

print("read file [1] input text [2]")
ask=input("choose the options: ")

if ask=="1":
    print("""\033[0;31m
             ______________________________________
            | language example: Arabic=ar          |
            | English=en ,, Spanish=es             |
            | French=fr                            |
            |                                      |
            |______________________________________|
            
            """)
    
    file=open(input("enter the file name :"),"r")
    language=input("enter the language: ")
    read=file.read()
    tts=gTTS(read,lang=language)
    a="sound"
    tts.save(a+'.mp3')#لحفظه كمقطع صوتي
    #os.system(a+".mp3")# لتشغيل المقطع الصوتي
elif ask=="2":
    print("""\033[0;31m
             ______________________________________
            | language example: Arabic=ar          |
            | English=en ,, Spanish=es             |
            | French=fr                            |
            |                                      |
            |______________________________________|
            
            """)
    tts=gTTS(input("\033[0;34menter the text : "),lang=input("enter the languge --> "))
    a="sound"
    tts.save(a+'.mp3')#لحفظه كمقطع صوتي
    #os.system(a+".mp3")# لتشغيل المقطع الصوتي