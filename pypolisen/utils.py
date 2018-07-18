def try_this(return_success, exception, return_error):
    try:
        return return_success
    except exception:
        return return_error


def set_attr(item, attr, value):
    item[attr] = value
    return item


class Scope(object):

    def __init__(self, scope, func):
        self.scope = scope
        self.func = func

    def get(self, attribute):
        return self.scope[attribute]

    def execute(self):
        return self.func(get=self.get)
