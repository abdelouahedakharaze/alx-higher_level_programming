#include <Python.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p) {
    int list_size, list_allocated, i;
    const char *element_type;
    PyListObject *list = (PyListObject *)p;
    PyVarObject *var_obj = (PyVarObject *)p;

    list_size = var_obj->ob_size;
    list_allocated = list->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %d\n", list_size);
    printf("[*] Allocated = %d\n", list_allocated);

    for (i = 0; i < list_size; i++) {
        element_type = list->ob_item[i]->ob_type->tp_name;
        printf("Element %d: %s\n", i, element_type);
        if (strcmp(element_type, "bytes") == 0)
            print_python_bytes(list->ob_item[i]);
    }
}

void print_python_bytes(PyObject *p) {
    unsigned char index, bytes_size;
    PyBytesObject *bytes = (PyBytesObject *)p;

    printf("[.] bytes object info\n");
    if (strcmp(p->ob_type->tp_name, "bytes") != 0) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
    printf("  trying string: %s\n", bytes->ob_sval);

    if (((PyVarObject *)p)->ob_size > 10)
        bytes_size = 10;
    else
        bytes_size = ((PyVarObject *)p)->ob_size + 1;

    printf("  first %d bytes: ", bytes_size);
    for (index = 0; index < bytes_size; index++) {
        printf("%02hhx", bytes->ob_sval[index]);
        if (index == (bytes_size - 1))
            printf("\n");
        else
            printf(" ");
    }
}
