import pygame
import time



class rectSprite:
    def __init__(self, screen, color, rectX, rectY, rectWidth, rectHeight):
        self.screen = screen
        self.color = color
        self.rectX = rectX
        self.rectY = rectY
        self.rectWidth = rectWidth
        self.rectHeight = rectHeight
    
    def draw(self):
        pygame.draw.rect(self.screen, (self.color), pygame.Rect(self.rectX, self.rectY, self.rectWidth, self.rectHeight))

rowOne = [0, 3, 6]
rowTwo = [1, 4, 7]
rowThree = [2, 5, 8]
columnOne = [0, 1, 2]
columnTwo = [3, 4, 5]
columnThree = [6, 7, 8]

def getNextPosition(axis, currentPosition):
    if axis == "horizontal":

        if currentPosition in rowOne:
            currentIndex = rowOne.index(currentPosition)
            nextIndex = currentIndex + 1
            if nextIndex > 2:
                nextIndex = 2
            return rowOne[nextIndex]

        if currentPosition in rowTwo:
            currentIndex = rowTwo.index(currentPosition)
            nextIndex = currentIndex + 1
            if nextIndex > 2:
                nextIndex = 2
            return rowTwo[nextIndex]

        if currentPosition in rowThree:
            currentIndex = rowThree.index(currentPosition)
            nextIndex = currentIndex + 1
            if nextIndex > 2:
                nextIndex = 2
            return rowThree[nextIndex]

    if axis == "vertical":

        if currentPosition in columnOne:
            currentIndex = columnOne.index(currentPosition)
            nextIndex = currentIndex + 1
            if nextIndex > 2:
                nextIndex = 2
            return columnOne[nextIndex]

        if currentPosition in columnTwo:
            currentIndex = columnTwo.index(currentPosition)
            nextIndex = currentIndex + 1
            if nextIndex > 2:
                nextIndex = 2
            return columnTwo[nextIndex]

        if currentPosition in columnThree:
            currentIndex = columnThree.index(currentPosition)
            nextIndex = currentIndex + 1
            if nextIndex > 2:
                nextIndex = 2
            return columnThree[nextIndex]

def getPreviousPosition(axis, currentPosition):
    if axis == "horizontal":

        if currentPosition in rowOne:
            currentIndex = rowOne.index(currentPosition)
            nextIndex = currentIndex - 1
            if nextIndex < 0:
                nextIndex = 0
            return rowOne[nextIndex]

        if currentPosition in rowTwo:
            currentIndex = rowTwo.index(currentPosition)
            nextIndex = currentIndex - 1
            if nextIndex < 0:
                nextIndex = 0
            return rowTwo[nextIndex]

        if currentPosition in rowThree:
            currentIndex = rowThree.index(currentPosition)
            nextIndex = currentIndex - 1
            if nextIndex < 0:
                nextIndex = 0
            return rowThree[nextIndex]

    if axis == "vertical":

        if currentPosition in columnOne:
            currentIndex = columnOne.index(currentPosition)
            nextIndex = currentIndex - 1
            if nextIndex < 0:
                nextIndex = 0
            return columnOne[nextIndex]

        if currentPosition in columnTwo:
            currentIndex = columnTwo.index(currentPosition)
            nextIndex = currentIndex - 1
            if nextIndex < 0:
                nextIndex = 0
            return columnTwo[nextIndex]

        if currentPosition in columnThree:
            currentIndex = columnThree.index(currentPosition)
            nextIndex = currentIndex - 1
            if nextIndex < 0:
                nextIndex = 0
            return columnThree[nextIndex]

def main():
    pygame.init()

    pygame.font.init()

    myFont = pygame.font.SysFont("Arial", 30)

    info = pygame.display.Info()

    screenWidth = info.current_w

    screenHeight = info.current_h

    screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)

    done = False

    clock = pygame.time.Clock()

    playerRect = rectSprite(screen, (0, 128, 255), screenWidth / 2 - 30, 0, 60, 60)

    topLeftTable = rectSprite(screen, (255, 128, 0), screenWidth / 5 - 30, screenHeight / 4, 60, 60)

    topMiddleTable = rectSprite(screen, (255, 128, 0), screenWidth / 2 - 30, screenHeight / 4, 60, 60)

    topRightTable = rectSprite(screen, (255, 128, 0), screenWidth / 5 * 4 - 30, screenHeight / 4, 60, 60)

    middleLeftTable = rectSprite(screen, (255, 128, 0), screenWidth / 5 - 30, screenHeight / 2, 60, 60)

    centerTable = rectSprite(screen, (255, 128, 0), screenWidth / 2 - 30, screenHeight / 2, 60, 60)

    middleRightTable = rectSprite(screen, (255, 128, 0), screenWidth / 5 * 4 - 30, screenHeight / 2, 60, 60)

    bottomLeftTable = rectSprite(screen, (255, 128, 0), screenWidth / 5 - 30, screenHeight / 4 * 3, 60, 60)

    bottomMiddleTable = rectSprite(screen, (255, 128, 0), screenWidth / 2 - 30, screenHeight / 4 * 3, 60, 60)

    bottomRightTable = rectSprite(screen, (255, 128, 0), screenWidth / 5 * 4 - 30, screenHeight / 4 * 3, 60, 60)

    spriteList = [playerRect, topLeftTable, topMiddleTable, topRightTable, middleLeftTable, centerTable, middleRightTable,
                  bottomLeftTable, bottomMiddleTable, bottomRightTable]

    playerPosition = 9

    while not done:

        for event in pygame.event.get():

            buttonPressed = pygame.key.get_pressed()

            if buttonPressed[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                print("Shutting down!")
                done = True

            if buttonPressed[pygame.K_DOWN] and playerPosition == 9:
                playerPosition = 3

            if buttonPressed[pygame.K_DOWN] and not playerPosition == 9:
                playerPosition = getNextPosition("vertical", playerPosition)
                print(playerPosition)

            if buttonPressed[pygame.K_UP] and not playerPosition == 9:
                playerPosition = getPreviousPosition("vertical", playerPosition)
                print(playerPosition)

            if buttonPressed[pygame.K_RIGHT] and not playerPosition == 9:
                playerPosition = getNextPosition("horizontal", playerPosition)
                print(playerPosition)

            if buttonPressed[pygame.K_LEFT] and not playerPosition == 9:
                playerPosition = getPreviousPosition("horizontal", playerPosition)
                print(playerPosition)

        screen.fill((0, 0, 0))

        for n in spriteList:
            n.draw()

        if playerPosition == 9:
            textSurface = myFont.render("Press Down to start!", False, (0, 128, 255))

            screen.blit(textSurface, (0, 0))

        pygame.display.flip()

        pygame.event.pump()

        clock.tick(60)

    pygame.quit()

main()