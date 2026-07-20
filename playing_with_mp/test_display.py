
from machine import Pin, I2C
import time
from ssd1306 import SSD1306_I2C

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

# Write text
oled.text("Hello World!", 0, 0)
oled.text("OLED Display", 0, 20)
oled.text("with MicroPython", 0, 40)
oled.contrast(255)
oled.show()


