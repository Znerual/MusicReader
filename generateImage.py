import numpy as np
import cv2
import random
from CONST import _CONST as const
from analyseData import Test
CONST = const()
def create_blank(width, height, rgb_color=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image
def showImage(imageData):
    cv2.namedWindow('red', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('red', 500,500)

    cv2.imshow('red', imageData)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def recWayFunction(counter, before, lastDirection,  tail):
    #goal-point == (64,64)
    def generateDirection():
        #print("generateDirection")
        newPath = random.randint(0,1)
        ldirection = (0,0)
        if (lastDirection == (0,0) or validDirection(before, lastDirection) == False):
            newPath = 1
        if (newPath == 0):
            return lastDirection
        while True:
            xOry = random.randint(0,1)
            x = 0
            y = 0
            if (xOry == 0):
                x = random.randint(-CONST.MAX_STEP_SIZE,CONST.MAX_STEP_SIZE)
            else:
                y = random.randint(-CONST.MAX_STEP_SIZE,CONST.MAX_STEP_SIZE)
            ldirection = (x,y)
            if (validDirection(before, ldirection) == True):
                break
        return ldirection
    def validDirection(position, direction):
        x,y = position
        dx,dy = direction
        if (dx == 0 and dy == 0):
            return False
        if (x + dx >= 0 and x + dx < CONST.WIDTH and y + dy < CONST.HEIGHT and y + dy >= 0):
            return True
        return False

    direction = generateDirection()
    #print("d:" + str(direction))
    position = tuple(map(sum, zip(direction, before)))
    #print("p:" + str(position))
    tail.append(position)
    if (position != CONST.GOAL and counter < CONST.MAX_ITERATION_LENGTH):
        if (counter % 10 == 0):
            print(counter)
        return recWayFunction(counter + 1 ,position, direction, tail)
        print(counter)
    else:
        print("finished generating")
        return tail
black = (0, 0, 0)

print("initialising")
path = recWayFunction(0,(0,0),(0,0),[(0,0)])
print("created Path")
testResult = Test().findJumps(path, CONST.MAX_STEP_SIZE)
print("tested data")
print("Tests were " + str(testResult))
image = create_blank(CONST.WIDTH, CONST.HEIGHT, rgb_color=black)
#for x,y in path:
#    image[x,y] = [255,255,255]
for i in range(0, len(path) -1):
    x1,y1 = path[i]
    x2,y2 = path[i+1]
    print("x1: " + str(x1) + " x2: " + str(x2) + " y1: " + str(y1) + " y2: " + str(y2))
    if (x2 - x1 == 0):
        image[x1,y1:y2] = [255 - i ,255 - (i/2),255 - (i /5)]
    if (y2 - y1 == 0):
        image[x1:x2,y1] = [255 - i ,255 - (i/2),255 - (i /5)]
print("Pfadlänge: " + str(len(path)))
showImage(image)
