import pygame

'''Basic Window Creation'''

pygame.init()
width = 1000
height = 900
screen =  pygame.display.set_mode([width,height])
pygame.display.set_caption('2-player Chess Game')
font_small = pygame.font.Font('Font\Roboto-Black.ttf', 20)
font_big = pygame.font.Font('Font\Roboto-Black.ttf', 50)
timer = pygame.time.Clock()
fps = 60


#Detailes of Piece

#Position On Board

#White
white_pieces = ['boat' , 'knight' , 'bishop' , 'king' ,'queen' , 'bishop' , 'knight' , 'boat' ,
                'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' ]
white_position = [(0,0) , (1,0) , (2,0) , (3,0) , (4,0) , (5,0) , (6,0) , (7,0) ,
                  (0,1) , (1,1) , (2,1) , (3,1) , (4,1) , (5,1) , (6,1) , (7,1)]


#Black
black_pieces = ['boat' , 'knight' , 'bishop' , 'king' ,'queen' , 'bishop' , 'knight' , 'boat' ,
                'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' ]
black_position = [(0,7) , (1,7) , (2,7) , (3,7) , (4,7) , (5,7) , (6,7) , (7,7) ,
                  (0,6) , (1,6) , (2,6) , (3,6) , (4,6) , (5,6) , (6,6) , (7,6)]

white_killed = []
black_killed = []

turn = 0
selected_piece = 100
possible_moves = []


#Image of Pieces

#Black
b_queen = pygame.image.load('Board\B_q.png')
b_queen_small = pygame.transform.smoothscale(b_queen,(60,60))
b_king = pygame.image.load('Board\B_k.png')
b_king_small = pygame.transform.smoothscale(b_king,(60,60))
b_knight = pygame.image.load('Board\B_kn.png')
b_knight_small = pygame.transform.smoothscale(b_knight,(60,60))
b_bishop = pygame.image.load('Board\B_b.png')
b_bishop_small = pygame.transform.smoothscale(b_bishop,(60,60))
b_pawn = pygame.image.load('Board\B_p.png')
b_pawn_small = pygame.transform.smoothscale(b_pawn,(60,60))
b_boat = pygame.image.load('Board\B_r.png')
b_boat_small = pygame.transform.smoothscale(b_boat,(60,60))

black_image = [b_queen , b_king , b_knight , b_bishop , b_pawn , b_boat]
black_image_size = [b_queen_small , b_king_small , b_knight_small , b_bishop_small , b_pawn_small , b_boat_small]


#White
w_queen = pygame.image.load('Board\w_q.png')
w_queen_small = pygame.transform.smoothscale(w_queen,(60,60))
w_king = pygame.image.load('Board\w_k.png')
w_king_small = pygame.transform.smoothscale(w_king,(60,60))
w_knight = pygame.image.load('Board\w_kn.png')
w_knight_small = pygame.transform.smoothscale(w_knight,(60,60))
w_bishop = pygame.image.load('Board\w_b.png')
w_bishop_small = pygame.transform.smoothscale(w_bishop,(60,60))
w_pawn = pygame.image.load('Board\w_p.png')
w_pawn_small = pygame.transform.smoothscale(w_pawn,(60,60))
w_boat = pygame.image.load('Board\w_r.png')
w_boat_small = pygame.transform.smoothscale(w_boat,(60,60))

white_image = [w_queen , w_king , w_knight , w_bishop , w_pawn , w_boat]
white_image_size = [w_queen_small , w_king_small , w_knight_small , w_bishop_small , w_pawn_small , w_boat_small]



order_pieces = ['queen' , 'king' , 'knight' , 'bishop' , 'pawn' , 'boat']#Order of Image in the List

#Game Board
def draw_board():
    color = 'black'
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen , color , [600 - (column * 200) , row * 100 ,100 , 100])
        else:
            pygame.draw.rect(screen , color , [700 - (column * 200) , row * 100 ,100 , 100])
        pygame.draw.rect(screen , 'white' , [0 , 800 , width , 100])
        pygame.draw.rect(screen , 'black' , [0 , 800 , width , 100] , 5)
        pygame.draw.rect(screen , 'white' , [800 , 0 , 200 , height])
        pygame.draw.rect(screen , 'black' , [800 , 0 , 200 , height] , 5)
        status = ["White: Your Turn to Move","Black: Your Turn to Move"]
        screen.blit(font_big.render(status[turn] , True , 'Black') , (100,820))
        #below comment code is for boarder
        '''for i in range(9):
            pygame.draw.line(screen , 'black' , (200 , 100 * i) , (1000 , 100 * i) , 5)'''


#Pieces Place
def place_pieces():
    for i in range(len(white_pieces)):
        index = order_pieces.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(w_pawn_small , (white_position[i][0] * 100 + 20 , white_position[i][1] * 100 + 15))
        else:
            screen.blit(white_image_size[index] , (white_position[i][0] * 100 + 20 , white_position[i][1] * 100 + 15))
        if turn == 0:
            if selected_piece == i:
                pygame.draw.rect(screen , 'green' , [white_position[i][0] * 100 , white_position[i][1] * 100 , 100 , 100] , 5)

    for i in range(len(black_pieces)):
        index = order_pieces.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(b_pawn_small , (black_position[i][0] * 100 + 20 , black_position[i][1] * 100 + 15))
        else:
            screen.blit(black_image_size[index] , (black_position[i][0] * 100 + 20 , black_position[i][1] * 100 + 15))
        if turn == 1:
            if selected_piece == i:
                pygame.draw.rect(screen , 'green' , [black_position[i][0] * 100 , black_position[i][1] * 100 , 100 , 100] , 5)


#Check pieces validation
def check(pieces,location,turn):
    moves_list = []
    all_moves = []
    for i in range (len(pieces)):
        place = location[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(place , turn)
        elif piece == 'boat':
            moves_list = check_boat(place , turn)
        elif piece == 'knight':
            moves_list = check_knight(place , turn)
        elif piece == 'bishop':
            moves_list = check_bishop(place , turn)
        elif piece == 'king':
            moves_list = check_king(place , turn)
        elif piece == 'queen':
            moves_list = check_queen(place , turn)
        


    
#Main Function

black_option = check(black_pieces , black_position , 'black')
white_option = check(white_pieces , white_position , 'white')
run = True
while run:
    timer.tick(fps)#Refresh Rate
    screen.fill('grey')#Background color
    valid_moves = []
    draw_board()

    place_pieces()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False                                                                                   #Cross Work Due to This
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coordinate = event.pos[0] // 100 
            y_coordinate = event.pos[1] // 100
            click_coordinate = (x_coordinate , y_coordinate)
            if turn == 0:
                if click_coordinate in white_position:
                    selected_piece = white_position.index(click_coordinate)
                if click_coordinate in valid_moves and selected_piece !=100:
                    white_position[selected_piece] = click_coordinate
                    if click_coordinate in black_position:
                        black_piece = black_position.index(click_coordinate)
                        white_killed.append(black_pieces[black_piece])
                        black_position.pop(black_piece)
                        black_pieces.pop(black_piece)
                    black_option = check(black_pieces , black_position , 'black')
                    white_option = check(white_pieces , white_position , 'white')
                    turn = 1
                    selected_piece = 100
                    valid_moves = []
            if turn == 1:
                if click_coordinate in black_position:
                    selected_piece = black_position.index(click_coordinate)
                if click_coordinate in valid_moves and selected_piece !=100:
                    black_position[selected_piece] = click_coordinate
                    if click_coordinate in black_position:
                        white_piece = white_position.index(click_coordinate)
                        black_killed.append(white_pieces[white_piece])
                        white_position.pop(white_piece)
                        white_pieces.pop(white_piece)
                    black_option = check(black_pieces , black_position , 'black')
                    white_option = check(white_pieces , white_position , 'white')
                    turn = 0
                    selected_piece = 100
                    valid_moves = []





    pygame.display.flip()
pygame.quit()
