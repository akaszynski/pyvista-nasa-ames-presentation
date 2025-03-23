>>> from ansys.mapdl.core import launch_mapdl
>>> mapdl = launch_mapdl()
>>> print(mapdl)

Product:             ANSYS Mechanical Enterprise
MAPDL Version:       RELEASE  2021 R1           BUILD 21.0
PyMAPDL Version:     Version: 0.57.0

>>> points = np.random.random((10, 3))
>>> for i, (x, y, z) in enumerate(points):
    mapdl.k(i + 1, x, y, z)
