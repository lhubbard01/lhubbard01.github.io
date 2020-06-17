---
layout: post
title: Writing C for Python
type: post
---


Let's say that we want to have more control over what python can do for us.  There are two options. write the extension in pure python, and writing the extension with c to interface with python.  The latter offers more speed and flexibility, while the former offers easier maintainability and readability. I think the latter is worth exploring due to the speed ups that can be offered within a language relatively close to the machine.
A lot of this was gathered from python's documentation, but there is also some further add on's that I plan on covering eventually.  To start, python2 and python3 have some differences in their c interface. I will be covering python3 here, but that difference is important to keep in mind if you search for further documentation. Most of python is handled via PyObject pointers.  





this example function will attend to computing a ratio of growth of an asset scaled by the number of such assets that can be purchased

```c
#include <Python.h>

static PyObject * compute( PyObject * self, PyObject * args )
{
	double initialValue, 
		projectedValue,
		buyingPower;

	if (!PyArg_ParseTuple(args, "ddd", &intialValue, &projectedValue, &buyingPower))
		return NULL;
	double assets = floor( initialvalue / buyingPower );	
	double growth = ( projectedValue / initialValue ) * assets;
		
	return Py_BuildValue( "d", growth );
}
```

So first things first, our signature contains a reference to the python object that is actually the function, and one python object containing the arguments being passed in to the function. The arguments are passed to the addresses of the respective variables inside the function scope. We then run the actual business logic.  Returned is a PyObject created in Py\_BuildValue, with d representing double.  

If this is all we want to do, and it will be for this tutorial, we will then prepare for the module.

```c
static PyMethodDef moduleNameMethods[] = {
	{"growth", compute, METH_VARARGS, "compute the growth of a particular asset"},
	{NULL,NULL,0,NULL}
}
```

This is where python functions are defined for the building logic. You will want to replace moduleName with whatever you want your module to actaully be called.

```c
static struct PyModuleDef modulenamemodule = {
	PyModuleDef_HEAD_INIT,
	"modulename",
	NULL, // this can be documenation string
	-1, //per-interpreter state of the module
	moduleNameMethods
};

PyMODINIT_FUNC PyInit_modulename()
{
	Py_Initialize();
	return PyModule_Create( &modulenamemodule);	
}
```

The moduleDef struct requires the same name as the module itself, as does the PyInit function.

With that, we have the bare minimum to have python install the module to its import directory for runtime use.  In order to install it to this location, we will have python run over setup.py

```python
#setup.py
from distutils.core import setup, Extension
    
module = Extension("modulename", sources=["srcs for install, ie modulename.c"])
	
setup(name="modulename",
            version="1.0",
	        description = ""
            ext_modules = [modulename])	
```

And that should be it.  Compiling will not work done through C without including the Python.h path, while _python setup.py install_ will take care of all of that


