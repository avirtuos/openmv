# Untitled - By: virtuoso - Sat Mar 31 2018

import pyb, sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

clock = time.clock()
from pyb import UART

uart = UART(1, 115200, timeout_char=1000)                         # init with given baudrate
uart.init(115200, bits=8, parity=None, stop=1, timeout_char=1000) # init with given parameters




while(True):
    clock.tick()
    img = sensor.snapshot()
    print(clock.fps())
    for i in range(10):
            x = (pyb.rng() % (2*img.width())) - (img.width()//2)
            y = (pyb.rng() % (2*img.height())) - (img.height()//2)
            w = (pyb.rng() % (img.width()//2))
            h = (pyb.rng() % (img.height()//2))
            r = (pyb.rng() % 127) + 128
            g = (pyb.rng() % 127) + 128
            b = (pyb.rng() % 127) + 128

            # If the first argument is a scaler then this method expects
            # to see x, y, w, and h. Otherwise, it expects a (x,y,w,h) tuple.
            img.draw_rectangle([x, y, w, h], color = (r, g, b), thickness = 2, fill = False)
    uart.write(str(clock.fps()))
