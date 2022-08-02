from distutils.core import setup
from distutils.extension import Extension

boost_dir = '/usr/local/Cellar/boost/1.79.0_1'
boost_python_dir = '/usr/local/Cellar/boost-python3/1.79.0'

hello_ext = Extension(
    "hello_ext",
    sources=["hello_ext.cpp"],
    # libraries=["boost_python"],
    # include_dirs=[f'{boost_dir}/include/boost'],
    include_dirs=[f'{boost_dir}/include', f'{boost_python_dir}/lib'],
    library_dirs=[f'{boost_dir}/lib'],
)

setup(name="hello-world", version="0.1", ext_modules=[hello_ext])
