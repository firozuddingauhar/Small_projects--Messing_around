import tkinter as tk
from tkinter import messagebox
import random

class MinesweeperGUI:
    def __init__(self, master, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.master = master
        self.buttons = {}
        self.board = Board(dim_size, num_bombs)
        self.create_widgets()

    def create_widgets(self):
        for x in range(self.dim_size):
            for y in range(self.dim_size):
                btn = tk.Button(self.master, text=' ', width=10, height=5, command=lambda x=x, y=y: self.on_button_click(x, y))
                btn.grid(column=x, row=y)
                self.buttons[x, y] = btn

    def on_button_click(self, x, y):
        if not self.board.dig(x, y):
            self.reveal_board(True)
            messagebox.showinfo("Game Over", "You clicked a bomb! Game over.")
            self.reset_board()
        else:
            self.update_buttons()
            if self.check_win():
                messagebox.showinfo("Congratulations!", "You have won the game!")
                self.reset_board()

    def reveal_board(self, reveal_bombs=False):
        for x in range(self.dim_size):
            for y in range(self.dim_size):
                btn = self.buttons[x, y]
                if reveal_bombs and self.board.board[x][y] == '*':
                    btn.configure(text='*', bg='red')
                elif (x, y) in self.board.dug:
                    btn.configure(text=str(self.board.board[x][y]))

    def update_buttons(self):
        for x in range(self.dim_size):
            for y in range(self.dim_size):
                btn = self.buttons[x, y]
                if (x, y) in self.board.dug:
                    btn.config(state=tk.DISABLED, relief=tk.SUNKEN)
                    value = self.board.board[x][y]
                    if value == '*':
                        btn.configure(text='*', bg='red')
                    elif value == 0:
                        btn.configure(text=' ', bg='lightgrey')
                    else:
                        btn.configure(text=str(value), bg='lightgrey')
                else:
                    btn.configure(text=' ', state=tk.NORMAL, bg='SystemButtonFace', relief=tk.RAISED)

    def check_win(self):
        return len(self.board.dug) == self.dim_size ** 2 - self.num_bombs

    def reset_board(self):
        for x in range(self.dim_size):
            for y in range(self.dim_size):
                btn = self.buttons[x, y]
                btn.configure(text=' ', state=tk.NORMAL, bg='SystemButtonFace', relief=tk.RAISED)
        self.board = Board(self.dim_size, self.num_bombs)


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set() 

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size  
            col = loc % self.dim_size 
            if board[row][col] == '*':
                continue
            board[row][col] = '*' 
            bombs_planted += 1
        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)


    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def dig(self, row, col):
        self.dug.add((row, col)) 
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue 
                self.dig(r, c)

        return True

    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        string_rep = ''
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

if __name__ == '__main__':
    #dim_size = int(input("Enter the dimensions of the board: "))
    #num_bombs = int(input("Enter the number of bombs: "))
    root = tk.Tk()
    root.title("Minesweeper")
    #game = MinesweeperGUI(root, dim_size=dim_size, num_bombs=num_bombs)
    game = MinesweeperGUI(root, 10, 10)
    root.mainloop()
