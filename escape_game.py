import random


class Player:
    def __init__(self, name: str, row: int, column: int, health: int):
        self.__name = name
        self.__row = row
        self.__column = column
        self.__health = health
        self.__treasure_amount = 0

    def __str__(self):
        return f"{self.__name} - {self.__row} - {self.__column} - {self.__health} - {self.__treasure_amount}"


class IslandObject:
    def __init__(self, symbol: str, additional_info: str):
        self.__symbol = symbol
        self.__additional_info = additional_info


class Mine(IslandObject):
    def __init__(self, symbol: str, additional_info: str, health_deduct: int):
        super().__init__(symbol, additional_info)
        self.__health_deduct = health_deduct


class Medicine(IslandObject):
    def __init__(self, symbol: str, additional_info: str, health_added: int):
        super().__init__(symbol,  additional_info)
        self.__health_deduct = health_added


class Danger(IslandObject):
    def __init__(self, symbol: str, additional_info: str, danger_name: str, severity: str, health_deduct: int):
        super().__init__(symbol, additional_info)
        self.__danger_name = danger_name
        self.__health_deduct = health_deduct


class Treasure(IslandObject):
    def __init__(self, symbol: str, additional_info: str):
        super().__init__(symbol, additional_info)


# Main program
island = [[None for i in range(6)] for j in range(8)]

def place_mine(x_coordinate: int, y_coordinate: int, additional_info: str, health_deduct: int):
    mine = Mine(x_coordinate, y_coordinate, additional_info, health_deduct)
    for i in range(5):
        row = random.randint(0, 5)
        column = random.randint(0, 7)
        if island[row][column] != mine:
            island[row][column] = mine

def place_treasure(x_coordinate: int, y_coordinate: int, additional_info: str, health_added: int):
    treasure = Treasure(x_coordinate, y_coordinate, additional_info)
    for i in range(2):
        row = random.randint(0, 5)
        column = random.randint(0, 7)
        if island[row][column] != treasure:
            island[row][column] = treasure

def place_medicine(x_coordinate: int, y_coordinate: int, additional_info: str, health_added: int):
    medicine = Medicine(x_coordinate, y_coordinate, additional_info, health_added)

