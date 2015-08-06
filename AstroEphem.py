import ephem
import math
import pygame
#Install pygame if you don't have the library

def Render(screen,sun,jupiter):
    pygame.draw.circle(screen,(0,255,255),sun)
    pygame.display.flip()

def ToDegrees(lon):
    #This function converts longitude to degrees for trigonometric calculations
    parts = lon.split(":")
    for part in range(0,len(parts)):
        parts[part] = float(parts[part])
    deg = parts[0]
    deg += parts[1]/60
    deg += parts[2]/600
    return deg

if __name__ == "__main__":
    screen = pygame.display.set_mode(600,600)
    Jupiter = ephem.Jupiter()
    date = ephem.now()
    Jupiter.compute(date)
    lon = Jupiter.hlon
    deg = ToDegrees(lon)
    xpos = math.sin(math.radians(deg))*Jupiter.sun_distance
