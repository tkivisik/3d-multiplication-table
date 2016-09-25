## 3D Multiplication Table
## Taavi Kivisik

## Idea
## * Leemet can walk around (location changes)
## * Leemet can look around (see the value of landscape)
## * Landscape is displayed (. . 3)
## * Build GUI
## * GAME - number ==> click the right spot
## * GAME - number ==> shortest route to that number

## todo
## * GUI - menu, drag-drop game

import os                   # to clear the screen
from pathlib import Path    # to build a file path

class Landscape(object):
    filler = "."
    level_indicator = "x"
    
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.data = [[[0 for x in range(self.size)]
                        for x in range(self.size)]
                        for x in range(self.size)]  # 3D matrix of 0s

        # Only compute each multiplication once.
        for x in range(1, self.size + 1):
            for y in range(1, x + 1):
                for z in range(1, y + 1):
                    self.data[x-1][y-1][z-1] = x * y * z
#                    print(x, "*", y, "*", z, "=", self.data[x-1][y-1][z-1])
        print("{0} is created.".format(self.name))

    def show_landscape(self, x, y, z):
        # Counting downwards mirrors the landscape so highest row will be iterated first.
        for row in range(self.size, 0, -1):
            line = ""

            # Columns
            if y == row:
                for column in range(1, self.size + 1):
                    if x == column:
                        line += str(self.get_value(x, y, z)).rjust(3)
                    else:
                        line += self.filler.rjust(3)
            else:
                for column in range(1, self.size + 1):
                    line += self.filler.rjust(3)

            if z >= row:
                line += self.level_indicator.rjust(6)
            print(line)

    def get_value(self, x, y, z):
        descended = sorted([x, y, z], reverse = True)
        data_x = descended[0]
        data_y = descended[1]
        data_z = descended[2]
        return self.data[data_x-1][data_y-1][data_z-1]

    def export_csv(self, separator = ",", file_name = "3d-multiplication-data.csv"):
        file = Path("./{0}".format(file_name))

        # Only write a file when it doesn't exist already
        if not file.is_file():
            export_this = "row{0}column{0}level{0}value\n".format(separator)
            for x in range(1, self.size + 1):
                for y in range(1, x + 1):
                    for z in range(1, y + 1):
                        export_this += "{0}{4}{1}{4}{2}{4}{3}\n".format(z,y,x,self.data[x-1][y-1][z-1],separator)
            f = open("3d-multiplication-data.csv", "w")
            f.write(export_this)
            f.close()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.x = 1
        self.y = 1
        self.z = 1
        print("{0} is ready to play :)".format(self.name))

    def print_location(self):
        print("You have arrived to: Cube({0},{1},{2}) = {3}".format(self.x, self.y, self.z,
                                            Cube.get_value(self.x, self.y, self.z)))

    #MOVEMENTS
    def move_right(self):
        if self.x < Cube.size:
            self.x += 1
        self.print_location()
    def move_left(self):
        if self.x > 1:
            self.x -= 1
        self.print_location()

    def move_forward(self):
        if self.y < Cube.size:
            self.y += 1
        self.print_location()
    def move_backward(self):
        if self.y > 1:
            self.y -= 1
        self.print_location()

    def move_up(self):
        if self.z < Cube.size:
            self.z += 1
        self.print_location()
    def move_down(self):
        if self.z > 1:
            self.z -= 1
        self.print_location()



### INITIATION
clear = lambda: os.system('cls')
Cube = Landscape("Cube", 20)
Leemet = Player("Leemet")
Cube.export_csv()


while True:
    clear()
    Cube.show_landscape(Leemet.x, Leemet.y, Leemet.z)
    print("Click WASD and EQ keys to move around the", Cube.name)
    print("E for EXIT\n")
    action = input()
    
    ##  Forward-backward = Y
    if action == "w":
        Leemet.move_forward()
    elif action == "s":
        Leemet.move_backward()

    ##  Left-Right = X
    elif action == "d":
        Leemet.move_right()
    elif action == "a":
        Leemet.move_left()
    
    ##  Up-Down = Z
    elif action == "e":
        Leemet.move_up()
    elif action == "q":
        Leemet.move_down()

    ##  EXIT
    elif action == "x":
        break
