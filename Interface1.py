import pygame

pygame.init()
color_facile = (0, 0, 0)
color_moyen = (0, 0, 0)
color_difficile = (0, 0, 0)
color_diabolique = (0, 0, 0)
taille_ecran_menu = [800*0.66, 800*0.66]
taille_ecran_menu_difficulte = [800*0.66, 800*0.66]
taille_ecran_sudoku = [800*0.66, 800*0.66]
taille_sudoku = [600*0.66,600*0.66]
background_color = (0, 38, 38)
background_color_selection = (0, 58, 58)
taille_police = int(65*0.66)
taille_police_titre = int(80*0.66)
taille_police_button = int(25*0.66)
taille_police_chiffre = int(60*0.66)
police_ecriture_menu = pygame.font.SysFont('Didot', taille_police)
police_ecriture_sudoku = pygame.font.SysFont('Comic sans ms', taille_police_titre)
police_ecriture_button = pygame.font.SysFont('Comic sans ms', taille_police_button)
police_ecriture_chiffre = pygame.font.SysFont('Didot', taille_police_chiffre)
violet = (110, 5, 255)
noir = (0, 0, 0)
blanc = (255, 255, 255)
coor_jouer = (80, 80, 150, 80)
rouge = (255, 0, 0)
blue = (0, 0, 255)
vert = (0, 255, 0)
rouge_clair = (255, 100, 100)
gris_clair = (200, 200, 200)
jaune_orange = (255, 255, 120)
grid=[[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]



class Interface:
    def __init__(self, taille_ecran_menu, police_ecriture_menu, background_color):  # Constructeur de la classe
        self.ecran = pygame.display.set_mode(taille_ecran_menu)
        self.police_ecriture_menu = police_ecriture_menu
        self.background_color = background_color
        self.ecran.fill(background_color)


# create a class menu herited from the class Interface
class Menu(Interface):
    def __init__(self, taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color, color_jouer,
                 color_quitter):
        super().__init__(taille_ecran_menu, police_ecriture_menu, background_color)
        self.color_jouer = color_jouer
        self.color_quitter = color_quitter
        value = police_ecriture_sudoku.render(str("SUDOKU"), True, jaune_orange)
        self.ecran.blit(value, (230*0.66, 50*0.66))
        # pygame.draw.rect(self.ecran, violet, coor_jouer, 0)
        pygame.draw.ellipse(self.ecran, violet, [taille_ecran_menu[1] // 2 - 100, 200*0.66, 300*0.66, 100*0.66], 0)
        pygame.draw.ellipse(self.ecran, violet, [taille_ecran_menu[1] // 2 - 100, 350*0.66, 300*0.66, 100*0.66], 0)
        value = police_ecriture_menu.render(str("Jouer"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 80*0.66 - 100, 225*0.66))
        value = police_ecriture_menu.render(str("Jouer"), True, self.color_jouer)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 85*0.66 - 100, 225*0.66 + 3))

        value = police_ecriture_menu.render(str("Quitter"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 65*0.66 - 100, 375*0.66))
        value = police_ecriture_menu.render(str("Quitter"), True, self.color_quitter)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 70*0.66 - 100, 375*0.66 + 3))

# creat a class Menu_mode herited from the class Interface with 2 buttons (importer et générer)
class Menu_mode(Interface):
    def __init__(self, taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color, color_importer,
                 color_generer):
        super().__init__(taille_ecran_menu, police_ecriture_menu, background_color)
        self.color_importer = color_importer
        self.color_generer = color_generer
        value = police_ecriture_sudoku.render(str("SUDOKU"), True, jaune_orange)
        self.ecran.blit(value, (230*0.66, 50*0.66))
        # pygame.draw.rect(self.ecran, violet, coor_jouer, 0)
        pygame.draw.ellipse(self.ecran, violet, [taille_ecran_menu[1] // 2 - 100, 200*0.66, 300*0.66, 100*0.66], 0)
        pygame.draw.ellipse(self.ecran, violet, [taille_ecran_menu[1] // 2 - 100, 350*0.66, 300*0.66, 100*0.66], 0)
        value = police_ecriture_menu.render(str("Importer"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 65*0.66 - 100, 225*0.66))
        value = police_ecriture_menu.render(str("Importer"), True, self.color_importer)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 70*0.66 - 100, 225*0.66 + 3))

        value = police_ecriture_menu.render(str("Générer"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 65*0.66 - 100, 375*0.66))
        value = police_ecriture_menu.render(str("Générer"), True, self.color_generer)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 70*0.66 - 100, 375*0.66 + 3))

        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_menu[0] - 100*0.66, taille_ecran_menu[1] - 30*0.66, 100*0.66, 30*0.66), 0)
        value = police_ecriture_button.render(str("Retour"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu[0] - 95*0.66, taille_ecran_menu[1] - 35*0.66))


# creat the class Menu_difficulte herited from the class Interface
class Menu_difficulte(Interface):
    def __init__(self, taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color, color_facile,
                 color_moyen, color_difficile, color_diabolique):
        super().__init__(taille_ecran_menu, police_ecriture_menu, background_color)
        self.color_facile = color_facile
        self.color_moyen = color_moyen
        self.color_difficile = color_difficile
        self.color_diabolique = color_diabolique
        value = police_ecriture_sudoku.render(str("SUDOKU"), True, jaune_orange)
        self.ecran.blit(value, (230*0.66, 50*0.66))
        # pygame.draw.rect(self.ecran, violet, coor_jouer, 0)
        pygame.draw.ellipse(self.ecran, violet, [taille_ecran_menu_difficulte[1] / 3.2, 200*0.66, 300*0.66, 100*0.66], 0)
        pygame.draw.ellipse(self.ecran, violet, [taille_ecran_menu_difficulte[1] / 3.2, 350*0.66, 300*0.66, 100*0.66], 0)
        pygame.draw.ellipse(self.ecran, violet, [taille_ecran_menu_difficulte[1] / 3.2, 500*0.66, 300*0.66, 100*0.66], 0)
        pygame.draw.ellipse(self.ecran, violet, [taille_ecran_menu_difficulte[1] / 3.2, 650*0.66, 300*0.66, 100*0.66], 0)

        value = police_ecriture_menu.render(str("Facile"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 80*0.66, 225*0.66))
        value = police_ecriture_menu.render(str("Facile"), True, self.color_facile)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 85*0.66, 225*0.66 + 3))

        value = police_ecriture_menu.render(str("Moyen"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 80*0.66, 375*0.66))
        value = police_ecriture_menu.render(str("Moyen"), True, self.color_moyen)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 85*0.66, 375*0.66 + 3))

        value = police_ecriture_menu.render(str("Difficile"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 65*0.66, 525*0.66))
        value = police_ecriture_menu.render(str("Difficile"), True, self.color_difficile)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 70*0.66, 525*0.66 + 3))

        value = police_ecriture_menu.render(str("Diabolique"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 30*0.66, 675*0.66))
        value = police_ecriture_menu.render(str("Diabolique"), True, self.color_diabolique)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + +35*0.66, 675*0.66 + 3))

        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_sudoku[0] - 100*0.66, taille_ecran_sudoku[1] - 30*0.66, 100*0.66, 30*0.66), 0)
        value = police_ecriture_button.render(str("Retour"), True, noir)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 95*0.66, taille_ecran_sudoku[1] - 35*0.66))

class Menu_difficulte(Interface):
    def __init__(self, taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color, color_facile,
                 color_moyen, color_difficile, color_diabolique):
        super().__init__(taille_ecran_menu, police_ecriture_menu, background_color)
        self.color_facile = color_facile
        self.color_moyen = color_moyen
        self.color_difficile = color_difficile
        self.color_diabolique = color_diabolique
        value = police_ecriture_sudoku.render(str("SUDOKU"), True, jaune_orange)
        self.ecran.blit(value, (230*0.66, 50*0.66))
        # pygame.draw.rect(self.ecran, violet, coor_jouer, 0)
        pygame.draw.ellipse(self.ecran, violet, [taille_ecran_menu_difficulte[1] / 3.2, 200*0.66, 300*0.66, 100*0.66], 0)
        pygame.draw.ellipse(self.ecran, violet, [taille_ecran_menu_difficulte[1] / 3.2, 350*0.66, 300*0.66, 100*0.66], 0)
        pygame.draw.ellipse(self.ecran, violet, [taille_ecran_menu_difficulte[1] / 3.2, 500*0.66, 300*0.66, 100*0.66], 0)
        pygame.draw.ellipse(self.ecran, violet, [taille_ecran_menu_difficulte[1] / 3.2, 650*0.66, 300*0.66, 100*0.66], 0)

        value = police_ecriture_menu.render(str("Facile"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 80*0.66, 225*0.66))
        value = police_ecriture_menu.render(str("Facile"), True, self.color_facile)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 85*0.66, 225*0.66 + 3))

        value = police_ecriture_menu.render(str("Moyen"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 80*0.66, 375*0.66))
        value = police_ecriture_menu.render(str("Moyen"), True, self.color_moyen)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 85*0.66, 375*0.66 + 3))

        value = police_ecriture_menu.render(str("Difficile"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 65*0.66, 525*0.66))
        value = police_ecriture_menu.render(str("Difficile"), True, self.color_difficile)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 70*0.66, 525*0.66 + 3))

        value = police_ecriture_menu.render(str("Diabolique"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 30*0.66, 675*0.66))
        value = police_ecriture_menu.render(str("Diabolique"), True, self.color_diabolique)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + +35*0.66, 675*0.66 + 3))

        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_sudoku[0] - 100*0.66, taille_ecran_sudoku[1] - 30*0.66, 100*0.66, 30*0.66), 0)
        value = police_ecriture_button.render(str("Retour"), True, noir)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 95*0.66, taille_ecran_sudoku[1] - 35*0.66))


# creat the class Sudoku herited from the class Interface, contains a grid of 9x9 squares at the coordinates 100,100 from pygame draw
class Sudoku(Interface):
    def __init__(self, taille_ecran_sudoku, grid):
        super().__init__(taille_ecran_sudoku, police_ecriture_menu, background_color)
        self.grid = grid
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(self.ecran, noir, (100*0.66, 100*0.66 + i * taille_sudoku[1] // 9),
                                 (100*0.66 + 9 * taille_sudoku[0] // 9, 100*0.66 + i * taille_sudoku[1] // 9), 5)
                pygame.draw.line(self.ecran, noir, (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66),
                                 (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66 + 9 * taille_sudoku[1] // 9), 5)
            else:
                pygame.draw.line(self.ecran, noir, (100*0.66, 100*0.66 + i * taille_sudoku[1] // 9),
                                 (100*0.66 + 9 * taille_sudoku[0] // 9, 100*0.66 + i * taille_sudoku[1] // 9), 1)
                pygame.draw.line(self.ecran, noir, (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66),
                                 (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66 + 9 * taille_sudoku[1] // 9), 1)
        # bouton retour
        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_sudoku[0] - 100*0.66, taille_ecran_sudoku[1] - 30*0.66, 100*0.66, 30*0.66), 0)
        value = police_ecriture_button.render(str("Retour"), True, noir)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 95*0.66, taille_ecran_sudoku[1] - 35*0.66))
        # bouton solve
        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_sudoku[0] - 210*0.66, taille_ecran_sudoku[1] - 30*0.66, 110*0.66, 30*0.66), 0)
        value = police_ecriture_button.render(str("Résoudre"), True, noir)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 210*0.66, taille_ecran_sudoku[1] - 35*0.66))

        # affiche la grille de sudoku
        for i in range(0, 9):
            for j in range(0, 9):
                if self.grid[i][j] != 0:
                    value = police_ecriture_chiffre.render(str(self.grid[i][j]), True, noir)
                    self.ecran.blit(value, (100*0.66 + (j + 0.35) * taille_sudoku[0] // 9, 100*0.66 + ( i + 0.25 ) * taille_sudoku[1] // 9))

class SudokuImporter(Interface):
    def __init__(self, taille_ecran_sudoku, grid, nombrevie=None):
        super().__init__(taille_ecran_sudoku, police_ecriture_menu, background_color)
        self.grid = grid
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(self.ecran, noir, (100*0.66, 100*0.66 + i * taille_sudoku[1] // 9),
                                 (100*0.66 + 9 * taille_sudoku[0] // 9, 100*0.66 + i * taille_sudoku[1] // 9), 5)
                pygame.draw.line(self.ecran, noir, (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66),
                                 (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66 + 9 * taille_sudoku[1] // 9), 5)
            else:
                pygame.draw.line(self.ecran, noir, (100*0.66, 100*0.66 + i * taille_sudoku[1] // 9),
                                 (100*0.66 + 9 * taille_sudoku[0] // 9, 100*0.66 + i * taille_sudoku[1] // 9), 1)
                pygame.draw.line(self.ecran, noir, (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66),
                                 (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66 + 9 * taille_sudoku[1] // 9), 1)
        # bouton retour
        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_sudoku[0] - 100*0.66, taille_ecran_sudoku[1] - 30*0.66, 100*0.66, 30*0.66), 0)
        value = police_ecriture_button.render(str("Retour"), True, noir)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 90*0.66, taille_ecran_sudoku[1] - 35*0.66))
        # bouton solve
        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_sudoku[0] - 225*0.66, taille_ecran_sudoku[1] - 30*0.66, 110*0.66, 30*0.66), 0)
        value = police_ecriture_button.render(str("Résoudre"), True, noir)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 225*0.66, taille_ecran_sudoku[1] - 35*0.66))
        # bouton importer
        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_sudoku[0] - 350*0.66, taille_ecran_sudoku[1] - 30*0.66, 110*0.66, 30*0.66), 0)
        value = police_ecriture_button.render(str("Importer"), True, noir)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 345*0.66, taille_ecran_sudoku[1] - 35*0.66))
        # affiche la grille de sudoku
        for i in range(0, 9):
            for j in range(0, 9):
                if self.grid[i][j] != 0:
                    value = police_ecriture_chiffre.render(str(self.grid[i][j]), True, noir)
                    self.ecran.blit(value, (100*0.66 + (j + 0.35) * taille_sudoku[0] // 9, 100*0.66 + ( i + 0.25 ) * taille_sudoku[1] // 9))
        # affiche le nombre de vie
        value = police_ecriture_button.render(str("Vies restantes :") + str(nombrevie), True, noir)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 705 * 0.66, taille_ecran_sudoku[1] - 35 * 0.66))








