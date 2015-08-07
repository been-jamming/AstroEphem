import ephem
import math
import pygame
#Install pygame if you don't have the library

def Render(screen,planets):
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,0,0),planets[0],3)#draw Mercury
    pygame.draw.circle(screen,(204,0,153),planets[1],5)#draw Venus
    pygame.draw.circle(screen,(0,0,255),planets[2],6)#draw Earth
    pygame.draw.circle(screen,(255,50,50),planets[3],5)#draw Mars
    pygame.draw.circle(screen,(75,255,255),planets[4],9)#draw Jupiter
    pygame.draw.circle(screen,(255,255,255),planets[5],7)#draw Saturn
    pygame.draw.circle(screen,(20,20,255),planets[6],4)#draw Uranus
    pygame.draw.circle(screen,(0,0,255),planets[7],5)#draw Neptune
    pygame.draw.circle(screen,(200,200,200),planets[8],3)
    pygame.draw.circle(screen,(255,255,0),(300,300),int(zoom/3))#draw Sun
    pygame.display.flip()

def UpdatePlanets(planets,zoom = 200):
    outcoords=[]
    for planet in planets:
        planet.compute(ephem.now())
        lon = planet.hlon
        deg = ToDegrees(lon)
        dist = planet.sun_distance
        if dist == 0:
            dist = 1
        xpos = math.cos(math.radians(deg))*dist*zoom+300
        ypos = math.sin(math.radians(deg))*dist*zoom+300
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
    planets = [ephem.Mercury(),ephem.Venus(),ephem.Sun(),ephem.Mars(),ephem.Jupiter(),ephem.Saturn(),ephem.Uranus(),ephem.Neptune(),ephem.Pluto()]
    zoom = 200
    while True:
        coords = UpdatePlanets(planets,zoom)
        Render(screen,coords)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    zoom = zoom * 0.8
                elif event.button == 4:
                    zoom = zoom * 1.25
