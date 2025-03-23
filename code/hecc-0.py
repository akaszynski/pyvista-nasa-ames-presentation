import pyminiply

>>> timeit pv.read("CE-18_Impeller.ply")
1.23 s ± 6.6 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

>>> timeit mesh = pyminiply.read_as_mesh("CE-18_Impeller.ply")
358 ms ± 6.51 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

>>> mesh = pyminiply.read_as_mesh("CE-18_Impeller.ply")
PolyData (0x719e12b9a140)
  N Cells:    9065852
  N Points:   4535625
  N Strips:   0
  X Bounds:   -1.121e+00, 5.420e+00
  Y Bounds:   -8.481e+00, 8.485e+00
  Z Bounds:   -8.481e+00, 8.482e+00
  N Arrays:   1
