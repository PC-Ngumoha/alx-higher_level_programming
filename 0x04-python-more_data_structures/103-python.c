#include <stdio.h>
#include <string.h>
#include <Python.h>

void print_python_bytes(PyObject *p);

/**
* print_python_list - prints python list object info
* @p: PyObject
*
* Return: void
*/
void print_python_list(PyObject *p)
{
	int size, alloc, idx;
	PyObject *obj;

	alloc = ((PyListObject *)p)->allocated;
	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	for (idx = 0; idx < size; idx++)
	{
		obj = PyList_GET_ITEM(p, idx);
		printf("Element %d: %s\n", idx, obj->ob_type->tp_name);
		if (PyBytes_CheckExact(obj))
			print_python_bytes(obj);
	}
}

/**
* print_python_bytes - prints python byte object info
* @p: PyObject
*
* Return: void
*/
void print_python_bytes(PyObject *p)
{
	#define NUM_BYTES 10

	int size, num, i;
	char *byte_string, bytes[NUM_BYTES];

	printf("[.] bytes object info\n");
	if (PyBytes_CheckExact(p))
	{
		byte_string = PyBytes_AsString(p);
		size = PyBytes_Size(p);
		num = 0;
		while (byte_string[num] != '\0' && num != NUM_BYTES)
		{
			bytes[num] = byte_string[num];
			num++;
		}
		if (byte_string[num] == '\0')
		{
			i = num;
			while (i != NUM_BYTES)
			{
				bytes[i] = '\0';
				i++;
			}
		}
		if (size < NUM_BYTES)
			num = size + 1; 
		if (size > NUM_BYTES)
			num = NUM_BYTES;
		
		printf("  size: %d\n", size);
		printf("  trying string: %s\n", byte_string);
		printf("  first %d bytes:", num);
		for (i = 0; i < num; i++)
		{
			printf(" ");
			printf("%02hhx", bytes[i]);
		}
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
