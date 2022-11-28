# Setup tools for the SWIG GRT python bindings
from distutils.core import setup, Extension
import numpy as np
import sys

include_dirs = [np.get_include(), sys.prefix + "/include"]

# Assume libgrt has been installed as a conda package
# and it is available in the conda environment.
# Create an extension module for the swig wrapper
grt_module = Extension(
    "_GRT",
    sources=["GRT.i"],
    swig_opts=["-python", "-py3", "-c++", "-Wall", "-verbose"] + ["-I" + d for d in include_dirs],
    include_dirs=include_dirs,
    library_dirs=[sys.prefix + "/lib"],
    libraries=["grt"],
)


# Create the setup
setup(
    name="GRT",
    version="0.2.5",
    author="Nick Gillian",
    description="""Python bindings for the Gesture Recognition Toolkit (GRT)""",
    ext_modules=[grt_module],
    py_modules=["GRT"],
    requires=["numpy", "swig"],
)
