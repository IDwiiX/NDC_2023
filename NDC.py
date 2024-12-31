# Pyxel Studio
'''
Documentation
##################################################
# Description :Puisque Flappy bird est mort , son fantom continue son chemain et il peut traverser les murs . 
##################################################

jeu : Flappy Zak 
But : Voler sans tomber tout en évitant les obstacles sur le chemain  
Genre : Action 
Niveaux de difficulté : Plus notre score augmente plus la vitesse de défilement augmente 

##################################################

# Sélection de niveau :
ESPACE = commancer le jeu 
# Un seul personnage 
# Touches :
- Espace = Sauter
- Escape = Quitter

##################################################
# Futurs Ajouts / Bugs à Corriger :
Plusieurs arènes 
Corriger les collisions
##################################################


##################################################
# Crédits :
##################################################
MAROIHI Kamar 
BELHAJ SOULAMI Zakariae 
MOHAMED KABIRI Ali '''


import pyxel
import random

#Constantes du jeu
TITLE = "Flappy Zak"
HEIGHT = 128
WIDTH = 128
CASE = 5
FRAME_REFRESH = 10

pyxel.init(WIDTH, HEIGHT, title = TITLE)
pyxel.load("2.pyxres")

score = 0
life = 3
perso = [1,15]
direction=[1,-1]
c = 0
start = False
cpt = 0
deplacement = False

x1_obstacle = 30
x2_obstacle = 60
x3_obstacle = 90

    
def update():
    
    global perso
    global direction
    global cible
    global score
    global FRAME_REFRESH 
    
    global x1_obstacle
    global x2_obstacle
    global x3_obstacle
    
    global life
    global cpt
    global deplacement
    global c
    global start
    
    
    #quand le fantome passe à droite pour sortir à gauche
    if start == False and pyxel.btn(pyxel.KEY_SPACE):
        start = True
        
    elif start == True :
        
        if pyxel.frame_count % FRAME_REFRESH==0:
            perso[0] =  (perso[0] +direction[0])%128
            perso[1] = (perso[1] -direction[1])%128
            
        if perso[0] > WIDTH/CASE - 1 or perso[1] > HEIGHT/CASE - 1:
            score += 1
            perso = [1,15]
            x1_obstacle = 30 * random.uniform(1, 4.2)
            x2_obstacle = 60 * random.uniform(1, 2.1)
            x3_obstacle = 90 * random.uniform(1, 1.4)
            
        #Quand le fantome saute
            
        if pyxel.btn(pyxel.KEY_SPACE) :
            deplacement = True
            cpt = 0
        if cpt < 10 and deplacement == True:
                direction = [1,1]
                cpt += 1
        elif cpt == 10 :
                direction = [1, -1]
                deplacement == False

    
    if pyxel.btn(pyxel.KEY_ESCAPE) :
        exit()
                



def draw():
    
    global x1_obstacle
    global x2_obstacle
    global x3_obstacle
    global start 
    
    if start == False :
        pyxel.cls(2)
        pyxel.blt(56, 60,0, 25, 32, 8,8) 
        pyxel.blt(63, 60,0, 32, 32, 8,8)
        pyxel.text(2,45, f"Click on the space bar to start  ",7)
        pyxel.text(40,52, f" the game :) ",7)
        
    else :
        pyxel.cls(0)
        pyxel.blt(90,4,0, 48, 25, 8,8 )
        pyxel.blt(100,4,0, 48, 25, 8,8 )
        pyxel.blt(110,4,0, 48, 25, 8,8 )

        pyxel.blt(90,60,0, 40, 24, 8,8 )
        pyxel.blt(50,20,0, 40, 24, 8,8 )
        pyxel.bltm(0, 0, 0, 192 - pyxel.frame_count % 192, 0, 128, 128)
        #pyxel.rect(0, 0, WIDTH, HEIGHT, 2)
            
        pyxel.text(4, 4, f"SCORE : {score}", 7)
        #pyxel.text(92,4, f"LIFE: {life}", 7)
        
        #Perso
        x_perso, y_perso = perso[0], perso[1]
        pyxel.blt(x_perso * CASE, y_perso * CASE,0, 65, 17, 7,7)
            
        #Terre en bas 
        pyxel.blt(0, 121, 0, 0, 40, 24, 8)
        pyxel.blt(24, 121, 0, 0, 40, 24, 8)
        pyxel.blt(48, 121, 0, 0, 40, 24, 8)
        pyxel.blt(72, 121, 0, 0, 40, 24, 8)
        pyxel.blt(96, 121, 0, 0, 40, 24, 8)
        pyxel.blt(120, 121, 0, 0, 40, 24, 8)
            
        #Terre en haut
        pyxel.blt(0, 18, 0, 0, 40, 24, 8)
        pyxel.blt(24, 18, 0, 0, 40, 24, 8)
        pyxel.blt(48, 18, 0, 0, 40, 24, 8)
        pyxel.blt(72, 18, 0, 0, 40, 24, 8)
        pyxel.blt(96, 18, 0, 0, 40, 24, 8)
        pyxel.blt(120, 18, 0, 0, 40, 24, 8)
            
        #Obstacle
        pyxel.blt(x1_obstacle, 25 ,0, 32, 48, 8, 24,0)
        pyxel.blt(x1_obstacle, 40 ,0, 32, 48, 8, 24,0)
            
        pyxel.blt(x3_obstacle, 25 ,0, 32, 48, 8, 24,0)
        pyxel.blt(x3_obstacle, 40 ,0, 32, 48, 8, 24,0)
        
        pyxel.blt(x2_obstacle , 98 ,0, 32, 48, 8, 24,0)
        pyxel.blt(x2_obstacle , 83 ,0, 32, 48, 8, 24,0)
        
        #Coeur
        pyxel.blt(90,4,0, 48, 25, 8,8 )
        pyxel.blt(100,4,0, 48, 25, 8,8 )
        pyxel.blt(110,4,0, 48, 25, 8,8 )
        
    
    
pyxel.run(update, draw)
 