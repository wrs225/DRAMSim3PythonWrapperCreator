from distutils.core import setup, Extension
#name of module
name  = "dram_system"
  
#version of module
version = "1.0"
  
# specify the name of the extension and source files
# required to compile this
ext_modules = Extension(name='_dram_system',sources=["dram_system.i","dram_system_wrap.cxx"])
  
setup(name=name,
      version=version,
      ext_modules=[ext_modules])