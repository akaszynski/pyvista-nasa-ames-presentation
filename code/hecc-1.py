import pyvista as pv
from pyvista import examples

mesh = pv.read("CE-18_Impeller.ply")

cubemap = examples.download_sky_box_cube_map()
pl = pv.Plotter()
pl.set_environment_texture(cubemap)
pl.add_mesh(
    mesh,
    color="w",
    pbr=True,
    metallic=1.0,
    roughness=0.5,
    diffuse=0.4,
)
pl.show()
