from filosofos_beta import *
from tkinter import *



root = Tk()
root.title("La cena de los filósofos")
root.resizable(1,1)
root.config(bg="white")
root.config(bd=0)

fondo = Canvas(width=500, height=500, bg="white")
fondo.pack()
fil1 = filosofo("white")
fil2 = filosofo("white")
fil3 = filosofo("white")
fil4 = filosofo("white")
fil5 = filosofo("white")

f1 = fondo.create_rectangle(200, 100, 300, 130, fill=fil1.color, outline="black")
f1text = fondo.create_text(250, 115, text="Filósofo 1", font=("Arial", 10))

f2 = fondo.create_rectangle(320, 170, 420, 200, fill=fil2.color, outline="black")
f2text = fondo.create_text(370, 185, text="Filósofo 2", font=("Arial", 10))

f3 = fondo.create_rectangle(280, 260, 380, 290, fill=fil3.color, outline="black")
f3text = fondo.create_text(330, 275, text="Filósofo 3", font=("Arial", 10))

f4 = fondo.create_rectangle(140, 260, 220, 290, fill=fil4.color, outline="black")
f4text = fondo.create_text(190, 275, text="Filósofo 4", font=("Arial", 10))

f5 = fondo.create_rectangle(80, 170, 180, 200, fill=fil5.color, outline="black")
f5text = fondo.create_text(130, 185, text="Filósofo 5", font=("Arial", 10))


root.mainloop()