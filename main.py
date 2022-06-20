import pygame
import random
from pygame.math import Vector2
from triangle import Triangle
from settings import *
from colors import *

class Sierpinski:
    
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.xoff = X_OFF
        self.yoff = Y_OFF
        self.gameWinWidth = GAMEWIN_WIDTH
        self.gameWinHeight = GAMEWIN_HEIGHT
        self.fps = FPS
        self.clock = None
        self.titleFont = None
        self.grid = None
        self.win = None
        self.gameWin = None
        self.gameWinRect = None
        self.counter = 0
        self.level = 0
        self.maxLevel = MAXLEVEL
        self.triangles = []
        self.mainTriangle = None
        

    def grid_init(self):
        pygame.init()
        pygame.font.init()
        
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(TITLE)
        
        self.gameWinRect = pygame.Rect(self.xoff, self.yoff, self.gameWinWidth, self.gameWinHeight)
        self.gameWin = self.win.subsurface(self.gameWinRect)
        
        self.win.fill(MID_BLACK)
        self.gameWin.fill(BLACK)
        
        self.titleFont = pygame.font.SysFont(TITLE_FONT, FONT_SIZE)
        title = self.titleFont.render(TITLE, 1, GOLD)
        w, h = title.get_size()
        blitX = (self.width - w) // 2
        blitY = (self.yoff - h) // 2
        self.win.blit(title, (blitX, blitY))
        
        self.clock = pygame.time.Clock()
        
        margin = int(GAMEWIN_WIDTH * 0.05)
        pointA = Vector2(GAMEWIN_WIDTH // 2, margin)
        pointB = Vector2(margin, GAMEWIN_HEIGHT - margin)
        pointC = Vector2(GAMEWIN_WIDTH - margin, GAMEWIN_HEIGHT - margin)

        self.mainTriangle = Triangle(pointA, pointB, pointC)        
        self.triangles.append(self.mainTriangle)
        pygame.display.update()

    
    def close(self):
        pygame.font.quit()
        pygame.quit()
        
    
    def draw(self):
        self.mainTriangle.draw(self.gameWin)
        pygame.display.update()
        
    
    def add_level(self):
        for i in range(len(self.triangles)):
            triangle = self.triangles.pop(0)
            triangle.create_children()
            self.triangles.extend(triangle.getChildren())
            
        
        print(len(self.triangles))
        


    def run(self):
        if not pygame.display.init():
            self.grid_init()
            
        run = True
        while run:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_SPACE]:
                    self.add_level()

                            
            self.draw()
            
        self.close()
        


if __name__ == "__main__":
    print("Hello, World!")
    X = Sierpinski()
    X.run()