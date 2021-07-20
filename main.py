import pygame as pg

from game import Game
from settings import *

game_name = "Asteroid Frenzy"
pg.init()
pg.mixer.init()
pg.display.set_caption(game_name)
pg.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

g = Game(game_name)
g.run()