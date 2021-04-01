import random


class NoMemoryError(FileNotFoundError):
    pass


class TicTacToeTr:

    def __init__(self, size=3, memory_filename="mem_tr.txt", player=1, bot=2, backup_filename="backup_tr.txt"):
        self.PLAYER = bot
        self.BOT = player

        self.memory_filename = memory_filename
        self.size = size
        self.board = [[0 for _1 in range(size)] for _2 in range(size)]
        self.prev_board = [[j for j in i] for i in self.board]
        self.prev_turn = "0,0"
        self.remembered = dict()
        self.backup_filename = backup_filename

    def check_win(self, boar=False):
        if not boar:
            boar = self.board

        for i in range(self.size):
            b = True
            for j in range(1, self.size):
                if boar[i][j] != boar[i][j - 1]:
                    b = False
            if b and boar[i][0] != 0:
                return boar[i][0]

            b = True
            for j in range(1, self.size):
                if boar[j][i] != boar[j - 1][i]:
                    b = False
            if b and boar[0][i] != 0:
                return boar[0][i]

        b = True
        for i in range(1, self.size):
            if boar[i][i] != boar[i - 1][i - 1]:
                b = False
        if b and boar[0][0] != 0:
            return boar[0][0]

        b = True
        for i in range(1, self.size):
            if boar[i][self.size - 1 - i] != boar[i - 1][self.size - 1 - (i - 1)]:
                b = False
        if b and boar[0][self.size - 1] != 0:
            return boar[0][self.size - 1]
        return 0

    def remember(self):
        text = []
        try:
            with open(self.memory_filename, "r") as f:
                for i in f:
                    text.append(i)
            for i in text:
                self.remembered[i.split(":")[0]] = []
                for j in i.split(":")[1].split(";")[:-1]:
                    self.remembered[i.split(":")[0]].append(j)
        except FileNotFoundError:
            raise NoMemoryError

    def memorize(self, turn):
        if turn not in self.remembered[str(self.prev_board)]:
            self.remembered[str(self.prev_board)].append(turn)

    def do_turn(self):

        if str(self.board) not in self.remembered.keys():
            self.remembered[str(self.board)] = []

        if str(self.prev_board) not in self.remembered.keys():
            self.remembered[str(self.prev_board)] = []

        if self.check_win() != 0:
            if self.check_win() == self.PLAYER:
                self.memorize(self.prev_turn)
            return self.check_win()

        for i in range(self.size):
            for j in range(self.size):
                if (self.board[i][j] == 0) and (str(i) + "," + str(j) not in self.remembered[str(self.board)]):
                    self.prev_board = [[j for j in i] for i in self.board]
                    self.board[i][j] = self.BOT
                    self.prev_turn = str(i) + "," + str(j)
                    return [True, i, j]
        self.memorize(self.prev_turn)
        return False

    def memorize_to_file(self):
        with open(self.memory_filename, "w+") as f:
            for i in self.remembered:
                f.write(i)
                f.write(":")
                for j in self.remembered[i]:
                    f.write(j)
                    f.write(";")
                f.write("\b")
                f.write("\n")

    def player_turn(self, column, row):
        if self.board[row][column] == 0:
            self.board[row][column] = self.PLAYER
            return True
        else:
            return False

    def display_board(self):
        for i in self.board:
            for j in i:
                print(j, end="")
            print()
        print()

    def do_bad_move(self):
        if self.check_win() != 0:
            return self.check_win()
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    self.board[i][j] = self.BOT
                    return [True, i, j]
        return False

    def detect_draw(self):
        for i in self.board:
            for j in i:
                if j == 0:
                    return False
        return True

    def backup(self):
        with open(self.backup_filename, "w+") as f:
            for i in self.remembered:
                f.write(i)
                f.write(":")
                for j in self.remembered[i]:
                    f.write(j)
                    f.write(";")
                f.write("\b")
                f.write("\n")

    def nullify(self):
        self.board = [[0 for _1 in range(self.size)] for _2 in range(self.size)]
        self.prev_board = [[j for j in i] for i in self.board]
        self.prev_turn = "0,0"

    def smart_random_move(self):
        board = [[self.board[i][j] for j in range(self.size)] for i in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] == 0:
                    board[i][j] = self.PLAYER
                    if self.check_win(board) == self.PLAYER:
                        print(j, i)
                        self.display_board()
                        return [j, i]
                    board[i][j] = 0
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] == 0:
                    board[i][j] = self.BOT
                    if self.check_win(board) == self.BOT:
                        print(j, i)
                        self.display_board()
                        return [j, i]
                    board[i][j] = 0
        return [random.randint(0, self.size-1), random.randint(0, self.size-1)]



def random_move(size=3):
    size -= 1
    return random.randint(0, size), random.randint(0, size)
