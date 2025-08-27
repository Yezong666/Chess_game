import pygame

COLOR_RED = (84, 0, 0)
COLOR_WHITE = (255, 255, 255)
DARK_YELLOW = (186,142,35)
COLOR_PINK = (255,105,180)
WIDTH_SIDE = 100



class Chess_board():
    def __init__(self):
        self.chessboard = [
            ["bR", "bK", "bB", "bQu", "bKi", "bB", "bK", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "],
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
                    self.highlight_tile(screen, x, y, COLOR_RED)   
                else:
                    self.highlight_tile(screen, x, y, COLOR_WHITE)
                if tile != " ":
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
                      f"piece was '{piece}'")
                return
                
        screen.blit(img, (x*WIDTH_SIDE, y*WIDTH_SIDE))



    #Highlight the piece selected, and return its location
    def select_piece(self, screen, chessboard, x, y, selected_piece):
        if x >= 0 and x <= 7 and y >= 0 and y <= 7:
            if selected_piece[0] != False:
                if (selected_piece[1] + selected_piece[2]) %2:
                    self.highlight_tile(screen, selected_piece[1], selected_piece[2], COLOR_RED)
                else: 
                    self.highlight_tile(screen, selected_piece[1], selected_piece[2], COLOR_WHITE)
                self.put_piece(screen, chessboard[selected_piece[2]][selected_piece[1]], selected_piece[1] ,selected_piece[2])

            if chessboard[y][x] != " ":
                self.highlight_tile(screen, x, y, DARK_YELLOW)
                self.put_piece(screen, chessboard[y][x], x ,y)
                return (chessboard[y][x], x, y)
        return (False, 0, 0)
    

    #Return a list of possible move and highlight the tiles the piece can move to
    def check_moves(self, chessboard, selected_piece, ally=False):
        color_piece = selected_piece[0][0]
        piece = selected_piece[0][1:]
        x = selected_piece[1]
        y = selected_piece[2]
        moves = []
        print(f"ally = {ally}")
        match piece:
            case "P":
                if color_piece == "w":
                    
                    if y == 6:
                        num_moves = 2
                    else:
                        num_moves = 1
                    i = 1
                    while (chessboard[y-i][x]) == " " and num_moves > 0:
                        moves.append((x,y-i))
                        num_moves -= 1
                        i+=1
                    if (y-1) >= 0:
                        if (x-1) >= 0 and (chessboard[y-1][x-1][0] == "b" or ally == True):
                            moves.append((x-1, y-1))
                        if (x+1) <= 7 and (chessboard[y-1][x+1][0] == "b" or ally == True):
                            moves.append((x+1, y-1))
                        
                else:
                    if y == 1:
                        num_moves = 2
                    else:
                        num_moves = 1
                    i = 1
                    while (chessboard[y+i][x]) == " " and num_moves > 0:
                        moves.append((x,y+i))
                        num_moves -= 1
                        i+=1
                    if (y+1) >= 0:
                        if (x-1) >= 0 and (chessboard[y+1][x-1][0] == "w" or ally == True):
                            moves.append((x-1, y+1))
                        if (x+1) <= 7 and (chessboard[y+1][x+1][0] == "w" or ally == True):
                            moves.append((x+1, y+1))
                        
            case "R":
                couples = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for couple in couples:
                    i = 1
                    while((x+i*couple[0]) >= 0 and (x+i*couple[0]) <= 7 and (y+i*couple[1]) >= 0 and (y+i*couple[1]) <= 7):
                        if chessboard[y+i*couple[1]][x+i*couple[0]] == " ":
                            moves.append((x+i*couple[0],y+i*couple[1]))
                            i+=1
                        else:
                            if chessboard[y+i*couple[1]][x+i*couple[0]][0] != color_piece or ally == True:
                                moves.append((x+i*couple[0],y+i*couple[1]))
                            i = 10

            case "K":
                if x + 2 <= 7:
                    if y + 1 <= 7:
                        if chessboard[y+1][x+2] == " " or chessboard[y+1][x+2][0] != color_piece or ally==True:
                            moves.append((x+2,y+1))
                    if y - 1 >= 0:
                        if chessboard[y-1][x+2] == " " or chessboard[y-1][x+2][0] != color_piece or ally == True:
                            moves.append((x+2,y-1))
                if x - 2 >= 0:
                    if y + 1 <= 7:
                        if chessboard[y+1][x-2] == " " or chessboard[y+1][x-2][0] != color_piece or ally == True:
                            moves.append((x-2,y+1))
                    if y - 1 >= 0:
                        if chessboard[y-1][x-2] == " " or chessboard[y-1][x-2][0] != color_piece or ally == True:
                            moves.append((x-2,y-1))
                if y + 2 <= 7:
                    if x + 1 <= 7:
                        if chessboard[y+2][x+1] == " " or chessboard[y+2][x+1][0] != color_piece or ally == True:
                            moves.append((x+1,y+2))
                    if x - 1 >= 0:
                        if chessboard[y+2][x-1] == " " or chessboard[y+2][x-1][0] != color_piece or ally == True:
                            moves.append((x-1,y+2))
                if y - 2 >= 0:
                    if x + 1 <= 7:
                        if chessboard[y-2][x+1] == " " or chessboard[y-2][x+1][0] != color_piece or ally == True:
                            moves.append((x+1,y-2))
                    if x - 1 >= 0:
                        if chessboard[y-2][x-1] == " " or chessboard[y-2][x-1][0] != color_piece or ally == True:
                            moves.append((x-1,y-2))
            case "B":
                couples = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
                for couple in couples:
                    i = 1
                    while((x+i*couple[0]) >= 0 and (x+i*couple[0]) <= 7 and (y+i*couple[1]) >= 0 and (y+i*couple[1]) <= 7):
                        if chessboard[y+i*couple[1]][x+i*couple[0]] == " ":
                            moves.append((x+i*couple[0],y+i*couple[1]))
                            i+=1
                        else:
                            if chessboard[y+i*couple[1]][x+i*couple[0]][0] != color_piece or ally == True:
                                moves.append((x+i*couple[0],y+i*couple[1]))
                            i = 10
            case "Qu":
                #bishop moves
                couples = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
                for couple in couples:
                    i = 1
                    while((x+i*couple[0]) >= 0 and (x+i*couple[0]) <= 7 and (y+i*couple[1]) >= 0 and (y+i*couple[1]) <= 7):
                        if chessboard[y+i*couple[1]][x+i*couple[0]] == " ":
                            moves.append((x+i*couple[0],y+i*couple[1]))
                            i+=1
                        else:
                            if chessboard[y+i*couple[1]][x+i*couple[0]][0] != color_piece or ally == True:
                                moves.append((x+i*couple[0],y+i*couple[1]))
                            i = 10
                #+ rook moves
                couples = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for couple in couples:
                    i = 1
                    while((x+i*couple[0]) >= 0 and (x+i*couple[0]) <= 7 and (y+i*couple[1]) >= 0 and (y+i*couple[1]) <= 7):
                        if chessboard[y+i*couple[1]][x+i*couple[0]] == " ":
                            moves.append((x+i*couple[0],y+i*couple[1]))
                            i+=1
                        else:
                            if chessboard[y+i*couple[1]][x+i*couple[0]][0] != color_piece or ally == True:
                                moves.append((x+i*couple[0],y+i*couple[1]))
                            i = 10
            case "Ki":
                if x + 1 <= 7:
                    if y + 1 <= 7:
                        if chessboard[y+1][x+1] == " " or chessboard[y+1][x+1][0] != color_piece or ally == True:
                            moves.append((x+1,y+1))
                    if y - 1 >= 0:
                        if chessboard[y-1][x+1] == " " or chessboard[y-1][x+1][0] != color_piece or ally == True:
                            moves.append((x+1,y-1))
                    if chessboard[y][x+1] == " " or chessboard[y][x+1][0] != color_piece or ally == True:
                            moves.append((x+1,y))
                if x - 1 >= 0:
                    if y + 1 <= 7:
                        if chessboard[y+1][x-1] == " " or chessboard[y+1][x-1][0] != color_piece or ally == True:
                            moves.append((x-1,y+1))
                    if y - 1 >= 0:
                        if chessboard[y-1][x-1] == " " or chessboard[y-1][x-1][0] != color_piece or ally == True:
                            moves.append((x-1,y-1))
                    if chessboard[y][x-1] == " " or chessboard[y][x-1][0] != color_piece or ally == True:
                            moves.append((x-1,y))
                if y + 1 <= 7:
                    if chessboard[y+1][x] == " " or chessboard[y+1][x][0] != color_piece or ally == True:
                            moves.append((x,y+1))
                if y - 1 >= 0:
                        if chessboard[y-1][x] == " " or chessboard[y-1][x][0] != color_piece or ally == True:
                            moves.append((x,y-1))
            case _:
                print("ERROR SUPPOSED TO NEVER HAPPEN"
                      f"piece was '{piece}'")
        print(moves)
        return moves
    


    def highlight_moves(self, screen, chessboard, moves):
        for move in moves:
            if chessboard[move[1]][move[0]] == " ":
                self.highlight_tile(screen, move[0], move[1], DARK_YELLOW)
            else:
                self.highlight_tile(screen, move[0], move[1], COLOR_PINK)
                self.put_piece(screen, chessboard[move[1]][move[0]], move[0], move[1])


    def highlight_tile(self, screen, x, y, color):
        pygame.draw.rect(screen, color, (x * WIDTH_SIDE, y * WIDTH_SIDE, WIDTH_SIDE, WIDTH_SIDE))


    def remove_highlighted_moves(self, screen, chessboard, highlighted_moves):
        for move in highlighted_moves:
            if (move[0] + move[1]) %2:
                self.highlight_tile(screen, move[0], move[1], COLOR_RED)
            else: 
                self.highlight_tile(screen, move[0], move[1], COLOR_WHITE)
            if chessboard[move[1]][move[0]] != " ":
                self.put_piece(screen, chessboard[move[1]][move[0]], move[0] ,move[1])
        return []
    
    def move_piece(self, screen, chessboard, x, y, piece):
        chessboard[y][x] = piece[0]
        chessboard[piece[2]][piece[1]] = " "
        if (x + y) %2:
            self.highlight_tile(screen, x, y, COLOR_RED)
        else: 
            self.highlight_tile(screen, x, y, COLOR_WHITE)
        self.put_piece(screen, piece[0], x, y)
        if (piece[1] + piece[2]) %2:
            self.highlight_tile(screen, piece[1], piece[2], COLOR_RED)
        else: 
            self.highlight_tile(screen, piece[1], piece[2], COLOR_WHITE)
     
    def unselect_piece(self, screen, piece):
        if (piece[1] + piece[2]) %2:
            self.highlight_tile(screen, piece[1], piece[2], COLOR_RED)
        else: 
            self.highlight_tile(screen, piece[1], piece[2], COLOR_WHITE)
        self.put_piece(screen, piece[0], piece[1], piece[2])

    def get_state(self, chessboard):
        chess_state = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]
        i = 0
        j = 0
        for line in chessboard:
            for tile in line:
                if tile[0] == "b":
                    get_moves = self.check_moves(chessboard, (tile, i, j), ally=True)
                    for move in get_moves:
                        chess_state[move[1]][move[0]] += 1
                elif tile[0] == "w":
                    get_moves = self.check_moves(chessboard, (tile, i, j), ally=True)
                    for move in get_moves:
                        chess_state[move[1]][move[0]] -= 1
                i+=1
            j+=1
            i = 0
        return chess_state

    def white_attack(self, chessboard):
        chess_state = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]
        i = 0
        j = 0
        for line in chessboard:
            for tile in line:
                if tile[0] == "w":
                    get_moves = self.check_moves(chessboard, (tile, i, j), ally=True)
                    for move in get_moves:
                        chess_state[move[1]][move[0]] -= 1
                i+=1
            j+=1
            i = 0
        return chess_state
        
    def get_black_pieces_attacked(self, chessboard, white_attacking):
        pieces = []
        i = 0
        j = 0
        for line in white_attacking:
            for tile in line:
                if tile < 0:
                    if chessboard[j][i][0] == "b":
                        pieces.append((chessboard[j][i], i, j))
                i+=1
            j+=1
            i = 0
        return pieces
