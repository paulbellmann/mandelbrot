import numpy
import matplotlib.pyplot as plt

""" Hallo Paul! LG s"""

class Mandelbrot(object):
    """Creates a Mandelbrot object with various constructor parameters"""

    def __init__(self, realFrom, realTo, imgFrom, imgTo, interval, max_iter):
        self.realFrom, self.realTo = realFrom, realTo
        self.imgFrom, self.imgTo = imgFrom, imgTo
        self.interval, self.max_iter = interval, max_iter

    def mandelbrot(self, Re, Im, max_iter):
        """calculates how many iterations it takes to get |Zn| = 2"""
        c = complex(Re, Im)
        z = 0.0j

        for i in xrange(max_iter):
            z = z*z + c
            # |Zn| = 2
            if (z.real*z.real + z.imag*z.imag) >= 4:
                return i

        return max_iter

    def do_the_loop(self):
        """loops through realFrom -> realTo and also imgFrom -> imgTo with the given interval step 
        and creates array with the values from mandelbrot()"""
        columns = len(numpy.arange(self.imgFrom, self.imgTo, self.interval))
        rows = len(numpy.arange(self.realFrom, self.realTo, self.interval))

        # creates array with x / y zeros
        self.result = numpy.zeros([rows, columns])

        # real axis
        for row_index, Re in enumerate(numpy.arange(self.realFrom, self.realTo, self.interval)):
            # imag axis
            for column_index, Im in enumerate(numpy.arange(self.imgFrom, self.imgTo, self.interval)):
                self.result[row_index, column_index] = self.mandelbrot(Re, Im, self.max_iter)

        return self.result

    def show_image(self):
        """shows a plot for local testing"""
        plt.figure(dpi=100)
        plt.imshow(self.result.T, cmap='hot', interpolation='bilinear', extent=[-2, 1, -1, 1])
        plt.xlabel('Re')
        plt.ylabel('Im')
        plt.show()