iris = {}


def add_iris(id_n, *args, **kwargs):
    data = {}
    data['species'] = args[0] if len(args) > 0 else ''
    data['petal_length'] = args[1] if len(args) > 1 else ''
    data['petal_width'] = args[2] if len(args) > 2 else ''
    for key, value in kwargs.items():
        data[key] = value
    iris[id_n] = data
