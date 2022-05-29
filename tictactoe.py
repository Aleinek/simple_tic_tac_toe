grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

moves = 0
x = -1
y = -1

def print_grid():
    print('---------')
    for rows in range(3):
        columns = 0
        print(f'| {grid[rows][columns]} {grid[rows][columns + 1]} {grid[rows][columns + 2]} |')
    print('---------')


print_grid()
while moves < 9:
    try:
        x, y = input().split()

        x = int(x)
        y = int(y)

        if 1 <= x <= 3 and 1 <= y <= 3:
            x -= 1
            y -= 1
            if grid[x][y] == ' ':
                if moves % 2:
                    grid[x][y] = 'X'
                else:
                    grid[x][y] = 'O'
                moves += 1
            else:
                print('This cell is occupied! Choose another one!')
                x = -1
                y = -1
                continue
        else:
            print('Coordinates should be from 1 to 3!')
            x = -1
            y = -1
            continue

        print_grid()

        if moves == 9:
            print('Draw')
        if grid[0][0] == grid[1][0] == grid[2][0] and grid[0][0] != ' ':
            print(f'{grid[0][0]} wins')
            break
        if grid[0][1] == grid[1][1] == grid[2][1] and grid[0][1] != ' ':
            print(f'{grid[0][1]} wins')
            break
        if grid[0][2] == grid[1][2] == grid[2][2] and grid[0][2] != ' ':
            print(f'{grid[0][2]} wins')
            break
        if grid[0][0] == grid[0][1] == grid[0][2] and grid[0][0] != ' ':
            print(f'{grid[0][0]} wins')
            break
        if grid[1][0] == grid[1][1] == grid[1][2] and grid[1][0] != ' ':
            print(f'{grid[1][0]} wins')
            break
        if grid[2][0] == grid[2][1] == grid[2][2] and grid[2][0] != ' ':
            print(f'{grid[2][0]} wins')
            break
        if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
            print(f'{grid[0][0]} wins')
            break
        if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
            print(f'{grid[0][2]} wins')
            break
    except ValueError:
        print('You should enter numbers!')
        x = -1
        y = -1
        continue

