import pyansys
result = pyansys.Result('file.rst')
nnum, disp = result.nodal_solution(0)
result.plot_nodal_solution(0)
