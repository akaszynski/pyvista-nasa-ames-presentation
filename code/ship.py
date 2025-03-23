pl = pv.Plotter()
pl.add_mesh(
    rays,
    scalars=depths,
    cmap=['green', 'blue', 'red'],
)
pl.add_mesh(ship)
pl.show()
