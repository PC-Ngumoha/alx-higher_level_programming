#include <Python.h>

/**
* print_python_list_info - prints python list information
* @p: Pointer to an arbitrary python object
* 
* Return: nothing
*/
void print_python_list_info(PyObject *p)
{
	if (PyList_CheckExact(p))
	{
		int size, allocated, idx;
		PyObject *obj;

		size = Py_SIZE(p);
		allocated = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %d\n", allocated);
		
		for (idx = 0; idx < size; idx++)
		{
			obj = PyList_GetItem(p, idx);
			printf("Element %d: %s\n", idx, Py_TYPE(obj)->tp_name);
		}
	}
}
