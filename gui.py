from filosofos_beta import *
from tkinter import *

root = Tk()
root.title("La cena de los filósofos")
root.resizable(1,1)
root.config(bg="white")
root.config(bd=0)

fondo = Canvas(width=500, height=500, bg="white")
fondo.pack()

f1 = fondo.create_rectangle(200, 100, 300, 130, fill="white", outline="black")
f1text = fondo.create_text(250, 115, text="Filósofo 1", font=("Arial", 10))

f2 = fondo.create_rectangle(320, 170, 420, 200, fill="white", outline="black")
f2text = fondo.create_text(370, 185, text="Filósofo 2", font=("Arial", 10))

f3 = fondo.create_rectangle(280, 260, 380, 290, fill="white", outline="black")
f3text = fondo.create_text(330, 275, text="Filósofo 3", font=("Arial", 10))

f4 = fondo.create_rectangle(140, 260, 220, 290, fill="white", outline="black")
f4text = fondo.create_text(190, 275, text="Filósofo 4", font=("Arial", 10))

f5 = fondo.create_rectangle(80, 170, 180, 200, fill="white", outline="black")
f5text = fondo.create_text(130, 185, text="Filósofo 5", font=("Arial", 10))

leyenda = fondo.create_text(350, 100, text="Leyenda", font=("Arial", 10))


root.mainloop()