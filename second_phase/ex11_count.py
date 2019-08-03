# typedef struct_object {
#     /* 引用计数 */
#     int ob_refcnt;
#     /* 对象指针 */
#     struct_typeobject *ob_type;
# } PyObject;
# /* 增加引用计数的宏定义 */
# #define Py_INCREF(op)   ((op)->ob_refcnt++)
# /* 减少引用计数的宏定义 */
# #define Py_DECREF(op) \ //减少计数
#     if (--(op)->ob_refcnt != 0) \
#         ; \
#     else \
#         __Py_Dealloc((PyObject *)(op))


# 循环引用会导致内存泄露 - Python除了引用技术还引入了标记清理和分代回收
# 在Python 3.6以前如果重写__del__魔术方法会导致循环引用处理失效
# 如果不想造成循环引用可以使用弱引用
list1 = []
list2 = []
list1.append(list2)
list2.append(list1)