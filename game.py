import pygame as pg
import sys

from settings import *

class Game:
    def __init__(self, name, assets=None):
        self.name = name
        self.start = False

    def run(self):
        self.game_loop()

    def game_loop(self):
        while True:
            # self.clock.tick(FPS)
            self.event_handler()
            self.update()
            self.draw()

    def update(self):
        pass

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.type == pg.K_RETURN:
                    self.start = True

    def draw(self):
        pass