import smbus
import time

MPU9250_ADDRESS = 0x68

MPU9250_WHO_AM_I = 0x75
MPU9250_ACCEL_XOUT_H = 0x3B
MPU9250_ACCEL_YOUT_H = 0x3D
MPU9250_ACCEL_ZOUT_H = 0x3F
MPU9250_GYRO_XOUT_H = 0x43
MPU9250_GYRO_YOUT_H = 0x45
MPU9250_GYRO_ZOUT_H = 0x47
MPU9150_RA_XOUT_L = 0x03
MPU9150_RA_XOUT_H = 0x04
MPU9150_RA_YOUT_L = 0x05
MPU9150_RA_YOUT_H = 0x06
MPU9150_RA_ZOUT_L = 0x07
MPU9150_RA_ZOUT_H = 0x08

bus = smbus.SMBus(1)

def read_byte(reg):
    return bus.read_byte_data(MPU9250_ADDRESS, reg)

def read_word(reg):
    high = bus.read_byte_data(MPU9250_ADDRESS, reg)
    low = bus.read_byte_data(MPU9250_ADDRESS, reg + 1)
    value = (high << 8) + low
    return value

def read_word_reverse(reg):
    high = bus.read_byte_data(MPU9250_ADDRESS, reg)
    low = bus.read_byte_data(MPU9250_ADDRESS, reg - 1)
    value = (high << 8) + low
    return value

def read_acceleration():
    x = read_word(MPU9250_ACCEL_XOUT_H)
    y = read_word(MPU9250_ACCEL_YOUT_H)
    z = read_word(MPU9250_ACCEL_ZOUT_H)
    
    scale_factor = 16384.0
    Axyz = [x / scale_factor, y / scale_factor, z / scale_factor,]
    return Axyz

def read_gyroscope():
    x = read_word(MPU9250_GYRO_XOUT_H)
    y = read_word(MPU9250_GYRO_YOUT_H)
    z = read_word(MPU9250_GYRO_ZOUT_H)
    
    scale_factor = 250.0 / 32768.0
    Gxyz = [x * scale_factor, y * scale_factor, z * scale_factor,]
    return Gxyz

def read_ra():
    x = read_word_reverse(MPU9150_RA_XOUT_H)
    y = read_word_reverse(MPU9150_RA_YOUT_H)
    z = read_word_reverse(MPU9150_RA_ZOUT_H)
    
    scale_factor = 1200.0 / 4096.0
    Rxyz = [x * scale_factor, y * scale_factor, z * scale_factor,]
    return Rxyz

who_am_i = read_byte(MPU9250_WHO_AM_I)
if who_am_i == 0x71:  
    print("MPU-9250 is connected.")
else:
    print("MPU-9250 connection failed. WHO_AM_I =", who_am_i)
    exit()

try:
    while True:
        accel_data = read_acceleration()
        gyro_data = read_gyroscope()
        compass_data = read_ra()
       
        print("Acceleration (X,Y,Z):", accel_data)
        print("Gyroscope (X,Y,Z):", gyro_data)
        print("Compass (X,Y,Z):", compass_data)
       
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    bus.close()
