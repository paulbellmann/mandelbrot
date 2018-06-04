from mandelbrot import Mandelbrot

# realFrom, realTo, imgFrom, imgTo, interval, max_iter
m = Mandelbrot(-2, 1, -1, 1, 0.01, 500)
m.do_the_loop()
m.show_image()

# print len(m.do_the_loop().ravel().tolist())
# print (1-(-2))/0.1

# (realTo - realFrom) / interval => wie viel in einer zeile, ab wann umbruch