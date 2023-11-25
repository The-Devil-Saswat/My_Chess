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

#It is 1 when king is checked else 0
check_counter = 0

#Detailes of Piece

#Position On Board

#White start position
white_pieces = ['boat' , 'knight' , 'bishop' , 'king' ,'queen' , 'bishop' , 'knight' , 'boat' ,
                'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' ]
white_position = [(0,0) , (1,0) , (2,0) , (3,0) , (4,0) , (5,0) , (6,0) , (7,0) ,
                  (0,1) , (1,1) , (2,1) , (3,1) , (4,1) , (5,1) , (6,1) , (7,1)]


#Black start position
black_pieces = ['boat' , 'knight' , 'bishop' , 'king' ,'queen' , 'bishop' , 'knight' , 'boat' ,
                'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' , 'pawn' ]
black_position = [(0,7) , (1,7) , (2,7) , (3,7) , (4,7) , (5,7) , (6,7) , (7,7) ,
                  (0,6) , (1,6) , (2,6) , (3,6) , (4,6) , (5,6) , (6,6) , (7,6)]


#Captured Pieces
white_killed = []
black_killed = []


#Turn can be 0 or 1
turn = 0
selected_piece = 100
possible_moves = []


#Image of Pieces

#Black
b_queen = pygame.image.load('Board\B_q.png')
b_queen_mid = pygame.transform.smoothscale(b_queen,(60,60))
b_queen_small = pygame.transform.smoothscale(b_queen_mid,(45,45))
b_king = pygame.image.load('Board\B_k.png')
b_king_mid = pygame.transform.smoothscale(b_king,(60,60))
b_king_small = pygame.transform.smoothscale(b_king_mid,(45,45))
b_knight = pygame.image.load('Board\B_kn.png')
b_knight_mid = pygame.transform.smoothscale(b_knight,(60,60))
b_knight_small = pygame.transform.smoothscale(b_knight_mid,(45,45))
b_bishop = pygame.image.load('Board\B_b.png')
b_bishop_mid = pygame.transform.smoothscale(b_bishop,(60,60))
b_bishop_small = pygame.transform.smoothscale(b_bishop_mid,(45,45))
b_pawn = pygame.image.load('Board\B_p.png')
b_pawn_mid = pygame.transform.smoothscale(b_pawn,(60,60))
b_pawn_small = pygame.transform.smoothscale(b_pawn_mid,(45,45))
b_boat = pygame.image.load('Board\B_r.png')
b_boat_mid = pygame.transform.smoothscale(b_boat,(60,60))
b_boat_small = pygame.transform.smoothscale(b_boat_mid,(45,45))

black_image = [b_king , b_queen , b_knight , b_bishop , b_pawn , b_boat]
black_image_size = [b_king_mid , b_queen_mid , b_knight_mid , b_bishop_mid , b_pawn_mid , b_boat_mid]
black_image_small = [b_king_small , b_queen_small , b_knight_small , b_bishop_small , b_pawn_small , b_boat_small]


#White
w_queen = pygame.image.load('Board\w_q.png')
w_queen_mid = pygame.transform.smoothscale(w_queen,(60,60))
w_queen_small = pygame.transform.smoothscale(w_queen_mid,(45,45))
w_king = pygame.image.load('Board\w_k.png')
w_king_mid = pygame.transform.smoothscale(w_king,(60,60))
w_king_small = pygame.transform.smoothscale(w_king_mid,(45,45))
w_knight = pygame.image.load('Board\w_kn.png')
w_knight_mid = pygame.transform.smoothscale(w_knight,(60,60))
w_knight_small = pygame.transform.smoothscale(w_knight_mid,(45,45))
w_bishop = pygame.image.load('Board\w_b.png')
w_bishop_mid = pygame.transform.smoothscale(w_bishop,(60,60))
w_bishop_small = pygame.transform.smoothscale(w_bishop_mid,(45,45))
w_pawn = pygame.image.load('Board\w_p.png')
w_pawn_mid = pygame.transform.smoothscale(w_pawn,(60,60))
w_pawn_small = pygame.transform.smoothscale(w_pawn_mid,(45,45))
w_boat = pygame.image.load('Board\w_r.png')
w_boat_mid = pygame.transform.smoothscale(w_boat,(60,60))
w_boat_small = pygame.transform.smoothscale(w_boat_mid,(45,45))

white_image = [w_king , w_queen , w_knight , w_bishop , w_pawn , w_boat]
white_image_size = [w_king_mid , w_queen_mid ,  w_knight_mid , w_bishop_mid , w_pawn_mid , w_boat_mid]
white_image_small = [w_king_small , w_queen_small ,  w_knight_small , w_bishop_small , w_pawn_small , w_boat_small]


#Order of Image in the List
order_pieces = ['king' , 'queen' , 'knight' , 'bishop' , 'pawn' , 'boat']

#Game Board
def draw_board():
    global check_counter
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
        status = ["White : Your Turn to Move" , "Black : Your Turn to Move" , "White : Your King is Check" , "Black : Your King is Check"]
        if check_counter == 1:
            screen.blit(font_big.render(status[turn + 2] , True , 'Red') , (100,820))
        else:
            screen.blit(font_big.render(status[turn] , True , 'Black') , (100,820))
        screen.blit(font_big.render(str(check_counter) , True , 'Black') , (110,820))
        #below comment code is for boarder
        '''for i in range(9):
            pygame.draw.line(screen , 'black' , (200 , 100 * i) , (1000 , 100 * i) , 5)'''


#Pieces Place
def place_pieces():
    for i in range(len(white_pieces)):
        index = order_pieces.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(w_pawn_mid , (white_position[i][0] * 100 + 20 , white_position[i][1] * 100 + 15))
        else:
            screen.blit(white_image_size[index] , (white_position[i][0] * 100 + 20 , white_position[i][1] * 100 + 15))
        if turn == 0:
            if selected_piece == i:
                pygame.draw.rect(screen , 'green' , [white_position[i][0] * 100 , white_position[i][1] * 100 , 100 , 100] , 5)

    for i in range(len(black_pieces)):
        index = order_pieces.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(b_pawn_mid , (black_position[i][0] * 100 + 20 , black_position[i][1] * 100 + 15))
        else:
            screen.blit(black_image_size[index] , (black_position[i][0] * 100 + 20 , black_position[i][1] * 100 + 15))
        if turn == 1:
            if selected_piece == i:
                pygame.draw.rect(screen , 'green' , [black_position[i][0] * 100 , black_position[i][1] * 100 , 100 , 100] , 5)


#Captured pieces that are show on the right hand side of the window
def draw_captured_pieces():
    for i in range(len(white_killed)):
        piece = white_killed[i]
        index = order_pieces.index(piece)
        screen.blit(black_image_small[index] , (825 , 10 + 50 * i))
    for i in range(len(black_killed)):
        piece = black_killed[i]
        index = order_pieces.index(piece)
        screen.blit(white_image_small[index] , (925 , 10 + 50 * i))


#Check if the king is checked or not
def draw_check():
    global check_counter
    if turn == 0:
        king_index = white_pieces.index('king')
        king_location = white_position[king_index]
        for i in range(len(black_option)):
            if king_location in black_option[i]:
                check_counter = 1
            else:
                check_counter = 0
    if turn == 1:
        king_index = black_pieces.index('king')
        king_location = black_position[king_index]
        for i in range(len(white_option)):
            if king_location in white_option[i]:
                check_counter = 1
            else:
                check_counter = 0
    


#Check pieces validation
def check(pieces,location,turn):
    moves_list = []
    all_moves = []
    for i in range (len(pieces)):
        position = location[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(position , turn)
        elif piece == 'boat':
            moves_list = check_boat(position , turn)
        elif piece == 'knight':
            moves_list = check_knight(position , turn)
        elif piece == 'bishop':
            moves_list = check_bishop(position , turn)
        elif piece == 'queen':
            moves_list = check_queen(position , turn)
        elif piece == 'king':
            moves_list = check_king(position , turn)
        
        all_moves.append(moves_list)
    return all_moves


#Pawn Movement Control
def check_pawn(position , color):
    moves = []
    if color == 'white':
        if(position[0] , position[1] + 1) not in white_position and (position[0] , position[1] + 1) not in black_position and position[1] < 7:
            moves.append((position[0] , position[1] + 1))
        if(position[0] , position[1] + 2) not in white_position and (position[0] , position[1] + 2) not in black_position and position[1] == 1:
            moves.append((position[0] , position[1] + 2 ))
        if(position[0] + 1 , position[1] + 1) in black_position:
            moves.append((position[0] + 1 , position[1] + 1))
        if(position[0] - 1 , position[1] + 1) in black_position:
            moves.append((position[0] - 1 , position[1] + 1))

    elif color == 'black':
        if(position[0] , position[1] - 1) not in white_position and (position[0] , position[1] - 1) not in black_position and position[1] > 0:
            moves.append((position[0] , position[1] - 1))
        if(position[0] , position[1] - 2) not in white_position and (position[0] , position[1] - 2) not in black_position and position[1] == 6:
            moves.append((position[0] , position[1] - 2 ))
        if(position[0] - 1 , position[1] - 1) in white_position:
            moves.append((position[0] - 1 , position[1] - 1))
        if(position[0] + 1 , position[1] - 1) in white_position:
            moves.append((position[0] + 1 , position[1] - 1))
    return moves


#Boat Movement Control
def check_boat(position , color):
    moves = []
    if color == 'white':
        enemies = black_position
        friends = white_position
    elif color == 'black':
        enemies = white_position
        friends = black_position
    #Down , Up , Right , Left
    for i in range(4): 
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        elif i == 3:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x) , position[1] + (chain * y)) not in friends and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <=7:
                moves.append((position[0] + (chain * x) , position[1] + (chain * y)))
                if (position[0] + (chain * x) , position[1] + (chain * y)) in enemies:
                    path = False
                chain += 1
            else:
                path = False
    return moves


#Knight Movement Control
def check_knight(position , color):
    moves = []
    if color == 'white':
        enemies = black_position
        friends = white_position
    elif color == 'black':
        enemies = white_position
        friends = black_position
    
    #Knight have 8 Possibel Moves
    #As it can move straight in any Direction
    #And the one step in another direction
    movement_possible = [(1,2) , (-1,2) , (1,-2) , (-1,-2) , (2,1) , (2,-1) , (-2,1) , (-2,-1)]
    for i in range(8):
        target = (position[0] + movement_possible[i][0] , position[1] + movement_possible[i][1])
        if target not in friends and 0 <= target[0] <= 7 and 0 <= target[1] <=7:
            moves.append(target)
    return moves


#Bishop Movement Control
def check_bishop(position , color):
    moves = []
    if color == 'white':
        enemies = black_position
        friends = white_position
    elif color == 'black':
        enemies = white_position
        friends = black_position
    #Down-Left , Down-Right , Up-Left , Up-Right
    for i in range(4): 
        path = True
        chain = 1
        if i == 0:
            x = -1
            y = 1
        elif i == 1:
            x = 1
            y = 1
        elif i == 2:
            x = -1
            y = -1
        elif i == 3:
            x = 1
            y = -1
        while path:
            if (position[0] + (chain * x) , position[1] + (chain * y)) not in friends and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <=7:
                moves.append((position[0] + (chain * x) , position[1] + (chain * y)))
                if (position[0] + (chain * x) , position[1] + (chain * y)) in enemies:
                    path = False
                chain += 1
            else:
                path = False
    return moves


#Queen Movement Control
def check_queen(position , color):
    moves = check_boat(position , color)
    second = check_bishop(position , color)
    for i in second:
        moves.append(i)
    
    return moves


#King Movement Control
def check_king(position , color):
    moves = []
    if color == 'white':
        enemies = black_position
        friends = white_position
    elif color == 'black':
        enemies = white_position
        friends = black_position
    movement_possible = [(1,0) , (1,1) , (0,1) , (-1,1) , (-1,0) , (-1,-1) , (0,-1) , (1,-1)]
    for i in range(8):
        target = (position[0] + movement_possible[i][0] , position[1] + movement_possible[i][1])
        if target not in friends and 0 <= target[0] <= 7 and 0 <= target[1] <=7:
            moves.append(target)
    return moves

#Check All Moves
def check_valid_moves():
    if turn == 0:
        options = white_option
    else:
        options = black_option
    return options[selected_piece]


#Marks Valid Moves
def draw_valid_moves(moves):
    color = 'green'
    for i in range (len(moves)):
        pygame.draw.rect(screen , color , [moves[i][0] * 100 , moves[i][1] * 100 , 100 , 100] , 5)
    

#Main Function
black_option = check(black_pieces , black_position , 'black')
white_option = check(white_pieces , white_position , 'white')
run = True
while run:

    #Refresh Rate
    timer.tick(fps) 

    #Backgroundcolor
    screen.fill('grey')
    draw_check()
    draw_board()
    draw_captured_pieces()
    place_pieces()
    
    valid_moves = []
    if selected_piece != 100 :
        valid_moves = check_valid_moves()
        draw_valid_moves(valid_moves)

    #Handling All Click Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False   
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
                    if click_coordinate in white_position:
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
