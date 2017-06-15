from bmp import write_grayscale as bmp
import fractal

mand = fractal.mandelbrot(448, 256)
print(mand)
bmp('mandel.bmp', mand)
