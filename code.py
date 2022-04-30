# commencer le code ici
import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(bg="black", borderwidth=0, highlightthickness=0, width=1000, height=600)
c = 0
def simulation():
    a = int(input("Combien de boules ?"))
    
    for i in range (a):
        quinaire = canvas.create_oval(i*50, 0, i*50+50, 50, fill="blue")
        unaire1 = canvas.create_oval(i*50, 650, i*50+50, 700, fill="blue")
        unaire2 = canvas.create_oval(i*50, 600, i*50+50, 650, fill="blue")
        unaire3 = canvas.create_oval(i*50, 550, i*50+50, 600, fill="blue")
        unaire4 = canvas.create_oval(i*50, 500, i*50+50, 550, fill="blue")
        ligne = canvas.create_line(25+50*i, 0,25+50*i, 700, width=2, fill ="blue")
    ligne = canvas.create_line(0, 150, 1000, 150, width=7, fill="blue")

    def click_quinaire(event):
        global c
        if c == 0:
            canvas.itemconfig(quinaire, fill="red")
            canvas.move(quinaire, 0, 97)
            canvas.itemconfig(quinaire, fill="red")
            c = 1
        elif c == 1:
            canvas.itemconfig(quinaire, fill="red")
            canvas.move(quinaire, 0, -97)
            canvas.itemconfig(quinaire, fill="blue")
            c = 0

    canvas.bind('<Button-1>', click_quinaire)


bouton1 = tk.Button(text="Mode simulation", command = simulation)
bouton2 = tk.Button(text="Mode opération")
canvas.grid()
bouton1.grid()
bouton2.grid()

racine.mainloop() # Lancement de la boucle principale
