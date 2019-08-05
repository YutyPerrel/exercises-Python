import collections
class BoardUtils:
    def scan_board(self, board, code_to_run_for_each_item):
        for i in range(len(board)):
            for j in range(len(board[i])):
                res = code_to_run_for_each_item(i, j, j == len(board[i])-1)
                if res is not None:
                    return res
    def if_location_empty(self, board, i, j):
        if board[i][j] == '.':
            return 1
        return 0



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
    def check_win(self,board, ij):
        i = int(ij[0])
        j = int(ij[1])
        sign = board[i][j]
        mone_column = 0
        mone_raw = 0
        if i == j:
            if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
                print("win in slant")
                return 1
        if (i + j) % 2 == 0:
            if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
                    print("win in slant")
                    return 1
        for x in range (0,3):
            if board[x][j] == sign:
                mone_column +=1
            if board[i][x] == sign:
                mone_raw += 1
        if mone_column == 3:
            print("win in column")
            return 1
        if mone_raw == 3:
            print("Win in raw")
            return 1


class HumanPlayer(BasePlayer):
    def __init__(self, score_keeper, name, my_tag):
        super().__init__(score_keeper)
        self.name = name
        self.my_tag = my_tag
    def next_move(self, board):
        result = 0
        while result == 0:
            self.print_board(board)
            next_move = input(self.name+ ", What's your next move? type the square position as (row column)")
            result = self.check_move(next_move, board)
        board[int(result[0])][int(result[1])] = self.my_tag
        return result

    def check_move(self, next_move, board):
        try:
            location = next_move.split(" ")
            i = int(location[0])
            j = int(location[1])
            if (i < 0 or i > 2 or j < 0 or j > 2):
                print("the legal values are between 0 to 2")
                return 0
            utils = BoardUtils()
            if utils.if_location_empty(board, i, j):
                return location
            print("your move is already chosen")
            return 0
        except:
            print("your move is not legal, right format is: row column example: 1 1")
            return 0
    def print_board(self, board):
        utils = BoardUtils()
        utils.scan_board(
            board,
            lambda  i, j, is_last: print(f"{board[i][j]:3}", end="\n" if is_last else "")
        )



class AIPlayer(BasePlayer):
    def __init__(self, score_keeper):
        super().__init__(score_keeper)
        self.name = 'Bot'
    next_action = None
    def next_move(self, board):
        AIPlayer.next_action = None
        utils = BoardUtils()
        def foreach_item(i, j, is_last):
            if AIPlayer.next_action is not None:
                return None
            #if board[i][j] == '.':
            if utils.if_location_empty(board, i, j):
                AIPlayer.next_action = [i, j]
                board[i][j] = 'o'
                return None
        if self.calculate_action(board) != None:
            board[AIPlayer.next_action[0]][AIPlayer.next_action[1]]= 'o'
        else:
            utils.scan_board(board, foreach_item)
        return AIPlayer.next_action

    def check_calculate_action(self, board, ij):
        utils = BoardUtils
        i = ij[0]
        j = ij[1]
        if utils.if_location_empty(utils, board, i, j):
            AIPlayer.next_action = [i, j]
            return AIPlayer.next_action
    def calculate_action(self, board):
        self.ij = [[1, 1],[0, 0],[0, 1],[2, 0],[2, 2]]
        self.mone = 0
        while self.check_calculate_action(board, self.ij[self.mone]) == None and self.mone < (len(self.ij) -1):
            self.mone +=1
        return AIPlayer.next_action


def create_opposit_player(num, score_keeper):
    if num == '0':
        second_player = AIPlayer(score_keeper)
    else:
        opposite_player_name = input("Enter second player name please: ")
        second_player = HumanPlayer(score_keeper, opposite_player_name, 'o')
    return second_player
score_keeper = Score()
first_player_name= input("Enter first player name please: ")
h =  HumanPlayer(score_keeper, first_player_name, 'x')

board_length = 5
x = input("for new game press 1 if not press 0")
while True:
    y = input("to play opposite computer - press 0, player- press 1")
    if y == '0' or y == '1':
        break
second_player = create_opposit_player(y, score_keeper)
while x != '0':
    board = [['.','.','.'],['.','.','.'],['.','.','.']]
    for i in range (0, board_length):
            res = h.next_move(board)
            if h.check_win(board, res):
                    h.game_over(True)
                    print(h.name + " Win")
                    i = 6
                    break
            if i < board_length -1:
                res = second_player.next_move(board)
                if second_player.check_win(board,res):
                    second_player.game_over(True)
                    print(second_player.name + " Win")
                    i = 6
                    break
    h.print_board(board)
    if i == 4:
        print("Game Over!")
    x = input("for new game press 1")
print(dict(second_player.score.score) )

