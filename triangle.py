import pygame
from pygame.math import Vector2
from pygame.surface import Surface
from typing import List
from colors import WHITE

class Triangle:
    
    def __init__(self, pointA: Vector2, pointB: Vector2, pointC: Vector2):
        self.pA = pointA
        self.pB = pointB
        self.pC = pointC
        
        self.children = []
        
    def draw(self, win: Surface) -> None:
        pygame.draw.lines(win, WHITE, True, (self.pA, self.pB, self.pC), width=2)
        for child in self.children:
            child.draw(win)
        
        pygame.display.update()
        
    def create_children(self) -> None:
        midAB = (self.pA + self.pB) // 2
        midBC = (self.pB + self.pC) // 2
        midAC = (self.pA + self.pC) // 2
        
        triangleA = Triangle(self.pA, midAB, midAC)
        triangleB = Triangle(self.pB, midAB, midBC)
        triangleC = Triangle(self.pC, midAC, midBC)
        
        self.children.extend((triangleA, triangleB, triangleC))
        
    def getChildren(self) -> List[object]:
        return self.children