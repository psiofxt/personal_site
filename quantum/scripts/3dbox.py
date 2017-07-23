from tvtk.tools import visual
import numpy
from mayavi.mlab import *
import math
import random

f = figure(size=(1000,1000))

def threeDbox():
    clf()
    nx = 1
    ny = 1
    nz = 1
    Lx = 1
    Ly = 1
    Lz = 1
    hbar = 1
    m = 1
    kx = nx*math.pi/Lx
    ky = ny*math.pi/Ly
    kz = nz*math.pi/Lz
    w = hbar*(kx**2 + ky**2 + kz**2) / (2*m)

    def phi(t):
        return numpy.exp(-w*t)

    t = 0
    def f(x, y, z):
        sin, cos = numpy.sin, numpy.cos
        return (math.sqrt(8) * sin(nx*math.pi * x) * sin(ny*math.pi * y) * sin(nz*math.pi * z)) ** 2
    x, y, z = numpy.mgrid[0:1:.01, 0:1:.01, 0:1:.01]

    filenum = 0

    """ LOOP TO SAVE FILES
    for r in range(1, 4):
        nx = r
        for q in range(1, 4):
            ny = q
            for p in range(1, 4):
                nz = p
                s = contour3d(x, y, z, f)
                colorbar()
                outline()
                title('nx = '+str(nx) + ' ny = '+str(ny)+ ' nz = '+str(nz))
                savefig('3dbox/3dbox_'+str(nx) + str(ny) + str(nz) + '.png')
                clf()
                filenum += 1
    """

    #testing LOOP -- creates a zoom out effect amplifying the energy
    """for r in range(1, 30):
        nx += .02
        ny += .02
        nz += .02
        s = contour3d(x, y, z, f)
        colorbar()
        outline()
        title('nx = '+str(nx) + ' ny = '+str(ny)+ ' nz = '+str(nz))
        savefig('test3dbox/3dbox_'+str(nx) + str(ny) + str(nz) + '.png')
        clf()"""

    #OPAQUE BLOBS REPRESENTING WAVE FUNCTION
    #WITH A CROSS SECTION IMAGE PLANE
    plot = pipeline.scalar_field(x, y, z, f)
    #pipeline.iso_surface(plot, opacity=.3)
    #pipeline.image_plane_widget(plot, plane_orientation='y_axes', slice_index=10)

    contour3d(x, y, z, f)
    title('nx = '+str(nx) + ' ny = '+str(ny)+ ' nz = '+str(nz))
    outline()
    colorbar()
    show()

threeDbox()

"""ANIMATION FUNCTION""""
@show
@animate(delay=1000)
def animated3Dbox():
    nx = 1
    ny = 1
    nz = 1
    Lx = 1
    Ly = 1
    Lz = 1
    hbar = 1
    m = 1
    kx = nx*math.pi/Lx
    ky = ny*math.pi/Ly
    kz = nz*math.pi/Lz
    w = hbar*(kx**2 + ky**2 + kz**2) / (2*m)
    sin, cos = numpy.sin, numpy.cos

    def phi(t):
        return numpy.exp(-w*t)

    t = 0
    def f(x, y, z):
        sin, cos = numpy.sin, numpy.cos
        return abs((math.sqrt(8) * sin(nx*math.pi * x) * sin(ny*math.pi * y) * sin(nz*math.pi * z)))

    x, y, z = numpy.mgrid[0:1:.01, 0:1:.01, 0:1:.01]
    c = contour3d(x, y, z, f, opacity=.8)
    plot = c.mlab_source
    outline()
    colorbar()

    while True:
        x, y, z = numpy.mgrid[0:1:.01, 0:1:.01, 0:1:.01]
        sc = numpy.zeros((100, 100, 100)) + (f(x, y, z)*(cos(-w*t) + sin(-w*t)))
        plot.scalars = sc
        yield
        t += .01

#animated3Dbox()
