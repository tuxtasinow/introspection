import inspect


def introspection_info(obj):
    info = {}

    info['type'] = type(obj).__name__

    attributes = []
    methods = []
    for item in dir(obj):
        if callable(getattr(obj, item)):
            methods.append(item)
        else:
            attributes.append(item)

    info['attributes'] = attributes
    info['methods'] = methods

    info['module'] = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else 'built-in'

    return info


number_info = introspection_info(52)
print(number_info)


class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello, {self.name}!'


my_object = MyClass('Urban')
object_info = introspection_info(my_object)
print(object_info)
