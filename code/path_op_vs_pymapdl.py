# mapping components of interest to path.
mapdl.pdef("Sx_my_path", "s", "x")
mapdl.pdef("Sy_my_path", "s", "y")
mapdl.pdef("Sz_my_path", "s", "z")
mapdl.pdef("Sxy_my_path", "s", "xy")
mapdl.pdef("Syz_my_path", "s", "yz")
mapdl.pdef("Szx_my_path", "s", "xz")

path_out = mapdl.prpath(
    "Sx_my_path",
    "Sy_my_path",
    "Sz_my_path",
    "Sxy_my_path",
    "Syz_my_path",
    "Szx_my_path",
)
table = np.genfromtxt(path_out.splitlines()[1:])
