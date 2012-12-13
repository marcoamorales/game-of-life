import copy
import time

alive_char = '@'
dead_char = '.'

def str2grid(filename, alive_char, dead_char):
    text_str = open(filename).read()
    split_grid = text_str.split('\n')
    cleaned_grid = filter(lambda x: len(x) > 0, split_grid)
    grid = map(lambda x: list(x.replace(alive_char, alive_char).replace(
        dead_char, dead_char)),cleaned_grid)
    return grid

class World(object):

    def __init__(self, grid, alive_char, dead_char):
        self.grid = grid
        self.alive_char = alive_char
        self.dead_char = dead_char

    def next_generation(self):
        second_grid = copy.deepcopy(self.grid)
        for i, row in enumerate(second_grid):
            for j, cell in enumerate(row):
                count_alive, count_dead = self.check_adjacent(second_grid, i, j)
                if self.is_alive(second_grid, i, j):
                    if count_alive not in [2,3]:
                        self.kill(self.grid, i, j)
                if not self.is_alive(second_grid, i, j):
                    if count_alive == 3:
                        self.revive(self.grid, i, j)
        return

    def check_adjacent(self, grid, i, j):
        alive = 0
        dead = 0
        '''
        o--
        -x-
        ---
        '''
        if i != 0 and j != 0 and grid[i-1][j-1] == self.alive_char:
            alive += 1
        else:
            dead += 1
        '''
        -o-
        -x-
        ---
        '''
        if i != 0 and grid[i][j-1] == self.alive_char:
            alive += 1
        else:
            dead += 1
        '''
        --o
        -x-
        ---
        '''
        if i != 0 and j < len(grid[0])-1 and grid[i-1][j+1] == self.alive_char:
            alive += 1
        else:
            dead += 1
        '''
        ---
        ox-
        ---
        '''
        if i != 0 and grid[i-1][j] == self.alive_char:
            alive += 1
        else:
            dead += 1
        '''
        ---
        -xo
        ---
        '''
        if j < len(grid[0])-1 and grid[i][j+1] == self.alive_char:
            alive += 1
        else:
            dead += 1
        '''
        ---
        -x-
        o--
        '''
        if i < len(grid)-1 and j != 0 and grid[i+1][j-1] == self.alive_char:
            alive += 1
        else:
            dead += 1
        '''
        ---
        -x-
        -o-
        '''
        if i < len(grid)-1 and grid[i+1][j] == self.alive_char:
            alive += 1
        else:
            dead += 1
        '''
        ---
        -x-
        --o
        '''
        if i < len(grid)-1 and j < len(grid[0])-1 and grid[i+1][j+1] == self.alive_char:
            alive += 1
        else:
            dead += 1
        return alive, dead

    def revive(self, grid, i, j):
        grid[i][j] = self.alive_char

    def kill(self, grid, i, j):
        grid[i][j] = self.dead_char

    def is_alive(self, grid, i, j):
        return grid[i][j] == self.alive_char

    def print_grid(self):
        for line in self.grid:
            print ''.join(line) + '\n'

def main():
    grid = str2grid('/home/marco/.virtualenvs/GameOfLife/gameoflife/game-of-life/initial_state.txt', '@', '.')
    w = World(grid, '@', '.')
    while True:
        w.print_grid()
        w.next_generation()
        time.sleep(1)

if __name__ == '__main__':
    main()
