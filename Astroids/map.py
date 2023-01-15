import numpy as np

from ship import Ship

class Map:
    def __init__(self, mapSize=None, map_array=None) -> None:
        self.mapSize = mapSize
        self.player_position = None
        self.left_threshold = 2

        if map_array is None:
            if self.mapSize is not None:
                self.map = np.tile(' ', self.mapSize[0] * self.mapSize[1]).reshape(self.mapSize)
            else:
                self.map =  self.create_map_from_string("Game/map_create.txt")
                # TODO: set mapSize by counting number of rows and longest row
                self.mapSize = self.map.shape()
        else:
            self.map = map_array

        # TODO:
        # Define properties for like rock:O, needle/spear:^, wall:#,|
        # map_create should only contain indicators
        # the specific char should be set by that properties
        self.map_symbols_def = {
            ">" : "TODO: change",
            "P" : "player",
            "g" : "ground",
            "s" : "spear/spike",
            "b" : "boarder",
            " " : "air"
        }
        self.map_symbols = {
            ">" : ">",
            "P" : "P",
            "g" : "#",
            "s" : "^",
            "b" : "|",
            " " : " "
        }
        self.collision_actions = {
            "g" : 0,
            "b" : 0,
            "s" : -1,
        }

    def create_map_from_string(self, path_map_create : str):
        # TODO-FIX: inserts one empty col in front and maybe similar in back
        # TODO: not clean, but somehow working
        with open(path_map_create, "r") as map_create:
            row = 0
            col = 0
            for point_char in map_create.read():
                if point_char == "\n":
                    row += 1
                    col = 0
                    continue
                elif point_char == "P":
                    self.player_position = np.array([row, col])
                    point_char = "x"
                
                self.map[row][col % self.mapSize[1]] = point_char
                col += 1
    
    ### inserted in draw_map (but not accurates)
    # def draw_map_outline(self, outside=True):
    #     offset = 0
    #     if not outside:
    #         offset = 2

    #     # top
    #     print((self.mapSize[1] + 2 - offset) * "-")

    #     # sides
    #     emptySpaces = (self.mapSize[1] - offset) * " "
    #     for i in range(self.mapSize[0] - offset):
    #         print(f"|{emptySpaces}|")

    #     # bottom
    #     print((self.mapSize[1] + 2 - offset) * "-")

    # def draw_map_inside(self):
    #     for i in range(self.mapSize[0]):
    #         print(self.mapSize[1] * "#")

    def draw_map(self, outline=False, fillMapWith:str =None):
        boarder = ""

        if outline:
            print("-" * (self.mapSize[1] + 2))
            boarder = "|"
        
        # i = 0
        for line in self.map:
            
            printLine = boarder
            for point in line:
                if (fillMapWith != None) & (fillMapWith != ""):
                    printLine += fillMapWith
                else:
                    # if point == "P":
                    #     continue
                    # print(f"line {i}, char: {point}")
                    printLine += self.map_symbols[point]
            # i+=1
            print(printLine + boarder)

        if outline:
            print("-" * (self.mapSize[1] + 2))

    def insert_ship(self, ship: Ship):
        # print(player)
        # x, y = tuple(self.player_position)
        r = self.player_position[0]
        c = self.player_position[1]
        
        self.map[r][c] = ship.idle_static

    def move_player(self, player, position: list):
        r = self.player_position[0]
        c = self.player_position[1]
        self.map[r][c] = " "
        # print(self.player_position, " -> ", end="")
        
        self.player_position = position
        # print(self.player_position)

        r = self.player_position[0]
        c = self.player_position[1]

        self.map[r][c] = player.idle_static
        # print(np.shape(self.map))

    def move_player_by(self, player, move_by):
        new_position = self.player_position + np.array(move_by)

        # clip to boundary
        if new_position[0] < 0:
            new_position[0] = 0
        
        if new_position[1] < self.left_threshold: # 0:
            new_position[1] = self.left_threshold # 0

        if new_position[0] > self.mapSize[0]-1:
            new_position[0] = self.mapSize[0]-1
        
        if new_position[1] > self.mapSize[1]-1:
            new_position[1] = self.mapSize[1]-1

        if ((new_position[0] == self.player_position[0]) 
            & (new_position[1] == self.player_position[1])):
            # dont call moving function if position not changed
            return

        collision_element = self.detect_collision(new_position)
        if collision_element is None:
            self.move_player(player, new_position)
            return
            
        # self.handle_collision()
        collision_action = self.collision_actions[collision_element]
        # if collision_action is not None:
        # game over will be executed by game.py
        # only problem if there are other actions specific for map.py
        return collision_action

        # otherwise don't move


    def detect_collision(self, position):
        # detect if collision occured
        # -> no: return None
        # -> yes: return object and/or its position
        r = position[0]
        c = position[1]

        map_element = self.map[r][c]
        if map_element == " ":
            return None
        
        ## seemingly not neccesarry
        # print("map_element:", map_element)
        # k_list = list(self.map_symbols.keys())
        # idx = list(self.map_symbols.values()).index(map_element)
        # key = k_list[idx]
        # return key
        return map_element


    def handle_collision(self):
        # called if detect_collision() != None
        # should decide how to handle
        # e.g. collision with ground -> dont move
        # collision with spike -> Game Over (damage)
        pass

    def get_player_position(self) -> tuple:
        return self.player_position

    # def set_player_to_threshold()

    def roll_map(self, player):
        self.map = np.roll(self.map, -1, axis=1)
        print(self.player_position)

        # this moves the player with the field -> don't want this
        self.player_position += [0, -1]
        self.player_position %= self.mapSize[1]
        
        # not moving player
        # self.move_player_by(player, [0, 1])
        # self.player_position %= self.mapSize[1]
        # print(self.player_position)

    def spawn_map(self):
        pass


if __name__ == '__main__':

    mapSize = (7, 80)
    map = Map(mapSize)
    map.create_map_from_string("Game\map_create.txt")
    # print(map.map)

    # map.draw_map_outline()
    # map.draw_map_inside()

    map.draw_map()

    # print(map.shape)
    # for i in map:
    #     for j in i:
    #         print(j,end = "")
    #     print("")
