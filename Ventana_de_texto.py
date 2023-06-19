Import tkinter
#Ventana
#Crea una ventana

Ventana = Tkinter.Tk()

Ventana.Tittle("Hola")
Ventana.geometry("500x250")

#no deja abrir la ventana
ventana.resizable(0,0)

#crea un label
mensaje = tkinter.Label(ventana, text="Hola").pack()

#sirve para que se muestre la ventana
ventana.mainloop()

