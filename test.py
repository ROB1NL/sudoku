from Interface import *
from Interface import *
pygame.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # quit the game if the user click the button on the bottom right
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if pos[0] > taille_ecran_sudoku[0] - 100 and pos[1] > taille_ecran_sudoku[1] - 30:
                    pygame.quit()
                    quit()


