import smbus
import time


class MPU9250:
    def __init__(self, address=0x68, bus_number=1):
        self.MPU9250_ADDRESS = address
        self.bus = smbus.SMBus(bus_number)

        self.MPU9250_WHO_AM_I = 0x75
        self.MPU9250_ACCEL_XOUT_H = 0x3B
        self.MPU9250_ACCEL_YOUT_H = 0x3D
        self.MPU9250_ACCEL_ZOUT_H = 0x3F
        self.MPU9250_GYRO_XOUT_H = 0x43
        self.MPU9250_GYRO_YOUT_H = 0x45
        self.MPU9250_GYRO_ZOUT_H = 0x47
        self.MPU9150_RA_XOUT_L = 0x03
        self.MPU9150_RA_XOUT_H = 0x04
        self.MPU9150_RA_YOUT_L = 0x05
        self.MPU9150_RA_YOUT_H = 0x06
        self.MPU9150_RA_ZOUT_L = 0x07
        self.MPU9150_RA_ZOUT_H = 0x08

        self.scale_factor_accel = 16384.0
        self.scale_factor_gyro = 250.0 / 32768.0
        self.scale_factor_ra = 1200.0 / 4096.0

        self.accel_data = [0, 0, 0]
        self.gyro_data = [0, 0, 0]
        self.ra_data = [0, 0, 0]

        who_am_i = self.read_byte(self.MPU9250_WHO_AM_I)
        if who_am_i == 0x71:
            print("MPU_9250 is connected.")
        else:
            print("MPU_9250 connection failed. WHO_AM_I =", who_am_i)
            exit()

    def read_byte(self, reg):
        return self.bus.read_byte_data(self.MPU9250_ADDRESS, reg)

    def read_word(self, reg):
        high = self.bus.read_byte_data(self.MPU9250_ADDRESS, reg)
        low = self.bus.read_byte_data(self.MPU9250_ADDRESS, reg + 1)
        value = (high << 8) + low
        return value

    def read_word_reverse(self, reg):
        high = self.bus.read_byte_data(self.MPU9250_ADDRESS, reg)
        low = self.bus.read_byte_data(self.MPU9250_ADDRESS, reg - 1)
        value = (high << 8) + low
        return value

    def read_acceleration(self):
        x = self.read_word(self.MPU9250_ACCEL_XOUT_H)
        y = self.read_word(self.MPU9250_ACCEL_YOUT_H)
        z = self.read_word(self.MPU9250_ACCEL_ZOUT_H)
        self.accel_data = [
            x / self.scale_factor_accel,
            y / self.scale_factor_accel,
            z / self.scale_factor_accel,
        ]

    def read_gyroscope(self):
        x = self.read_word(self.MPU9250_GYRO_XOUT_H)
        y = self.read_word(self.MPU9250_GYRO_YOUT_H)
        z = self.read_word(self.MPU9250_GYRO_ZOUT_H)
        self.gyro_data = [
            x * self.scale_factor_gyro,
            y * self.scale_factor_gyro,
            z * self.scale_factor_gyro,
        ]

    def read_ra(self):
        x = self.read_word_reverse(self.MPU9150_RA_XOUT_H)
        y = self.read_word_reverse(self.MPU9150_RA_YOUT_H)
        z = self.read_word_reverse(self.MPU9150_RA_ZOUT_H)
        self.ra_data = [
            x * self.scale_factor_ra,
            y * self.scale_factor_ra,
            z * self.scale_factor_ra,
        ]

    def update_data(self):
        self.read_acceleration()
        self.read_gyroscope()
        self.read_ra()

    def get_acceleration(self):
        return self.accel_data

    def get_gyroscope(self):
        return self.gyro_data

    def get_ra(self):
        return self.ra_data


if __name__ == "__main__":
    sensor = MPU9250()

try:
    while True:
        sensor.update_data()
        accel_data = sensor.get_acceleration()
        gyro_data = sensor.get_gyroscope()
        ra_data = sensor.get_ra()

        print("Acceleration (X,Y,Z):", accel_data)
        print("Gyroscope (X,Y,Z):", gyro_data)
        print("Compass (X,Y,Z):", ra_data)

        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    sensor.bus.close()
