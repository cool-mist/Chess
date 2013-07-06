def init_board():
    s='rnbqkbnrpppppppp'+'........'*4+'PPPPPPPPRNBQKBNR'
    board=list(s)
    return board

def print_board():
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


#-------------Human move related functions -----

def move(): # gets a human move validates it and updates the board
        l=0
        while not l:
            mv=raw_input('Enter your move : eg(e2-e4) ')
            v=valid(mv)
            i,f=process(mv)
            l=legal(i,f)
            if not l :
                print 'Valid move but Illegal !! :[ '
        
        human_move=[i,f]
        update_board(human_move)
        print_board()

def valid(mv):  # checks if the given input has the valid characters
    allowed='abcdefgh-12345678'
    if not len(mv)==5:
        print 'Extra characters supplied, try again '
        return 0
    else :
        for i in mv:
            if i not in allowed:
                print 'Invalid characters typed, try again '
                return 0
    mv0='abcdefgh'
    mv1='12345678'

    if mv[0] not in mv0:
        print 'Invalid initial column selected,must be in (a-h) try again'
        return 0
    elif mv[1] not in mv1:
        print 'Invalid initial row selected, must be in (1-8) try again '
        return 0
    elif not mv[2] == '-':
        print 'Use only \'-\' as separator ,try again '
        return 0
    elif mv[3] not in mv0:
        print 'Invalid Final column selected,must be in (a-h) try again'
        return 0
    elif mv[4] not in mv1:
        print 'Invalid Final row selected, must be in (1-8) try again '
        return 0
    return 1        
    
def process(mv):#converts user input to initial and final index
    row_dict={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    
    col=row_dict[mv[0]]
    row =8-int(mv[1])
    ii=8*row+col

    col=row_dict[mv[3]]
    row=8-int(mv[4])
    fi=8*row+col

     
    
    return ii,fi

    

def update_board(move): # move array stores initia and final index
    board[move[1]]=board[move[0]]
    board[move[0]]='.'
#---------------Legal testing functions--------

def common_sense(i,f):


    if board[i] == '.' :
            print 'Trying to move an imaginary piece !! '
            return 0
    
    color = -1 if board[i].islower() else 1

    if not color == human_col:
        print 'Trying to move your opponent\'s piece !!'
        return 0
    
    
        
    if not board[f] == '.':
        if board[i].islower():
            if board[f].islower():
                print 'Trying to capture your own piece !! '
                return 0
        else :
            if board[f].isupper():
                print 'I will never again give you white if you try to capture your own piece !! '
                return 0
    return 1
        
    
def legal(i,f):

    if(not common_sense(i,f)):
        print 'Do you have any commonsense ;[ ? try again '
        return 0
    
    return 1

#---------------Computer move funvtions--------

def comp_move():
    board[4]='.'
    print_board()



#----------------Match End---------------


def game_over():
    if 'k' not in board:
        print 'White wins , game over'
        return 1
    if 'K' not in board:
        print 'Black wins , game over'
        return 1
    else :
        return 0


#----------------------Main-----------------


def main():
    global board
    global human_col
    global comp_col
    turn=1
    human_col=1
    comp_col=-1
    board=[]
    m=[]
    #-----------
    board=init_board()
    print_board()
    #-----------

    while not game_over():
        if turn==1:
            move()
        else :
            comp_move()
        turn=turn*-1


    print 'Thanks for playing'

if __name__=='__main__':
    main()
