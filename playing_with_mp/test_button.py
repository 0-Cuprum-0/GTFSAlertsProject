from machine import Pin, I2C
import time
from ssd1306 import SSD1306_I2C



import time

from machine import Pin


led = Pin(6, Pin.OUT)
pin = Pin(7, Pin.IN, Pin.PULL_UP)
print(led.value())
    
rst = Pin(21, Pin.OUT)
rst.value(0)
time.sleep_ms(50)
rst.value(1)
time.sleep_ms(50)

oled_power = Pin(36, Pin.OUT)
oled_power.value(1)
time.sleep_ms(100)

i2c = I2C(0, scl=Pin(18), sda=Pin(17), freq=100000)


oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

oled.fill(0)

 

for i in range (100):
    oled.fill(0)

    if pin.value() == 0:
        print("Pressed!")
        oled.text("Pressed!", 0, 20)

        led.value(1)
    else:
        print("Not pressed!")
        oled.text("Not pressed!", 0, 20)

        led.value(0)

    oled.show()
    time.sleep(0.1)

oled.fill(0)
oled.show()

    
