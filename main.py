import gtts as TTS
import tkinter as tk
root = tk.Tk()
root.title("Text To Speech")
canvas = tk.Canvas(root,width=400,height=300)
canvas.pack()

ggtReverse = dict()
LangSupport = TTS.langs._main_langs()
langList = LangSupport.copy().values()
for langs in LangSupport.copy().keys():
    ggtReverse[LangSupport.copy()[langs]] = langs

#print(ggtReverse)
#print(langList)

#print(TTS.lang)
def CTTS():
    word = EntryText.get()
    LangGetGet = ggtReverse[LangGet.get()]
    output = TTS.gTTS(text=word,lang=LangGetGet,slow=False)
    output.save("TTS.mp3")


app_text = tk.Label(text="Text To Speech",font=('Arial',20,'bold'))
canvas.create_window(200,100,window=app_text)

EntryText=tk.Entry()
canvas.create_window(200,180,window=EntryText)

LangGet = tk.StringVar()
LangGet.set("English")
Languagues = tk.OptionMenu(root,LangGet,*langList)
canvas.create_window(200,230,window=Languagues)

TTSButton=tk.Button(text="Change Text To Speech",command=CTTS)
canvas.create_window(200,280,window=TTSButton)

root.mainloop()
