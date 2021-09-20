from tkinter import *
from tkinter import filedialog
from pygame import mixer

class Music:
    def __init__(self,root):
        root.resizable(0,0)
        root.title("Music Player")
        root.iconbitmap("Music Icon.ico")
        root.geometry('500x500')
        Button(root,text='LOAD',command=self.Load).place(relx=0.02,rely=0.02)
        Button(root,text='PLAY',command=self.play).place(relx=0.1,rely=0.02)
        Button(root,text='PAUSE',command=self.pause).place(relx=0.2,rely=0.02)
        Button(root,text='<').place(relx=0.3,rely=0.02)
        Button(root,text='>',command=next).place(relx=0.4,rely=0.02)
        # Button(root,text='+').place(relx=0.5,rely=0.02)
        # playlist = LabelFrame(self.root,text="Song Track",fg="#7D3C98").place(x=0,y=0,width=500,height=100)
        # song=Label(playlist,textvariable=self.song,fg="green").grid(row=0,column=0,padx=10,pady=5)
        self.song=False

    def Load(self):
        self.song=filedialog.askopenfilename()

    def play(self):
        if self.song:
            mixer.init()
            mixer.music.load(self.song)
            mixer.music.play()

    def pause(self):
        mixer.music.fadeout(1)

root =Tk()
run=Music(root)
root.mainloop()