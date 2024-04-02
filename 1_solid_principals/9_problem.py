class LightBulb:
    def turn_on(self):
        print("LightBulb: Turned on...")

    def turn_off(self):
        print("LightBulb: Turned Off...")


class ElectricPowerSwitch:
    def __init__(self, l:LightBulb):
        self.lightBulb = l
        self.on = False

    def press(self):
        if self.on:
            self.lightBulb.turn_off()
            self.on = False
        else:
            self.lightBulb.turn_on()
            self.on = True


l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()