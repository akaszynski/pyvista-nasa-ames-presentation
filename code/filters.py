import pyvista as pv
from pyvista import examples

dataset = examples.load_uniform()
outline = dataset.outline()
threshed = dataset.threshold(
    [100, 500],
)
contours = dataset.contour()
slices = dataset.slice_orthogonal()
glyphs = dataset.glyph(
    factor=1e-3,
    geom=pv.Sphere(),
)

pl = pv.Plotter(shape=(2, 2))
pl.add_mesh(outline, color="k")
pl.add_mesh(threshed, show_scalar_bar=False)
