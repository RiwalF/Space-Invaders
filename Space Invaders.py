#Space Invaders en POO

import pygame #importation des bibliothèques
import time
import random
import math
import sys

pygame.init()

class Jeu:#contient les variables et les fonctions du jeu
    def __init__(self):#initialisation de chaques variables

        self.ecran = pygame.display.set_mode((800,600))#Taille de la fenêtre

        pygame.display.set_caption('Space Invaders Riwal')#nomme la fenêtre
        
        #Variable de chaque boucle pour chaque menu
        self.jeu_encours = False #variable du jeu
        self.Menu_level = False#variable de la selection de niveau
        self.Menu_Skin = False#variable de la selection du Skin
        self.Menu_1v1 = False
        self.Menu = True#variable du menu principal
        self.allMenu = True#Boucle de chaque menu pour qu'il puisse se lancer n'importe quand 
        
        #Vaisseau
        self.skin_vaisseau = pygame.image.load("vaisseau_bas.png")#importation de l'image (vaisseau)
        self.skin_vaisseau2 = self.skin_vaisseau #sert à créer une deuxieme image qui ne sera pas controlable par l'utilisateur tout en ayant des parametres similaires
        self.vaisseau_position_X = 364#position du vaisseau en X sur l'écran
        self.vaisseau_position_Y = 500#position Y du vaisseau ( 0 = en haut de l'écran )
        self.vaisseau_direction_X = 0#Variable qui sert a ce que lorsque l'on reste appuyer sur une touche droite ou gauche le vaisseau avance en continue
        self.stats_Tir = 0 #Variable qui servira a compter le nombre de fois ou l'utilisateur tir dans une partie
        self.skin_selectionner = 0 #variable qui sert à changer de vaisseau
        self.score = 0 #score de l'utilisateur
        self.touchéJ1 = 0
        
        #Vaisseau 2
        self.skin_vaisseauj2 = pygame.image.load("vaisseau_bas.png")#importation de l'image (vaisseau)2
        self.vaisseau_position_X2 = 20#position du vaisseau en X sur l'écran2
        self.vaisseau_position_Y2 = 10#position Y du vaisseau ( 0 = en haut de l'écran )2
        self.vaisseau_direction_Y2 = 0#Variable qui sert a ce que lorsque l'on reste appuyer sur une touche droite ou gauche le vaisseau avance en continue2
        self.skin_selectionner2 = 0 #variable qui sert à changer de vaisseau2
        self.touchéJ2 = 0
        
        #Alien/Ennemi
        self.skin_vaisseauEnnemi = pygame.image.load("invader2.png")  #importation de l'image       
        self.vaisseauEnnemi_position_X = random.randint(0,740) #position du vaisseau en X sur l'écran , random sert à le placer aléatoirement
        self.vaisseauEnnemi_position_Y = 0#position Y de l'alien/Ennemi ( 0 = en haut de l'écran )
        self.vaisseauEnnemi_MvtMéchant = 0 #si le vaisseau arrive à droite cette variable devient 1 et il ira à gauche idem pour l'autre sens
        self.vit_Méchant = 0,1#cette variable sera ajoutez au X du méchant pour le faire allez de plus en plus vite vers la Gauche/droite
        
        self.skin_vaisseauEnnemi3 = pygame.image.load("alien.png")#importation de l'image         
        self.vaisseauEnnemi3_position_X = random.randint(0,740)#position du vaisseau en X sur l'écran , random sert à le placer aléatoirement
        self.vaisseauEnnemi3_position_Y = 0#position Y de l'alien/Ennemi ( 0 = en haut de l'écran )
        self.vaisseauEnnemi_MvtMéchant3 = 0#si le vaisseau arrive à droite cette variable devient 1 et il ira à gauche idem pour l'autre sens
        self.vit_Méchant3X = 0,5 #cette variable sera ajoutez au X du méchant pour le faire allez de plus en plus vite vers la Gauche/droite
        self.vit_Méchant3Y = 0,1#cette variable sera ajoutez au Y du méchant pour le faire allez de plus en plus vite vers le bas
        
        self.skin_vaisseauEnnemi2 = pygame.image.load("invader.png")#importation de l'image         
        self.vaisseauEnnemi2_position_X = random.randint(0,740)#position du vaisseau en X sur l'écran , random sert à le placer aléatoirement
        self.vaisseauEnnemi2_position_Y = 0#position Y de l'alien/Ennemi ( 0 = en haut de l'écran )
        self.vit_Méchant2 = 0.1#cette variable sera ajoutez au Y du méchant pour le faire allez de plus en plus vite vers le bas
        
        #Balle
        self.skin_Balle = pygame.image.load("balle.png")#importation de l'image 
        self.Balle_position_X = self.vaisseau_position_X+18#position de la balle au coordonnés donnés X
        self.Balle_position_Y = self.vaisseau_position_Y+40#position de la balle au coordonnés donnés Y
        self.mvtballe = False# Mode prêt de la balle
        self.Balle_selectionner = 0#variable qui sert à changer de Missile 
 
        #Balle 2
        self.skin_Balle2 = pygame.image.load("balle.png")#importation de l'image
        self.Balle_position_X2 = self.vaisseau_position_X2+18#position de la balle au coordonnés donnés X
        self.Balle_position_Y2 = self.vaisseau_position_Y2+40#position de la balle au coordonnés donnés Y
        self.mvtballe2 = False# Mode prêt de la balle
        self.Balle_selectionner2 = 0#variable qui sert à changer de Missile 
 
        #Affichage
        self.background = pygame.image.load('fondécran.jpg') #cherche l'image dans les document (fond d'écran)
        self.play_button = pygame.image.load("play.png")#importation de l'image (boutton play)
        self.game_level = pygame.image.load("gamelevel.png")#importation de l'image (boutton choix niveau)
        self.Skin_level = pygame.image.load("gameskin.png")#importation de l'image
        self.one_level = pygame.image.load("versus.png")#importation de l'image
        
        #Sons
        
        pygame.mixer.music.load('Background.mp3') #charger la musique
        pygame.mixer.music.set_volume(0.1)#volume musique
        pygame.mixer.music.play(-1) #-1 pour faire une loop
        self.BalleSon = pygame.mixer.Sound('Laser.wav') #charger le bruit du tir
        self.ExplosionSon = pygame.mixer.Sound('Explosion.wav')#charger le bruit de l'explosion
        
        
        #Autres
        self.level_selectionner = 0 #variable qui changera en fonction du choix du niveau
        self.level_Lancé = self.level_selectionner
        self.start = True
        self.score_level = 0
           
    def fonction_principale(self):# lancement de la Boucle principale qui calculera toutes les variables
        
        
        def collision_Menu_Skin(self,Balle_position_X,Balle_position_Y): #fonction qui calculera les collisions dans le menu de selection du Skin
            
            distance_Vaisseaumodif_balle = ((150-self.Balle_position_X)**2+(225-self.Balle_position_Y)**2)**(0.5)#calcul de la distance entre le vaisseau afficher au milieu de l'écran et la balle
            
            if distance_Vaisseaumodif_balle < 70:#si le résultat du calcul si dessus est inférieur à 70
                self.skin_selectionner += 1 #le vaisseau changera
                self.mvtballe = False # la balle s'arrete et revient au vaisseau
                
            if self.skin_selectionner == 3:# Il n'y a que 3 vaisseau différent le 0 le 1 et le 2 si cette variable = 3 
                self.skin_selectionner = 0#  on la ramène à 0
                
            distance_Ballemodif_balle = ((400-self.Balle_position_X)**2+(225-self.Balle_position_Y)**2)**(0.5)#calcul de la distance entre la balle afficher au milieu de l'écran et la balle tirer
                
            if distance_Ballemodif_balle < 70:#si le résultat du calcul si dessus est inférieur à 70
                self.Balle_selectionner += 1#la balle changera
                self.mvtballe = False # la balle s'arrete et revient au vaisseau
                
            if self.Balle_selectionner == 3:# Il n'y a que 3 Balle différentes la 0 la 1 et la 2 si cette variable = 3 
                self.Balle_selectionner = 0#  on la ramène à 0

            distance_menumodif_balle = ((650-self.Balle_position_X)**2+(112-self.Balle_position_Y)**2)**(0.5)#calcul de la distance entre le boutton Menu afficher au milieu de l'écran et la balle tirer
            
            if distance_menumodif_balle < 100:#si le résultat du calcul si dessus est inférieur à 100
                self.Menu_Skin = False #désactive le menu de la selection du Skin 
                self.Menu = True#active le menu Principal
                self.mvtballe=False # la balle s'arrete et revient au vaisseau
                
            

        def collision_Menu_level (self,Balle_position_X,Balle_position_Y):#fonction qui calculera les collisions dans le menu de selection du Niveau
            
            #Tout ces calculs calculent la distance entre la balle et chaque sélection de niveau/Menu
            distance_level1_balle = ((50-self.Balle_position_X)**2+(150-self.Balle_position_Y)**2)**(0.5) #Niveau 1
            distance_level2_balle = ((150-self.Balle_position_X)**2+(150-self.Balle_position_Y)**2)**(0.5)#Niveau 2
            distance_level3_balle = ((250-self.Balle_position_X)**2+(150-self.Balle_position_Y)**2)**(0.5)#Niveau 3
            distance_level4_balle = ((350-self.Balle_position_X)**2+(150-self.Balle_position_Y)**2)**(0.5)#Niveau 4
            distance_level5_balle = ((450-self.Balle_position_X)**2+(150-self.Balle_position_Y)**2)**(0.5)#Niveau 5
            distance_level6_balle = ((550-self.Balle_position_X)**2+(150-self.Balle_position_Y)**2)**(0.5)#Mode Infini/niveau 6
            distance_Réinitialiser_balle = ((600-self.Balle_position_X)**2+(150-self.Balle_position_Y)**2)**(0.5)#Réinitialiser
            distance_Menu_balle = ((750-self.Balle_position_X)**2+(150-self.Balle_position_Y)**2)**(0.5)#Menu
            
            if distance_level1_balle < 70:#si le résultat du calcul Niveau 1 au dessus est inférieur à 70
                self.level_selectionner = 1 #Alors le niveau selectionner sera le 1
                
            if distance_level2_balle < 70: #même chose pour tout les autres niveau suivant
                self.level_selectionner = 2
                
            if distance_level3_balle < 70:#idem
                self.level_selectionner = 3
                
            if distance_level4_balle < 70:#idem
                self.level_selectionner = 4
    
            if distance_level5_balle < 70:#idem
                self.level_selectionner = 5
                
            if distance_level6_balle < 70:#idem
                self.level_selectionner = 6
                
            if distance_Réinitialiser_balle < 70:#celui-ci réinitialise tout les rectangles affichés comme au lancement du menu 
                self.level_selectionner = 0

            if distance_Menu_balle < 70:#celui-ci sert à relancer le menu Principal
                self.Menu = True#active le Menu Principal
                self.Menu_level = False#désactive le Menu Sélection du niveau
                self.mvtballe = False# la balle s'arrete et revient au vaisseau

        def collision_Menu (self,level_selectionner,Balle_position_X,Balle_position_Y):#fonction qui calculera les collisions dans le Menu Principal
            
            #Toutes les variables ci-dessous sont réinitialisez comme au lancement du JEU #
            self.vaisseauEnnemi_position_X = random.randint(0,740)                        #
            self.vaisseauEnnemi_position_Y = 0                                            #
            self.vit_Méchant = 1                                                          #
            self.vaisseauEnnemi2_position_X = random.randint(0,740)                       #
            self.vaisseauEnnemi2_position_Y = 0                                           #
            self.vit_Méchant2 = 0.1                                                       #
            self.vaisseauEnnemi3_position_X = random.randint(0,740)                       #
            self.vaisseauEnnemi3_position_Y = 0                                           #
            self.vit_Méchant3X = 1                                                        #
            self.vit_Méchant3Y = 0.2                                                      #
            self.score = 0                                                                #
            self.stats_Tir = 0                                                            #
            #Toutes les variables ci-dessus sont réinitialisez comme au lancement du JEU  #
            
            distance_Play_balle = ((300-self.Balle_position_X)**2+(320-self.Balle_position_Y)**2)**(0.5)#calcul de la distance entre le boutton play afficher au milieu de l'écran et la balle
            
            if self.level_selectionner > 0:#Fait en sorte de ne pas lancer un Niveau si aucun ne sont sélectionner
                
                if distance_Play_balle < 50:#si le résultat du calcul au dessus est inférieur à 30
                    self.Menu = False#Désactive le Menu Principal
                    self.jeu_encours = True#active le Jeu
                    self.mvtballe = False# la balle s'arrete et revient au vaisseau
                
            distance_gamelevel_balle = ((130-self.Balle_position_X)**2+(250-self.Balle_position_Y)**2)**(0.5)#calcul de la distance entre le boutton Choix jeu afficher au milieu de l'écran et la balle
            
            if distance_gamelevel_balle < 60:#si le résultat du calcul au dessus est inférieur à 100
                self.Menu = False#Désactive le Menu Principal
                self.Menu_level = True#active le menu choix level
                self.mvtballe=False# la balle s'arrete et revient au vaisseau
                
            distance_gameskin_balle = ((630-self.Balle_position_X)**2+(320-self.Balle_position_Y)**2)**(0.5)#calcul de la distance entre le boutton Choix Vaisseau afficher au milieu de l'écran et la balle
            
            if distance_gameskin_balle < 50:#si le résultat du calcul au dessus est inférieur à 50
                self.Menu = False#Désactive le Menu Principal
                self.mvtballe=False# la balle s'arrete et revient au vaisseau
                self.Menu_Skin = True#active le menu choix vaisseau
                
            distance_game1v1_balle = ((480-self.Balle_position_X)**2+(320-self.Balle_position_Y)**2)**(0.5)
            
            if distance_game1v1_balle < 50:#si le résultat du calcul au dessus est inférieur à 50
                self.start = True
                self.mvtballe=False# la balle s'arrete et revient au vaisseau
                self.Menu = False#Désactive le Menu Principal
                self.Menu_1v1 = True#active le menu choix vaisseau
            
        def collision_Jeu_1v1 (self,Balle_position_X,Balle_position_Y):#fonction qui calculera les collisions durant le Jeu


            distance_J2_BalleJ1 = ((self.vaisseau_position_X2-self.Balle_position_X-20)**2+(self.vaisseau_position_Y2-self.Balle_position_Y)**2)**(0.5)
            
            if distance_J2_BalleJ1 < 50:
                self.mvtballe = False
                self.ExplosionSon.play()#joue le son de l'explosion 
                self.touchéJ1 += 1
            
            
            distance_J1_BalleJ2 = ((self.vaisseau_position_X-self.Balle_position_X2-20)**2+(self.vaisseau_position_Y-self.Balle_position_Y2)**2)**(0.5)
            
            if distance_J1_BalleJ2 < 50:
                self.mvtballe2 = False
                self.ExplosionSon.play()#joue le son de l'explosion 
                self.touchéJ2 += 1
            
            if self.touchéJ1 == 5 or self.touchéJ2 == 5:
                
                if self.touchéJ1 == 5:
                    self.ExplosionSon.play()#joue le son de l'explosion 
                    Titre = pygame.font.Font('freesansbold.ttf', 60) #création du type d'ecriture et de police 
                    message = Titre.render("Victoire du Joueur 1", True, (0,255,0))#création du texte en Gras ou pas
                    self.ecran.blit(message, (90, 200))  # affichage du message aux coordonnées
                    
                if self.touchéJ2 == 5:
                    self.ExplosionSon.play()#joue le son de l'explosion 
                    Titre = pygame.font.Font('freesansbold.ttf', 60) #création du type d'ecriture et de police 
                    message = Titre.render("Victoire du Joueur 2", True, (0,255,0))#création du texte en Gras ou pas
                    self.ecran.blit(message, (90, 200))  # affichage du message aux coordonnées

            
                self.skin_vaisseau = pygame.image.load("vaisseau_bas.png")#importation de l'image (vaisseau)
                self.skin_vaisseau2 = self.skin_vaisseau #sert à créer une deuxieme image qui ne sera pas controlable par l'utilisateur tout en ayant des parametres similaires
                self.vaisseau_position_X = 364#position du vaisseau en X sur l'écran
                self.vaisseau_position_Y = 500#position Y du vaisseau ( 0 = en haut de l'écran )
                self.vaisseau_direction_X = 0#Variable qui sert a ce que lorsque l'on reste appuyer sur une touche droite ou gauche le vaisseau avance en continue
                self.skin_Balle = pygame.image.load("balle.png")#importation de l'image 
                self.Balle_position_X = self.vaisseau_position_X+18#position de la balle au coordonnés donnés X
                self.Balle_position_Y = self.vaisseau_position_Y+40#position de la balle au coordonnés donnés Y
                self.mvtballe = False# Mode prêt de la balle
                self.Balle_selectionner = 0#variable qui sert à changer de Missile 
                pygame.display.update()#mise à jour de l'écran
                time.sleep(4) #pause de l'écran pendant 4 secondes
                self.touchéJ1 = 0
                self.touchéJ2 = 0
                self.Menu_1v1 = False #désactive le Jeu
                self.mvtballe = False #la balle s'arrete et revient au vaisseau
                self.Menu = True #active le Menu Principal
                
                
        def collision_Jeu (self,Balle_position_X,Balle_position_Y):#fonction qui calculera les collisions durant le Jeu
                
            distance_Ennemi_balle = ((self.vaisseauEnnemi_position_X-self.Balle_position_X)**2+(self.vaisseauEnnemi_position_Y-self.Balle_position_Y)**2)**(0.5)#calcul de la distance entre l'alien1 et la balle
            distance_Ennemi_Vaisseau = ((self.vaisseauEnnemi_position_X-self.vaisseau_position_X)**2+(self.vaisseauEnnemi_position_Y-self.vaisseau_position_Y)**2)**(0.5)#calcul de la distance entre l'alien1 et le vaisseau

            distance_Ennemi2_balle = ((self.vaisseauEnnemi2_position_X-self.Balle_position_X)**2+(self.vaisseauEnnemi2_position_Y-self.Balle_position_Y)**2)**(0.5)#calcul de la distance entre l'alien2 et la balle
            distance_Ennemi2_Vaisseau = ((self.vaisseauEnnemi2_position_X-self.vaisseau_position_X)**2+(self.vaisseauEnnemi2_position_Y-self.vaisseau_position_Y)**2)**(0.5)#calcul de la distance entre l'alien2 et le vaisseau
            
            distance_Ennemi3_balle = ((self.vaisseauEnnemi3_position_X-self.Balle_position_X)**2+(self.vaisseauEnnemi3_position_Y-self.Balle_position_Y)**2)**(0.5)#calcul de la distance entre l'alien3 et la balle
            distance_Ennemi3_Vaisseau = ((self.vaisseauEnnemi3_position_X-self.vaisseau_position_X)**2+(self.vaisseauEnnemi3_position_Y-self.vaisseau_position_Y)**2)**(0.5)#calcul de la distance entre l'alien3 et le vaisseau
            
            if distance_Ennemi_balle < 35 :#Si la distance entre l'alien1 et la balle est inférieur à 35
                 
                self.ExplosionSon.play()#joue le son de l'explosion 
                self.vaisseauEnnemi_position_X = random.randint(0,740)#replace l'alien aléatoirement entre 0 et 740
                self.vaisseauEnnemi_position_Y = 0#replace l'alien en haut de l'écran
                self.vit_Méchant += 1 #accelere l'alien X
                self.score += 1 #additionne des points au score

            if distance_Ennemi2_balle < 45 :#Si la distance entre l'alien2 et la balle est inférieur à 35
                
                self.ExplosionSon.play()#joue le son de l'explosion 
                self.vaisseauEnnemi2_position_X = random.randint(0,740)#replace l'alien aléatoirement entre 0 et 740
                self.vaisseauEnnemi2_position_Y = 0#replace l'alien en haut de l'écran
                self.vit_Méchant2 += 0.1#accelere l'alien Y
                self.score += 2#additionne des points au score
                
            if distance_Ennemi3_balle < 35 :#Si la distance entre l'alien2 et la balle est inférieur à 35
                
                self.ExplosionSon.play()#joue le son de l'explosion 
                self.vaisseauEnnemi3_position_X = random.randint(0,740)#replace l'alien aléatoirement entre 0 et 740
                self.vaisseauEnnemi3_position_Y = 0#replace l'alien en haut de l'écran
                self.vit_Méchant3X += 0.5#accelere l'alien X
                self.vit_Méchant3Y += 0.1#accelere l'alien Y
                self.score += 3#additionne des points au score

            if distance_Ennemi_Vaisseau < 35 or distance_Ennemi2_Vaisseau < 35 or distance_Ennemi3_Vaisseau < 35:#Si la distance entre l'alien2 et le vaisseau est inférieur à 35
                
                self.ExplosionSon.play()#joue le son de l'explosion 
                Titre = pygame.font.Font('freesansbold.ttf', 100) #création du type d'ecriture et de police 
                message = Titre.render("GAME OVER", True, (255,0,0))#création du texte en Gras ou pas
                self.ecran.blit(message, (90, 200))  # affichage du message aux coordonnées 
                
                score = pygame.font.Font('freesansbold.ttf', 18) #création du type d'ecriture et de police
                message = score.render(f"Score : {self.score}", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (700, 0))  # affichage du message aux coordonnées
                
                pygame.display.update()#mise à jour de l'écran
                time.sleep(4) #pause de l'écran pendant 4 secondes
                self.jeu_encours = False #désactive le Jeu
                self.mvtballe = False #la balle s'arrete et revient au vaisseau
                self.Menu = True #active le Menu Principal
                
                
        def modeballe_1v1 (self):#création du mode de la balle dans cette fonction
            
            self.skin_Balle = pygame.image.load("Balle_droite.png")#importation de l'image 
            self.skin_Balle2 = pygame.image.load("Balle_gauche.png")#importation de l'image 
            
            if self.Balle_position_X<=0:   #Vérifie si la balle ne sort pas de l'écran (en haut)
                self.mvtballe=False #Si elle sort alors elle la mets en mode prêt(en bas)
        
            if self.mvtballe==False: #Mode Prêt de la balle
                self.Balle_position_X = self.vaisseau_position_X+40#position de la balle au coordonnés donnés X
                self.Balle_position_Y = self.vaisseau_position_Y+18#position de la balle au coordonnés donnés Y
        
            if self.mvtballe==True:#Mode Feu de la balle
                self.Balle_position_X -= 7 #effectue le mouvement de la balle
 
 

            if self.Balle_position_X2>=800:   #Vérifie si la balle ne sort pas de l'écran (en haut)
                self.mvtballe2=False #Si elle sort alors elle la mets en mode prêt(en bas)
        
            if self.mvtballe2==False: #Mode Prêt de la balle
                self.Balle_position_X2 = self.vaisseau_position_X2-7#position de la balle au coordonnés donnés X
                self.Balle_position_Y2 = self.vaisseau_position_Y2+18#position de la balle au coordonnés donnés Y
        
            if self.mvtballe2==True:#Mode Feu de la balle
                self.Balle_position_X2 += 7 #effectue le mouvement de la balle
                
                
        def modeballe (self):#création du mode de la balle dans cette fonction
            
            if self.Balle_position_Y<=0:   #Vérifie si la balle ne sort pas de l'écran (en haut)
                self.mvtballe=False #Si elle sort alors elle la mets en mode prêt(en bas)
        
            if self.mvtballe==False: #Mode Prêt de la balle
                self.Balle_position_X = self.vaisseau_position_X+18#position de la balle au coordonnés donnés X
                self.Balle_position_Y = self.vaisseau_position_Y+40#position de la balle au coordonnés donnés Y
        
            if self.mvtballe==True:#Mode Feu de la balle
                self.Balle_position_Y -= 10 #effectue le mouvement de la balle
                
        def Mouvement_Ennemi_GD(self):#Création du mouvement de lalien 1 (Gauche Droite)
        
            self.ecran.blit(self.skin_vaisseauEnnemi, (self.vaisseauEnnemi_position_X, self.vaisseauEnnemi_position_Y))#affichage de l'alien
                 
            if self.vaisseauEnnemi_MvtMéchant == 0:#Si cette variable = 0
                if self.vaisseauEnnemi_position_X >= 740:#et que celle si = 740
                    self.vaisseauEnnemi_position_Y += 60#alors l'alien descend de 60
                    self.vaisseauEnnemi_MvtMéchant = 1#et la première = 1
                self.vaisseauEnnemi_position_X += self.vit_Méchant#sinon le vaisseau avances vers la droite
                
            if self.vaisseauEnnemi_MvtMéchant == 1:#Si cette variable = 1
                if self.vaisseauEnnemi_position_X <= 0:#et que celle si = 0
                    self.vaisseauEnnemi_position_Y += 60#alors l'alien descend de 60
                    self.vaisseauEnnemi_MvtMéchant = 0#et la première = 0
                self.vaisseauEnnemi_position_X -= self.vit_Méchant#sinon le vaisseau avances vers la gauche


        def Mouvement_Ennemi_HB(self):#Création du mouvement de lalien 2 (Haut Bas)
        
            self.ecran.blit(self.skin_vaisseauEnnemi2, (self.vaisseauEnnemi2_position_X, self.vaisseauEnnemi2_position_Y))#affichage de l'alien
                
            self.vaisseauEnnemi2_position_Y += self.vit_Méchant2# le vaisseau avance vers le bas
            
            if self.vaisseauEnnemi2_position_Y >= 600:#si le vaisseau arrive en bas  
                
                Titre = pygame.font.Font('freesansbold.ttf', 100)#création du type d'ecriture et de police 
                message = Titre.render("GAME OVER", True, (255,0,0))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (90, 200))  # affichage du message aux coordonnées
                
                score = pygame.font.Font('freesansbold.ttf', 18)#création du type d'ecriture et de police 
                message = score.render(f"Score : {self.score}", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (700, 0))  # affichage du message aux coordonnées
                
                pygame.display.update()#mise à jour de l'écran
                time.sleep(4) #pause de l'écran pendant 4 secondes
                self.jeu_encours = False #désactive le Jeu
                self.mvtballe = False #la balle s'arrete et revient au vaisseau
                self.Menu = True #active le Menu Principal
                
        def Mouvement_Ennemi_Diago(self):#Création du mouvement de lalien 3 (Diagonale)
            
            self.ecran.blit(self.skin_vaisseauEnnemi3, (self.vaisseauEnnemi3_position_X, self.vaisseauEnnemi3_position_Y))#affichage de l'alien
            self.vaisseauEnnemi3_position_Y += self.vit_Méchant3Y# le vaisseau avance vers le bas
            self.vaisseauEnnemi3_position_X += self.vit_Méchant3Y# le vaisseau avance vers un coté
                                                                 # donc en diagonale
                                                                 
            if self.vaisseauEnnemi3_position_Y >= 550:#si le vaisseau arrive en bas le joueur perd
                
                Titre = pygame.font.Font('freesansbold.ttf', 100)#création du type d'ecriture et de police 
                message = Titre.render("GAME OVER", True, (255,0,0))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (90, 200))  # affichage du message aux coordonnées

                score = pygame.font.Font('freesansbold.ttf', 18)#création du type d'ecriture et de police 
                message = score.render(f"Score : {self.score}", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (700, 0))  # affichage du message aux coordonnées
                
                pygame.display.update()#mise à jour de l'écran
                time.sleep(4) #pause de l'écran pendant 4 secondes
                self.jeu_encours = False #désactive le Jeu
                self.mvtballe = False #la balle s'arrete et revient au vaisseau
                self.Menu = True #active le Menu Principal
            
                
            if self.vaisseauEnnemi_MvtMéchant3 == 0:#Si cette variable = 0                
                if self.vaisseauEnnemi3_position_X >= 740:#alors que celle si = 740
                    self.vaisseauEnnemi_MvtMéchant3 = 1#la première = 1
                self.vaisseauEnnemi3_position_X += self.vit_Méchant3X#sinon le vaisseau avances vers la droite
                
            if self.vaisseauEnnemi_MvtMéchant3 == 1:#Si cette variable = 1
                if self.vaisseauEnnemi3_position_X <= 0:#alors que celle si = 0
                    self.vaisseauEnnemi_MvtMéchant3 = 0#la première = 0
                self.vaisseauEnnemi3_position_X -= self.vit_Méchant3X#sinon le vaisseau avances vers la gauche
                
####################################################################################################################################################################################################################################################
                
        def Test_evenementANDaffichage_BallePLUSVaisseau_1v1(self):#Test de chaque touche et action plus affichage
            
            self.skin_vaisseau = pygame.image.load("vaisseau_droite.png")#importation de l'image (vaisseau)
            self.skin_vaisseau2 = pygame.image.load("vaisseau_gauche.png")#importation de l'image (vaisseau)
            
            while self.start == True:
                self.vaisseau_position_X2 = 20
                self.vaisseau_position_Y2 = 10
                self.vaisseau_position_X = 720
                self.vaisseau_position_Y = 500
                self.start = False
             
            self.ecran.blit(self.skin_vaisseau2, (self.vaisseau_position_X2, self.vaisseau_position_Y2))#affichage du vaisseau
            self.ecran.blit(self.skin_Balle2, (self.Balle_position_X2, self.Balle_position_Y2))#affichage de la Balle
     
            self.ecran.blit(self.skin_vaisseau, (self.vaisseau_position_X, self.vaisseau_position_Y))#affichage du vaisseau
            self.ecran.blit(self.skin_Balle, (self.Balle_position_X, self.Balle_position_Y))#affichage de la Balle
            
            for evenement in pygame.event.get():#Test tout les évenement
                if evenement.type == pygame.QUIT:#si la croix est cliqué
                    sys.exit()#ferme le jeu

                if evenement.type == pygame.KEYDOWN:#si une touche est appuyé
                        
                    if evenement.key == pygame.K_UP:#si cette touche est la fleche droite
                        self.vaisseau_direction_Y = -5 #change la variable direction qui s'additionera à la position du vaisseau pour le déplacer

                    if evenement.key == pygame.K_DOWN:#si cette touche est la fleche gauche
                        self.vaisseau_direction_Y = 5#change la variable direction qui s'additionera à la position du vaisseau pour le déplacer
                        
                    if evenement.key == pygame.K_RETURN :#touche espace tapée
                        #self.BalleSon.play()#joue le son de la balle 
                        self.mvtballe=True #met l'obus en mode FEU
                        self.stats_Tir += 1#compte le nombre de fois tirés



                    if evenement.key == pygame.K_z:#si cette touche est la fleche droite
                        self.vaisseau_direction_Y2 = -5 #change la variable direction qui s'additionera à la position du vaisseau pour le déplacer

                    if evenement.key == pygame.K_s:#si cette touche est la fleche gauche
                        self.vaisseau_direction_Y2 = 5#change la variable direction qui s'additionera à la position du vaisseau pour le déplacer
                        
                    if evenement.key == pygame.K_SPACE :#touche espace tapée
                        #self.BalleSon.play()#joue le son de la balle 
                        self.mvtballe2=True #met l'obus en mode FEU
                        self.stats_Tir += 1#compte le nombre de fois tirés
                        


                if evenement.type == pygame.KEYUP: #Touche relachée ( si je ne mets pas le test de cet évenements le vaisseau avancerais vers un coté sans s'arreter dès que l'on apuirais sur une touche )
                    if evenement.key == pygame.K_UP or evenement.key == pygame.K_DOWN or evenement.key == pygame.K_s or evenement.key == pygame.K_z : #si cette touche est gauche ou droite
                        self.vaisseau_direction_X = 0 #réinitialise les variables direction 
                        self.vaisseau_direction_Y = 0
                        self.vaisseau_direction_Y2 = 0 

            if self.vaisseau_position_Y + self.vaisseau_direction_Y > 520 or self.vaisseau_position_Y + self.vaisseau_direction_Y < 10:#si l'addition des direction aux positions ont un résultat est supérieur à 720 et inférieur à 10 l'action ci dessous sera annulé 
                self.vaisseau_direction_Y = 0

                        
            if self.vaisseau_position_Y2 + self.vaisseau_direction_Y2 > 520 or self.vaisseau_position_Y2 + self.vaisseau_direction_Y2 < 10:#si l'addition des direction aux positions ont un résultat est supérieur à 720 et inférieur à 10 l'action ci dessous sera annulé 
                self.vaisseau_direction_Y2 = 0
                
            self.vaisseau_position_Y += self.vaisseau_direction_Y #addition des coordonnés pour déplacer le vaisseau
            self.vaisseau_position_Y2 += self.vaisseau_direction_Y2 #addition des coordonnés pour déplacer le vaisseau
            
            self.ecran.blit(self.skin_vaisseau, (self.vaisseau_position_X, self.vaisseau_position_Y))#affichage du vaisseau au nouvelle coordonées
            self.ecran.blit(self.skin_vaisseau2, (self.vaisseau_position_X2, self.vaisseau_position_Y2))#affichage du vaisseau au nouvelle coordonées
            
            self.ecran.blit(self.background, (0,0))#affichage du fond d'écran
            self.ecran.blit(self.skin_Balle, (self.Balle_position_X, self.Balle_position_Y))#affichage de la balle
            self.ecran.blit(self.skin_Balle2, (self.Balle_position_X2, self.Balle_position_Y2))#affichage de la Balle
####################################################################################################################################################################################################################################################

        def Test_evenementANDaffichage_BallePLUSVaisseau(self):#Test de chaque touche et action plus affichage 
            
            self.ecran.blit(self.skin_vaisseau, (self.vaisseau_position_X, self.vaisseau_position_Y))#affichage du vaisseau
            self.ecran.blit(self.skin_Balle, (self.Balle_position_X, self.Balle_position_Y))#affichage de la Balle
                
            for evenement in pygame.event.get():#Test tout les évenement
                
                if evenement.type == pygame.QUIT:#si la croix est cliqué
                    sys.exit()#ferme le jeu

                if evenement.type == pygame.KEYDOWN:#si une touche est appuyé
                        
                    if evenement.key == pygame.K_RIGHT:#si cette touche est la fleche droite
                        self.vaisseau_direction_X = 5 #change la variable direction qui s'additionera à la position du vaisseau pour le déplacer

                    if evenement.key == pygame.K_LEFT:#si cette touche est la fleche gauche
                        self.vaisseau_direction_X = -5#change la variable direction qui s'additionera à la position du vaisseau pour le déplacer
                        
                    if evenement.key == pygame.K_SPACE :#touche espace tapée
                        #self.BalleSon.play()#joue le son de la balle 
                        self.mvtballe=True #met l'obus en mode FEU
                        self.stats_Tir += 1#compte le nombre de fois tirés 
                
                if evenement.type == pygame.KEYUP: #Touche relachée ( si je ne mets pas le test de cette évenements le vaisseau avancerais vers un coté sans s'arreter dès que l'on apuirais sur une touche )
                    if evenement.key == pygame.K_RIGHT or evenement.key == pygame.K_LEFT : #si cette touche est gauche ou droite
                        self.vaisseau_direction_X = 0 #réinitialise les variables direction 
                        self.vaisseau_direction_Y = 0
                        
            if self.vaisseau_position_X + self.vaisseau_direction_X > 720 or self.vaisseau_position_X + self.vaisseau_direction_X < 10:#si l'addition des direction aux positions ont un résultat est supérieur à 720 et inférieur à 10 l'action ci dessous sera annulé 
                self.vaisseau_direction_X = 0
                
            self.vaisseau_position_X += self.vaisseau_direction_X #addition des coordonnés pour déplacer le vaisseau
            self.ecran.blit(self.skin_vaisseau, (self.vaisseau_position_X, self.vaisseau_position_Y))#affichage du vaisseau au nouvelle coordonées
            
            self.ecran.blit(self.background, (0,0))#affichage du fond d'écran
            self.ecran.blit(self.skin_Balle, (self.Balle_position_X, self.Balle_position_Y))#affichage de la balle
            
        def level_Lancé(self):#fonction qui créer les niveaux
            
            if self.level_Lancé == 1: #si niveau 1 sélectionner
                Mouvement_Ennemi_GD(self)#lance la fonction du première alien
                if self.score >= 12:#si le score = 12 
                              
                    Titre = pygame.font.Font('freesansbold.ttf', 48)#création du type d'ecriture et de police
                    message = Titre.render("Niveau 1 Réussi", True, (0,255,0))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (230, 135))  # affichage du message aux coordonnées
                    stats = pygame.font.Font('freesansbold.ttf', 28)#création du type d'ecriture et de police
                    message = stats.render(f"Nombre de fois tirés : {self.stats_Tir}", True, (255,255,255))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (240, 250))  # affichage du message aux coordonnées
                    
                    
                    pygame.display.update()#mise à jour de l'écran
                    time.sleep(4) #pause de l'écran pendant 4 secondes
                    self.jeu_encours = False #désactive le Jeu
                    self.mvtballe = False #la balle s'arrete et revient au vaisseau
                    self.Menu = True #active le Menu Principal
                    
            if self.level_Lancé == 2:#si niveau 2 sélectionner
                Mouvement_Ennemi_HB(self)#lance la fonction du 2eme alien
                if self.score >= 25:
                              
                    Titre = pygame.font.Font('freesansbold.ttf', 48)#création du type d'ecriture et de police
                    message = Titre.render("Niveau 2 Réussi", True, (0,255,0))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (230, 135))  # affichage du message aux coordonnées
                    stats = pygame.font.Font('freesansbold.ttf', 28)#création du type d'ecriture et de police
                    message = stats.render(f"Nombre de fois tirés : {self.stats_Tir}", True, (255,255,255))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (240, 250))  # affichage du message aux coordonnées

                    pygame.display.update()#mise à jour de l'écran
                    time.sleep(4) #pause de l'écran pendant 4 secondes
                    self.jeu_encours = False #désactive le Jeu
                    self.mvtballe = False #la balle s'arrete et revient au vaisseau
                    self.Menu = True #active le Menu Principal
                    
            if self.level_Lancé == 3:#si niveau 3 sélectionner
                Mouvement_Ennemi_HB(self)#lance la fonction du 2eme alien
                if self.score >=10:
                    Mouvement_Ennemi_GD(self)#lance la fonction du première alien
                    if self.score >= 40:
                        
                        Titre = pygame.font.Font('freesansbold.ttf', 48)#création du type d'ecriture et de police
                        message = Titre.render("Niveau 3 Réussi", True, (0,255,0))#création du texte en Gras ou pas et de la couleur
                        self.ecran.blit(message, (230, 135))  # affichage du message aux coordonnées
                        stats = pygame.font.Font('freesansbold.ttf', 28)#création du type d'ecriture et de police
                        message = stats.render(f"Nombre de fois tirés : {self.stats_Tir}", True, (255,255,255))#création du texte en Gras ou pas et de la couleur
                        self.ecran.blit(message, (240, 250))  # affichage du message aux coordonnées
                        
                        pygame.display.update()#mise à jour de l'écran
                        time.sleep(4) #pause de l'écran pendant 4 secondes
                        self.jeu_encours = False #désactive le Jeu
                        self.mvtballe = False #la balle s'arrete et revient au vaisseau
                        self.Menu = True #active le Menu Principal
                        
            if self.level_Lancé == 4:#si niveau 4 sélectionner
                Mouvement_Ennemi_Diago(self)#lance la fonction du 3eme alien
                if self.score >= 30:
                        Titre = pygame.font.Font('freesansbold.ttf', 48)#création du type d'ecriture et de police
                        message = Titre.render("Niveau 4 Réussi", True, (0,255,0))#création du texte en Gras ou pas et de la couleur
                        self.ecran.blit(message, (230, 135))  # affichage du message aux coordonnées
                        stats = pygame.font.Font('freesansbold.ttf', 28)#création du type d'ecriture et de police
                        message = stats.render(f"Nombre de fois tirés : {self.stats_Tir}", True, (255,255,255))#création du texte en Gras ou pas et de la couleur
                        self.ecran.blit(message, (240, 250))  # affichage du message aux coordonnées
                        
                        pygame.display.update()#mise à jour de l'écran
                        time.sleep(4) #pause de l'écran pendant 4 secondes
                        self.jeu_encours = False #désactive le Jeu
                        self.mvtballe = False #la balle s'arrete et revient au vaisseau
                        self.Menu = True #active le Menu Principal
                        
            if self.level_Lancé == 5:#si niveau 5 sélectionner
                Mouvement_Ennemi_HB(self)#lance la fonction du 2eme alien
                if self.score >=15:
                    Mouvement_Ennemi_GD(self) #lance la fonction du première alien
                    if self.score >= 25:
                        Mouvement_Ennemi_Diago(self)#lance la fonction du 3eme alien
                        if self.score >= 80:

                            Titre = pygame.font.Font('freesansbold.ttf', 48)#création du type d'ecriture et de police
                            message = Titre.render("Niveau 5 Réussi", True, (0,255,0))#création du texte en Gras ou pas et de la couleur
                            self.ecran.blit(message, (230, 135))  # affichage du message aux coordonnées
                            stats = pygame.font.Font('freesansbold.ttf', 28)#création du type d'ecriture et de police
                            message = stats.render(f"Nombre de fois tirés : {self.stats_Tir}", True, (255,255,255))#création du texte en Gras ou pas et de la couleur
                            self.ecran.blit(message, (240, 250))  # affichage du message aux coordonnées
                            
                            pygame.display.update()#mise à jour de l'écran
                            time.sleep(4) #pause de l'écran pendant 4 secondes
                            self.jeu_encours = False #désactive le Jeu
                            self.mvtballe = False #la balle s'arrete et revient au vaisseau
                            self.Menu = True #active le Menu Principal
                            
            if self.level_Lancé == 6:#si niveau 6 sélectionner
                Mouvement_Ennemi_HB(self)#lance la fonction du 2eme alien
                Mouvement_Ennemi_GD(self)#lance la fonction du première alien
                Mouvement_Ennemi_Diago(self)#lance la fonction du 3eme alien
            


            
        while self.allMenu:#Boucle qui chargera chaque Menu
            
            while self.Menu :#boucle du menu Principal
            
                Test_evenementANDaffichage_BallePLUSVaisseau(self)#lancement de fonction créer auparavant 
                collision_Menu(self,self.level_selectionner,self.Balle_position_X,self.Balle_position_Y)
                modeballe(self)
            
                Titre = pygame.font.Font('freesansbold.ttf', 48)#création du type d'ecriture et de police
                message = Titre.render("Welcome to my SPACE INVADERS", True, (255,0,0))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (0, 5))  # affichage du message aux coordonnées
            
                créer = pygame.font.Font('freesansbold.ttf', 18)#création du type d'ecriture et de police
                message = créer.render("Made by Riwal Fortin with the help of Mr.DAVIAUD and Mr.GARIN ", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (118, 70))  # affichage du message aux coordonnées*
            
                utiliser = pygame.font.Font('freesansbold.ttf', 18)#création du type d'ecriture et de police
                message = utiliser.render("Déplacer votre vaisseau et tirer sur chaque bouton pour les utiliser ;)", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (100, 100))  # affichage du message aux coordonnées
            
                gamelevel = pygame.font.Font('freesansbold.ttf', 18)#création du type d'ecriture et de police
                message = gamelevel.render("Choix du niveau", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (84, 400))  # affichage du message aux coordonnées
            
                play = pygame.font.Font('freesansbold.ttf', 18)#création du type d'ecriture et de police
                message = play.render("Play", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (304, 400))  # affichage du message aux coordonnées
                
                play = pygame.font.Font('freesansbold.ttf', 18)#création du type d'ecriture et de police
                message = play.render("1v1", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (470, 400))  # affichage du message aux coordonnées
                
                play = pygame.font.Font('freesansbold.ttf', 18)#création du type d'ecriture et de police
                message = play.render("Choix du Vaisseau", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (560, 400))  # affichage du message aux coordonnées
            
                self.ecran.blit(self.skin_vaisseau, (self.vaisseau_position_X, self.vaisseau_position_Y))#affichage du vaisseau
                self.ecran.blit(self.play_button, (260, 250))#affichage du boutton play
                self.ecran.blit(self.game_level, (90, 250))#affichage du boutton choix niveau
                self.ecran.blit(self.Skin_level, (580, 250))#affichage du boutton choix vaisseau
                self.ecran.blit(self.one_level, (420, 250))#affichage du boutton choix vaisseau
                
                if self.level_selectionner == 0:#Vérifie si un niveau est sélectionner
                    play = pygame.font.Font('freesansbold.ttf', 18)#création du type d'ecriture et de police
                    message = play.render(f"Veuillez sélectionnez un niveau", False, (255,0,0))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (270, 160))  # affichage du message aux coordonnées
                    
                if self.level_selectionner > 0:#si un niveau est sélectionner alors
                    if self.level_selectionner == 6:#si le mode infinie est choisis
                        play = pygame.font.Font('freesansbold.ttf', 18)#création du type d'ecriture et de police
                        message = play.render(f"Mode Infinie Sélectionner", False, (0,0,255))#création du texte en Gras ou pas et de la couleur
                        self.ecran.blit(message, (290, 160))  # affichage du message aux coordonnées
                        self.level_Lancé = self.level_selectionner#sert à lancé le bon niveau
                    else:#sinon                         
                        play = pygame.font.Font('freesansbold.ttf', 18)#création du type d'ecriture et de police
                        message = play.render(f"Level {self.level_selectionner} Sélectionner", False, (0,255,0))#création du texte en Gras ou pas et de la couleur
                        self.ecran.blit(message, (315, 160))  # affichage du message aux coordonnées
                        self.level_Lancé = self.level_selectionner#sert à lancé le bon niveau
            
                pygame.display.flip() #création d'une boucle
            
            
            while self.Menu_level :#boucle du menu level

                Test_evenementANDaffichage_BallePLUSVaisseau(self)#lancement de fonction créer auparavant 
                modeballe(self)
                collision_Menu_level (self,self.Balle_position_X,self.Balle_position_Y)
            
                self.ecran.blit(self.skin_vaisseau, (self.vaisseau_position_X, self.vaisseau_position_Y))# affichage du vaisseau
            
                Titre = pygame.font.Font('freesansbold.ttf', 48)#création du type d'ecriture et de police
                message = Titre.render("Choix du Niveaux", True, (255,0,0))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (190, 5))  # affichage du message aux coordonnées
            
                utiliser = pygame.font.Font('freesansbold.ttf', 18)#création du type d'ecriture et de police
                message = utiliser.render("Déplacer votre vaisseau et tirer sur une case pour selectionner un Niveau", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (80, 80))  # affichage du message aux coordonnées
                
                #if self.score_level == 0:
                
                if self.level_selectionner == 0:#Si aucun niveau n'est s'électionner
                    pygame.draw.rect(self.ecran,(255,255,255),(0,100,100,200),3)#création d'un rectangle+affichage du rectangle
                    LVL = pygame.font.Font('freesansbold.ttf', 15)#création du type d'ecriture et de police
                    message = LVL.render("Niveau 1", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (17, 150))  # affichage du message aux coordonnées
                    pygame.draw.rect(self.ecran,(255,255,255),(100,100,100,200),3)#création d'un rectangle+affichage du rectangle
                    message = LVL.render("Niveau 2", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (117, 150))  # affichage du message aux coordonnées
                    pygame.draw.rect(self.ecran,(255,255,255),(200,100,100,200),3)#création d'un rectangle+affichage du rectangle
                    message = LVL.render("Niveau 3", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (217, 150))  # affichage du message aux coordonnées
                    pygame.draw.rect(self.ecran,(255,255,255),(300,100,100,200),3)#création d'un rectangle+affichage du rectangle
                    message = LVL.render("Niveau 4", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (317, 150))  # affichage du message aux coordonnées
                    pygame.draw.rect(self.ecran,(255,255,255),(400,100,100,200),3)#création d'un rectangle+affichage du rectangle
                    message = LVL.render("Niveau 5", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (417, 150))  # affichage du message aux coordonnées
                    pygame.draw.rect(self.ecran,(255,255,255),(500,100,100,200),3)#création d'un rectangle+affichage du rectangle
                    message = LVL.render("Mode Infini", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (508, 150))  # affichage du message aux coordonnées
                    
                pygame.draw.rect(self.ecran,(255,255,255),(600,100,100,200),3)#création d'un rectangle+affichage du rectangle
                message = LVL.render("Réinitialiser", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (605, 150))  # affichage du message aux coordonnées
                pygame.draw.rect(self.ecran,(255,255,255),(700,100,100,200),3)#création d'un rectangle+affichage du rectangle
                message = LVL.render("Retour Menu", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (703, 150))  # affichage du message aux coordonnées
                    
                if self.level_selectionner == 1:#si le niveau 1 est sélectionner
                    pygame.draw.rect(self.ecran,(0,255,0),(0,100,100,200),3)#création d'un rectangle+affichage du rectangle
                    LVL = pygame.font.Font('freesansbold.ttf', 15)#création du type d'ecriture et de police
                    message = LVL.render("Niveau 1", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (17, 150))  # affichage du message aux coordonnées
                    
                if self.level_selectionner == 2:#si le niveau 2 est sélectionner
                    pygame.draw.rect(self.ecran,(0,255,0),(100,100,100,200),3)#création d'un rectangle+affichage du rectangle
                    message = LVL.render("Niveau 2", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (117, 150))  # affichage du message aux coordonnées
                
                if self.level_selectionner == 3:#si le niveau 3 est sélectionner
                    pygame.draw.rect(self.ecran,(0,255,0),(200,100,100,200),3)#création d'un rectangle+affichage du rectangle
                    message = LVL.render("Niveau 3", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (217, 150))  # affichage du message aux coordonnées

                if self.level_selectionner == 4:#si le niveau 4 est sélectionner
                    pygame.draw.rect(self.ecran,(0,255,0),(300,100,100,200),3)#création d'un rectangle+affichage du rectangle
                    message = LVL.render("Niveau 4", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (317, 150))  # affichage du message aux coordonnées

                if self.level_selectionner == 5:#si le niveau 5 est sélectionner
                    pygame.draw.rect(self.ecran,(0,255,0),(400,100,100,200),3)#création d'un rectangle+affichage du rectangle
                    message = LVL.render("Niveau 5", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (417, 150))  # affichage du message aux coordonnées

                if self.level_selectionner == 6:#si le niveau 6 est sélectionner
                    pygame.draw.rect(self.ecran,(0,255,0),(500,100,100,200),3)#création d'un rectangle+affichage du rectangle
                    message = LVL.render("Mode Infini", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                    self.ecran.blit(message, (508, 150))  # affichage du message aux coordonnées
                
                if self.level_selectionner == 7: #si la réinitialisation est sélectionner 
                    self.level_selectionner = 0 # execute la même chose que si la boucle était lancé               
                
                
            
                pygame.display.flip() #créer une boucle
                
            while self.Menu_Skin:#création de la boucle choix vaiseau
                
                self.ecran.blit(self.background, (0,0))#affichage fond d'écran 
                Test_evenementANDaffichage_BallePLUSVaisseau(self)#lancement de fonction créer auparavant 
                modeballe(self)
                collision_Menu_Skin(self,self.Balle_position_X,self.Balle_position_Y)
                
                self.ecran.blit(self.skin_vaisseau, (self.vaisseau_position_X, self.vaisseau_position_Y))#affichage du vaisseau
                
                Titre = pygame.font.Font('freesansbold.ttf', 48)#création du type d'ecriture et de police
                message = Titre.render("Choix du Skin", True, (255,0,0))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (210, 5))  # affichage du message aux coordonnées
                
                utiliser = pygame.font.Font('freesansbold.ttf', 18)#création du type d'ecriture et de police
                message = utiliser.render("Déplacer votre vaisseau et tirez sur chaque carré pour modifier votre Vaisseau/Balle", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (37, 80))  # affichage du message aux coordonnées
                
                pygame.draw.rect(self.ecran,(255,0,0),(50,125,200,200),3)#création d'un rectangle+affichage du rectangle
                pygame.draw.rect(self.ecran,(255,0,0),(300,125,200,200),3)#création d'un rectangle+affichage du rectangle
                pygame.draw.rect(self.ecran,(255,0,0),(550,125,200,200),3)#création d'un rectangle+affichage du rectangle
                
                menu = pygame.font.Font('freesansbold.ttf', 25)#création du type d'ecriture et de police
                message = menu.render("MENU", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (618, 200))  # affichage du message aux coordonnées
                
                self.ecran.blit(self.skin_vaisseau2, (117, 190))#affichage du vaisseau dans le rectangle au milieu de l'écran
                self.ecran.blit(self.skin_Balle2, (387, 210))#affichage de la balle dans le rectangle au milieu de l'écran
                
                if self.skin_selectionner == 0:#si le vaisseau sélectionner = 0
                    self.skin_vaisseau = pygame.image.load("vaisseau_bas.png")#importation de l'image (vaisseau)
                    self.skin_vaisseau2 = pygame.image.load("vaisseau_bas.png")#importation de l'image (vaisseau)
                    
                if self.skin_selectionner == 1:#si le vaisseau sélectionner = 1
                    self.skin_vaisseau = pygame.image.load("vaisseau.png")#importation de l'image (vaisseau)
                    self.skin_vaisseau2 = pygame.image.load("vaisseau.png")#importation de l'image (vaisseau)
                    
                if self.skin_selectionner == 2:#si le vaisseau sélectionner = 2
                    self.skin_vaisseau = pygame.image.load("space-invaders orange.png")#importation de l'image (vaisseau)
                    self.skin_vaisseau2 = pygame.image.load("space-invaders orange.png")#importation de l'image (vaisseau)
                    
                if self.Balle_selectionner == 0:#si la balle sélectionner = 0
                    self.skin_Balle = pygame.image.load("balle.png")#importation de l'image 
                    self.skin_Balle2 = pygame.image.load("balle.png")#importation de l'image 
                    
                if self.Balle_selectionner == 1:#si la balle sélectionner = 1
                    self.skin_Balle = pygame.image.load("missile.png")#importation de l'image 
                    self.skin_Balle2 = pygame.image.load("missile.png")#importation de l'image 
                    
                if self.Balle_selectionner == 2:#si la balle sélectionner = 2
                    self.skin_Balle = pygame.image.load("missile 2.png")#importation de l'image 
                    self.skin_Balle2 = pygame.image.load("missile 2.png")#importation de l'image            
                
                pygame.display.update()#mise à jour des images
                pygame.display.flip()#création d'une boucle
                
            while self.Menu_1v1:#création de la boucle choix vaiseau
                
                Test_evenementANDaffichage_BallePLUSVaisseau_1v1(self)#lancement de fonction créer auparavant 
                modeballe_1v1(self)
                self.ecran.blit(self.skin_vaisseau, (self.vaisseau_position_X, self.vaisseau_position_Y))
                self.ecran.blit(self.skin_vaisseau2, (self.vaisseau_position_X2, self.vaisseau_position_Y2))
                
                score = pygame.font.Font('freesansbold.ttf', 18)#création du type d'ecriture et de police
                message = score.render(f"Score Joueur 1 : {self.touchéJ1}", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (630, 0))  # affichage du message aux coordonnées
                
                message = score.render(f"Score Joueur 2 : {self.touchéJ2}", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (5, 0))  # affichage du message aux coordonnées

                
                collision_Jeu_1v1(self,self.Balle_position_X,self.Balle_position_Y)#lancement de fonction créer auparavant 
            
            
                pygame.display.update()#mise à jour des images
                pygame.display.flip()#création d'une boucle
                
            while self.jeu_encours:#création de la boucle du Jeu
            
                Test_evenementANDaffichage_BallePLUSVaisseau(self)#lancement de fonction créer auparavant 
                modeballe(self)
                self.ecran.blit(self.skin_vaisseau, (self.vaisseau_position_X, self.vaisseau_position_Y))
                level_Lancé(self)
                
                score = pygame.font.Font('freesansbold.ttf', 18)#création du type d'ecriture et de police
                message = score.render(f"Score : {self.score}", False, (255,255,255))#création du texte en Gras ou pas et de la couleur
                self.ecran.blit(message, (700, 0))  # affichage du message aux coordonnées
                
                collision_Jeu(self,self.Balle_position_X,self.Balle_position_Y)#lancement de fonction créer auparavant 
            
            
                pygame.display.update()#mise à jour des images
                pygame.display.flip()#création d'une boucle
                
            pygame.display.flip()#création d'une boucle de toutes les boucles
                
                
pygame.init#initialisation de Pygame
Jeu().fonction_principale()#lancement de la fonction Jeu et de la fonction principale