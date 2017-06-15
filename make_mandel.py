from bmp import write_grayscale as bmp
from bmp import dimensions as bmpdim

import fractal
import png

mand = fractal.mandelbrot(448, 256)
print(mand)
bmp('mandel.bmp', mand)
png.from_array(mand, 'L').save('mandel.png')

w, h = bmpdim('mandel.bmp')
print(bmpdim('mandel.bmp'))
print("Width: ", w, " Height: ", h)


