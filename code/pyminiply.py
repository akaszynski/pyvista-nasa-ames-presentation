"""Python wrapper of the miniply library."""

import numpy as np
from pyvista import ID_TYPE
from pyvista.core.utilities import numpy_to_idarr
from pyvista.core.pointset import PolyData
from vtkmodules.vtkCommonDataModel import vtkCellArray
from pyminiply._wrapper import load_ply


def _load_ply(filename: str, read_normals: bool = True) -> PolyData:
    points, faces = load_ply(filename, read_normals)

    pdata = PolyData()
    pdata.points = points

    carr = vtkCellArray()
    offset = np.arange(0, faces.size + 1, faces.shape[1], dtype=ID_TYPE)
    carr.SetData(numpy_to_idarr(offset, deep=True), numpy_to_idarr(faces, deep=True))
    pdata.SetPolys(carr)
    return pdata
