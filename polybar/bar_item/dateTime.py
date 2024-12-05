from tkinter import *
from tkinter.ttk import *
from time import strftime
import datetime

root = Tk()
root.title("degital clock ")
root.config(bg='#888A85')
root.minsize('400','190')

# fonc for import time
def timedate ():
    realTime = strftime('%H: %M: %S')
    degits.config(text=realTime)
    degits.after(100, timedate)
    date = datetime.date.today()
    datE.config(text=date)



degits = Label(root,background='#888A85',foreground='#000000',font=("ds-digita",30,"bold"))
degits.place(x=40,y=50)
datE = Label(root,background='#888A85',foreground='#000000',font=("ds-digita",30,"bold"))
datE.place(x=40,y=90)
# not configured yet 
timeZone = Label(root,text="agadir",background='#888A85',foreground='#000000',font=("ds-digita",12,"bold"))
timeZone.place(x=270,y=70)

timedate()


# colorchooser.askcolor()

root.mainloop()



