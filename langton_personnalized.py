from tkinter import *

#Variables----------------------------------
cote = 510
case = 101
resolution = cote / case
vitesse = 1
continuer = False
rule1_bool, rule2_bool=True, True
rule1, rule2=[], []
patern1, patern2=[[0],[0,0]]
#Classe---------------------------------------
class Fourmi():
    def __init__(self): #Constructeur
        self.posX = 50
        self.posY = 50
        self.orientation = 90
        self.dureeVie = 0

    #MÃ©thodes

    def modifOrientation(self, patern):
        self.orientation+=patern[0][0]
        if self.orientation < -90:
                self.orientation += 360
        if self.orientation > 180:
                self.orientation -= 360
                
    def modifPosition(self,patern):
        if self.orientation == 90:
            self.posX += patern[1][0]
            self.posY += patern[1][1]
        if self.orientation == 0:
            self.posX -= patern[1][1]
            self.posY += patern[1][0]
        if self.orientation == 180:
            self.posX += patern[1][1]
            self.posY -= patern[1][0]
        if self.orientation == -90 :
            self.posX -= patern[1][0]
            self.posY -= patern[1][1]

    def MaJfourmi(self):
        global grille, patern1, patern2
        if grille[self.posX][self.posY] == 1:
            grille[self.posX][self.posY] = 0
            self.modifPosition(patern1)
            self.modifOrientation(patern1)
        elif grille[self.posX][self.posY] == 0:
            grille[self.posX][self.posY] = 1
            self.modifPosition(patern2)
            self.modifOrientation(patern2)
            

    def creationRegles(self):
        regles = Tk()


def afficherGrille1ereFois(grille):
    global canvas, fourmi, fenetre, listeItem
    listeItem = []
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j] == 0:
                couleur = "black"
            else:
                couleur = "white"
            if i == fourmi.posX and j == fourmi.posY:
                couleur = "red"
            a = canvas.create_rectangle(i * resolution, j * resolution, i * resolution + resolution, j * resolution + resolution, fill = couleur)
            listeItem.append(a)

def afficherGrille(grille):
    global fenetre, canvas, listeItem, fourmi, dureeDeVie
    o = 0
    for i in range(len(grille[0])):
        for j in range(len(grille)):
            if grille[i][j] == 1:
                couleur = "white"
            else:
                couleur = "black"
            if i == fourmi.posX and j == fourmi.posY:
                couleur = "red"
            if couleur != canvas.itemcget(listeItem[o], "fill"):
                canvas.itemconfig(listeItem[o], fill = couleur)
            o += 1
    dureeDeVie.config(text =  "Duree de vie : " + str(fourmi.dureeVie))

def defining_rules(rule):
    patern=[[90],[0,0]]
    p=len(rule)
    i=0
    while i<p:
        if rule[i] == "Up" :
            patern[0][0]=0
            patern[1][1]-=1
        if rule[i] == "Down" :
            patern[0][0]=180
            patern[1][1]+=1
        if rule[i] == 'Right':
            patern[0][0]=-90
            patern[1][0]+=1
        if rule[i] == 'Left':
            patern[0][0]=90
            patern[1][0]-=1
        i+=1
    return(patern)


def keyPress(event):
    global grille, fourmi, continuer, patern1, patern2, rule2, rule1, rule1_bool, rule2_bool
    
    if rule1_bool :
        if event.keysym == "Return":
            patern1=defining_rules(rule1)
            print(patern1)
            rule1_bool=False
            print("It is your first rule. Now type the second one :")
        else:
            rule1.append(event.keysym)
            print(rule1,"\nYou can type the next move")
            
    elif rule2_bool :
        if event.keysym == "Return":
            patern2=defining_rules(rule2)
            print(patern2)
            rule2_bool=False
            print("This is the second rule. Now, type 'Up' arrow for 1 move, enter for continuity.") 
        else:
            rule2.append(event.keysym)
            print(rule2,"\nYou can type the next move")
    else :
        if event.keysym == "Up":
            fourmi.MaJfourmi()
            fourmi.dureeVie += 1
            afficherGrille(grille)
        elif event.keysym == "Return":
            if continuer == False:
                continuer = True
                lancementSimulation()
            else:
                continuer = False

def lancementSimulation():
    global fenetre, grille, continuer, fourmi
    fourmi.MaJfourmi()
    fourmi.dureeVie += 1
    afficherGrille(grille)
    if continuer:
        fenetre.after(vitesse, lancementSimulation)

def simulation():
    global fenetre, fourmi, grille, canvas, dureeDeVie
    fenetre = Tk()
    fenetre.title("Fourmi de Langton")
    canvas = Canvas(fenetre, width = 500, height = 500, bg = 'black')
    canvas.pack(padx = 15, pady = 15)
    fourmi = Fourmi()
    grille = [[1 for l in range(case)] for c in range(case)]
    afficherGrille1ereFois(grille)
    dureeDeVie = Label(fenetre, text = "Duree de vie : " + str(fourmi.dureeVie))
    dureeDeVie.pack(padx = 20, pady = 20)
    fenetre.bind("<Key>", keyPress)
    fenetre.mainloop()
print("Type the move you want the ant to execute step by step, then press enter to confirm the set. 2 set of rules total.")
simulation()
