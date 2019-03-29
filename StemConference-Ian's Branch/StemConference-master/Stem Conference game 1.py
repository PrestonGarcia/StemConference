import pygame
import time
import os
import random

filePath = os.getcwd()
ex = os.path.join(filePath, "ex.png")
bcgd = os.path.join(filePath, "bcgd.png")
there = os.path.join(filePath, "there.png")
notthere = os.path.join(filePath, "notthere.png")

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
    if direction == "right" and not abs(distanceFromTarget) <= 100:
        while playerRect.rectX <= (xCoords - (horizontalDistanceTables) / 4):
            playerRect.rectX -= (horizontalDistanceTables) / 20
            screen.blit(backgroundImage, [0, 0])
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()
        while playerRect.rectY <= targetTable.rectY - 100:
            playerRect.rectY -= distanceFromTarget / 10
            screen.blit(backgroundImage, [0, 0])
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()
        while playerRect.rectX >= targetTable.rectX + 20:
            playerRect.rectX += (horizontalDistanceTables) / 20
            screen.blit(backgroundImage, [0, 0])
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()
    if direction == "left" and not abs(distanceFromTarget) <= 100:
        while playerRect.rectX >= (xCoords + (horizontalDistanceTables) / 4):
            playerRect.rectX += (horizontalDistanceTables) / 20
            screen.blit(backgroundImage, [0, 0])
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()
        while playerRect.rectY <= targetTable.rectY - 100:
            playerRect.rectY -= distanceFromTarget / 10
            screen.blit(backgroundImage, [0, 0])
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()
        while playerRect.rectX <= targetTable.rectX - 20:
            playerRect.rectX -= (horizontalDistanceTables) / 20
            screen.blit(backgroundImage, [0, 0])
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()

def moveUp(xCoords, targetTable, distanceFromTarget, direction):
    if direction == "right" and not abs(distanceFromTarget) <= 100:
        print(distanceFromTarget)
        while playerRect.rectX <= (xCoords - (horizontalDistanceTables) / 4):
            playerRect.rectX -= (horizontalDistanceTables) / 20
            screen.blit(backgroundImage, [0, 0])
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()
        while playerRect.rectY >= targetTable.rectY - 100:
            playerRect.rectY -= distanceFromTarget / 10
            screen.blit(backgroundImage, [0, 0])
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()
        while playerRect.rectX >= targetTable.rectX + 20:
            playerRect.rectX += (horizontalDistanceTables) / 20
            screen.blit(backgroundImage, [0, 0])
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()
    if direction == "left" and not abs(distanceFromTarget) <= 100:
        while playerRect.rectX >= (xCoords + (horizontalDistanceTables) / 4):
            playerRect.rectX += (horizontalDistanceTables) / 20
            screen.blit(backgroundImage, [0, 0])
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()
        while playerRect.rectY >= targetTable.rectY - 100:
            playerRect.rectY -= distanceFromTarget / 10
            screen.blit(backgroundImage, [0, 0])
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()
        while playerRect.rectX <= targetTable.rectX - 20:
            playerRect.rectX -= (horizontalDistanceTables) / 20
            screen.blit(backgroundImage, [0, 0])
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))
            screen.blit(dayIndicator, (0, 0))
            time.sleep(0.25)
            for n in spriteList:
                n.draw()
            pygame.display.flip()
            pygame.event.pump()

def setup(amountEarned):
    global finalAmount
    finalAmount += amountEarned

def main():
    day = 1

    finalAmount = 160

    totalMoney = 0

    needNewTime = True

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

    global blackBackground

    blackBackground = pygame.Surface(screen.get_size())
    blackBackground.convert()
    blackBackground.fill((0, 0, 0))

    done = False

    global clock

    clock = pygame.time.Clock()

    teacherTable = rectSprite(screen, (0, 128, 255), screenWidth / 2 - 30, 0, 60, 60, notthere)

    global playerRect

    playerRect = rectSprite(screen, (0, 128, 255), screenWidth / 2 - 30, 0, 60, 60, there)

    topLeftTable = studentSprite(screen, (255, 128, 0), screenWidth / 5 - 30, screenHeight / 4, 60, 60, ex)

    topMiddleTable = studentSprite(screen, (255, 128, 0), screenWidth / 2 - 30, screenHeight / 4, 60, 60, ex)

    topRightTable = studentSprite(screen, (255, 128, 0), screenWidth / 5 * 4 - 30, screenHeight / 4, 60, 60, ex)

    middleLeftTable = studentSprite(screen, (255, 128, 0), screenWidth / 5 - 30, screenHeight / 2, 60, 60, ex)

    centerTable = studentSprite(screen, (255, 128, 0), screenWidth / 2 - 30, screenHeight / 2, 60, 60, ex)

    middleRightTable = studentSprite(screen, (255, 128, 0), screenWidth / 5 * 4 - 30, screenHeight / 2, 60, 60, ex)

    bottomLeftTable = studentSprite(screen, (255, 128, 0), screenWidth / 5 - 30, screenHeight / 4 * 3, 60, 60, ex)

    bottomMiddleTable = studentSprite(screen, (255, 128, 0), screenWidth / 2 - 30, screenHeight / 4 * 3, 60, 60, ex)

    bottomRightTable = studentSprite(screen, (255, 128, 0), screenWidth / 5 * 4 - 30, screenHeight / 4 * 3, 60, 60, ex)

    global horizontalDistanceTables

    horizontalDistanceTables = middleLeftTable.rectX - centerTable.rectX

    global spriteList

    spriteList = [topLeftTable, middleLeftTable, bottomLeftTable, topMiddleTable, centerTable, bottomMiddleTable,
                  topRightTable, middleRightTable, bottomRightTable, teacherTable,  playerRect]

    global classMates

    classMates = spriteList[0:-2]

    print(classMates)

    rightList = [0, 1, 2, 3, 4, 5]

    leftList = [6, 7, 8]

    playerPosition = 9

    startScreen = True

    dayEndScreen = False

    setupFinished = False

    rentToggle = True
    foodToggle = True
    billsToggle = True
    tripToggle = True

    rentValue = 0
    foodValue = 0
    billsValue = 0
    tripValue = 0

    global dayIndicator

    dayIndicator = myFont.render("Day %s" % (day), False, (0, 0, 0))

    global questionMark

    questionMark = myFont.render("?", False, (0, 0, 0))

    pygame.mouse.set_visible(False)

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
            startTime = time.time()
        elif dayEndScreen:
            for event in pygame.event.get():
                mousePosition = pygame.mouse.get_pos()
                buttonPressed = pygame.key.get_pressed()

                selectionWidth = screenWidth/4
                if not setupFinished:
                    pygame.mouse.set_visible(True)
                    pygame.mouse.set_pos(screenWidth/2, screenHeight/2)
                    screen.blit(blackBackground, (0, 0))
                    setupFinished = True

                moneyIndicator = myFont.render("Money: %s" % (totalMoney), False, (255, 255, 255))
                screen.blit(moneyIndicator, (0, 0))

                payRent = myFont.render("Pay Your Rent: $500", False, (255, 255, 255))
                screen.blit(payRent, (screenWidth*7 / 16, screenHeight / 6))

                buyFood = myFont.render("Buy Tomorrow's Food: $30", False, (255, 255, 255))
                screen.blit(buyFood, (screenWidth * 27 / 64, screenHeight*2 / 6))

                payBills = myFont.render("Pay Your Bills: $300", False, (255, 255, 255))
                screen.blit(payBills, (screenWidth * 7 / 16, screenHeight * 3 / 6))

                buyTrip = myFont.render("Go on a Trip to Europe: $3000", False, (255, 255, 255))
                screen.blit(buyTrip, (screenWidth * 53 /128, screenHeight * 4 / 6))

                confirmButton = myFont.render("Confirm your Selections", False, (255, 255, 255))
                screen.blit(confirmButton, (screenWidth * 55 / 128, screenHeight * 5 / 6))
                pygame.draw.lines(screen, (255, 255, 255), True, [(screenWidth * 3 / 8, screenHeight * 5 / 6),
                                                            (screenWidth * 3 / 8 + selectionWidth,
                                                             screenHeight * 5 / 6),
                                                            (screenWidth * 3 / 8 + selectionWidth,
                                                             screenHeight * 5 / 6 + 50),
                                                            (screenWidth * 3 / 8, screenHeight * 5 / 6 + 50)])

                if event.type == pygame.MOUSEBUTTONDOWN and mousePosition[0] >= screenWidth*3/8 and mousePosition[1] >= screenHeight/6 \
                                                        and mousePosition[0] <= screenWidth*3/8 + selectionWidth and mousePosition[1] <= screenHeight/6 + 50:
                    if rentToggle:
                        pygame.draw.lines(screen, (255, 255, 255), True, [(screenWidth * 3 / 8, screenHeight / 6),
                                                                          (screenWidth * 3 / 8 + selectionWidth,
                                                                           screenHeight / 6),
                                                                          (screenWidth * 3 / 8 + selectionWidth,
                                                                           screenHeight / 6 + 50),
                                                                          (screenWidth * 3 / 8, screenHeight / 6 + 50)])
                        rentValue = 500
                        rentToggle = False
                    else:
                        pygame.draw.lines(screen, (0, 0, 0), True, [(screenWidth * 3 / 8, screenHeight / 6),
                                                                          (screenWidth * 3 / 8 + selectionWidth,
                                                                           screenHeight / 6),
                                                                          (screenWidth * 3 / 8 + selectionWidth,
                                                                           screenHeight / 6 + 50),
                                                                          (screenWidth * 3 / 8, screenHeight / 6 + 50)])
                        rentValue = 0
                        rentToggle = True
                if event.type == pygame.MOUSEBUTTONDOWN and mousePosition[0] >= screenWidth*3/8 and mousePosition[1] >= screenHeight*2/6 \
                                                        and mousePosition[0] <= screenWidth*3/8 + selectionWidth and mousePosition[1] <= screenHeight*2/6 + 50:
                    if foodToggle:
                        pygame.draw.lines(screen, (255, 255, 255), True, [(screenWidth * 3 / 8, screenHeight*2 / 6),
                                                                          (screenWidth * 3 / 8 + selectionWidth,
                                                                           screenHeight*2 / 6),
                                                                          (screenWidth * 3 / 8 + selectionWidth,
                                                                           screenHeight*2 / 6 + 50),
                                                                          (screenWidth * 3 / 8, screenHeight*2 / 6 + 50)])
                        foodValue = 30
                        foodToggle = False
                    else:
                        pygame.draw.lines(screen, (0, 0, 0), True, [(screenWidth * 3 / 8, screenHeight*2 / 6),
                                                                          (screenWidth * 3 / 8 + selectionWidth,
                                                                           screenHeight*2 / 6),
                                                                          (screenWidth * 3 / 8 + selectionWidth,
                                                                           screenHeight*2 / 6 + 50),
                                                                          (screenWidth * 3 / 8, screenHeight*2 / 6 + 50)])
                        foodValue = 0
                        foodToggle = True

                if event.type == pygame.MOUSEBUTTONDOWN and mousePosition[0] >= screenWidth*3/8 and mousePosition[1] >= screenHeight*3/6 \
                                                        and mousePosition[0] <= screenWidth*3/8 + selectionWidth and mousePosition[1] <= screenHeight*3/6 + 50:
                    if billsToggle:
                        pygame.draw.lines(screen, (255, 255, 255), True, [(screenWidth * 3 / 8, screenHeight*3 / 6),
                                                                          (screenWidth * 3 / 8 + selectionWidth,
                                                                           screenHeight*3 / 6),
                                                                          (screenWidth * 3 / 8 + selectionWidth,
                                                                           screenHeight*3 / 6 + 50),
                                                                          (screenWidth * 3 / 8, screenHeight*3 / 6 + 50)])
                        billsValue = 300
                        billsToggle = False
                    else:
                        pygame.draw.lines(screen, (0, 0, 0), True, [(screenWidth * 3 / 8, screenHeight*3 / 6),
                                                                          (screenWidth * 3 / 8 + selectionWidth,
                                                                           screenHeight*3 / 6),
                                                                          (screenWidth * 3 / 8 + selectionWidth,
                                                                           screenHeight*3 / 6 + 50),
                                                                          (screenWidth * 3 / 8, screenHeight*3 / 6 + 50)])
                        billsValue = 0
                        billsToggle = True

                if event.type == pygame.MOUSEBUTTONDOWN and mousePosition[0] >= screenWidth*3/8 and mousePosition[1] >= screenHeight*4/6 \
                                                        and mousePosition[0] <= screenWidth*3/8 + selectionWidth and mousePosition[1] <= screenHeight*4/6 + 50:
                    if tripToggle:
                        pygame.draw.lines(screen, (255, 255, 255), True, [(screenWidth * 3 / 8, screenHeight*4 / 6),
                                                                          (screenWidth * 3 / 8 + selectionWidth,
                                                                           screenHeight*4 / 6),
                                                                          (screenWidth * 3 / 8 + selectionWidth,
                                                                           screenHeight*4 / 6 + 50),
                                                                          (screenWidth * 3 / 8, screenHeight*4 / 6 + 50)])
                        tripValue = 3000
                        tripToggle = False
                    else:
                        pygame.draw.lines(screen, (0, 0, 0), True, [(screenWidth * 3 / 8, screenHeight*4 / 6),
                                                                          (screenWidth * 3 / 8 + selectionWidth,
                                                                           screenHeight*4 / 6),
                                                                          (screenWidth * 3 / 8 + selectionWidth,
                                                                           screenHeight*4 / 6 + 50),
                                                                          (screenWidth * 3 / 8, screenHeight*4 / 6 + 50)])
                        tripValue = 0
                        tripToggle = True

                if event.type == pygame.MOUSEBUTTONDOWN and mousePosition[0] >= screenWidth * 3 / 8 and mousePosition[1] >= screenHeight * 5 / 6 \
                                                        and mousePosition[0] <= screenWidth * 3 / 8 + selectionWidth and mousePosition[1] <= screenHeight * 5 / 6 + 50:
                    totalMoney -= tripValue - foodValue - billsValue - rentValue
                    if totalMoney < 0:
                        gameOver()
                        print("Game Over!")
                        done = True
                    else:
                        day += 1
                        if day > 5:
                            gameOver()
                        dayEndScreen = False
                        setupFinished = False
                        startTime = time.time()
                if buttonPressed[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                    print("Shutting down!")
                    done = True

        else:
            endTime = startTime + 90
            timeRemaining = int(endTime - time.time())
            dayIndicator = myFont.render("Day %s" % day, False, (0, 0, 0))

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
                        for n in classMates:
                            if n.confused == True:
                                screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))
                        screen.blit(dayIndicator, (0, 0))
                        timeIndicator = myFont.render("Time %s" % (timeRemaining), False, (0, 0, 0))
                        screen.blit(timeIndicator, (0, 40))
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
                    playerPosition = getNextPosition("horizontal", playerPosition)
                    playerTable = numberToTable(playerPosition)
                    distanceFromTarget = playerRect.rectX - playerTable.rectX
                    while playerRect.rectX < playerTable.rectX:
                        playerRect.rectX -= distanceFromTarget / 10
                        time.sleep(0.25)
                        screen.blit(backgroundImage, [0, 0])
                        for n in classMates:
                            if n.confused == True:
                                screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))
                        screen.blit(dayIndicator, (0, 0))
                        timeIndicator = myFont.render("Time %s" % (timeRemaining), False, (0, 0, 0))
                        screen.blit(timeIndicator, (0, 40))
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
                        for n in classMates:
                            if n.confused == True:
                                screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))
                        screen.blit(dayIndicator, (0, 0))
                        timeIndicator = myFont.render("Time %s" % (timeRemaining), False, (0, 0, 0))
                        screen.blit(timeIndicator, (0, 40))
                        for n in spriteList:
                            n.draw()
                        pygame.display.flip()
                        pygame.event.pump()


            if time.time() >= endTime:
                totalMoney += finalAmount
                dayEndScreen = True

            screen.blit(backgroundImage, [0, 0])
            for n in classMates:
                if n.confused == True:
                    screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))
            screen.blit(dayIndicator, (0, 0))
            timeIndicator = myFont.render("Time %s" % (timeRemaining), False, (0, 0, 0))
            screen.blit(timeIndicator, (0, 40))

            timeIndicator = myFont.render("Time %s" % (timeRemaining), False, (0, 0, 0))
            screen.blit(timeIndicator, (0, 40))

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
                    finalAmount -= 5
                    n.resolveConfusion()

                chance = random.randint(day, 10)

                if chance == 10:
                    n.becomeConfused()

            needNewTime = True

        for n in classMates:
            if n.confused == True:
                screen.blit(questionMark, (n.rectX + 40, n.rectY - 10))

        pygame.display.flip()

        pygame.event.pump()

        clock.tick(60)

    pygame.quit()

main()