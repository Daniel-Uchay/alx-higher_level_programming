#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
  * print_python_list - Print python list info
  * @p: modulo object
  * Return: Nothing
  */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = (((PyVarObject *)(p))->ob_size);
	Py_ssize_t allo = (((PyListObject *)(p))->allocated);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allo);
}

/**
  * print_python_bytes - Print python list info
  * @p: modulo object
  * Return: Nothing
  */
void print_python_bytes(PyObject *p)
{
	(void) p;
	printf("[.] bytes object info\n");
}
