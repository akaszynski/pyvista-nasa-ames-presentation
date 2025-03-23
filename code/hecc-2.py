from femorph import utilities
import numpy as np

# compute PFH
vox_length = mesh.length / 50
mesh.points = mesh.points.astype(np.float64)
pfh, pfh_points, _, _ = utilities.compute_pfh(mesh, vox_length)

# construct a pointset out of the PFH and plot it
pfh_ps = pv.PointSet(pfh_points)
pfh_ps["pfh"] = pfh
pfh_ps.plot(component=5, point_size=30, show_scalar_bar=False)
