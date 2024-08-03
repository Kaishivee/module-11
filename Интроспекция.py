from pprint import pprint

list_ = [1, 2, 3, 4, 5]


def introspection_info(x):
    info = {
        'type': type(x),
        'attributes': [i for i in dir(x) if i.startswith('_')],
        'methods': [n for n in dir(x) if not i.startswith('_')],
        'module': type(x).__module__
    }
    return info


pprint(introspection_info(list_))
