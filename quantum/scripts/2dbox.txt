from tvtk.tools import visual
import numpy
from mayavi.mlab import *
import math
import random

f = figure(size=(1000,1000))

def twoDbox():
    clf()
    nx = 1
    ny = 1
    Lx = 1
    Ly = 1
    hbar = 1
    m = 1
    kx = nx*math.pi/Lx
    ky = ny*math.pi/Ly
    w = hbar*(kx**2 + ky**2) / (2*m)

    t = numpy.linspace(0, .001, num=100)

    def phi(t):
        return numpy.exp(-w*t)

    t = 0
    def f(x, y):
        sin, cos = numpy.sin, numpy.cos
        return (math.sqrt(4) * sin(nx*math.pi * x) * sin(ny*math.pi * y) * phi(t)) ** 2
    x, y = numpy.mgrid[0:1:.01, 0:1:.01]

    filenum = 0

    # LOOP TO SAVE FILES

    """for r in range(1, 7):
        nx = r
        for q in range(1, 7):
            ny = q
            s = surf(x, y, f, warp_scale='auto')
            colorbar()
            outline()
            title('nx = '+str(nx) + ' ny = '+str(ny))
            savefig('2dbox/2dbox'+str(nx) + str(ny) + '_squared.png')
            clf()
            filenum += 1"""
    clf()
    s = surf(x, y, f, warp_scale="auto")
    title('nx = '+str(nx) + ' ny = '+str(ny))
    colorbar()
    outline()
    show()

twoDbox()


"""ANIMATION FUNCTION"""
@show
@animate(delay=1000)
def animated2Dbox():
    nx = 2
    ny = 2
    Lx = 1
    Ly = 1
    hbar = 1
    m = 1
    kx = nx*math.pi/Lx
    ky = ny*math.pi/Ly
    w = hbar*(kx**2 + ky**2) / (2*m)

    t = numpy.linspace(0, .001, num=100)
    sin, cos = numpy.sin, numpy.cos

    t = 0
    def f(x, y):
        sin, cos = numpy.sin, numpy.cos
        return (math.sqrt(4) * sin(nx*math.pi * x) * sin(ny*math.pi * y)) #* numpy.exp(-w*t)

    x, y = numpy.mgrid[0:1:.01, 0:1:.01]
    s = surf(x, y, f, warp_scale='auto')
    plot = s.mlab_source
    outline()
    #colorbar()
    title('nx = '+str(nx) + ' ny = '+str(ny))

    while True:
        x, y = numpy.mgrid[0:1:.01, 0:1:.01]
        sc = numpy.zeros((100, 100)) + (f(x, y)*(cos(-w*t) + sin(-w*t)))
        plot.scalars = sc
        yield
        t += .001

#animated2Dbox()
