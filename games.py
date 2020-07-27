import os
import random


games_path = 'Game'
games = os.listdir(games_path)

def play_game():
    game = random.choice(games)
    game = "Game\\" + game
    cmd = "start " + game
    os.system(cmd)
    return "Opening game"