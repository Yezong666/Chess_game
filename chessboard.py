import pygame

COLOR_RED = (84, 0, 0)
COLOR_WHITE = (255, 255, 255)
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

    #draw the chessboard
    def draw(self, screen):
        flipcolor = 0
        x = 0
        y = 0
        for line in self.chessboard:
            for piece in line:
                if flipcolor % 2:
                    pygame.draw.rect(screen, COLOR_RED, (x*WIDTH_SIDE, y *WIDTH_SIDE,WIDTH_SIDE ,WIDTH_SIDE))   
                else:
                    pygame.draw.rect(screen, COLOR_WHITE, (x*WIDTH_SIDE, y *WIDTH_SIDE,WIDTH_SIDE ,WIDTH_SIDE))
                if piece != "":
                    self.put_piece(screen, piece, x, y)
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




    def highlight(self, chessboard, x, y):
        pass
        #Highlight the moves of the piece in coordinates x, y : do it later
    




