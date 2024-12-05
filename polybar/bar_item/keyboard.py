import subprocess
from tkinter import *

def key(layoat):
    command = f'setxkbmap {layoat}'
    title.configure(text=layoat)
    title.place(x=170,y=10)
    subprocess.run(command, shell=True)
def eng():
    key('us')
def ara():
    key('ar')
def xmod():
    subprocess.run('xmodmap $HOME/.config/xmodmap/xmodmap', shell=True)
    title.configure(text='xmodmap')
    title.place(x=125,y=10)
root = Tk()    

root.title("degital clock ")
root.config(bg='#888A85')
root.minsize('400','190')

title = Label(root,background='#888A85',fg='#A40000',font=('tajawal',18,'bold'))

us = Button(root,text='us',background='#8AE234',fg='#A40000',font=('tajawal',18,'bold'),command=eng)
us.place(x=60,y=120)
ar = Button(root,text='ar',background='#8AE234',fg='#A40000',font=('tajawal',18,'bold'),command=ara)
ar.place(x=160,y=120)
xmodmap = Button(root,text='xmod',background='#8AE234',fg='#A40000',font=('tajawal',18,'bold'),command=xmod)
xmodmap.place(x=250,y=120)
root.mainloop()