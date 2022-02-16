from random import randint


class Cell(object):
    """Представляет клетку в игре сапер"""

    def __init__(self, is_mine: bool, x, y):
        self.is_mine = is_mine
        self.is_hide = True
        self.n = None
        self.x = x
        self.y = y


class Saper(object):
    """Представляет класс по игре в сапер"""

    def __init__(self, xn, yn, mn):
        self.grid = []
        self.xn = xn
        self.yn = yn
        self.mn = mn
        self.is_first_step = True

        if self.mn + 9 > self.xn * self.yn:
            self.mn = self.xn * self.yn - 9

        for i in range(yn):
            self.grid.append([])
            for j in range(xn):
                self.grid[i].append(Cell(False, j, i))

    def around(self, cell_1, cell_2):
        if abs(cell_1.x - cell_2.x) <= 1 and abs(cell_1.y - cell_2.y) <= 1:
            return True
        return False

    def create_grid(self, x_first_click, y_first_click):
        mine_used = 0
        while mine_used != self.mn:
            i = randint(0, self.yn - 1)
            j = randint(0, self.xn - 1)
            if self.around(self.grid[i][j], self.grid[y_first_click][x_first_click]) or self.grid[i][j].is_mine:
                continue
            self.grid[i][j].is_mine = True
            mine_used += 1

    def n_mines(self, x, y):
        border_left = x - 1 if x > 0 else 0
        border_right = x + 2 if x < self.xn - 1 else self.xn
        border_up = y - 1 if y > 0 else 0
        border_down = y + 2 if y < self.yn - 1 else self.yn

        quantity_mines = 0
        for i in range(border_up, border_down):
            for j in range(border_left, border_right):
                if i == y and j == x:
                    continue
                if self.grid[i][j].is_mine:
                    quantity_mines += 1

        return quantity_mines

    def click_rec(self, x, y, used_arr=None):
        if used_arr is None:
            used_arr = []
        if not self.grid[y][x].is_hide:
            return [], []
        quantity_mines = self.n_mines(x, y)
        if quantity_mines > 0:
            return [((x, y), quantity_mines)], []
        used_arr += [(x, y)]
        mine_arr = [((x, y), quantity_mines)]

        border_left = x - 1 if x > 0 else 0
        border_right = x + 2 if x < self.xn - 1 else self.xn
        border_up = y - 1 if y > 0 else 0
        border_down = y + 2 if y < self.yn - 1 else self.yn

        for i in range(border_up, border_down):
            for j in range(border_left, border_right):
                if i == y and j == x:
                    continue
                if (j, i) in used_arr:
                    continue
                used_arr.append((j, i))
                quantity_mines = self.n_mines(j, i)
                if quantity_mines == 0:
                    mine_arr_rec, used_arr_rec = self.click_rec(j, i, used_arr)
                    for element in mine_arr_rec:
                        if element not in mine_arr:
                            mine_arr.append(element)
                    for element in used_arr_rec:
                        if element not in used_arr:
                            used_arr.append(element)
                else:
                    element = ((j, i), quantity_mines)
                    if element not in mine_arr:
                        mine_arr.append(element)
        return mine_arr, used_arr

    def click(self, x, y):
        if self.is_first_step:
            self.create_grid(x, y)
            self.is_first_step = False
        if self.grid[y][x].is_mine:
            return -1
        mine_arr, _ = self.click_rec(x, y)
        for cell in mine_arr:
            xc, yc = cell[0][0], cell[0][1]
            self.grid[yc][xc].is_hide = False
            self.grid[yc][xc].n = cell[1]
        return mine_arr
