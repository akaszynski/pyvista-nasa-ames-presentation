>>> from pyvista import examples
>>> dataset = examples.download_frog()
>>> dataset
UniformGrid (0x7f4d81806700)
  N Cells:      31594185
  N Points:	31960000
  X Bounds:	0.000e+00, 4.990e+02
  Y Bounds:	0.000e+00, 4.690e+02
  Z Bounds:	0.000e+00, 2.025e+02
  Dimensions:	500, 470, 136
  Spacing:	1.000e+00, 1.000e+00, 1.500e+00
  N Arrays:	1
>>> dataset.plot(volume=True)
