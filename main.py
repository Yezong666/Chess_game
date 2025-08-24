import pygame
from chessboard import Chess_board

#temporary consts
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

def main():
    #Init part
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    x = SCREEN_WIDTH / 2    #width screen game
    y = SCREEN_HEIGHT / 2   #height screen game

    chess_board = Chess_board()
    chess_board.draw(screen)
    dt = 0
    while(1):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            
        #pygame.Surface.fill(screen, (0,0,0))
           
        
        pygame.display.flip()
        
        
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
