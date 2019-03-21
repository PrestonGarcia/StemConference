import pygame
import time

ex = "C:\\Users\\prest\\Desktop\\Coding\\Stem Conference\\ex.png"
bcgd = "C:\\Users\\prest\\Desktop\\Coding\\Stem Conference\\bcgd.png"
there = "C:\\Users\\prest\\Desktop\\Coding\\Stem Conference\\there.png"
notthere = "C:\\Users\\prest\\Desktop\\Coding\\Stem Conference\\notthere.png"

class rectSprite:
    def __init__(self, screen, color, rectX, rectY, rectWidth, rectHeight, image):
        self.screen = screen
        self.color = color
        self.rectX = rectX
        self.rectY = rectY
        self.rectWidth = rectWidth
        self.rectHeight = rectHeight
        self.image = image
        self.image = pygame.image.load(image)
        self.rect = pygame.Rect((self.rectX, self.rectY) , (self.rectWidth, self.rectHeight))

    def draw(self):
        self.screen.blit(self.image, (self.rectX, self.rectY))

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

def numberToTable(number):

    return spriteList[number]

def moveDown(xCoords, targetTable, distanceFromTarget, direction):
    if direction == "right":
        while playerRect.rectX <= (xCoords - (horizontalDistanceTables) / 2):
            playerRect.rectX -= (horizontalDistanceTables) / 20
            screen.blit(backgroundImage, [0, 0])
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()
        while playerRect.rectY <= targetTable.rectY - 100:
            playerRect.rectY -= distanceFromTarget / 10
            screen.blit(backgroundImage, [0, 0])
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()
        while playerRect.rectX >= targetTable.rectX + 20:
            playerRect.rectX += (horizontalDistanceTables) / 20
            screen.blit(backgroundImage, [0, 0])
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()
    if direction == "left":
        while playerRect.rectX >= (xCoords + (horizontalDistanceTables) / 2):
            playerRect.rectX += (horizontalDistanceTables) / 20
            screen.blit(backgroundImage, [0, 0])
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()
        while playerRect.rectY <= targetTable.rectY - 100:
            playerRect.rectY -= distanceFromTarget / 10
            screen.blit(backgroundImage, [0, 0])
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()
        while playerRect.rectX <= targetTable.rectX - 20:
            playerRect.rectX -= (horizontalDistanceTables) / 20
            screen.blit(backgroundImage, [0, 0])
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()





def main():
    pygame.init()

    pygame.font.init()

    myFont = pygame.font.SysFont("Arial", 30)

    global backgroundImage

    backgroundImage = pygame.image.load(bcgd)

    info = pygame.display.Info()

    screenWidth = info.current_w

    screenHeight = info.current_h

    backgroundImage = pygame.transform.scale(backgroundImage, (screenWidth, screenHeight))

    global screen

    screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)

    done = False

    global clock

    clock = pygame.time.Clock()

    teacherTable = rectSprite(screen, (0, 128, 255), screenWidth / 2 - 30, 0, 60, 60, notthere)

    global playerRect

    playerRect = rectSprite(screen, (0, 128, 255), screenWidth / 2 - 30, 0, 60, 60, there)

    topLeftTable = rectSprite(screen, (255, 128, 0), screenWidth / 5 - 30, screenHeight / 4, 60, 60, ex)

    topMiddleTable = rectSprite(screen, (255, 128, 0), screenWidth / 2 - 30, screenHeight / 4, 60, 60, ex)

    topRightTable = rectSprite(screen, (255, 128, 0), screenWidth / 5 * 4 - 30, screenHeight / 4, 60, 60, ex)

    middleLeftTable = rectSprite(screen, (255, 128, 0), screenWidth / 5 - 30, screenHeight / 2, 60, 60, ex)

    centerTable = rectSprite(screen, (255, 128, 0), screenWidth / 2 - 30, screenHeight / 2, 60, 60, ex)

    middleRightTable = rectSprite(screen, (255, 128, 0), screenWidth / 5 * 4 - 30, screenHeight / 2, 60, 60, ex)

    bottomLeftTable = rectSprite(screen, (255, 128, 0), screenWidth / 5 - 30, screenHeight / 4 * 3, 60, 60, ex)

    bottomMiddleTable = rectSprite(screen, (255, 128, 0), screenWidth / 2 - 30, screenHeight / 4 * 3, 60, 60, ex)

    bottomRightTable = rectSprite(screen, (255, 128, 0), screenWidth / 5 * 4 - 30, screenHeight / 4 * 3, 60, 60, ex)

    global horizontalDistanceTables

    horizontalDistanceTables = middleLeftTable.rectX - centerTable.rectX

    global spriteList

    spriteList = [topLeftTable, middleLeftTable, bottomLeftTable, topMiddleTable, centerTable, bottomMiddleTable,
                  topRightTable, middleRightTable, bottomRightTable, teacherTable,  playerRect]

    rightList = [0, 1, 3, 4]

    leftList = [6, 7]

    playerPosition = 9

    startScreen = True
    while not done:
        if startScreen:
            controlCaption = myFont.render("Controls:", False, (255, 255, 255))

            screen.blit(controlCaption, (screenWidth / 2 - 40, 0))

            leftArrowCaption = myFont.render("← - Move one table to the left", False, (255, 255, 255))

            screen.blit(leftArrowCaption, (screenWidth / 2 - 170, screenHeight / 7))

            upArrowCaption = myFont.render("↑ - Move one table up", False, (255, 255, 255))

            screen.blit(upArrowCaption, (screenWidth / 2 - 120, screenHeight / 7 * 2))

            rightArrowCaption = myFont.render("→ - Move one table to the right", False, (255, 255, 255))

            screen.blit(rightArrowCaption, (screenWidth / 2 - 175, screenHeight / 7 * 3))

            downArrowCaption = myFont.render("↓ - Move one table down", False, (255, 255, 255))

            screen.blit(downArrowCaption, (screenWidth / 2 - 125, screenHeight / 7 * 4))

            spaceCaption = myFont.render("Spacebar interacts with the students", False, (255, 255, 255))

            screen.blit(spaceCaption, (screenWidth / 2 - 195, screenHeight / 7 * 5))

            escapeToExit = myFont.render("Press esc to exit", False, (255, 255, 255))

            screen.blit(escapeToExit, (screenWidth /2 - 85, screenHeight / 7 * 6))

            spaceToStart = myFont.render("Press space to start!", False, (255, 255, 255))

            screen.blit(spaceToStart, (screenWidth / 2 - 100, screenHeight - 40))


            for event in pygame.event.get():
                buttonPressed = pygame.key.get_pressed()

                if buttonPressed[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                    print("Shutting down!")
                    done = True

                if buttonPressed[pygame.K_SPACE]:
                    startScreen = False
        else:
            for event in pygame.event.get():

                buttonPressed = pygame.key.get_pressed()

                if buttonPressed[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                    print("Shutting down!")
                    done = True

                if buttonPressed[pygame.K_DOWN] and playerPosition == 9:
                    playerPosition = 3
                    while playerRect.rectY < (topMiddleTable.rectY - 100):
                        playerRect.rectY += screenHeight / 40
                        playerRect.rect.move(playerRect.rectX, playerRect.rectY)
                        time.sleep(0.25)
                        screen.blit(backgroundImage, [0, 0])
                        for n in spriteList:
                            n.draw()
                        pygame.display.flip()
                        pygame.event.pump()

                elif buttonPressed[pygame.K_DOWN] and not playerPosition == 9:
                    currentPosition = playerPosition
                    currentXCoords = int(playerRect.rectX)
                    playerPosition = getNextPosition("vertical", playerPosition)
                    playerTable = numberToTable(playerPosition)
                    distanceFromTarget = playerRect.rectY - playerTable.rectY - 1
                    if currentPosition in rightList:
                        moveDown(currentXCoords, playerTable, distanceFromTarget, "right")
                    if currentPosition in leftList:
                        moveDown(currentXCoords, playerTable, distanceFromTarget, "left")



                elif buttonPressed[pygame.K_UP] and not playerPosition == 9:
                    playerPosition = getPreviousPosition("vertical", playerPosition)
                    playerTable = numberToTable(playerPosition)
                    distanceFromTarget = playerRect.rectY - playerTable.rectY
                    while playerRect.rectY > playerTable.rectY:
                        playerRect.rectY -= distanceFromTarget / 10
                        time.sleep(0.25)
                        screen.blit(backgroundImage, [0, 0])
                        for n in spriteList:
                            n.draw()
                        pygame.display.flip()
                        pygame.event.pump()

                elif buttonPressed[pygame.K_RIGHT] and not playerPosition == 9:
                    playerPosition = getNextPosition("horizontal", playerPosition)
                    playerTable = numberToTable(playerPosition)
                    distanceFromTarget = playerRect.rectX - playerTable.rectX
                    while playerRect.rectX < playerTable.rectX:
                        playerRect.rectX -= distanceFromTarget / 10
                        time.sleep(0.25)
                        screen.blit(backgroundImage, [0, 0])
                        for n in spriteList:
                            n.draw()
                        pygame.display.flip()
                        pygame.event.pump()

                elif buttonPressed[pygame.K_LEFT] and not playerPosition == 9:
                    playerPosition = getPreviousPosition("horizontal", playerPosition)
                    playerTable = numberToTable(playerPosition)
                    distanceFromTarget = playerRect.rectX - playerTable.rectX
                    while playerRect.rectX > playerTable.rectX:
                        playerRect.rectX -= distanceFromTarget / 10
                        time.sleep(0.25)
                        screen.blit(backgroundImage, [0, 0])
                        for n in spriteList:
                            n.draw()
                        pygame.display.flip()
                        pygame.event.pump()

            screen.blit(backgroundImage, [0, 0])

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