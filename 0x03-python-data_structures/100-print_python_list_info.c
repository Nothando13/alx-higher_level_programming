#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
<<<<<<< HEAD
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
       int size, alloc, i;
       PyObject *obj;

       size = Py_SIZE(p);
       alloc = ((PyListObject *)p)->allocated;

       printf("[*] Size of the Python List = %d\n", size);
       printf("[*] Allocated = %d\n", alloc);

       for (i = 0; i < size; i++)
       {
               printf("Element %d: ". i);

               obj = PyList_GetItem(p, i);
               printf("%s\n", Py_TYPE(obj)->tp_name);
       }
}
=======
 * @p: A Pyobject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyOject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}	


>>>>>>> ffdd96fbd78609e11136213d5dad2e112d69e95e
