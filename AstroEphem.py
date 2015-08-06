import ephem
import math
import pygame
#Install pygame if you don't have the library

def Render(screen,planets):
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,255,0),(300,300),10)
    pygame.draw.circle(screen,(255,0,0),planets[0],2)
    pygame.draw.circle(screen,(204,0,153),planets[1],5)
    pygame.draw.circle(screen,(0,0,255),planets[2],6)
    pygame.display.flip()

def UpdatePlanets(planets):
    outcoords=[]
    for planet in planets:
        planet.compute(ephem.now())
        lon = planet.hlon
        deg = ToDegrees(lon)
        xpos = math.cos(math.radians(deg))*planet.sun_distance*200+300
        ypos = math.sin(math.radians(deg))*planet.sun_distance*200+300
        outcoords.append([int(xpos),int(ypos)])
    return outcoords

def ToDegrees(lon):
    #This function converts longitude to degrees for trigonometric calculations
    parts = str(lon).split(":")
    for part in range(0,len(parts)):
        parts[part] = float(parts[part])
    deg = parts[0]
    deg += parts[1]/60
    deg += parts[2]/600
    return -deg

if __name__ == "__main__":
    screen = pygame.display.set_mode((600,600))
    planets = [ephem.Mercury(),ephem.Venus(),ephem.Mars(),ephem.Jupiter(),ephem.Saturn(),ephem.Uranus(),ephem.Neptune()]
    while True:
        coords = UpdatePlanets(planets)
        Render(screen,coords)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
