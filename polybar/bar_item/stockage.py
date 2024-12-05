import psutil
from tkinter import *
import time
diskInfo = psutil.disk_usage('/')
print(diskInfo)
total = f"- Total :           {diskInfo.total / (1024 ** 3):.2f} GB"
used = f"- Used :           {diskInfo.used / (1024 ** 3):.2f} GB"
free = f"- Free :           {diskInfo.free / (1024 ** 3):.2f} GB"
percent = f"- Percent :         {diskInfo.percent} %"
def stock():
    Total = Label(root, text=total,background='#888A85',fg='#000000',font=('tajawal',15,'bold'))
    Total.place(x=40,y=50) 
    Used = Label(root, text=used,background='#888A85',fg='#000000',font=('tajawal',15,'bold'))
    Used.place(x=40,y=80) 
    Free = Label(root, text=free,background='#888A85',fg='#000000',font=('tajawal',15,'bold'))
    Free.place(x=40,y=110) 
    Percent = Label(root, text=percent,background='#888A85',fg='#000000',font=('tajawal',15,'bold'))
    Percent.place(x=40,y=140)

root = Tk()
root.title('stockage')
root.minsize('400','190')
root.config(background='#888A85')
title = Label(root, text='stockage',background='#888A85',fg='#A40000',font=('tajawal',18,'bold'))
title.place(x=125,y=10)
stock()
# time.sleep(6)
# root.destroy()

root.mainloop()
