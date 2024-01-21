# draw knight's journey on an n x n board
# gradient of square represents how many moves it takes to get there

import turtle as t
import tkinter as tk


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.colour = -1
        self.set = False
        self.new_colour = -1


    def get_position(self):
        return (self.x, self.y)


    def __str__(self):
        return f"{self.colour}"
        return f"({self.x}, {self.y}, {self.colour}, {self.set}, {self.new_colour})"


class Board:
    def __init__(self, size, start):
        self.size = size
        self.cell_list = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(Cell(i, j))
            self.cell_list.append(row)
        self.cell_list[start[0]][start[1]].colour = 0
        self.cell_list[start[0]][start[1]].set = True


    def within_bounds(self, n):
        return 0 <= n < self.size


    def get_L_move_squares(self, current_cell):
        current_x = current_cell.x
        current_y = current_cell.y

        returnList = []
        n = self.size

        if self.within_bounds(current_y + 2):
            if self.within_bounds(current_x + 1):
                returnList.append(self.cell_list[current_x+1][current_y+2])
            if self.within_bounds(current_x - 1):
                returnList.append(self.cell_list[current_x-1][current_y+2])

        if self.within_bounds(current_y - 2):
            if self.within_bounds(current_x + 1):
                returnList.append(self.cell_list[current_x+1][current_y-2])
            if self.within_bounds(current_x - 1):
                returnList.append(self.cell_list[current_x-1][current_y-2])

        if self.within_bounds(current_x + 2):
            if self.within_bounds(current_y + 1):
                returnList.append(self.cell_list[current_x+2][current_y+1])
            if self.within_bounds(current_y - 1):
                returnList.append(self.cell_list[current_x+2][current_y-1])

        if self.within_bounds(current_x - 2):
            if self.within_bounds(current_y + 1):
                returnList.append(self.cell_list[current_x-2][current_y+1])
            if self.within_bounds(current_y - 1):
                returnList.append(self.cell_list[current_x-2][current_y-1])

        # filter only set cells
        returnList = [c for c in returnList if c.set]

        return returnList


    def permute(self):
        # each cell looks at L-move cells 
        # and sets colour to minimum value + 1
        for row in self.cell_list:
            for cell in row:
                if not cell.set:
                    min_val = -1
                    cells_to_check = self.get_L_move_squares(cell)
                    for new_cell in cells_to_check:
                        min_val = new_cell.colour

                    if min_val != -1:
                        cell.new_colour = min_val + 1

        for row in self.cell_list:
            for cell in row:
                if cell.new_colour != -1 and not cell.set:
                    cell.colour = cell.new_colour
                    cell.set = True


    def add_cell(self, x, y, cell):
        self.cell_list[x][y] = cell


    def __str__(self):
        retStr = ""
        for j in range(len(self.cell_list)-1, -1, -1):
            for i, elt in enumerate(self.cell_list[j]):
                retStr += str(elt)
                if i != len(self.cell_list[j])-1:
                    retStr += " "
            retStr += "\n"

        return retStr
    

    def draw_board(self):
        root = tk.Tk()
        root.title("Knight's Journey")

        board_frame = tk.Frame(root)
        board_frame.pack()

        # size of square
        s = 10
        colour_dict = {0: 'black', 1: 'red', 2: 'orange', 3: 'yellow',
                       4: 'green', 5: 'blue', 6: 'indigo', 7: 'violet'}

        canvas = tk.Canvas(board_frame, width=f"{s*self.size}", height=f"{s*self.size}")
        canvas.grid()

        for row in self.cell_list:
            for cell in row:
                points = [
                        s*cell.x, s*cell.y,
                        s*cell.x + s, s*cell.y,
                        s*cell.x + s, s*cell.y + s,
                        s*cell.x, s*cell.y + s
                ]
                canvas.create_polygon(points, outline="black", fill = "#" + str(hex(cell.colour))[2:].zfill(3), width=2)
                        # "#" + str(hex(cell.colour))[2:].zfill(3)
                        # colour_dict[cell.colour % len(colour_dict.keys())]

        root.mainloop()


def main():
    n = 101
    board = Board(n, (n//2, n//2))
    # board = Board(8, (0, 0))
    # print(board)
    for _ in range(board.size * 2):
        board.permute()
    # print(board)
    board.draw_board()

if __name__ == "__main__":
    main()
