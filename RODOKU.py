import random
from random import shuffle
from Interface import *
import numpy as np
pygame.init()

if __name__ == '__main__':
    ecran = pygame.display.set_mode(taille_ecran_menu)
    ecran.fill(background_color)

selected = "Jouer"
MENU = True
SUDOKU = False
MENU_DIFFICULTE = False
MENU_MODE = False
color_jouer, color_quitter = rouge_clair, blanc
color_facile, color_moyen, color_difficile, color_diabolique = rouge_clair, blanc, blanc, blanc
color_importer, color_generer = rouge_clair, blanc

def possible(y,x,n,grid):
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid[i][x] == n:
            return False
    x0 = ( x // 3)*3 # renvoi les coordonnee du coin haut gauche du bloc de 3
    y0 = ( y // 3)*3 #
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def Solve(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n,grid):
                        grid[y][x] = n
                        yield from Solve(grid)
                        grid[y][x] = 0
                return
    yield (grid)

def Generate_grid(grid=None):
    if grid is None:
        grid = [[0 for x in range(9)] for y in range(9)]
        grid[random.randint(0,8)][random.randint(0,8)] = random.randint(1,9)
    I, J, N = list(range(9)), list(range(9)), list(range(1,10))
    shuffle(I)
    shuffle(J)
    shuffle(N)
    for i in I:
        for j in J:
            if grid[i][j] == 0:
                for n in N:
                    if possible(i,j,n,grid):
                        grid[i][j] = n
                        Generate_grid(grid)
                        grid[i][j] = 0
                return
    return grid


if __name__ == '__main__':
    while True:
        if MENU:
            menu = Menu(taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color, color_jouer,
                        color_quitter)
            pygame.display.flip()  # Actualise lecran
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # quit game if a click collide the elipse button at [taille_ecran_menu[1] // 2, 350, 300, 100]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if pygame.draw.ellipse(pygame.display.set_mode(taille_ecran_menu), violet,
                                               [taille_ecran_menu[1] // 2, 350*0.66, 300*0.66, 100*0.66], 0).collidepoint(event.pos):
                            pygame.quit()
                            quit()
                        if pygame.draw.ellipse(pygame.display.set_mode(taille_ecran_menu), violet,
                                               [taille_ecran_menu[1] // 2, 200*0.66, 300*0.66, 100*0.66], 0).collidepoint(event.pos):
                            MENU = False
                            MENU_MODE = True
                            MENU_DIFFICULTE = False
                            SUDOKU = False
                            selected = "facile"
                # on scroll up or down
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        if selected == "Jouer":
                            selected = "Quitter"
                        elif selected == "Quitter":
                            selected = "Jouer"
                    if event.button == 5:
                        if selected == "Jouer":
                            selected = "Quitter"
                        elif selected == "Quitter":
                            selected = "Jouer"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_z:
                        selected = "Jouer"
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        selected = "Quitter"
                    if event.key == pygame.K_RETURN:
                        if selected == "Quitter":
                            pygame.quit()
                            quit()
                    if event.key == pygame.K_RETURN and selected == "Quitter":
                        pygame.quit()
                    elif event.key == pygame.K_RETURN and selected == "Jouer":
                        MENU = False
                        MENU_MODE = True
                        MENU_DIFFICULTE = False
                        SUDOKU = False
                        selected = "facile"

            if selected == "Jouer":
                color_jouer, color_quitter = rouge_clair, blanc
            elif selected == "Quitter":
                color_jouer, color_quitter = blanc, rouge_clair

        if MENU_MODE:
            menu_mode = Menu_mode(taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color,color_importer, color_generer)
            pygame.display.flip()  # Actualise lecran
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        if pos[0] > taille_ecran_menu[0] - 100*0.66 and pos[1] > taille_ecran_menu[1] - 30*0.66:
                            selected = "Jouer"
                            MENU = True
                            MENU_MODE = False
                            SUDOKU = False
                            MENU_DIFFICULTE = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        if selected == "importer":
                            selected = "générer"
                        elif selected == "générer":
                            selected = "importer"
                    elif event.button == 5:
                        if selected == "importer":
                            selected = "générer"
                        elif selected == "générer":
                            selected = "importer"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_z:
                        selected = "importer"
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        selected = "générer"
                    if event.key == pygame.K_RETURN:
                        if selected == "générer":
                            MENU_MODE = False
                            MENU_DIFFICULTE = True
                            MENU = False
                            SUDOKU = False
                        elif  selected == "importer":
                            MENU_DIFFICULTE = True
                            MENU_MODE = False
                            MENU = False
                            SUDOKU = False
                            selected = "facile"


                # on click sur le bouton importer
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if pygame.draw.ellipse(pygame.display.set_mode(taille_ecran_menu), violet,
                                               [taille_ecran_menu[1] // 2, 350 * 0.66, 300 * 0.66, 100 * 0.66],
                                               0).collidepoint(event.pos):
                            MENU_MODE = False
                            MENU_DIFFICULTE = True
                            MENU = False
                            SUDOKU = False
                            selected = "facile"
                # on click sur le bouton générer
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if pygame.draw.ellipse(pygame.display.set_mode(taille_ecran_menu), violet,
                                               [taille_ecran_menu[1] // 2, 200 * 0.66, 300 * 0.66, 100 * 0.66],
                                               0).collidepoint(event.pos):
                            MENU_MODE = False
                            MENU_DIFFICULTE = True
                            MENU = False
                            SUDOKU = False
                            selected = "facile"

            if selected == "générer":
                color_importer, color_generer = blanc, rouge_clair
            elif selected == "importer":
                color_importer, color_generer = rouge_clair, blanc


        if MENU_DIFFICULTE:
            menu_difficulte = Menu_difficulte(taille_ecran_menu_difficulte, police_ecriture_menu, police_ecriture_sudoku,
                                              background_color, color_facile, color_moyen, color_difficile,
                                              color_diabolique)
            pygame.display.flip()  # Actualise lecran
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if pygame.draw.ellipse(pygame.display.set_mode(taille_ecran_menu), violet,
                                               [taille_ecran_menu[1] // 2, 200*0.66, 300*0.66, 100*0.66], 0).collidepoint(event.pos):
                            MENU_DIFFICULTE = False
                            SUDOKU = True
                            MENU = False
                            MENU_MODE = False
                            selected = "facile"
                            print(selected)

                        if pygame.draw.ellipse(pygame.display.set_mode(taille_ecran_menu), violet,
                                               [taille_ecran_menu[1] // 2, 350*0.66, 300*0.66, 100*0.66], 0).collidepoint(event.pos):
                            MENU_DIFFICULTE = False
                            SUDOKU = True
                            MENU = False
                            MENU_MODE = False
                            selected = "moyen"
                            print(selected)

                        if pygame.draw.ellipse(pygame.display.set_mode(taille_ecran_menu), violet,
                                               [taille_ecran_menu[1] // 2, 500*0.66, 300*0.66, 100*0.66], 0).collidepoint(event.pos):
                            MENU_DIFFICULTE = False
                            SUDOKU = True
                            MENU = False
                            MENU_MODE = False
                            selected = "difficile"
                            print(selected)

                        if pygame.draw.ellipse(pygame.display.set_mode(taille_ecran_menu), violet,
                                               [taille_ecran_menu[1] // 2, 650*0.66, 300*0.66, 100*0.66], 0).collidepoint(event.pos):
                            MENU_DIFFICULTE = False
                            SUDOKU = True
                            MENU = False
                            MENU_MODE = False
                            selected = "diabolique"
                            print(selected)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        if pos[0] > taille_ecran_sudoku[0] - 100*0.66 and pos[1] > taille_ecran_sudoku[1] - 30*0.66:
                            selected = "Jouer"
                            MENU_DIFFICULTE = False
                            MENU_MODE = True
                            MENU = False
                            SUDOKU = False

                # on scroll down and up
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 5:
                        if selected == "facile":
                            selected = "moyen"
                        elif selected == "moyen":
                            selected = "difficile"
                        elif selected == "difficile":
                            selected = "diabolique"
                        elif selected == "diabolique":
                            selected = "facile"
                    if event.button == 4:
                        if selected == "facile":
                            selected = "diabolique"
                        elif selected == "moyen":
                            selected = "facile"
                        elif selected == "difficile":
                            selected = "moyen"
                        elif selected == "diabolique":
                            selected = "difficile"

                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and selected == "facile":
                        selected = "moyen"
                    elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and selected == "moyen":
                        selected = "difficile"
                    elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and selected == "difficile":
                        selected = "diabolique"
                    elif (event.key == pygame.K_UP or event.key == pygame.K_z) and selected == "diabolique":
                        selected = "difficile"
                    elif (event.key == pygame.K_UP or event.key == pygame.K_z) and selected == "difficile":
                        selected = "moyen"
                    elif (event.key == pygame.K_UP or event.key == pygame.K_z) and selected == "moyen":
                        selected = "facile"
                    if event.key == pygame.K_RETURN:
                        MENU_DIFFICULTE = False
                        SUDOKU = True
                        MENU_MODE = False
                        MENU = False

            if selected == "facile":
                color_facile, color_moyen, color_difficile, color_diabolique = rouge_clair, blanc, blanc, blanc
            elif selected == "moyen":
                color_facile, color_moyen, color_difficile, color_diabolique = blanc, rouge_clair, blanc, blanc
            elif selected == "difficile":
                color_facile, color_moyen, color_difficile, color_diabolique = blanc, blanc, rouge_clair, blanc
            elif selected == "diabolique":
                color_facile, color_moyen, color_difficile, color_diabolique = blanc, blanc, blanc, rouge_clair

        if SUDOKU:
            if selected == "facile":
                grid = Generate_grid()

            elif selected == "moyen":
                grid = Generate_grid()

            elif selected == "difficile":
                grid = Generate_grid()
                selected = "done"

            elif selected == "diabolique":
                grid = Generate_grid()
            elif selected == "done":
                pass

            sudoku = Sudoku(taille_ecran_sudoku, grid)
            pygame.display.flip()  # Actualise lecran
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        if pos[0] > taille_ecran_sudoku[0] - 100*0.66 and pos[1] > taille_ecran_sudoku[1] - 30*0.66:
                            selected = "facile"
                            SUDOKU = False
                            MENU_DIFFICULTE = True
                            MENU = False
                            MENU_MODE = False
