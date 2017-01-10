from functools import wraps
def auto_as_view(cbv):

    new = wraps(cbv)(cbv.as_view())
    new._original = cbv
    return new
