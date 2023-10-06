import tkinter as tk
from time import strftime

def update_time():
    myClock['text'] = strftime('%H:%M:%S')
    myClock.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock using Python")

myClock = tk.Label(root, font='Tahoma 150 bold', fg='white', bg='#af25f0')
myClock.pack()

update_time()

root.mainloop()
