import tkinter as tk
import sys 

racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(bg = "black", highlightbackground = "blue", highlightthickness = 10, width = 1000, height = 700)
all_list = []

def error_handler(boulenb):
    if boulenb < 1 or boulenb > 20:
        racine.destroy()
        sys.exit(84)

def simulation() -> None:
    global all_list
    a: int = int(input("Combien de boules ?\n"))
    error_handler(a)

    for i in range (a):
        boules_list = []
        # création des différentes boules
        quinaire = canvas.create_oval(10 + i * 50, 10, i * 50 + 60, 60, fill = "blue")
        unaire1 = canvas.create_oval(10 + i * 50, 510, i * 50 + 60, 560, fill = "blue")
        unaire2 = canvas.create_oval(10 + i * 50, 560, i * 50 + 60, 610, fill = "blue")
        unaire3 = canvas.create_oval(10 + i * 50, 610, i * 50 + 60, 660, fill = "blue")
        unaire4 = canvas.create_oval(10 + i * 50, 660, i * 50 + 60, 710, fill = "blue")
        
        # ajout des boules dans la liste boules_list
        boules_list.append(quinaire) #i[0]
        boules_list.append(unaire1) #1
        boules_list.append(unaire2) #2
        boules_list.append(unaire3) #3
        boules_list.append(unaire4) #4
        
        # ajouter la liste boules_list dans la liste globale 
        all_list.append(boules_list)
        canvas.create_line(35 + 50 * i, 10, 35 + 50 * i, 710, width = 2, fill = "blue")
        
    canvas.create_line(0, 150, 1100, 150, width = 5, fill = "blue")

    def hover_style(event) -> None: #colorie les boules lorsque le curseur passe dessus (juste du style)
        x, y = event.x, event.y
        
        for i in all_list:
            quinaire = i[0]
            unaire1 = i[1]
            unaire2 = i[2]
            unaire3 = i[3]
            unaire4 = i[4]
            coords = canvas.coords(quinaire)
            u1_cords = canvas.coords(unaire1)
            u2_cords = canvas.coords(unaire2)
            u3_cords = canvas.coords(unaire3)
            u4_cords = canvas.coords(unaire4)

            if (x >= coords[0] and x <= coords[2] and y >= coords[1] and y <= coords[3]):
                canvas.itemconfig(quinaire, fill = "red")
            else:
                canvas.itemconfig(quinaire, fill = "blue")
            
            if (x >= u1_cords[0] and x <= u1_cords[2] and y >= u1_cords[1] and y <= u1_cords[3]):
                canvas.itemconfig(unaire1, fill = "yellow")
            else:
                canvas.itemconfig(unaire1, fill = "blue")
            
            if (x >= u2_cords[0] and x <= u2_cords[2] and y >= u2_cords[1] and y <= u2_cords[3]):
                canvas.itemconfig(unaire2, fill = "yellow")
            else:
                canvas.itemconfig(unaire2, fill = "blue")
                
            if (x >= u3_cords[0] and x <= u3_cords[2] and y >= u3_cords[1] and y <= u3_cords[3]):
                canvas.itemconfig(unaire3, fill = "yellow")
            else:
                canvas.itemconfig(unaire3, fill = "blue")
                
            if (x >= u4_cords[0] and x <= u4_cords[2] and y >= u4_cords[1] and y <= u4_cords[3]):
                canvas.itemconfig(unaire4, fill = "yellow")
            else:
                canvas.itemconfig(unaire4, fill = "blue")
    
    def click_boules(event) -> None: #définit les actions des boules lorsque l'on clique dessus
        x, y = event.x, event.y
        
        for i in all_list:
    
            j = 1
            quinaire = i[0]
            unaire1 = i[1]
            unaire2 = i[2]
            unaire3 = i[3]
            unaire4 = i[4]
            # ...
            coords = canvas.coords(quinaire)
            u1_cords = canvas.coords(unaire1)
            u2_cords = canvas.coords(unaire2)
            u3_cords = canvas.coords(unaire3)
            u4_cords = canvas.coords(unaire4)
            # ...
            ######################################################################################## déplacement de la quinaire
            
            if (x >= coords[0] and x <= coords[2] and y >= coords[1] and y <= coords[3]):
                if (coords[3] == 150):
                    j = -1
                canvas.move(i[0], 0, j * 90)
                
            ######################################################################################## déplacement de l'unaire 1
            
            elif (x >= u1_cords[0] and x <= u1_cords[2] and y >= u1_cords[1] and y <= u1_cords[3]):
                if (u1_cords[1] == 150):
                    j = -1
                    if u2_cords[1] == 200:
                        canvas.move(i[2], 0, j * -360)
                        if u3_cords[1] == 250:
                            canvas.move(i[3], 0, j * -360)
                            if u4_cords[1] == 300:
                                canvas.move(i[4], 0, j * -360)
                canvas.move(i[1], 0, j * -360)
                
            ######################################################################################## déplacement de l'unaire 2       
           
            elif (x >= u2_cords[0] and x <= u2_cords[2] and y >= u2_cords[1] and y <= u2_cords[3]):
                if u1_cords[1] != 150:
                    canvas.move(i[1],0,j * -360)
                if (u2_cords[1] == 200):
                    j = -1
                    if u3_cords[1] == 250:
                            canvas.move(i[3], 0, j * -360)
                            if u4_cords[1] == 300:
                                canvas.move(i[4], 0, j * -360)
                canvas.move(i[2], 0, j * -360)
                
             ######################################################################################## déplacement de l'unaire 3   
            
            elif (x >= u3_cords[0] and x <= u3_cords[2] and y >= u3_cords[1] and y <= u3_cords[3]):
                if u2_cords[1] != 200:
                    canvas.move(i[2],0,j * -360)
                    if u1_cords[1] != 150:
                        canvas.move(i[1], 0, j * -360)
                if (u3_cords[1] == 250):
                    j = -1
                    if u4_cords[1] == 300:
                        canvas.move(i[4], 0, j * -360)
                canvas.move(i[3], 0, j * -360)
                
            ######################################################################################## déplacement de l'unaire 4      
            
            elif (x >= u4_cords[0] and x <= u4_cords[2] and y >= u4_cords[1] and y <= u4_cords[3]):
                if u3_cords[1] != 250:
                    canvas.move(i[3], 0, j * -360)
                    if u2_cords[1] != 200:
                        canvas.move(i[2], 0, j * -360)
                        if u1_cords[1] != 150:
                            canvas.move(i[1],0,j * -360)
                if (u4_cords[1] == 300):
                    j = -1
                canvas.move(i[4], 0, j * -360)

    def réinitialiser():
        canvas.delete('all')
        for i in range (a):
            boules_list = []
            # création des différentes boules
            quinaire = canvas.create_oval(10 + i * 50, 10, i * 50 + 60, 60, fill = "blue")
            unaire1 = canvas.create_oval(10 + i * 50, 510, i * 50 + 60, 560, fill = "blue")
            unaire2 = canvas.create_oval(10 + i * 50, 560, i * 50 + 60, 610, fill = "blue")
            unaire3 = canvas.create_oval(10 + i * 50, 610, i * 50 + 60, 660, fill = "blue")
            unaire4 = canvas.create_oval(10 + i * 50, 660, i * 50 + 60, 710, fill = "blue")
        
            # ajout des boules dans la liste boules_list
            boules_list.append(quinaire) #i[0]
            boules_list.append(unaire1) #1
            boules_list.append(unaire2) #2
            boules_list.append(unaire3) #3
            boules_list.append(unaire4) #4
        
            # ajouter la liste boules_list dans la liste globale 
            all_list.append(boules_list)
            canvas.create_line(35 + 50 * i, 10, 35 + 50 * i, 710, width = 2, fill = "blue")
        
        canvas.create_line(0, 150, 1100, 150, width = 5, fill = "blue")

    canvas.bind('<Button-1>', click_boules)
    canvas.bind('<Motion>', hover_style)
    
    bouton3 = tk.Button(text="Réinitialiser", command = réinitialiser)
    bouton3.pack()

def adapt(n, column):
    global all_list

    if (n < 5):
        for i in range(1, n + 1):
            canvas.move(all_list[column][i], 0, -360)
            n -= 1
    if (n > 5):
        canvas.move(all_list[column][0], 0, 90)
        n -= 5
        for i in range(1, n + 1):
            canvas.move(all_list[column][i], 0, -360)
            n -= 1
    elif (n == 5):
        canvas.move(all_list[column][0], 0, 90)

def analyse_int(nb):
    snb = str(nb)

    for i in range(len(snb)):
        adapt(int(snb[i]), i)


def opération():
    global all_list

    def addition():
        
        m = int(entry1.get())
        n = int(entry2.get())
        #reinitialiser()
        result = n+m
        couper = [int(a) for a in str(result)]
        for i in range(len(couper)):
            boules_list = []
            # création des différentes boules
            quinaire = canvas.create_oval(10 + i * 50, 10, i * 50 + 60, 60, fill = "blue")
            unaire1 = canvas.create_oval(10 + i * 50, 510, i * 50 + 60, 560, fill = "blue")
            unaire2 = canvas.create_oval(10 + i * 50, 560, i * 50 + 60, 610, fill = "blue")
            unaire3 = canvas.create_oval(10 + i * 50, 610, i * 50 + 60, 660, fill = "blue")
            unaire4 = canvas.create_oval(10 + i * 50, 660, i * 50 + 60, 710, fill = "blue")
        
            # ajout des boules dans la liste boules_list
            boules_list.append(quinaire) #i[0]
            boules_list.append(unaire1) #1
            boules_list.append(unaire2) #2
            boules_list.append(unaire3) #3
            boules_list.append(unaire4) #4
        
            # ajouter de boules_list dans la liste globale 
            all_list.append(boules_list)
            canvas.create_line(35 + 50 * i, 10, 35 + 50 * i, 710, width = 2, fill = "blue")
    
        canvas.create_line(0, 150, 1100, 150, width = 5, fill = "blue")
        analyse_int(result)


    def soustraction():
        m = int(entry1.get())
        n = int(entry2.get())
        #reinitialiser()
        result = m-n
        couper = [int(a) for a in str(result)]
        for i in range(len(couper)):
            boules_list = []
            # création des différentes boules
            quinaire = canvas.create_oval(10 + i * 50, 10, i * 50 + 60, 60, fill = "blue")
            unaire1 = canvas.create_oval(10 + i * 50, 510, i * 50 + 60, 560, fill = "blue")
            unaire2 = canvas.create_oval(10 + i * 50, 560, i * 50 + 60, 610, fill = "blue")
            unaire3 = canvas.create_oval(10 + i * 50, 610, i * 50 + 60, 660, fill = "blue")
            unaire4 = canvas.create_oval(10 + i * 50, 660, i * 50 + 60, 710, fill = "blue")
        
            # ajout des boules dans la liste boules_list
            boules_list.append(quinaire) #i[0]
            boules_list.append(unaire1) #1
            boules_list.append(unaire2) #2
            boules_list.append(unaire3) #3
            boules_list.append(unaire4) #4
        
            # ajouter la liste boules_list dans la liste globale 
            all_list.append(boules_list)
            canvas.create_line(35 + 50 * i, 10, 35 + 50 * i, 710, width = 2, fill = "blue")
    
        canvas.create_line(0, 150, 1100, 150, width = 5, fill = "blue")
        analyse_int(result)
    
    def multiplication():
        m = int(entry1.get())
        n = int(entry2.get())
        #reinitialiser()
        result = n*m
        couper = [int(a) for a in str(result)]
        for i in range(len(couper)):
            boules_list = []
            # création des différentes boules
            quinaire = canvas.create_oval(10 + i * 50, 10, i * 50 + 60, 60, fill = "blue")
            unaire1 = canvas.create_oval(10 + i * 50, 510, i * 50 + 60, 560, fill = "blue")
            unaire2 = canvas.create_oval(10 + i * 50, 560, i * 50 + 60, 610, fill = "blue")
            unaire3 = canvas.create_oval(10 + i * 50, 610, i * 50 + 60, 660, fill = "blue")
            unaire4 = canvas.create_oval(10 + i * 50, 660, i * 50 + 60, 710, fill = "blue")
        
            # ajout des boules dans la liste boules_list
            boules_list.append(quinaire) #i[0]
            boules_list.append(unaire1) #1
            boules_list.append(unaire2) #2
            boules_list.append(unaire3) #3
            boules_list.append(unaire4) #4
        
            # ajouter la liste boules_list dans la liste globale 
            all_list.append(boules_list)
            canvas.create_line(35 + 50 * i, 10, 35 + 50 * i, 710, width = 2, fill = "blue")
    
        canvas.create_line(0, 150, 1100, 150, width = 5, fill = "blue")
        analyse_int(result)
    
    def division():
        m = int(entry1.get())
        n = int(entry2.get())
        #reinitialiser()
        result = m//n
        couper = [int(b) for b in str(result)]
        print(couper)
        for i in range(len(couper)):
            boules_list = []
            # création des différentes boules
            quinaire = canvas.create_oval(10 + i * 50, 10, i * 50 + 60, 60, fill = "blue")
            unaire1 = canvas.create_oval(10 + i * 50, 510, i * 50 + 60, 560, fill = "blue")
            unaire2 = canvas.create_oval(10 + i * 50, 560, i * 50 + 60, 610, fill = "blue")
            unaire3 = canvas.create_oval(10 + i * 50, 610, i * 50 + 60, 660, fill = "blue")
            unaire4 = canvas.create_oval(10 + i * 50, 660, i * 50 + 60, 710, fill = "blue")
        
            # ajout des boules dans la liste boules_list
            boules_list.append(quinaire) #i[0]
            boules_list.append(unaire1) #1
            boules_list.append(unaire2) #2
            boules_list.append(unaire3) #3
            boules_list.append(unaire4) #4
        
            # ajouter la liste boules_list dans la liste globale 
            all_list.append(boules_list)
            canvas.create_line(35 + 50 * i, 10, 35 + 50 * i, 710, width = 2, fill = "blue")
    
        canvas.create_line(0, 150, 1100, 150, width = 5, fill = "blue")
        analyse_int(result)
    
    

    # création fenêtre des opérations à entrer
    racine2 = tk.Tk()
    entry1 = tk.Entry(racine2)
    entry2 = tk.Entry(racine2)

    bouton_addition = tk.Button(racine2, text ="+", command = addition)
    bouton_sous = tk.Button(racine2, text ="-", command = soustraction)
    bouton_multi = tk.Button(racine2, text ="x", command = multiplication)
    bouton_division = tk.Button(racine2, text ="/", command = division)

    entry1.grid(row=3, column=0)
    entry2.grid(row=3, column=2)
    bouton_addition.grid(row=1, column=1)
    bouton_sous.grid(row=2, column=1)
    bouton_multi.grid(row=4, column=1)
    bouton_division.grid(row=5, column=1)


    

bouton1 = tk.Button(text="Mode simulation", command = simulation)
bouton2 = tk.Button(text="Mode opération", command = opération)

canvas.pack()
bouton1.pack(side=tk.LEFT)
bouton2.pack(side=tk.RIGHT)


racine.mainloop() # Lancement de la boucle principale

# bout de programme pris depuis un site :

num = 13579
x = [int(a) for a in str(num)]
print(x)

https://www.delftstack.com/fr/howto/python/split-integer-into-digits-python/#:~:text=%2C%207%2C%209%5D-,Utilisez%20les%20fonctions%20map()%20et%20str.,chaque%20élément%20d%27un%20itérable
