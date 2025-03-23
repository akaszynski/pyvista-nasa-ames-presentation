# same thing in pyvista
rst = mapdl.result
nnum, stress = rst.nodal_stress(0)
stress_yz = stress[:, 5]

# Create a line and sample over it
line = pv.Line(pl_start, pl_end, resolution=100)
out = line.sample(rst.grid)

# Note: We could have used a spline (or any dataset) and
# interpolated over it instead of a simple line.

# plot the interpolated stress from VTK and MAPDL
plt.plot(out.points[:, 1], out["Stress YZ"], "x")
plt.plot(table[:, 0], table[:, 6], label="Stress MAPDL")
plt.legend()
plt.show()
