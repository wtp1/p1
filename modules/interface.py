# -*- coding: utf_8 -*-
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode
from direct.gui.DirectGui import DirectFrame


myFrame = DirectFrame(frameColor=(0.5, 0.5, 0.5, 1),
                      frameSize=(-1.2, 1.2, -1, -0.5),
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
        #self.title = addTitle1("Panda3D: Tutorial - Fireflies using Deferred Shading")
        self.inst1 = addInstructions1(0.95, "HP:" + str(charlist.getCurrentCharacterHP()))
        #self.inst2 = addInstructions1(0.90, "Up/Down: More / Fewer Fireflies (Count: unknown)")
        #self.inst3 = addInstructions1(0.85, "Right/Left: Bigger / Smaller Fireflies (Radius: unknown)")
        #self.inst4 = addInstructions1(0.80, "V: View the render-to-texture results")

    def addInstructions(self, pos, msg):
        self.inst1.destroy()
        self.inst1 = addInstructions1(pos, msg)
