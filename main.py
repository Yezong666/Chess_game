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
    turn = 0    #turn % 2 = color turn : 0 = white ; 1 = black
    chessboard_state = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ]
    dt = 0
    while(1):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_loc = pygame.mouse.get_pos()
                mouse_loc_x = int((mouse_loc[0] - (mouse_loc[0] % 100)) / 100)
                mouse_loc_y = int((mouse_loc[1]  - (mouse_loc[1] % 100)) / 100)
                if (mouse_loc_x, mouse_loc_y) in possible_moves:
                    chess_board.move_piece(screen, chessboard, mouse_loc_x, mouse_loc_y, selected_piece)
                    selected_piece = (False, 0, 0)
                    possible_moves = chess_board.remove_highlighted_moves(screen, chessboard, possible_moves)
                    turn+=1
                    chessboard_state = chess_board.get_state(chessboard)
                    chessboard_white_attack = chess_board.white_attack(chessboard)
                    pieces_attacked = chess_board.get_black_pieces_attacked(chessboard, chessboard_white_attack)
                    for piece in pieces_attacked:
                        if piece[0] == "bKi":
                            pass # = King attacked, check if it's a Checkmate, if not do a move to stop the check
                    danger = chess_board.get_black_pieces_attacked(chessboard, chessboard_state)    #If not check, do a move (still not done)
                    print("chessboard_state")
                    for line in chessboard_state:
                        print(line)
                    print("\n")
                    print("chessboard_white_attack")
                    for line in chessboard_white_attack:
                        print(line)
                    print("\n")
                    print(pieces_attacked)
                else:
                    if chessboard[mouse_loc_y][mouse_loc_x][0] == "w":
                        if (turn+1)%2:
                            selected_piece = chess_board.select_piece(screen, chessboard, mouse_loc_x, mouse_loc_y, selected_piece)
                            possible_moves = chess_board.remove_highlighted_moves(screen, chessboard, possible_moves)
                    elif chessboard[mouse_loc_y][mouse_loc_x][0] == "b":
                        if turn%2:
                            selected_piece = chess_board.select_piece(screen, chessboard, mouse_loc_x, mouse_loc_y, selected_piece)
                            possible_moves = chess_board.remove_highlighted_moves(screen, chessboard, possible_moves)
                    else:
                        if selected_piece[0] != False:
                            possible_moves = chess_board.remove_highlighted_moves(screen, chessboard, possible_moves)
                            chess_board.unselect_piece(screen, selected_piece)
                            selected_piece = (False, 0, 0)
                if selected_piece[0] != False:
                    possible_moves = chess_board.check_moves(chessboard, selected_piece)
                    chess_board.highlight_moves(screen, chessboard, possible_moves)
        
           
        
        pygame.display.flip()
        
        
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
