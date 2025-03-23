p = pv.Plotter()
p.add_mesh(
    copygrid,
    scalars='ux',
    n_colors=9
)
p.camera_position='xy'
p.show() 
