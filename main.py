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
    king_attacked = 0   #0 = not attacked ; 1 = check ; 2 = checkmate
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
                    king_attacked = 0
                    chessboard_pieces_attacked = chess_board.pieces_attacked(chessboard, turn)
                    pieces_attacked = chess_board.get_pieces_attacked(chessboard, chessboard_pieces_attacked)
                    for piece in pieces_attacked:
                        if piece[0][1:] == "Ki": 
                            king_attacked = 1
                            king_loc = piece
                            print(f"King attacked at {king_loc}")  #Make a "check" animation ? 
                    
                else:
                    if chessboard[mouse_loc_y][mouse_loc_x][0] == "w" and (turn+1)%2:
                        selected_piece = chess_board.select_piece(screen, chessboard, mouse_loc_x, mouse_loc_y, selected_piece)
                        possible_moves = chess_board.remove_highlighted_moves(screen, chessboard, possible_moves)

                    elif chessboard[mouse_loc_y][mouse_loc_x][0] == "b" and turn%2:
                        selected_piece = chess_board.select_piece(screen, chessboard, mouse_loc_x, mouse_loc_y, selected_piece)
                        possible_moves = chess_board.remove_highlighted_moves(screen, chessboard, possible_moves)
                        
                    else:
                        if selected_piece[0] != False:
                            possible_moves = chess_board.remove_highlighted_moves(screen, chessboard, possible_moves)
                            chess_board.unselect_piece(screen, selected_piece)
                            selected_piece = (False, 0, 0)
                           #King attacked, try to find moves that can save the king, if can't it's checkmate
                        #only 1 attacker, can be killed or blocked and be safe
                                #add in possible moves all pieces who can kill the attacker
                                #add in possible moves all moves blocking the attacker
                        
                        #chess_board.highlight_moves(screen, chessboard, king_moves)
                        #print (king_moves)
                            #find_pieces_attacking_king()
                            #chessboard_black_attack()
                            #find_pieces_attacking_attacker()
                            #for pieces in pieces_attacking_attacker:
                            #   simulate attack and check again if king would be under attack
                            #   if still under attack, cancel and go to the next one in the list
                            #if king still under attack (attacker can't be killed):
                            #   get_tiles_to_block()
                            #   find_pieces_can_block()
                            #   sort pieces from weakest to strongest (pawn > bishop > knight > rook > queen)
                            #   for pieces in find_pieces_can_block:
                            #       simulate block and check again if king would still be under attack
                            #       if still under attackn cancel and go to the next one in list
                chessboard_pieces_attacked = chess_board.pieces_attacked(chessboard, turn)    #If not check, do a move (still not done)
                    

                if selected_piece[0] != False:
                    if king_attacked == 0:
                        if selected_piece[0][1:] == "Ki":
                            possible_moves = chess_board.check_king_moves(chessboard, chessboard_pieces_attacked, selected_piece)
                        else:
                            possible_moves = chess_board.check_moves(chessboard, selected_piece)
                        chess_board.highlight_moves(screen, chessboard, possible_moves)
                    else:
                        attackers = chess_board.find_piece_attacking_king(chessboard, king_loc)
                        piece_moves = chess_board.check_moves(chessboard, selected_piece)
                        tiles_to_block = chess_board.find_tiles_to_block(chessboard, king_loc, attackers)
                        possible_moves = []
                        if len(attackers) == 1:
                            for move in piece_moves:
                                if (move[0] == attackers[0][1] and move[1] == attackers[0][2]) or move in tiles_to_block:
                                    possible_moves.append(move)
                        if selected_piece[0][1:] == "Ki":
                            possible_moves = chess_board.check_king_moves(chessboard, chessboard_pieces_attacked, king_loc, attackers)
                        
                        print(possible_moves)
                        chess_board.highlight_moves(screen, chessboard, possible_moves)
        
           
        
        pygame.display.flip()
        
        
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
