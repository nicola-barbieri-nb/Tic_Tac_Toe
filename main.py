import random

markers = ['X', 'O']

win_combos = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

def print_grid(grid):
    vert_bar = '|     |     |     |'
    line = '-'*len(vert_bar)
    print(line)
    print(vert_bar)
    print('| ', grid[0], ' | ', grid[1], ' | ', grid[2], ' |')
    print(vert_bar)
    print(line)
    print(vert_bar)
    print('| ', grid[3], ' | ', grid[4], ' | ', grid[5], ' |')
    print(vert_bar)
    print(line)
    print(vert_bar)
    print('| ', grid[6], ' | ', grid[7], ' | ', grid[8], ' |')
    print(vert_bar)
    print(line)

def update_grid(grid, marker):
    cond = True
    while cond:
        position=input('Use numeric Pad:\n')
        if int(position) in range(1,10):
            if int(position) in range(1,4):
                idx = int(position) + 5
            if int(position) in range(4, 7):
                idx = int(position) - 1
            if int(position) in range(7, 10):
                idx = int(position) - 7
            if grid[idx] == ' ':
                grid[idx] = marker
                cond = False
            else:
                print('Cell already taken!')

    print_grid(grid)
    return grid

def check_if_full(grid):
    if ' ' not in grid:
        print('the board is full')
        return True

def check_if_won(grid, marker):
    for combo in win_combos:
        if grid[combo[0]] == marker and grid[combo[1]] == marker and grid[combo[2]] == marker:
            print(f"{marker} won!")
            return True


# game_grid = [' '] * 9

# game_grid[0]= 'X'
# game_grid[8]= 'O'

# for item in game_grid:
#     print(item)
# print(type(game_grid))



def play_game():
    game_grid = [' '] * 9
    first_player = random.choice([0,1])
    print(f"First player to start is {markers[first_player]}")
    while not check_if_full(game_grid):
        game_grid = update_grid(game_grid, markers[first_player])
        if check_if_won(game_grid, markers[first_player]):
            # another_game = input('Another game? Y or N').lower()
            # if another_game == 'n':
            break
            # else:
            #     play_game()
        first_player += 1
        first_player = first_player % 2
    another_game = input('Another game? Y or N\n').lower()
    if another_game == 'y':
        play_game()

play_game()

