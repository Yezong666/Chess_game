import pygame
from chessboard import Chess_board

#temporary consts
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

def main():
    #Init part
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    x = SCREEN_WIDTH / 2    #width screen game
    y = SCREEN_HEIGHT / 2   #height screen game

    chess_board = Chess_board()
    chess_board.draw(screen)
    chessboard = chess_board.chessboard
    selected_piece = [False, 0, 0]      #(Piece, x, y)
    possible_moves = []
    dt = 0
    while(1):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_loc = pygame.mouse.get_pos()
                mouse_loc_x = int((mouse_loc[0] - (mouse_loc[0] % 100)) / 100)
                mouse_loc_y = int((mouse_loc[1]  - (mouse_loc[1] % 100)) / 100)
                print(f"mouse_loc_x = {mouse_loc_x}, mouse_loc_y = {mouse_loc_y}, possible_moves = {possible_moves}")
                if (mouse_loc_x, mouse_loc_y) in possible_moves:
                    chess_board.move_piece(screen, chessboard, mouse_loc_x, mouse_loc_y, selected_piece)
                    selected_piece = (False, 0, 0)
                    possible_moves = chess_board.remove_highlighted_moves(screen, chessboard, possible_moves)
                else:
                    selected_piece = chess_board.select_piece(screen, chessboard, mouse_loc_x, mouse_loc_y, selected_piece)
                    possible_moves = chess_board.remove_highlighted_moves(screen, chessboard, possible_moves)
                if selected_piece[0] != False:
                    possible_moves = chess_board.check_moves(screen, chessboard, selected_piece)
        
           
        
        pygame.display.flip()
        
        
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
