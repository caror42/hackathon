import numpy as np
stars = []
timestep = 1*10**-9
G = 6.6743*10**-11
class star:
    def __init__(self, xpos, ypos, xvel, yvel, mass):
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = xvel
        self.yvel = yvel
        self.mass = mass
    def setPos(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def setVel(self, xvel, yvel):
        self.xvel = xvel
        self.yvel = yvel
def angToXY(angle, mag):
    return(mag*np.cos(angle), mag*np.sin(angle))
def distance(x1, y1, x2, y2):
    return(np.sqrt((x1-x2)**2+(y1-y2)**2))
def XYToAng(x, y):
    if x == 0:
        if y > 0:
            ang = np.pi/2
        else:
            ang = 3*np.pi/2
    elif (y < 0 and x < 0) or (y > 0 and x < 0):
        ang = np.arctan(y/x) + np.pi
    elif (y == 0 and x < 0):
        ang = np.pi
    else:
        ang = np.arctan(y/x)
    return(ang,np.sqrt(x**2+y**2))
def addVec(x1, y1, x2, y2):
    return(x1+x2, y1+y2)
def newVelAndPos(stars):
    newXVel = [];
    newYVel = [];
    for stary in stars:
        currXVel = stary.xvel
        currYVel = stary.yvel
        for staryy in stars:
            if(staryy != stary):
                a = G*staryy.mass/(distance(stary.xpos, stary.ypos, staryy.xpos, staryy.ypos)**2)
                aAng, junk = XYToAng(staryy.xpos-stary.xpos, staryy.ypos-stary.ypos)
                ax, ay = angToXY(aAng, a)
                currXVel = (ax*timestep+currXVel)
                currYVel = (ay*timestep+currYVel)
        newXVel.append(currXVel)
        newYVel.append(currYVel)
    for i in range(len(stars)):
        stars[i].setVel(newXVel[i], newYVel[i])
        stars[i].setPos(stars[i].xpos+newXVel[i]*timestep, stars[i].ypos+newYVel[i]*timestep)