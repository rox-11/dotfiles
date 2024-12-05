
import psutil 
from tkinter import ttk
from tkinter import *

# varaibles
batPercent = int(psutil.sensors_battery().percent)
batplug = psutil.sensors_battery().power_plugged

# bat main fonction
def bat():

    persent = Label(partOne,text=f"{batPercent} %", fg='#000000',font=('tajawal',15,'bold'))
    persent.place(x=80,y=120,width='100')

    if batPercent >=90 :
        etat30 = Label(partOne,width='4',height='5',background='#000000')
        etat30.place(x=90,y=20)
        etat45 = Label(partOne,width='4',height='5',background='#000000')
        etat45.place(x=130,y=20)
        etat65 = Label(partOne,width='4',height='5',background='#000000')
        etat65.place(x=170,y=20)
        etat75 = Label(partOne,width='4',height='5',background='#000000')
        etat75.place(x=210,y=20)
        etat85 = Label(partOne,width='4',height='3',background='#000000')
        etat85.place(x=250,y=38)
        persent.configure(background="#4E9A06")

    elif batPercent >=70 and batPercent <= 89:
        etat30 = Label(partOne,width='4',height='5',background='#000000')
        etat30.place(x=90,y=20)
        etat45 = Label(partOne,width='4',height='5',background='#000000')
        etat45.place(x=130,y=20)
        etat65 = Label(partOne,width='4',height='5',background='#000000')
        etat65.place(x=170,y=20)
        etat75 = Label(partOne,width='4',height='5',background='#000000')
        etat75.place(x=210,y=20)
        etat85 = Label(partOne,width='4',height='3',background='#BABDB6')
        etat85.place(x=250,y=38)
        persent.configure(background="#8AE234")
    elif batPercent >=50 and batPercent <= 69:
        etat30 = Label(partOne,width='4',height='5',background='#000000')
        etat30.place(x=90,y=20)
        etat45 = Label(partOne,width='4',height='5',background='#000000')
        etat45.place(x=130,y=20)
        etat65 = Label(partOne,width='4',height='5',background='#000000')
        etat65.place(x=170,y=20)
        etat75 = Label(partOne,width='4',height='5',background='#BABDB6')
        etat75.place(x=210,y=20)
        etat85 = Label(partOne,width='4',height='3',background='#BABDB6')
        etat85.place(x=250,y=38)
        persent.configure(background="#C4A000")

    elif batPercent >=30 and batPercent <= 49:
        etat30 = Label(partOne,width='4',height='5',background='#000000')
        etat30.place(x=90,y=20)
        etat45 = Label(partOne,width='4',height='5',background='#000000')
        etat45.place(x=130,y=20)
        etat65 = Label(partOne,width='4',height='5',background='#BABDB6')
        etat65.place(x=170,y=20)
        etat75 = Label(partOne,width='4',height='5',background='#BABDB6')
        etat75.place(x=210,y=20)
        etat85 = Label(partOne,width='4',height='3',background='#BABDB6')
        etat85.place(x=250,y=38)
        persent.configure(background="#FCAF3E")
    elif batPercent >=1 and batPercent <= 29:
        etat30 = Label(partOne,width='4',height='5',background='#000000')
        etat30.place(x=90,y=20)
        etat45 = Label(partOne,width='4',height='5',background='#BABDB6')
        etat45.place(x=130,y=20)
        etat65 = Label(partOne,width='4',height='5',background='#BABDB6')
        etat65.place(x=170,y=20)
        etat75 = Label(partOne,width='4',height='5',background='#BABDB6')
        etat75.place(x=210,y=20)
        etat85 = Label(partOne,width='4',height='3',background='#BABDB6')
        etat85.place(x=250,y=38)
        persent.configure(background="#A40000")
    else:
        print("Error")

    # plug state
    plugstate = Label(partOne,fg='#000000',font=('tajawal',15,'bold'))
    plugstate.place(x=200,y=120,width='110')
    if batplug == True:
        plugstate.configure(text='pluged',background='#4E9A06')
    else:
        plugstate.configure(text='unpluged',background='#A40000') 
         
     
root = Tk()
root.title('battery')
root.minsize('400','190')
root.config(background='#888A85')

# Frame                      
partOne = Frame(root,width='400',height='180',background='#888A85')
partOne.place(x=0,y=0)

bat()
root.mainloop()

