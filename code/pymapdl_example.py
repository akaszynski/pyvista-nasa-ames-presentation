# Define mesh controls and generate mesh
mapdl.esize(0.0075)
mapdl.vmesh("all")

# Save mesh as VTK object
grid = mapdl.mesh.grid

# Map the imported data to MAPDL grid
inter_grid = grid.interpolate(
    wrapped,
    sharpness=5,
    radius=0.0001,
    strategy="closest_point",
)

# Save node numbers
node_num = inter_grid.point_data["ansys_node_num"]
