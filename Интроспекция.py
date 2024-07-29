from pprint import pprint
import inspect

some_list = [1, 2, 3]


def introspection_info(x):
    info = {
        'type': type(x),
        'methods and attributes': dir(x),
        'module': inspect.ismodule(x),
        'isinstance': isinstance(x, list),
        'isfunction': inspect.isfunction(x),
        'iscallable': callable(x),
    }

    return info


pprint(introspection_info(some_list))
