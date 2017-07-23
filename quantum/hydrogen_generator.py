import numpy
import scipy.special
import scipy.misc
from mayavi.mlab import *

a0 = 1
r = lambda x, y, z: numpy.sqrt(x**2 + y**2 + z**2)
theta = lambda x, y, z: numpy.arccos(z/r(x,y,z))
phi = lambda x, y, z: numpy.arctan(y/x)
R = lambda r ,n, l: (2*r/n/a0)**l * numpy.exp(-r/n/a0) * scipy.special.genlaguerre(n-l-1, 2*l+1)(2*r/n/a0)
entire_func = lambda r, theta, phi, n, l, m: R(r, n, l) * scipy.special.sph_harm(m, l, phi, theta)
squared = lambda r, theta, phi, n, l, m: abs(entire_func(r, theta, phi, n, l, m))**2

#x, y, z = numpy.ogrid[-50:50:100j,-50:50:100j,-140:140:100j]
x, y, z = numpy.ogrid[-25:25:100j, -25:25:100j, -25:25:100j]
#x, y, z = numpy.ogrid[-400:400:100j, -400:400:100j, -400:400:100j]

figure(size=(1000,1000))

n = 4
l = 2
m = 2
final_func = squared(r(x, y, z), theta(x, y, z), phi(x, y, z), n, l, m)
plot = contour3d(final_func, contours=32, transparent=True, opacity=.7)
pipeline.image_plane_widget(plot, plane_orientation='y_axes', slice_index=10)

colorbar()
title = title('n = '+str(n) + ' l = '+str(l)+ ' m = '+str(m))
outline()
show()
