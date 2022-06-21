import random
from random import shuffle
import tkinter
from tkinter import filedialog
import numpy




def get_path():
    top=tkinter.Tk()
    top.withdraw()
    chemin = filedialog.askopenfilename()
    top.destroy()
    return chemin


def read() :
    i=0
    j=0
    with open(str(get_path()),'r') as doc :
        for line in doc :
            for letter in line.split() :
                if (ord(letter)>= 48 and ord(letter)<=57 ):
                    if (i<=8 and j<=8) :
                        grid[j][i]=ord(letter)-48
                        i+=1
                        if i== 9 :
                            i=0
                            j+=1
                else :
                    print("charactere non valide : ",letter)
    print(grid)
    doc.close()


def solve(grid):
    # Find next empty cell
    findEmpty = emptyCell(grid)

    if not findEmpty:
        return True  # Board is filled
    else:
        row, column = findEmpty

    for i in range(1, 10):
        if isValid(grid, i, (row, column)):
            grid[row][column] = i

            if solve(grid):
                return True

            grid[row][column] = 0

    return False

def isValid2(y,x,n,grid):
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

def isValid(board, num, pos):
    raw = pos[0]
    column = pos[1]
    # Check Row
    for i in range(9):
        if num == board[raw][i]:
            return False
    # Check Column
    for i in range(9):
        if num == board[i][column]:
            return False

    # Check Sub Grid
    subrow = raw // 3
    subcolumn = column // 3

    for i in range(subrow * 3, (subrow * 3) + 3):
        for j in range(subcolumn * 3, (subcolumn * 3) + 3):
            if num == board[i][j]:
                return False
    return True


def emptyCell(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return (row, column)
    return None

import pygame

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
MENU_IMPORTER = False
#definition des couleurs de surbrillance pour afficher la selection
color_jouer, color_quitter = rouge_clair, blanc
color_facile, color_moyen, color_difficile, color_diabolique = rouge_clair, blanc, blanc, blanc
color_importer, color_generer = rouge_clair, blanc


def solve2(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if isValid(y,x,n,grid):
                        grid[y][x] = n
                        yield from solve(grid)
                        grid[y][x] = 0
                return
    yield (grid)

def create_grid():
    grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]
    nb = randint(0,9)
    temp = Liste_grille[nb]
    for i in range(0, 9):
        for j in range(0, 9):
            grid[i][j] = temp[i][j]
    list_nb_utilise =[]
    if selected=="facile": #suppr 44 chiffre
        for k in range(0,45):
            case = randint(0,81)
            while case in list_nb_utilise :
                case = randint(0,81)
            ligne = case//9 -1
            colonne = case%9 -1
            grid[colonne][ligne]=0
            list_nb_utilise.append(case)
    if selected == "moyen" : #suppr 47 chiffre
        for k in range(0,48):
            case = randint(0,81)
            while case in list_nb_utilise :
                case = randint(0,81)
            ligne = case//9 -1
            colonne = case%9 -1
            grid[colonne][ligne]=0
            list_nb_utilise.append(case)
    if selected == "difficile" :#suppr 52 chiffre
        for k in range(0,52):
            case = randint(0,81)
            while case in list_nb_utilise :
                case = randint(0,81)
            ligne = case//9 -1
            colonne = case%9 -1
            grid[colonne][ligne]=0
            list_nb_utilise.append(case)
    if selected == "diabolique" :#suppr 55 chiffre
        for k in range(0,55):
            case = randint(0,81)
            while case in list_nb_utilise :
                case = randint(0,81)
            ligne = case//9 -1
            colonne = case%9 -1
            grid[colonne][ligne]=0
            list_nb_utilise.append(case)
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
                            MENU_IMPORTER = False
                            selected = "importer"
                #On définit le "scroll" pour naviguer dans le menu
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
                #On définit les touches de clavier pour naviguer dans le menu
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
                        MENU_IMPORTER = False
                        selected = "importer"
#Gestion de l'affichage des couleurs pour un effet "surbrillance" sur la selection
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
                        #Bouton retour
                        if pos[0] > taille_ecran_menu[0] - 100*0.66 and pos[1] > taille_ecran_menu[1] - 30*0.66:
                            selected = "Jouer"
                            MENU = True
                            MENU_MODE = False
                            SUDOKU = False
                            MENU_DIFFICULTE = False
                            MENU_IMPORTER = False
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
                            MENU_IMPORTER = False
                            selected = "facile"
                        elif selected == "importer":
                            MENU_DIFFICULTE = False
                            MENU_MODE = False
                            MENU = False
                            SUDOKU = False
                            MENU_IMPORTER = True
                            selected = ""






                # on click sur le bouton importer
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if pygame.draw.ellipse(pygame.display.set_mode(taille_ecran_menu), violet,
                                               [taille_ecran_menu[1] // 2 - 100, 200*0.66, 300*0.66, 100*0.66],
                                               0).collidepoint(event.pos):
                            MENU_MODE = False
                            MENU_DIFFICULTE = False
                            MENU_IMPORTER = True
                            MENU = False
                            SUDOKU = False



                # on click sur le bouton générer
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: #1 correspond au clic gauche
                        if pygame.draw.ellipse(pygame.display.set_mode(taille_ecran_menu), violet,
                                               [taille_ecran_menu[1] // 2 - 100, 350*0.66, 300*0.66, 100*0.66],
                                               0).collidepoint(event.pos):
                            MENU_MODE = False
                            MENU_DIFFICULTE = True
                            MENU = False
                            SUDOKU = False
                            MENU_IMPORTER = False
                            selected = "facile"
#gestion des couleurs pour l'affichage de la selection par "surbrillance"
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
                        #definition des differents boutons selon ou on clique avec sa souris
                        if pygame.draw.ellipse(pygame.display.set_mode(taille_ecran_menu), violet,
                                               [taille_ecran_menu[1] // 2, 200*0.66, 300*0.66, 100*0.66], 0).collidepoint(event.pos):
                            MENU_DIFFICULTE = False
                            SUDOKU = True
                            MENU = False
                            MENU_MODE = False
                            MENU_IMPORTER = False
                            selected = "facile"
                            grid = create_grid()
                            print(selected)

                        if pygame.draw.ellipse(pygame.display.set_mode(taille_ecran_menu), violet,
                                               [taille_ecran_menu[1] // 2, 350*0.66, 300*0.66, 100*0.66], 0).collidepoint(event.pos):
                            MENU_DIFFICULTE = False
                            SUDOKU = True
                            MENU = False
                            MENU_MODE = False
                            MENU_IMPORTER = False
                            selected = "moyen"
                            grid = create_grid()
                            print(selected)

                        if pygame.draw.ellipse(pygame.display.set_mode(taille_ecran_menu), violet,
                                               [taille_ecran_menu[1] // 2, 500*0.66, 300*0.66, 100*0.66], 0).collidepoint(event.pos):
                            MENU_DIFFICULTE = False
                            SUDOKU = True
                            MENU = False
                            MENU_MODE = False
                            MENU_IMPORTER = False
                            selected = "difficile"
                            grid = create_grid()
                            print(selected)

                        if pygame.draw.ellipse(pygame.display.set_mode(taille_ecran_menu), violet,
                                               [taille_ecran_menu[1] // 2, 650*0.66, 300*0.66, 100*0.66], 0).collidepoint(event.pos):
                            MENU_DIFFICULTE = False
                            SUDOKU = True
                            MENU = False
                            MENU_MODE = False
                            MENU_IMPORTER = False
                            selected = "diabolique"
                            grid = create_grid()
                            print(selected)

                #bouton retour pour retourner au menu "mode"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        if pos[0] > taille_ecran_sudoku[0] - 100*0.66 and pos[1] > taille_ecran_sudoku[1] - 30*0.66:
                            selected = "Jouer"
                            MENU_DIFFICULTE = False
                            MENU_MODE = True
                            MENU = False
                            SUDOKU = False
                            MENU_IMPORTER = False


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

                #On definit le deplacement dans le menu avec z et s ou "bas" et "haut"
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
                    #si on presse la touche entree, on entre dans le menu "Sudoku"
                    if event.key == pygame.K_RETURN:
                        grid = create_grid()
                        MENU_DIFFICULTE = False
                        SUDOKU = True
                        MENU_MODE = False
                        MENU = False
                        MENU_IMPORTER = False
            #definition des couleurs de surbrillance pour afficher la selection.
            if selected == "facile":
                color_facile, color_moyen, color_difficile, color_diabolique = rouge_clair, blanc, blanc, blanc
            elif selected == "moyen":
                color_facile, color_moyen, color_difficile, color_diabolique = blanc, rouge_clair, blanc, blanc
            elif selected == "difficile":
                color_facile, color_moyen, color_difficile, color_diabolique = blanc, blanc, rouge_clair, blanc
            elif selected == "diabolique":
                color_facile, color_moyen, color_difficile, color_diabolique = blanc, blanc, blanc, rouge_clair

        if SUDOKU:
            sudoku = Sudoku(taille_ecran_sudoku, grid)
            pygame.display.flip()  # Actualise lecran
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #bouton retour
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        if pos[0] > taille_ecran_sudoku[0] - 100*0.66 and pos[1] > taille_ecran_sudoku[1] - 30*0.66:
                            SUDOKU = False
                            MENU_DIFFICULTE = True
                            MENU = False
                            MENU_MODE = False
                            MENU_IMPORTER = False
                            selected = "facile"
                        #bouton resoudre
                        elif pos[0] > taille_ecran_sudoku[0] - 210 * 0.66 and pos[1] > taille_ecran_sudoku[1] - 30 * 0.66:
                            solve(grid)
                            sudoku = Sudoku(taille_ecran_sudoku, grid)
                            pygame.display.flip()
        if MENU_IMPORTER:
            sudokuimporter = SudokuImporter(taille_ecran_sudoku, grid)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # bouton retour
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        x, y = (pos[0]), (pos[1])
                        if 66 < x < 462 and 66 < y < 462:
                            x, y = (x - 22) // 44, (y - 22) // 44
                            pygame.draw.rect(sudokuimporter.ecran, rouge,
                                             pygame.Rect(x * 44 + 23, y * 44 + 23, 43, 43), 2)
                            pygame.display.update((x * 44 + 23, y * 44 + 23, 43, 43))
                            pygame.event.set_blocked((pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION))
                            pygame.key.set_repeat(1)
                            pygame.event.clear()
                            pygame.event.wait()

                        if pos[0] > taille_ecran_sudoku[0] - 100 * 0.66 and pos[1] > taille_ecran_sudoku[
                            1] - 30 * 0.66:
                            pygame.key.set_repeat(0)
                            SUDOKU = False
                            MENU_DIFFICULTE = False
                            MENU = False
                            MENU_MODE = True
                            MENU_IMPORTER = False
                            selected = "importer"
                            grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
                        # bouton resoudre
                        elif pos[0] > taille_ecran_sudoku[0] - 225 * 0.66 and pos[1] > taille_ecran_sudoku[
                            1] - 30 * 0.66:
                            print(grid)
                            print(solve(grid))
                            print(grid)
                            sudokuimporter = SudokuImporter(taille_ecran_sudoku, grid)
                        # bouton importer
                        elif pos[0] > taille_ecran_sudoku[0] - 350 * 0.66 and pos[1] > taille_ecran_sudoku[
                            1] - 30 * 0.66:
                            read()
                            sudokuimporter = SudokuImporter(taille_ecran_sudoku, grid)
                        else:
                            x = pos[0]
                            y = pos[1]
                            var1 = 0
                            var2 = 0
                            for i in range(0, 10):
                                for j in range(0, 10):
                                    if ((x - 66) // 44 == i) and ((y - 66) // 44 == j):
                                        var1 = i
                                        var2 = j
                for i in range(9):
                    for j in range(9):
                        if grid[i][j] != 0:
                            pygame.draw.rect(sudokuimporter.ecran, background_color_selection,
                                             pygame.Rect(j * 44 + 67, i * 44 + 67, 43, 43), 0)
                            value = police_ecriture_chiffre.render(str(sudokuimporter.grid[i][j]), True, noir)
                            sudokuimporter.ecran.blit(value, (100 * 0.66 + (j + 0.35) * taille_sudoku[0] // 9,
                                                              100 * 0.66 + (i + 0.25) * taille_sudoku[1] // 9))
                for i in range(0, 10):
                    if i % 3 == 0:
                        pygame.draw.line(sudokuimporter.ecran, noir,
                                         (100 * 0.66, 100 * 0.66 + i * taille_sudoku[1] // 9),
                                         (100 * 0.66 + 9 * taille_sudoku[0] // 9,
                                          100 * 0.66 + i * taille_sudoku[1] // 9), 5)
                        pygame.draw.line(sudokuimporter.ecran, noir,
                                         (100 * 0.66 + i * taille_sudoku[0] // 9, 100 * 0.66),
                                         (100 * 0.66 + i * taille_sudoku[0] // 9,
                                          100 * 0.66 + 9 * taille_sudoku[1] // 9), 5)
                    else:
                        pygame.draw.line(sudokuimporter.ecran, noir,
                                         (100 * 0.66, 100 * 0.66 + i * taille_sudoku[1] // 9),
                                         (100 * 0.66 + 9 * taille_sudoku[0] // 9,
                                          100 * 0.66 + i * taille_sudoku[1] // 9), 1)
                        pygame.draw.line(sudokuimporter.ecran, noir,
                                         (100 * 0.66 + i * taille_sudoku[0] // 9, 100 * 0.66),
                                         (100 * 0.66 + i * taille_sudoku[0] // 9,
                                          100 * 0.66 + 9 * taille_sudoku[1] // 9), 1)
                pygame.display.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        value = 1
                        if isValid(grid, value, (var2, var1)):
                            grid[var2][var1] = value
                    if event.key == pygame.K_2:
                        value = 2
                        if isValid(grid, value, (var2, var1)):
                            grid[var2][var1] = value
                    if event.key == pygame.K_3:
                        value = 3
                        if isValid(grid, value, (var2, var1)):
                            grid[var2][var1] = value
                    if event.key == pygame.K_4:
                        value = 4
                        if isValid(grid, value, (var2, var1)):
                            grid[var2][var1] = value
                    if event.key == pygame.K_5:
                        value = 5
                        if isValid(grid, value, (var2, var1)):
                            grid[var2][var1] = value
                    if event.key == pygame.K_6:
                        value = 6
                        if isValid(grid, value, (var2, var1)):
                            grid[var2][var1] = value
                    if event.key == pygame.K_7:
                        value = 7
                        if isValid(grid, value, (var2, var1)):
                            grid[var2][var1] = value
                    if event.key == pygame.K_8:
                        value = 8
                        if isValid(grid, value, (var2, var1)):
                            grid[var2][var1] = value
                    if event.key == pygame.K_9:
                        value = 9
                        if isValid(grid, value, (var2, var1)):
                            grid[var2][var1] = value
                sudokuimporter = SudokuImporter(taille_ecran_sudoku, grid)


















