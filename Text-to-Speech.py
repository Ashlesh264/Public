from tkinter import *
from tkinter import ttk,messagebox
from gtts import gTTS
from playsound import playsound

def Text_to_speech():
    global replay
    try:
        FileName = entry_field1.get()+'.mp3'
        Message = entry_field2.get('1.0', 'end')
        speech = gTTS(text = Message)
        speech.save(FileName)
        playsound(FileName)
        replay = Button(root, text = "REPLAY", font = 'arial 15 bold' , command = Replay, bg = 'blue', fg = 'white')
        replay.place(x=25,y=340)
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        print(e)
        messagebox.showerror("Error", e)

def Replay():
    try:
        FileName = entry_field1.get()+'.mp3'
        playsound(FileName)
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        print(e)
        messagebox.showerror("Error", e)

def Exit():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

def Reset():
    global replay
    fn.set("")
    entry_field2.delete('1.0', 'end')
    replay.destroy()

root = Tk()
root.minsize(540,500)
root.maxsize(540,500)
background_image = PhotoImage(file="TTS.png")
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
root.title("TEXT TO SPEECH")
root.iconbitmap("Text-to-Speech.ico")

Label(root, text = "TEXT TO SPEECH", font = "algerian 20 bold", bg = 'white smoke').pack()

Label(root,text ="Enter File Name", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=70)
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=160)
root.wm_attributes('-transparentcolor', root['bg'])
fn = StringVar()
entry_field1 = Entry(root, textvariable = fn)
entry_field1.place(x=20,y=110)
entry_field2 = Text(root, wrap=WORD, height=6, width=60)
entry_field2.place(x=20,y=200)

Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech, bg = 'green', fg = 'white').place(x=25,y=340)

Button(root, text = 'EXIT', font = 'arial 15 bold', command = Exit, bg = 'red', fg = 'white').place(x=140,y=340)

Button(root, text = 'RESET', font = 'arial 15 bold', command = Reset, bg = 'orange', fg = 'white').place(x=240,y=340)

root.mainloop()