import pygame

COLOR_RED = (84, 0, 0)
COLOR_WHITE = (255, 255, 255)
DARK_YELLOW = (186,142,35)
WIDTH_SIDE = 100



class Chess_board():
    def __init__(self):
        self.chessboard = [
            ["bR", "bK", "bB", "bQu", "bKi", "bB", "bK", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wK", "wB", "wQu", "wKi", "wB", "wK", "wR"]
        ]

    #draw the chessboard(initialisation)
    def draw(self, screen):
        flipcolor = 0
        x = 0
        y = 0
        for line in self.chessboard:
            for tile in line:
                if flipcolor % 2:
                    pygame.draw.rect(screen, COLOR_RED, (x*WIDTH_SIDE, y *WIDTH_SIDE,WIDTH_SIDE ,WIDTH_SIDE))   
                else:
                    pygame.draw.rect(screen, COLOR_WHITE, (x*WIDTH_SIDE, y *WIDTH_SIDE,WIDTH_SIDE ,WIDTH_SIDE))
                if tile != "":
                    self.put_piece(screen, tile, x, y)
                flipcolor+=1
                x+=1
            x = 0
            y += 1
            flipcolor+=1
                
     
    def put_piece(self, screen, piece, x, y):
        match piece:
            case "wP":
                img = pygame.image.load("Chess_pieces_pictures/white_pawn.png").convert_alpha()
            case "bP":
                img = pygame.image.load("Chess_pieces_pictures/black_pawn.png").convert_alpha()
            case "wR":
                img = pygame.image.load("Chess_pieces_pictures/white_rook.png").convert_alpha()
            case "wK":
                img = pygame.image.load("Chess_pieces_pictures/white_knight.png").convert_alpha()
            case "wB":
                img = pygame.image.load("Chess_pieces_pictures/white_bishop.png").convert_alpha()
            case "wQu":
                img = pygame.image.load("Chess_pieces_pictures/white_queen.png").convert_alpha()
            case "wKi":
                img = pygame.image.load("Chess_pieces_pictures/white_king.png").convert_alpha()
            case "bR":
                img = pygame.image.load("Chess_pieces_pictures/black_rook.png").convert_alpha()
            case "bK":
                img = pygame.image.load("Chess_pieces_pictures/black_knight.png").convert_alpha()
            case "bB":
                img = pygame.image.load("Chess_pieces_pictures/black_bishop.png").convert_alpha()
            case "bQu":
                img = pygame.image.load("Chess_pieces_pictures/black_queen.png").convert_alpha()
            case "bKi":
                img = pygame.image.load("Chess_pieces_pictures/black_king.png").convert_alpha()
            case _:
                print("ERROR SUPPOSED TO NEVER HAPPEN"
                      f"piece was {piece}")
                
        screen.blit(img, (x*WIDTH_SIDE, y*WIDTH_SIDE))



    #Highlight the piece selected, and return its location
    def select_piece(self, screen, chessboard, x, y, selected_piece):
        if selected_piece[0] != False:
            if (selected_piece[1] + selected_piece[2]) %2:
                pygame.draw.rect(screen, COLOR_RED, (selected_piece[1]*WIDTH_SIDE, selected_piece[2] *WIDTH_SIDE,WIDTH_SIDE ,WIDTH_SIDE))
            else: 
                pygame.draw.rect(screen, COLOR_WHITE, (selected_piece[1]*WIDTH_SIDE, selected_piece[2] *WIDTH_SIDE,WIDTH_SIDE ,WIDTH_SIDE))
            self.put_piece(screen, chessboard[selected_piece[2]][selected_piece[1]], selected_piece[1] ,selected_piece[2])

        if chessboard[y][x] != "":
            pygame.draw.rect(screen, DARK_YELLOW, (x*WIDTH_SIDE, y *WIDTH_SIDE,WIDTH_SIDE ,WIDTH_SIDE))
            self.put_piece(screen, chessboard[y][x], x ,y)
            return (chessboard[y][x], x, y)
        return (False, 0, 0)
    

    #Return a list of possible move and highlight the tiles the piece can move to
    def check_moves(self, screen, chessboard, selected_piece):
        color_piece = selected_piece[0][0]
        piece = selected_piece[0][1:]
        moves = []
        match piece:
            case "P":
                if color_piece == "w":
                    
                    if selected_piece[2] == 6:
                        num_moves = 2
                    else:
                        num_moves = 1
                    i = 1
                    while (chessboard[selected_piece[2]-i][selected_piece[1]]) == "" and num_moves > 0:
                        moves.append((selected_piece[1],selected_piece[2]-i))
                        pygame.draw.rect(screen, DARK_YELLOW, (selected_piece[1]*WIDTH_SIDE, (selected_piece[2]-i) *WIDTH_SIDE,WIDTH_SIDE ,WIDTH_SIDE))
                        num_moves -= 1
                        i+=1            
                else:
                    if selected_piece[2] == 1:
                        num_moves = 2
                    else:
                        num_moves = 1
                    i = 1
                    while (chessboard[selected_piece[2]+i][selected_piece[1]]) == "" and num_moves > 0:
                        moves.append((selected_piece[1],selected_piece[2]+i))
                        pygame.draw.rect(screen, DARK_YELLOW, (selected_piece[1]*WIDTH_SIDE, (selected_piece[2]+i) *WIDTH_SIDE,WIDTH_SIDE ,WIDTH_SIDE))
                        num_moves -= 1
                        i+=1
            case "R":
                pass
            case "K":
                pass
            case "B":
                pass
            case "Qu":
                pass
            case "Ki":
                pass

            case _:
                print("ERROR SUPPOSED TO NEVER HAPPEN"
                      f"piece was {piece}")
                
        return moves
    

    def remove_highlighted_moves(self, screen, chessboard, highlighted_moves):
        for move in highlighted_moves:
            if (move[0] + move[1]) %2:
                pygame.draw.rect(screen, COLOR_RED, (move[0]*WIDTH_SIDE, move[1] *WIDTH_SIDE,WIDTH_SIDE ,WIDTH_SIDE))
            else: 
                pygame.draw.rect(screen, COLOR_WHITE, (move[0]*WIDTH_SIDE, move[1] *WIDTH_SIDE,WIDTH_SIDE ,WIDTH_SIDE))
            if chessboard[move[1]][move[0]] != "":
                self.put_piece(screen, chessboard[move[1]][move[0]], move[0] ,move[1])
    




