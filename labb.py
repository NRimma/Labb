import pygame
def updateP(pts):
    for i in range(45):
        pts[0]-=1
        pts[1]+=1
        img = pygame.draw.circle(pygame.display.set_mode((700, 600)), color, pts, 50)
        pygame.display.update()
        pygame.display.flip()
    for j in range(45):
        pts[0]+=1
        pts[1]+=1
        img = pygame.draw.circle(pygame.display.set_mode((700, 600)), color, pts, 50)
        pygame.display.update()
        pygame.display.flip()
    for k in range(45):
        pts[0]+=1
        pts[1]-=1
        img = pygame.draw.circle(pygame.display.set_mode((700, 600)), color, pts, 50)
        pygame.display.update()
        pygame.display.flip()
    for q in range(45):
        pts[0]-=1
        pts[1]-=1
        img = pygame.draw.circle(pygame.display.set_mode((700, 600)), color, pts, 50)
        pygame.display.update()
        pygame.display.flip()

def shear(pts):
    for i in range(100):
        pts[0] += 1
        img = pygame.draw.circle(pygame.display.set_mode((700, 600)), color, pts, 50)
        pygame.display.update()
        pygame.display.flip()
    for j in range(200):
        pts[0] -= 1
        img = pygame.draw.circle(pygame.display.set_mode((700, 600)), color, pts, 50)
        pygame.display.update()
        pygame.display.flip()
    
surface = pygame.display.set_mode((700, 600))
color = (255, 255, 255)
points = [200,150]
pygame.display.init()
img = pygame.draw.circle(surface, color, [200, 150], 50)
pygame.display.flip()
pygame.time.wait(1000)
img = pygame.draw.circle(surface, color, [200, 150], 50)
pygame.time.wait(1000)
updateP([200,150]) 
shear(points)
pygame.display.flip()



