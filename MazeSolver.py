import random

class Maze:
    
    def __init__(self, maze):
        self.maze = maze
        self.unsolved = True

    def CanMove(self, row, col):
        if 0 <= row < len(self.maze) and 0 <= col < len(self.maze[row]):
            return self.maze[row][col] == " " or self.maze[row][col] == "E"
        else:
            return False

    def Move(self, row, col):
        if self.unsolved:
            if self.maze[row][col] == "E":
                self.unsolved = False
            elif self.maze[row][col] != "S":
                self.maze[row][col] = 'P'
            
            # up
            if ( self.CanMove(row-1, col) ):
                self.Move(row-1, col)
                if self.unsolved:
                    self.maze[row-1][col] = 'D'

            # right
            if ( self.CanMove(row, col + 1) ):
                self.Move(row, col + 1)
                if self.unsolved:
                    self.maze[row][col+1] = 'D'
            # down
            if ( self.CanMove(row + 1, col) ):
                self.Move(row + 1, col)
                if self.unsolved:
                    self.maze[row + 1][col] = 'D'

            # Left
            if ( self.CanMove(row, col-1) ):
                self.Move(row, col-1)
                if self.unsolved:
                    self.maze[row][col-1] = 'D'

    def Print(self):
        for line in self.maze:
            for letter in line:
                print(letter, end='')
            print()
        print()

    def FindStart(self):
        for row, line in enumerate(self.maze):
            endColumn = line.index("S")
            if endColumn >= 0:
                return row, endColumn
    
    def Solve(self):
        startRow, startCol = self.FindStart()
        self.Move( startRow, startCol )

for mazeNumber in range(1):
    mazeList = []
    mazeList.append([' ',' ',' ',' ',' ','W','W','W','W','W'])
    mazeList.append([' ',' ',' ','W',' ',' ',' ',' ','W','W'])
    mazeList.append(['W','W',' ','W',' ','W','W',' ','W','W'])
    mazeList.append(['W','W',' ','W',' ','W','W',' ','W','W'])
    mazeList.append([' ',' ',' ','W',' ','W','W',' ','W','W'])
    mazeList.append([' ','W','W','W',' ','W','W',' ','W','W'])
    mazeList.append([' ','W','W','W',' ','W','W',' ','W','W'])
    mazeList.append([' ',' ',' ',' ',' ',' ',' ','E',' ',' '])
    mazeList.append(['W','W','W','W','W','W','W','W','W',' '])
    mazeList.append(['W','W','W','W','W','W','W','W','W',' '])

    newMaze = Maze(mazeList)
    newMaze.Solve()
    print("Maze Number:", mazeNumber)
    newMaze.Print()
    print()
