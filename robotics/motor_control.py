from gpiozero import Motor

# Coded by Tae hyeon, Jung.


class MotorControl:
    # These are all pre-defined GPIO configuration.
    # Change this if pin connection has altered.
    motor = Motor(forward="GPIO6", backward="GPIO13")
    motor2 = Motor(forward="GPIO19", backward="GPIO26")
    motor3 = Motor(forward="GPIO15", backward="GPIO14")
    motor4 = Motor(forward="GPIO18", backward="GPIO23")

    def front(self):
        self.motor.forward()
        self.motor2.forward()
        self.motor3.forward()
        self.motor4.forward()

    def stop(self):
        self.motor.stop()
        self.motor2.stop()
        self.motor3.stop()
        self.motor4.stop()

    def back(self):
        self.motor.backward()
        self.motor2.backward()
        self.motor3.backward()
        self.motor4.backward()

    def right(self):
        self.motor.forward(0.2)
        self.motor3.forward(0.2)
        self.motor2.backward(0.2)
        self.motor4.backward(0.2)

    def left(self):
        self.motor2.forward(0.2)
        self.motor4.forward(0.2)
        self.motor.backward(0.2)
        self.motor3.backward(0.2)
