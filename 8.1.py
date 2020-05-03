import smbus
import time

LIGHTSENSOR = 0x23

HIGH_RES = 0x20
bus = smbus.SMBus(1)


def convertToNumber(data):
    result = (data[1] + (256 * data[0])) / 1.2
    return (result)


def readLight(addr=LIGHTSENSOR):
    data = bus.read_i2c_block_data(addr, HIGH_RES)
    return convertToNumber(data)


def main():
    while True:
        lightLevel = readLight()
        print("Light Level : " + format(lightLevel, '.2f') + " lx")
        time.sleep(0.5)


if __name__ == "__main__":
    main()
