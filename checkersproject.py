import itertools

class Board:
    def __init__(self):
        self.board = []
        self.numJumps = 0
        self.maxJumps = 0

        for row in range(8):
            self.board.append([])
            for col in range(8):
                self.board[row].append(" ")

    def reset(self):
        for row in range(8):
            for col in range(8):
                self.board[row][col] = " "

    def addChecker(self, who, row, col):
        self.board[row][col] = who

    def jumpPossible(self, row, col):
        if 0 <= row <= len(self.board) - 1 and 0 <= col <= len(self.board) - 1:
            if self.board[row][col] == " ":
                return True

        return False

    def isChar(self, char, row, col):
        if 0 <= row <= len(self.board) - 1 and 0 <= col <= len(self.board) - 1:
            if self.board[row][col] == char:
                return True

        return False

    def chooseJumps(self):
        if self.maxJumps <= self.numJumps:
            return self.numJumps
        else:
            return self.maxJumps

    def difJump(self, row, col, signV, signH):
        if self.isChar("B", row + signV * 1, col + signH * 1):
            if self.jumpPossible(row + signV * 2, col + signH * 2):
                self.numJumps += 1
                self.maxJumps = self.chooseJumps()

                self.addChecker("W", row + signV * 2, col + signH * 2)
                self.addChecker(" ", row + signV * 1, col + signH * 1)
                self.addChecker(" ", row, col)

                self.doJumps(row + signV * 2, col + signH * 2)

                self.addChecker(" ", row + signV * 2, col + signH * 2)
                self.addChecker("B", row + signV * 1, col + signH * 1)
                self.addChecker("W", row, col)
                self.numJumps -= 1


    def doJumps(self, row, col):
        # Up right
        self.difJump(row, col, 1, 1)
        # Down Right
        self.difJump(row, col, -1, 1)
        # Down left
        self.difJump(row, col, -1, -1)
        # Up Left
        self.difJump(row, col, 1, -1)

    def Print(self):
        for row in self.board:
            for col in row:
                print(col, end='')
            print()
        return


def getMaxJumps():
    file = open("input2.txt")

    for _ in itertools.repeat(0, int(file.readline())):

        board = Board()
        wchars, bchars = file.readline().split(" ")
        initRow, initCol = file.readline().split(" ")

        for __ in itertools.repeat(0, int(wchars) - 1):
            wChar = file.readline().split(" ")
            board.addChecker("W", int(wChar[0]), int(wChar[1]))

        for __ in itertools.repeat(0, int(bchars)):
            bChar = file.readline().split(" ")
            board.addChecker("B", int(bChar[0]), int(bChar[1]))

        board.doJumps(int(initRow), int(initCol))
        print("The number of jumps is %d" % board.maxJumps)
        board.reset()
        file.close()

getMaxJumps()
