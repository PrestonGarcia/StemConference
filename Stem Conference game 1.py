import pygame
import time
import os
import random

filePath = os.getcwd()
ex = os.path.join(filePath, "ex.png")
bcgd = os.path.join(filePath, "bcgd.png")
there = os.path.join(filePath, "there.png")
notthere = os.path.join(filePath, "notthere.png")
idle = os.path.join(filePath, "idle.png")
replayButtonPath = os.path.join(filePath, "replayButton.png")

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

class studentSprite(rectSprite):
    def __init__(self, screen, color, rectX, rectY, rectWidth, rectHeight, image):
        super().__init__(screen, color, rectX, rectY, rectWidth, rectHeight, image)
        self.confused = False
        self.chances = 0
    def becomeConfused(self):
        self.confused = True
    def resolveConfusion(self):
        self.confused = False


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
    questionMark = os.path.join(filePath, "questionMark.png")
    questionMark = pygame.image.load(questionMark)
    if direction == "right" and not abs(distanceFromTarget) <= 80:
        playerRect.image = pygame.transform.rotate(playerRect.image, -90)
        while playerRect.rectX <= (xCoords - (horizontalDistanceTables) / 4):
            playerRect.rectX -= (horizontalDistanceTables) / 40
            screen.blit(backgroundImage, [0, 0])
            for n in spriteList:
                n.draw()
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX, n.rectY))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.125 / 2)
            pygame.display.flip()
            pygame.event.pump()
        playerRect.image = pygame.transform.rotate(playerRect.image, 90)
        while playerRect.rectY <= targetTable.rectY - 80:
            playerRect.rectY -= distanceFromTarget / 40
            screen.blit(backgroundImage, [0, 0])
            for n in spriteList:
                n.draw()
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX, n.rectY))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.125 / 2)
            pygame.display.flip()
            pygame.event.pump()
        playerRect.image = pygame.transform.rotate(playerRect.image, -90)
        while playerRect.rectX >= targetTable.rectX:
            playerRect.rectX += (horizontalDistanceTables) / 40
            screen.blit(backgroundImage, [0, 0])
            for n in spriteList:
                n.draw()
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX, n.rectY))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.125 / 2)
            pygame.display.flip()
            pygame.event.pump()
        playerRect.image = pygame.transform.rotate(playerRect.image, 90)
    if direction == "left" and not abs(distanceFromTarget) <= 80:
        playerRect.image = pygame.transform.rotate(playerRect.image, -90)
        while playerRect.rectX >= (xCoords + (horizontalDistanceTables) / 4):
            playerRect.rectX += (horizontalDistanceTables) / 40
            screen.blit(backgroundImage, [0, 0])
            for n in spriteList:
                n.draw()
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX, n.rectY))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.125 / 2)
            pygame.display.flip()
            pygame.event.pump()
        playerRect.image = pygame.transform.rotate(playerRect.image, 90)
        while playerRect.rectY <= targetTable.rectY - 100:
            playerRect.rectY -= distanceFromTarget / 40
            screen.blit(backgroundImage, [0, 0])
            for n in spriteList:
                n.draw()
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX, n.rectY))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.125 / 2)
            pygame.display.flip()
            pygame.event.pump()
        playerRect.image = pygame.transform.rotate(playerRect.image, -90)
        while playerRect.rectX <= targetTable.rectX:
            playerRect.rectX -= (horizontalDistanceTables) / 40
            screen.blit(backgroundImage, [0, 0])
            for n in spriteList:
                n.draw()
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX, n.rectY))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.125 / 2)
            pygame.display.flip()
            pygame.event.pump()
        playerRect.image = pygame.transform.rotate(playerRect.image, 90)

def moveUp(xCoords, targetTable, distanceFromTarget, direction):
    questionMark = os.path.join(filePath, "questionMark.png")
    questionMark = pygame.image.load(questionMark)
    if direction == "right" and not abs(distanceFromTarget) <= 80:
        playerRect.image = pygame.transform.rotate(playerRect.image, 90)
        while playerRect.rectX <= (xCoords - (horizontalDistanceTables) / 4):
            playerRect.rectX -= (horizontalDistanceTables) / 40
            screen.blit(backgroundImage, [0, 0])
            for n in spriteList:
                n.draw()
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX, n.rectY))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.125 / 4)
            pygame.display.flip()
            pygame.event.pump()
        playerRect.image = pygame.transform.rotate(playerRect.image, -90)
        while playerRect.rectY >= targetTable.rectY - 100:
            playerRect.rectY -= distanceFromTarget / 40
            screen.blit(backgroundImage, [0, 0])
            for n in spriteList:
                n.draw()
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX, n.rectY))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.125 / 4)
            pygame.display.flip()
            pygame.event.pump()
        playerRect.image = pygame.transform.rotate(playerRect.image, 90)
        while playerRect.rectX >= targetTable.rectX:
            playerRect.rectX += (horizontalDistanceTables) / 40
            screen.blit(backgroundImage, [0, 0])
            for n in spriteList:
                n.draw()
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX, n.rectY))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.125 / 4)
            pygame.display.flip()
            pygame.event.pump()
        playerRect.image = pygame.transform.rotate(playerRect.image, -90)
    if direction == "left" and not abs(distanceFromTarget) <= 80:
        playerRect.image = pygame.transform.rotate(playerRect.image, -90)
        while playerRect.rectX >= (xCoords + (horizontalDistanceTables) / 4):
            playerRect.rectX += (horizontalDistanceTables) / 40
            screen.blit(backgroundImage, [0, 0])
            for n in spriteList:
                n.draw()
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX, n.rectY))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.125 / 2)
            pygame.display.flip()
            pygame.event.pump()
        playerRect.image = pygame.transform.rotate(playerRect.image, 90)
        while playerRect.rectY >= targetTable.rectY - 100:

            playerRect.rectY -= distanceFromTarget / 40
            screen.blit(backgroundImage, [0, 0])
            for n in spriteList:
                n.draw()
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX, n.rectY))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.125 / 4)
            pygame.display.flip()
            pygame.event.pump()
        playerRect.image = pygame.transform.rotate(playerRect.image, -90)
        while playerRect.rectX <= targetTable.rectX:
            playerRect.rectX -= (horizontalDistanceTables) / 40
            screen.blit(backgroundImage, [0, 0])
            for n in spriteList:
                n.draw()
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX, n.rectY))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.125 / 2)
            pygame.display.flip()
            pygame.event.pump()
        playerRect.image = pygame.transform.rotate(playerRect.image, 90)


def gameOver():

    done = False

    while not done:

        for event in pygame.event.get():



            buttonPressed = pygame.key.get_pressed()

            if buttonPressed[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                done = True

            screen.fill((0, 0, 0))

            gameOverText = myFont.render("Game over, you didn't have enough money!", False, (255, 255, 255))

            replayPrompt = myFont.render("Press the button to replay", False, (255, 255, 255))

            replayButton = pygame.image.load(replayButtonPath)

            screen.blit(gameOverText, (screenWidth / 2 - 245, screenHeight / 4))

            screen.blit(replayPrompt, (screenWidth / 2 - 140, screenHeight / 2))

            screen.blit(replayButton, (screenWidth / 2 - 50, 3 * screenHeight / 4))

            if (event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 650
                and pygame.mouse.get_pos()[0] < 714 and pygame.mouse.get_pos()[1] > 618 and
                pygame.mouse.get_pos()[1] < 642):

                main()


        pygame.display.flip()

        pygame.event.pump()







def main():

    questionMark = os.path.join(filePath, "questionMark.png")

    day = 1

    finalAmount = 30

    needNewTime = True

    pygame.init()

    pygame.font.init()

    global myFont

    myFont = pygame.font.SysFont("Arial", 30)

    global backgroundImage

    backgroundImage = pygame.image.load(bcgd)

    info = pygame.display.Info()

    global screenWidth

    screenWidth = info.current_w

    global screenHeight

    screenHeight = info.current_h

    backgroundImage = pygame.transform.scale(backgroundImage, (screenWidth, screenHeight))

    global screen

    screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)

    done = False

    global clock

    clock = pygame.time.Clock()

    teacherTable = rectSprite(screen, (0, 128, 255), screenWidth / 2, 0, 60, 60, notthere)

    global playerRect

    playerRect = rectSprite(screen, (0, 128, 255), screenWidth / 2, 0, 60, 60, there)

    topLeftTable = studentSprite(screen, (255, 128, 0), screenWidth / 5, screenHeight / 4, 60, 60, ex)

    topMiddleTable = studentSprite(screen, (255, 128, 0), screenWidth / 2, screenHeight / 4, 60, 60, ex)

    topRightTable = studentSprite(screen, (255, 128, 0), screenWidth / 5 * 4, screenHeight / 4, 60, 60, ex)

    middleLeftTable = studentSprite(screen, (255, 128, 0), screenWidth / 5, screenHeight / 2, 60, 60, ex)

    centerTable = studentSprite(screen, (255, 128, 0), screenWidth / 2, screenHeight / 2, 60, 60, ex)

    middleRightTable = studentSprite(screen, (255, 128, 0), screenWidth / 5 * 4, screenHeight / 2, 60, 60, ex)

    bottomLeftTable = studentSprite(screen, (255, 128, 0), screenWidth / 5, screenHeight / 4 * 3, 60, 60, ex)

    bottomMiddleTable = studentSprite(screen, (255, 128, 0), screenWidth / 2, screenHeight / 4 * 3, 60, 60, ex)

    bottomRightTable = studentSprite(screen, (255, 128, 0), screenWidth / 5 * 4, screenHeight / 4 * 3, 60, 60, ex)

    global horizontalDistanceTables

    horizontalDistanceTables = middleLeftTable.rectX - centerTable.rectX

    global spriteList

    spriteList = [topLeftTable, middleLeftTable, bottomLeftTable, topMiddleTable, centerTable, bottomMiddleTable,
                  topRightTable, middleRightTable, bottomRightTable, teacherTable,  playerRect]

    global classMates

    classMates = spriteList[0:-2]

    rightList = [0, 1, 2, 3, 4, 5]

    leftList = [6, 7, 8]

    playerPosition = 9

    startScreen = True

    global dayIndicator

    dayIndicator = myFont.render("Day %s" % (day), False, (0, 0, 0))

    questionMark = pygame.image.load(questionMark)

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
                    done = True

                if buttonPressed[pygame.K_SPACE]:
                    startScreen = False
        else:
            for event in pygame.event.get():

                buttonPressed = pygame.key.get_pressed()

                if buttonPressed[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                    done = True

                if buttonPressed[pygame.K_DOWN] and playerPosition == 9:
                    playerRect.image = pygame.image.load(idle)
                    playerPosition = 3
                    while playerRect.rectY < (topMiddleTable.rectY - 100):
                        playerRect.rectY += screenHeight / 160
                        playerRect.rect.move(playerRect.rectX, playerRect.rectY)
                        time.sleep(0.25 / 4)
                        screen.blit(backgroundImage, [0, 0])
                        for n in classMates:
                            if n.confused == True:
                                screen.blit(questionMark, (n.rectX, n.rectY))
                        screen.blit(dayIndicator, (0, 0))
                        for n in spriteList:
                            n.draw()
                        pygame.display.flip()
                        pygame.event.pump()

                elif buttonPressed[pygame.K_DOWN] and not playerPosition == 9:
                    currentPosition = playerPosition
                    currentXCoords = int(playerRect.rectX)
                    playerPosition = getNextPosition("vertical", playerPosition)
                    playerTable = numberToTable(playerPosition)
                    distanceFromTarget = playerRect.rectY - playerTable.rectY
                    if currentPosition in rightList:
                        moveDown(currentXCoords, playerTable, distanceFromTarget, "right")
                    if currentPosition in leftList:
                        moveDown(currentXCoords, playerTable, distanceFromTarget, "left")

                if buttonPressed[pygame.K_SPACE]:
                    numberToTable(playerPosition).resolveConfusion()



                elif buttonPressed[pygame.K_UP] and not playerPosition == 9:
                    currentPosition = playerPosition
                    playerPosition = getPreviousPosition("vertical", playerPosition)
                    playerTable = numberToTable(playerPosition)
                    distanceFromTarget = playerRect.rectY - playerTable.rectY
                    currentXCoords = int(playerRect.rectX)
                    if currentPosition in rightList:
                        moveUp(currentXCoords, playerTable, distanceFromTarget, "right")
                    if currentPosition in leftList:
                        moveUp(currentXCoords, playerTable, distanceFromTarget, "left")
                elif buttonPressed[pygame.K_RIGHT] and not playerPosition == 9:
                    playerRect.image = pygame.transform.rotate(playerRect.image, 90)
                    playerPosition = getNextPosition("horizontal", playerPosition)
                    playerTable = numberToTable(playerPosition)
                    distanceFromTarget = playerRect.rectX - playerTable.rectX
                    while playerRect.rectX < playerTable.rectX:
                        playerRect.rectX -= distanceFromTarget / 40
                        time.sleep(0.25 / 4)
                        screen.blit(backgroundImage, [0, 0])
                        for n in spriteList:
                            n.draw()
                        for n in classMates:
                            if n.confused == True:
                                screen.blit(questionMark, (n.rectX, n.rectY))
                        screen.blit(dayIndicator, (0, 0))
                        pygame.display.flip()
                        pygame.event.pump()
                    playerRect.image = pygame.transform.rotate(playerRect.image, -90)

                elif buttonPressed[pygame.K_LEFT] and not playerPosition == 9:
                    playerRect.image = pygame.transform.rotate(playerRect.image, -90)
                    playerPosition = getPreviousPosition("horizontal", playerPosition)
                    playerTable = numberToTable(playerPosition)
                    distanceFromTarget = playerRect.rectX - playerTable.rectX
                    while playerRect.rectX > playerTable.rectX:
                        playerRect.rectX -= distanceFromTarget / 40
                        time.sleep(0.25 / 4)
                        screen.blit(backgroundImage, [0, 0])
                        for n in spriteList:
                            n.draw()
                        for n in classMates:
                            if n.confused == True:
                                screen.blit(questionMark, (n.rectX, n.rectY))
                        screen.blit(dayIndicator, (0, 0))
                        pygame.display.flip()
                        pygame.event.pump()
                    playerRect.image = pygame.transform.rotate(playerRect.image, 90)

            screen.blit(backgroundImage, [0, 0])
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX, n.rectY))
            screen.blit(dayIndicator, (0, 0))

            for n in spriteList:
                n.draw()

            if playerPosition == 9:

                textSurface = myFont.render("Press Down to start!", False, (0, 128, 255))

                screen.blit(textSurface, (screenWidth / 2 - 90, screenHeight / 2))

        screen.blit(dayIndicator, (0, 0))

        if needNewTime:

            recordedTime = time.time()

            needNewTime = False

        elif time.time() >= (recordedTime + 10):

            for n in classMates:

                if n.confused == True:
                    n.chances += 1
                if n.chances == 2:
                    finalAmount -= 2
                    n.resolveConfusion()

                chance = random.randint(day, 10)

                if chance == 10:
                    n.becomeConfused()

            needNewTime = True

        for n in classMates:
            if n.confused == True:
                screen.blit(questionMark, (n.rectX, n.rectY))

        if finalAmount <= 0:
            gameOver()


        pygame.display.flip()

        pygame.event.pump()

        clock.tick(60)



    pygame.quit()

main()

