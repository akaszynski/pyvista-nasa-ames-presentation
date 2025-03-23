#include "miniply/miniply.h"
#include <cstdio>

#include <nanobind/nanobind.h>
#include <nanobind/ndarray.h>
#include <nanobind/stl/string.h>

#include "array_support.h"

namespace nb = nanobind;
using namespace nb::literals;

/**
 * This function reads a 3D mesh from a .ply file using the miniply
 * and reutrns numpy arrays with vertices and triangle indices.
 */
nb::tuple LoadPLY(const std::string &filename, 
                  bool read_normals = true, bool read_uv = true) {

  miniply::PLYReader reader(filename.c_str());
