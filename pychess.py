from math import ceil
from math import floor

row='12345678'
col='abcdefgh'

board_margin=(0,1,2,3,4,5,6,7,8,15,16,23,24,31,32,39,40,47,48,55,56,57,58,59,60,61,62,63)
second_margin=(9,10,11,12,13,14,17,22,25,30,33,38,41,46,49,50,51,52,53,54)

king=(1,-1,7,8,9,-7,-8,-9)
rook=(1,-1,8,-8)
bishop=(7,9,-7,-9)

def empty_board():
    board=list('.'*64)
    return board
def init_board():
    s='rnbqkbnrpppppppp'+'........'*4+'PPPPPPPPRNBQKBNR'
    board=list(s)
    return board

def print_board(board):
    r='12345678'
    print '  +',
    for i in range(8):
        print '-',
    print '+'
    for i in range(8):
        print r[7-i]+' |',
        for j in range(8):
            print board[8*i+j],
        print '|'
    print '  +',
    for i in range(8):
        print '-',
    print '+'
    print '    a','b','c','d','e','f','g','h'

    
def conv(notation):   # converts human readable move to computer index
    global col
    return  (9-int(notation[1]))*8+col.index(notation[0])-8

def get_move(color):     #Get move for the given color

    global row,col
    
    player = 'white'
    if color == 0:
        player = 'black'
    raw_string=raw_input((player,"Enter move : "))
    src=raw_string.split('-')[0]
    des=raw_string.split('-')[1]

    if (src[0] in col) and (src[1] in row) and (des[0] in col) and (des[1] in row):   
        return (conv(src),conv(des))
    return 0


def rm(i,b):         # A debug method to remove a piece
    b[i]='.'
    return b
def place(i,p,b):    # A debug function to place a piece
    b[i]=p
    return b
def roundto(x,n,s):
    if s=='>':
        return int(ceil(x/float(n))*n)
    else:
        return int(floor(x/float(n))*n)
    
#------------Legal Functions ------------------#
def propogate(src,des,direction,board):
    mid = src
    
    while True:
        mid = mid+direction
        if mid == des:
            return True
        elif board[mid] == '.' :
            if mid in board_margin:
                return False
            else:
                continue
        else :
            return False
def legal_king(src,des,board):
    global king
    for i in king:
            if (des-src) == i:
                return True
    return False
def legal_knight(src,des,board):
    irow = src/8
    icol = src%8
    frow = des/8
    fcol = des%8

    if abs(icol-fcol) == 1:
        if abs (frow-irow) == 2:
            return True
        else :
            return False
    elif abs(icol-fcol) == 2:
        if abs (frow-irow) == 1:
            return True
        else :
            return False
    return False
    
    
def legal_rook(src,des,board):
    if des > src:
        if des < roundto(src,8,'>'):
            direction = 1
        else:
            if (des-src)%8 == 0:
                direction = 8
            else:
                return False
            
    else:
        if des >= roundto(src,8,'<'):
            direction = -1
        else:
            if (src-des)%8 == 0:
                direction = -8
            else :
                return False
    return propogate(src,des,direction,b)
def legal_bishop(src,des,board):

    if src > des:
        if (src-des)%7 == 0:
            direction = -7
        elif (src-des)%9 == 0:
            direction = -9
        else:
            return False
    else:
        if (des-src)%7 == 0:
            direction = 7
        elif (des-src)%9 == 0:
            direction = 9
        else:
            return False
    return propogate(src,des,direction,b)
    
        

def is_legal(src,des,board):      # check if move src -> des is legal in board 

    if not board[des] == '.':
        if board[src].islower():
            if board[des].islower():
                return False
        elif board[des].isupper():
            return False

    p=board[src].lower()   
    if p == 'k':
        return legal_king(src,des,board)
    elif p == 'r':
        return legal_rook(src,des,board)
    elif p == 'b':
        return legal_bishop(src,des,board)
    elif p == 'n':
        return legal_knight(src,des,board)
    elif p == 'q':
        if legal_rook(src,des,board)+legal_bishop(src,des,board):
            return True
    return False

def get_legal(color,board):    # Get List of Legal moves for that color

    legal_list=[]
    piece_list=[]
    if color == 1:
        for i in enumerate(board):
            if i[1].isupper():
                piece_list.append(i[0])
    else:
        for i in enumerate(board):
            if i[1].islower():
                piece_list.append(i[0])
        
    for src in piece_list:
        for des in range(64):
            if is_legal(src,des,board):
                legal_list.append((src,des))
    return legal_list


# ----------------- End Of Legal Functions --------------   
def play(board):
	human=1 #white for human
	comp=0  #black for comp
	
	first=human #First move- human
	second=comp #Second move- comp
	
	legal=0
	legal_moves=get_legal(first,board)
	while not legal:
		move=get_move(first)
		legal=check_legal(move,legal_moves)
	board=update(move,board)
	
	legal_moves=get_legal(second,board)
	move=comp_move(move,legal_moves)
	board=update(move,board)
	
	return board

def main():
	board=init_board()
	print_board(board)
	over=False
	while not over:
		board=play(board)
#main()
b=empty_board()
b=place(35,'r',b)
b=place(36,'K',b)
b=place(50,'b',b)
b=place(43,'Q',b)
print_board(b)
print get_legal(1,b)
