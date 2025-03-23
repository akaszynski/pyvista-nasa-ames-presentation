>>> from pyvista import examples
>>> dataset = examples.download_saddle_surface()
>>> dataset
PolyData (0x7f4d81806c40)
  N Cells:      5131
  N Points:     2669
  N Strips:     0
  X Bounds:     -2.001e+01, 2.000e+01
  Y Bounds:     -6.480e-01, 4.024e+01
  Z Bounds:     -6.093e-01, 1.513e+01
  N Arrays:     0
>>> dataset.plot(color='tan')
