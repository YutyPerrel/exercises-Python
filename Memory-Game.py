import collections
from random import randint
from collections import defaultdict
import pyautogui
import time
import os


class BoardUtils:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = []
        self.win_board = []

    def create_board(self):
        all = []
        i = 0
        counter = defaultdict(int)
        how_many_char = (self.x *self.y)/2
        while len(all)< how_many_char*2:
            till_num = 65+how_many_char-1
            random_num = randint(65, till_num)
            if counter[random_num] < 2:
                all.append(chr(random_num))
                i+=1
                counter[random_num]+=1
        z =0
        for i in range(self.x):
            new_know = []
            new_game = []
            for j in range(self.y):
                new_know.append(all[z])
                new_game.append('*')
                z+=1
            self.board.append(new_know)
            self.win_board.append(new_game)

    def print_board(self,x0, y0, x1 ,y1):
        for i in range(self.x):
            for j in range(self.y):
                print(' '+self.win_board[i][j]+ ' ', end='')
            print()

    def check_twin(self,x0, y0, x1 ,y1):
        if self.board[x0][y0]== self.board[x1][y1]:
            self.win_board[x0][y0]= self.board[x0][y0]
            self.win_board[x1][y1]= self.board[x1][y1]

    def show_step(self,step):
        locations = step.split(",")
        l1 = locations[0].split(" ")
        l2 = locations[1].split(" ")
        for i in range(self.x):
            for j in range(self.y):
                if i == int(l1[0]) and j == int(l1[1]) or i == int(l2[0]) and j == int(l2[1]):
                    print(' '+ self.board[i][j]+ ' ',end='')
                else:
                    print(' '+self.win_board[i][j]+ ' ', end='')
            print()
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'l')


class Score:
    def __init__(self):
        self.score = collections.defaultdict(int)
    def game_over(self, win, name):
        if win:
            self.score[name]+=1


class BasePlayer:
    def __init__(self, score_keeper):
        self.score = score_keeper
    def game_over(self, win):
        self.score.game_over(win, self.name)
    def check_win(self,board, x , y):
        for i in range(x):
            for j in range(y):
                if (board[i][j]=='*'):
                    return False
        return True


class HumanPlayer(BasePlayer):
    def __init__(self, score_keeper, name, my_tag):
        super().__init__(score_keeper)
        self.name = name
        self.my_tag = my_tag

    def check_win(self,board, x , y):
        if super().check_win(board, x, y):
            self.game_over(True)
            return True
        return False

    def next_move(self, board_obj):
        next_move2 = 0
        while next_move2 == 0:
            board_obj.print_board(0,0,0,0)
            next_move2 = input(self.name+ ", What's your next move? type the square position as (row column,row column)")
            print(next_move2)
        return next_move2

    def check_user_win(self, step, board_obj):
        locations = step.split(",")
        l1 = locations[0].split(" ")
        l2 = locations[1].split(" ")
        board_obj.check_twin(int(l1[0]), int(l1[1]), int(l2[0]) ,int(l2[1]))







score_keeper = Score()
first_player_name= input("Enter first player name please: ")


h =  HumanPlayer(score_keeper, first_player_name, 'x')
x= input("enter board length")
y= input("enter board width")
b = BoardUtils(int(x), int(y))
b.create_board()

z = 2
while z != '0':
    z=2
    move= h.next_move(b)
    b.show_step(move)
    h.check_user_win(move, b)
    if h.check_win(b.win_board, b.x, b.y):
        z =  input("You Win, if you want play again print 1, if not press 0")
    if z == '1':
        x= input("enter board length")
        y= input("enter board width")
        b = BoardUtils(int(x), int(y))
        b.create_board()


