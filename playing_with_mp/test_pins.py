from machine import Pin
import time
print("Hello world")

led = Pin(6, Pin.OUT)
print("Before")
print(led.value())
#led.off()
led.value(0)
print("After value 0")

print(led.value())

print("now wait 3 secs")
time.sleep(3)
led.value(1)
print("after turning on again")
print(led.value())
#print(btn.value())
try:
    for i in range (5):
        time.sleep(1)
        led.value(0)

        time.sleep(2)

        led.value(1)

except KeyboardInterrupt:
    print("Received Ctrl + C, stopping!")
