class Sounds():
    def __init__(self):
        #self.attack1Sound = base.loadMusic('sounds/metal1.ogg')
        #self.attack1Sound.setVolume(1)  # Volume is a percentage from 0 to 1
        #self.attack1Sound.setLoopCount(1)  # 0 means loop forever, 1 (default)
                                        # means play once. 2 or higher means
                                        # play that many times
        self.attack1Sound = base.loadSfx("res/sounds/metal1.ogg")

    def attack1(self):
        self.attack1Sound.play()
