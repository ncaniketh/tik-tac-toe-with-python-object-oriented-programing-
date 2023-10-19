import turtle
from time import sleep
from tkinter import *
from tkinter import messagebox


class Game:
    def __init__(self, master):
        self.master = master
        master.title("Tic tac toe")
        self.b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = "x"
        button = Button(master, text="Start Game", command=self.initDraw)
        button.place(relx=0.5, rely=0.5, anchor="center")

    def initDraw(self):
        self.master.destroy()
        self.draw()

    def draw_board(self):
        turtle.pencolor("white")
        turtle.pensize(10)
        turtle.up()
        turtle.goto(-3, -1)
        turtle.seth(0)
        turtle.down()
        turtle.fd(6)
        turtle.up()
        turtle.goto(-3, 1)
        turtle.seth(0)
        turtle.down()
        turtle.fd(6)
        turtle.up()
        turtle.goto(-1, -3)
        turtle.seth(90)
        turtle.down()
        turtle.fd(6)
        turtle.up()
        turtle.goto(1, -3)
        turtle.seth(90)
        turtle.down()
        turtle.fd(6)

    def draw_circle(self, x, y):
        turtle.up()
        turtle.goto(x, y - 0.75)
        turtle.seth(0)
        turtle.color("white")
        turtle.down()
        turtle.circle(0.75, steps=100)

    def draw_x(self, x, y):
        turtle.color("blue")
        turtle.up()
        turtle.goto(x - 0.75, y - 0.75)
        turtle.down()
        turtle.goto(x + 0.75, y + 0.75)
        turtle.up()
        turtle.goto(x - 0.75, y + 0.75)
        turtle.down()
        turtle.goto(x + 0.75, y - 0.75)

    def draw_piece(self, i, j, p):
        if p == 0:
            return
        x, y = 2 * (j - 1), -2 * (i - 1)
        if p == 1:
            self.draw_x(x, y)
        else:
            self.draw_circle(x, y)

    def draw(self):
        self.screen = turtle.Screen()
        self.screen.onclick(self.play)
        self.screen.setup(1000, 1000)
        self.screen.title("Tic Tac Toe ")
        self.screen.setworldcoordinates(-5, -5, 5, 5)
        self.screen.bgcolor("black")
        self.screen.tracer(0, 0)
        # turtle.hideturtle()
        self.draw_board()
        for i in range(3):
            for j in range(3):
                self.draw_piece(i, j, self.b[i][j])
        self.screen.update()

    # return 1 if player 1 wins, 2 if player 2 wins, 3 if tie, 0 if game is not over
    def gameover(self):
        if (
            self.b[0][0] > 0
            and self.b[0][0] == self.b[0][1]
            and self.b[0][1] == self.b[0][2]
        ):
            return self.b[0][0]
        if (
            self.b[1][0] > 0
            and self.b[1][0] == self.b[1][1]
            and self.b[1][1] == self.b[1][2]
        ):
            return self.b[1][0]
        if (
            self.b[2][0] > 0
            and self.b[2][0] == self.b[2][1]
            and self.b[2][1] == self.b[2][2]
        ):
            return self.b[2][0]
        if (
            self.b[0][0] > 0
            and self.b[0][0] == self.b[1][0]
            and self.b[1][0] == self.b[2][0]
        ):
            return self.b[0][0]
        if (
            self.b[0][1] > 0
            and self.b[0][1] == self.b[1][1]
            and self.b[1][1] == self.b[2][1]
        ):
            return self.b[0][1]
        if (
            self.b[0][2] > 0
            and self.b[0][2] == self.b[1][2]
            and self.b[1][2] == self.b[2][2]
        ):
            return self.b[0][2]
        if (
            self.b[0][0] > 0
            and self.b[0][0] == self.b[1][1]
            and self.b[1][1] == self.b[2][2]
        ):
            return self.b[0][0]
        if (
            self.b[2][0] > 0
            and self.b[2][0] == self.b[1][1]
            and self.b[1][1] == self.b[0][2]
        ):
            return self.b[2][0]
        p = 0
        for i in range(3):
            for j in range(3):
                p += 1 if self.b[i][j] > 0 else 0
        if p == 9:
            return 3
        else:
            return 0

    def play(self, x, y):
        i = 3 - int(y + 5) // 2
        j = int(x + 5) // 2 - 1
        if i > 2 or j > 2 or i < 0 or j < 0:
            return
        if self.b[i][j] != 0:
            root = Tk()
            root.withdraw()
            messagebox.showwarning("Warning", "Illegal move!")
            root.destroy()
            root.mainloop()
        if self.turn == "x":
            self.b[i][j], self.turn = 1, "o"
        else:
            self.b[i][j], self.turn = 2, "x"
        self.draw()
        r = self.gameover()
        if r != 0:
            output = ""
            root = Tk()
            root.withdraw()
            if r == 1:
                output = "X Won!"
            elif r == 2:
                output = "O Won!"
            elif r == 3:
                output = "Draw"
            messagebox.showinfo("Game Over", output)
            root.destroy()
            self.screen.bye()


def main():
    root = Tk()
    Game(root)
    root.mainloop()


main()
