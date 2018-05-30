from mandelbrot import Mandelbrot

# realFrom, realTo, imgFrom, imgTo, interval, max_iter
m = Mandelbrot(-2, 1, -1, 1, 0.01, 100)
m.do_the_loop()
m.show_image()