import pyvista

# read and plot a result
result = read('result.vtu')
result.plot(
    scalars='strain',
    cmap='jet',
)
