import numpy
import scipy.special
import scipy.misc
from mayavi import mlab

a0 = 1
r = lambda x, y, z: numpy.sqrt(x**2 + y**2 + z**2)
theta = lambda x, y, z: numpy.arccos(z/r(x,y,z))
phi = lambda x, y, z: numpy.arctan(y/x)
R = lambda r ,n, l: (2*r/n/a0)**l * numpy.exp(-r/n/a0) * scipy.special.genlaguerre(n-l-1, 2*l+1)(2*r/n/a0)
entire_func = lambda r, theta, phi, n, l, m: R(r, n, l) * scipy.special.sph_harm(m, l, phi, theta)
squared = lambda r, theta, phi, n, l, m: abs(entire_func(r, theta, phi, n, l, m))**2

#x, y, z = numpy.ogrid[-50:50:100j,-50:50:100j,-140:140:100j]
x, y, z = numpy.ogrid[-25:25:100j,-25:25:100j,-25:25:100j]

mlab.figure(size=(1000,1000))

n = 15
l = 4
m = 0
final_func = squared(r(x, y, z), theta(x, y, z), phi(x, y, z), n, l, m)
plot = mlab.contour3d(final_func, contours=32, transparent=True, opacity=.7)
mlab.pipeline.image_plane_widget(plot, plane_orientation='y_axes', slice_index=10)
#mlab.pipeline.image_plane_widget(plot, plane_orientation='x_axes', slice_index=50)
#mlab.pipeline.image_plane_widget(plot, plane_orientation='z_axes', slice_index=10)
mlab.colorbar()
mlab.title = mlab.title('n = '+str(n) + ' l = '+str(l)+ ' m = '+str(m))
mlab.outline()
mlab.show()
