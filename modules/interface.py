# -*- coding: utf_8 -*-
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode
from direct.gui.DirectGui import DirectFrame
from panda3d.core import ConfigVariableString
from direct.gui.OnscreenImage import OnscreenImage

WinSize = ConfigVariableString('win-size')
WinSize = WinSize.getValue()
WinSize = WinSize.split(" ")
WinSizeWidth = WinSize[0]
WinSizeHeight = WinSize[1]
WinSizeProportion = float(WinSizeWidth)/float(WinSizeHeight)
WinSizeProportionReverse = float(WinSizeHeight)/float(WinSizeWidth)
print(WinSizeWidth)
print(WinSizeHeight)
print(WinSizeProportion)
print(WinSizeProportionReverse)


# Нижняя панель
def createBottomPanel():
    Left = -WinSizeProportion
    Right = WinSizeProportion
    Bottom = -1
    Top = -0.5
    # frameSize   Sets the size of the frame  (Left,Right,Bottom,Top)
    # frameColor  sets the color of the object's frame    (R,G,B,A)
    # pos sets the position of the object (X,Y,Z)
    return DirectFrame(frameColor=(0.5, 0.5, 0.5, 1),
                       frameSize=(Left, Right, Bottom, Top),
                       pos=(0, 0, 0))


# Панель иконки персонажа
def createCharacterPanel():
    Left = -WinSizeProportion
    Right = WinSizeProportion
    Bottom = -1
    Top = -0.5
    # frameSize   Sets the size of the frame  (Left,Right,Bottom,Top)
    # frameColor  sets the color of the object's frame    (R,G,B,A)
    # pos sets the position of the object (X,Y,Z)
    return DirectFrame(frameColor=(0.5, 0.5, 0.5, 1),
                       frameSize=(Left, Right, Bottom, Top),
                       pos=(0, 0, 0))


# Function to put instructions on the screen.
def addInstructions1(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1, 1, 1, 1),
                        pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)


# Function to put title on the screen.
def addTitle1(text):
    return OnscreenText(text=text, style=1, fg=(1, 1, 1, 1),
                        pos=(1.3, -0.95), align=TextNode.ARight, scale = .07)


class ingameInterface():
    def __init__(self, charlist):
        self.BottomPanel = createBottomPanel()
        # PersonIcon = createPersonIcon()
        # print(BottomPanel["frameSize"])
        # print(PersonIcon["pos"])

        #self.title = addTitle1("Panda3D: Tutorial")
        self.inst1 = addInstructions1(0.95, "HP:" +
                                      str(charlist.getCurrentCharacterHP()))
        #self.inst2 = addInstructions1(0.90, "Up/Down")
        #self.inst3 = addInstructions1(0.85, "Right/Left")
        #self.inst4 = addInstructions1(0.80, "V: View")

    def getBottomPanel(self):
        return self.BottomPanel

    def addInstructions(self, pos, msg):
        self.inst1.destroy()
        self.inst1 = addInstructions1(pos, msg)

    # Создание иконки персонажа с основными параметрами
    #def createPersonIcon(person):
    def createPersonIcon(self, characterCounter, id):
        print("\r" + "def createPersonIcon")
        print("characterCounter = " + str(characterCounter))
        print("id = " + str(id) + "\r")
        if(characterCounter > 0):
            print("ok")
            # qwe2 = 0
            imgScale = 0.15
            imgPath = 'res/textures/avatar' + str(characterCounter) + '.png'
            # iconHeight = 110
            # iconWidth = 150
            iconHeight = 0.15
            iconWidth = 0.15
            # qwe1 = float(iconWidth) / float(WinSizeWidth)
            # print(qwe1)
            # 0.01875
            # 0.0702781844802
            # qwe2 = float(iconHeight) / float(WinSizeHeight)
            # print(qwe2)

            # (-1.7786458333333333, 1.7786458333333333, -1, -0.5)
            #  frameSize=(Left, Right, Bottom, Top),
            # BottomPanel = self.getBottomPanel()
            # BPanelBottom = BottomPanel["frameSize"][2]
            # print(BPanelBottom)
            # BPanelTop = BottomPanel["frameSize"][3]
            # print(BPanelTop)
            # LPoint3f(-1.57865, 0, -0.562225)
            posX = -WinSizeProportion + iconHeight
            posY = 0
            # posZ = -WinSizeProportionReverse  # -0.15
            characterCounter = characterCounter * 2
            posZ = -0.5 + iconWidth * characterCounter - 0.15
            return OnscreenImage(image=imgPath,
                                 scale=imgScale,
                                 pos=(posX, posY, posZ))
                                 # pos=(0, 0, qwe2))
