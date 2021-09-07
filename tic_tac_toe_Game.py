def draw_playing_field(value_table, slip = 0):
    '''
    Draws a game board with the current cell values.
    '''
    print(' '*slip, '-'*13)
    for i in range(3):
        print(' ' * slip, '|', value_table[0+i*3], '|', value_table[1+i*3], '|', value_table[2+i*3], '|')
        print(' ' * slip, '-' * 13)

def take_input(player_current):
    '''
    Checks for correct input and fills in cell values.
    '''
    pass

def take_input_comp(player_current):
    '''
    Checks for correct input and fills in cell values.
    '''
    pass

def take_input_human(player_current):
    '''
    Checks for correct input and fills in cell values.
    '''
    pass

def check_win(value_table):
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    pass


value_table = list(range(1,10))
player_current, player_next = 'O', 'X'
counter = 0
win = False
print('*' * 10, ' TIC-TAC-TOE GAME for Player and Computer ', '*' * 10)

while not win:
    counter += 1
    draw_playing_field(value_table)
    if counter % 2 == 0:
        player_current, player_next = 'O', 'X'
    else:
        player_current, player_next = 'X', 'O'



input('Press Enter to exit!')
