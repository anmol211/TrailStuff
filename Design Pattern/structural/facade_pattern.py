
class Lights:
    def light_on(self):
        print("Lights On")

    def light_off(self):
        print("Lights Off")


class Smoke:
    def smoke_on(self):
        print("Smoke On")

    def smoke_off(self):
        print("Smoke Off")


class Sensor:
    def sensor_on(self):
        print("Sensor On")

    def sensor_off(self):
        print("Sensor Off")

class Facade:
    def __init__(self):
        self.sensor = Sensor()
        self.smoke = Smoke()
        self.light = Lights()

    def emergency(self):
        self.sensor.sensor_on()
        self.light.light_on()
        self.smoke.smoke_on()

    def no_emergency(self):
        self.sensor.sensor_off()
        self.smoke.smoke_off()
        self.light.light_off()

if __name__ == '__main__':
    obj = Facade()
    s = "attack"

    if s == "attack":
        obj.emergency()
    else:
        obj.no_emergency()

