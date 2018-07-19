def try_this(return_success, exception, return_error):
    try:
        return return_success
    except exception:
        return return_error


def set_attr(item, attr, value):
    item[attr] = value
    return item
